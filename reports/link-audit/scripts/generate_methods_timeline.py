#!/usr/bin/env python3

from __future__ import annotations

import math
import re
import textwrap
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from regenerate_paper_reports import (
    KIND_BY_SECTION,
    PAPER_REPORTS_ROOT,
    REPORTS_ROOT,
    ROOT,
    SECTION_SLUGS,
    connection_score,
    parse_readme_block,
    slug_for_title,
)


METHODS_PATH = ROOT / "papers" / "methods" / "README.md"
BENCHMARKS_PATH = ROOT / "papers" / "benchmarks" / "README.md"
MODELS_PATH = ROOT / "papers" / "models" / "README.md"
SAFETY_PATH = ROOT / "papers" / "safety" / "README.md"

TIMELINE_MD = REPORTS_ROOT / "methods-timeline.md"
FIGURES_DIR = REPORTS_ROOT / "figures"
TIMELINE_SVG = FIGURES_DIR / "methods-timeline.svg"

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

LANE_ORDER = [
    "Grounding & Action Translation",
    "RL & Post-Training",
    "Data & Environment Synthesis",
    "Memory, Reflection & Programmatic Planning",
    "Multi-Agent Orchestration",
]

LANE_COLORS = {
    "Grounding & Action Translation": ("#DBEAFE", "#2563EB", "#1E3A8A"),
    "RL & Post-Training": ("#DCFCE7", "#16A34A", "#14532D"),
    "Data & Environment Synthesis": ("#FEF3C7", "#D97706", "#78350F"),
    "Memory, Reflection & Programmatic Planning": ("#FCE7F3", "#DB2777", "#831843"),
    "Multi-Agent Orchestration": ("#EDE9FE", "#7C3AED", "#4C1D95"),
}

SHORT_LABELS = {
    "SeeAct: GPT-4V Web Agent via Visual Grounding": "SeeAct",
    "UFO: Windows OS UI Agent via GPT-4V": "UFO",
    "OS-Copilot: Towards Generalist Computer Agents": "OS-Copilot",
    "DigiRL: Training In-The-Wild Device-Control": "DigiRL",
    "Ponder & Press: Advancing VLM Grounding": "Ponder & Press",
    "Magentic-One: Multi-Agent with Human-in-Loop": "Magentic-One",
    "WebRL: Self-Evolving Online Curriculum RL for Web Agents": "WebRL",
    "AgentTrek: Agent Trajectory Synthesis via Web Tutorials": "AgentTrek",
    "OS-Genesis: Automating GUI Agent Trajectory Construction": "OS-Genesis",
    "GUI-Reflection: Self-Reflection for GUI Agents": "GUI-Reflection",
    "PC Agent-E: Efficient Agent Training for Computer Use": "PC Agent-E",
    "Chain-of-Agents: Multi-Agent Collaboration": "Chain-of-Agents",
    "ComputerRL: End-to-End Online RL for Computer Use Agents": "ComputerRL",
    "Grounding Computer Use Agents on Human Demonstrations": "Human Demo Grounding",
    "GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training": "GUI-GENESIS",
    "ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory": "ActionEngine",
}

MANUAL_YEAR_MONTH = {
    "GUI-Reflection: Self-Reflection for GUI Agents": (2025, 6),
}


@dataclass
class TimelineEntry:
    title: str
    family: str
    year: int
    month: int
    time_label: str
    venue_or_date: str
    environment: str
    key_move: str
    report_path: Path
    benchmark_context: list[str]
    model_context: list[str]
    safety_context: list[str]

    @property
    def quarter_index(self) -> int:
        return (self.year - 2024) * 4 + ((self.month - 1) // 3)


def all_entries():
    entries = []
    for section, path in [
        ("Methods and Techniques", METHODS_PATH),
        ("Benchmarks and Datasets", BENCHMARKS_PATH),
        ("Models and Architectures", MODELS_PATH),
        ("Safety and Security", SAFETY_PATH),
    ]:
        entries.extend(parse_readme_block(path, section))
    return entries


def arxiv_year_month(url: str) -> tuple[int, int] | None:
    match = re.search(r"arxiv\.org/abs/(\d{2})(\d{2})\.\d+", url)
    if not match:
        return None
    return 2000 + int(match.group(1)), int(match.group(2))


def infer_year_month(entry) -> tuple[int, int]:
    if entry.title in MANUAL_YEAR_MONTH:
        return MANUAL_YEAR_MONTH[entry.title]

    for key in ["Link", "Code", "Website", "Model"]:
        link = entry.links.get(key)
        if not link:
            continue
        parsed = arxiv_year_month(link[1])
        if parsed:
            return parsed

    date_text = entry.meta.get("Date", "")
    month_match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
        date_text,
        re.I,
    )
    if month_match:
        return int(month_match.group(2)), MONTHS[month_match.group(1).lower()]

    year_match = re.search(r"(\d{4})", entry.meta.get("Venue", "") or date_text)
    if year_match:
        return int(year_match.group(1)), 6

    return 2026, 12


def family_for(entry) -> str:
    tags = set(entry.tags)
    if "multi-agent" in tags:
        return "Multi-Agent Orchestration"
    if {"memory", "program-synthesis", "self-reflection", "self-improvement", "error-correction"} & tags:
        return "Memory, Reflection & Programmatic Planning"
    if {"grounding", "gpt-4v", "dual-model", "human-demonstrations", "windows"} & tags:
        return "Grounding & Action Translation"
    if {"data-synthesis", "trajectories", "reverse-task", "post-training"} & tags:
        return "Data & Environment Synthesis"
    if {"reinforcement-learning", "efficient-training", "rl"} & tags:
        return "RL & Post-Training"
    return "Memory, Reflection & Programmatic Planning"


def environment_for(entry) -> str:
    tags = set(entry.tags)
    if {"web"} & tags:
        return "web"
    if {"mobile", "android", "phone"} & tags:
        return "mobile"
    if {"desktop", "windows", "macos"} & tags:
        return "desktop"
    return "cross-surface"


def key_move_for(entry) -> str:
    priority = [
        "Key Innovations",
        "Approach",
        "Pipeline",
        "Training Pipeline",
        "Features",
        "Components",
        "Addresses Three Challenges",
        "Solutions",
    ]
    blocks = {block.heading.lower(): block for block in entry.detail_blocks}
    for heading in priority:
        block = blocks.get(heading.lower())
        if block:
            items = block.items + block.prose
            if items:
                return normalize_text(items[0], 120)
    for block in entry.detail_blocks:
        items = block.items + block.prose
        if items:
            return normalize_text(items[0], 120)
    return normalize_text(entry.description, 120)


def normalize_text(text: str, limit: int = 120) -> str:
    clean = re.sub(r"\s+", " ", text.replace("|", "/")).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rsplit(" ", 1)[0] + "..."


def method_report_path(title: str) -> Path:
    section = "Methods and Techniques"
    return report_path_for_entry(title, section)


def normalize_slug_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def report_path_for_entry(title: str, section: str) -> Path:
    folder = PAPER_REPORTS_ROOT / SECTION_SLUGS[section]
    candidate = folder / f"{slug_for_title(title)}.md"
    if candidate.exists():
        return candidate

    target_key = normalize_slug_key(title)
    for path in folder.glob("*.md"):
        if normalize_slug_key(path.stem) == target_key:
            return path
    return candidate


def pick_context(method_entry, candidates, kind: str, limit: int) -> list[str]:
    current_year_month = infer_year_month(method_entry)

    def sort_key(candidate):
        score = connection_score(method_entry, candidate)
        c_year, c_month = infer_year_month(candidate)
        delta = abs((c_year - current_year_month[0]) * 12 + (c_month - current_year_month[1]))
        kind_bonus = 1 if KIND_BY_SECTION[candidate.section] == kind else 0
        return (score + kind_bonus * 2, -delta)

    ranked = sorted(
        [candidate for candidate in candidates if KIND_BY_SECTION[candidate.section] == kind],
        key=sort_key,
        reverse=True,
    )
    seen = set()
    picks = []
    for candidate in ranked:
        if candidate.title in seen:
            continue
        picks.append(candidate.title)
        seen.add(candidate.title)
        if len(picks) >= limit:
            break
    return picks


def link_for_title(title: str, entries_by_title: dict[str, object]) -> str:
    entry = entries_by_title[title]
    report_path = report_path_for_entry(title, entry.section)
    return str(report_path.relative_to(REPORTS_ROOT))


def markdown_link(title: str, entries_by_title: dict[str, object]) -> str:
    return f"[{title}]({link_for_title(title, entries_by_title)})"


def build_timeline_entries() -> tuple[list[TimelineEntry], dict[str, object]]:
    entries = all_entries()
    entries_by_title = {entry.title: entry for entry in entries}
    methods = [entry for entry in entries if entry.section == "Methods and Techniques"]

    timeline = []
    for entry in methods:
        year, month = infer_year_month(entry)
        venue_or_date = entry.meta.get("Venue") or entry.meta.get("Date") or "Date not stated"
        time_label = f"{year}-{month:02d}"
        timeline.append(
            TimelineEntry(
                title=entry.title,
                family=family_for(entry),
                year=year,
                month=month,
                time_label=time_label,
                venue_or_date=venue_or_date,
                environment=environment_for(entry),
                key_move=key_move_for(entry),
                report_path=method_report_path(entry.title),
                benchmark_context=pick_context(entry, entries, "benchmark", 2),
                model_context=pick_context(entry, entries, "model", 2),
                safety_context=pick_context(entry, entries, "safety", 1),
            )
        )

    timeline.sort(key=lambda item: (item.year, item.month, item.title))
    return timeline, entries_by_title


def build_svg(timeline: list[TimelineEntry]) -> str:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    left = 220
    top = 180
    quarter_step = 180
    box_w = 150
    box_h = 58
    box_gap = 18
    lane_gap = 36
    levels_by_lane: dict[str, list[tuple[TimelineEntry, int]]] = defaultdict(list)
    lane_level_ends: dict[str, list[int]] = defaultdict(list)

    for item in timeline:
        x = left + item.quarter_index * quarter_step
        levels = lane_level_ends[item.family]
        level = 0
        while level < len(levels) and x <= levels[level] + box_gap:
            level += 1
        if level == len(levels):
            levels.append(x + box_w)
        else:
            levels[level] = x + box_w
        levels_by_lane[item.family].append((item, level))

    lane_heights = {}
    for lane in LANE_ORDER:
        max_level = max((level for _, level in levels_by_lane.get(lane, [])), default=0)
        lane_heights[lane] = 90 + max_level * 70

    width = left + quarter_step * 12 + 120
    height = top + sum(lane_heights.values()) + lane_gap * (len(LANE_ORDER) - 1) + 140

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Computer-use agent methods timeline</title>',
        '<desc id="desc">Timeline of method papers in the repository, grouped by grounding, reinforcement learning, data synthesis, planning, and multi-agent orchestration.</desc>',
        '<rect width="100%" height="100%" fill="#F8FAFC" />',
        '<rect x="40" y="34" width="360" height="64" rx="18" fill="#0F172A" />',
        '<text x="66" y="66" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="700" fill="#F8FAFC">Computer-Use Agent Methods Timeline</text>',
        '<text x="66" y="92" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#CBD5E1">Grouped by method family and placed by public paper timing.</text>',
        '<rect x="420" y="34" width="760" height="64" rx="18" fill="#E2E8F0" />',
        '<text x="448" y="62" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" fill="#0F172A">Pressure before the method wave</text>',
        '<text x="448" y="88" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#334155">2023 benchmarks such as WebArena, Mind2Web, and Android in the Wild set the tasks that 2024-2026 methods try to solve.</text>',
    ]

    for q in range(13):
        x = left + q * quarter_step
        parts.append(f'<line x1="{x}" y1="{top - 40}" x2="{x}" y2="{height - 70}" stroke="#CBD5E1" stroke-width="1" />')

    quarter_labels = [
        ("2024 Q1", 0),
        ("2024 Q2", 1),
        ("2024 Q3", 2),
        ("2024 Q4", 3),
        ("2025 Q1", 4),
        ("2025 Q2", 5),
        ("2025 Q3", 6),
        ("2025 Q4", 7),
        ("2026 Q1", 8),
        ("2026 Q2", 9),
        ("2026 Q3", 10),
        ("2026 Q4", 11),
    ]
    for label, idx in quarter_labels:
        x = left + idx * quarter_step + quarter_step / 2
        parts.append(f'<text x="{x}" y="{top - 56}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="700" fill="#0F172A">{label}</text>')

    legend_x = width - 480
    legend_y = 120
    for idx, lane in enumerate(LANE_ORDER):
        fill, stroke, text_color = LANE_COLORS[lane]
        y = legend_y + idx * 24
        parts.append(f'<rect x="{legend_x}" y="{y - 11}" width="18" height="18" rx="4" fill="{fill}" stroke="{stroke}" />')
        parts.append(f'<text x="{legend_x + 28}" y="{y + 3}" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="{text_color}">{escape(lane)}</text>')

    lane_y = top
    for lane in LANE_ORDER:
        fill, stroke, text_color = LANE_COLORS[lane]
        lane_h = lane_heights[lane]
        parts.append(f'<rect x="28" y="{lane_y - 24}" width="{width - 56}" height="{lane_h}" rx="22" fill="#FFFFFF" stroke="#E2E8F0" />')
        parts.append(f'<text x="52" y="{lane_y + 8}" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="{text_color}">{escape(lane)}</text>')

        for item, level in levels_by_lane.get(lane, []):
            x = left + item.quarter_index * quarter_step + 16
            y = lane_y + 24 + level * 70
            short = SHORT_LABELS.get(item.title, item.title)
            lines = textwrap.wrap(short, width=18)[:2]
            parts.append("<g>")
            parts.append(f"<title>{escape(item.title)} | {escape(item.venue_or_date)} | {escape(item.key_move)}</title>")
            parts.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2" />')
            for line_index, line in enumerate(lines):
                parts.append(
                    f'<text x="{x + box_w / 2}" y="{y + 24 + line_index * 15}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="{text_color}">{escape(line)}</text>'
                )
            parts.append(
                f'<text x="{x + box_w / 2}" y="{y + 48}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{text_color}">{escape(item.environment)} · {escape(item.venue_or_date)}</text>'
            )
            parts.append("</g>")

        lane_y += lane_h + lane_gap

    parts.append(
        '<text x="40" y="{}" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="#475569">Generated from tracked method entries in papers/methods/README.md and connected benchmark/model/safety context in the repo.</text>'.format(
            height - 26
        )
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def phase_for(item: TimelineEntry) -> str:
    if item.year == 2024 and item.month <= 6:
        return "2024 H1: first control loops"
    if item.year == 2024:
        return "2024 H2: grounding and orchestration"
    if item.year == 2025 and item.month <= 6:
        return "2025 H1: data and curriculum scaling"
    if item.year == 2025:
        return "2025 H2: open-foundation training push"
    return "2026: programmatic and post-training wave"


def family_note(family: str, titles: list[str], entries_by_title: dict[str, object]) -> str:
    linked = ", ".join(markdown_link(title, entries_by_title) for title in titles)
    if family == "Grounding & Action Translation":
        return f"{linked}. This lane converts perception into reliable action proposals, moving from GPT-4V prompting toward more explicit grounding and demonstration-backed action models."
    if family == "RL & Post-Training":
        return f"{linked}. This lane tries to break the static-demo bottleneck by using online interaction, curriculum construction, or more efficient post-training loops."
    if family == "Data & Environment Synthesis":
        return f"{linked}. This lane attacks the data scarcity problem by generating trajectories, reverse-synthesizing tasks, or rebuilding light-weight training environments with verifiable rewards."
    if family == "Memory, Reflection & Programmatic Planning":
        return f"{linked}. This lane shifts from reactive clicking toward recovery behavior, persistent state, and explicit planning structures."
    return f"{linked}. This lane explores decomposition into specialized agents or human-supervised orchestrators for harder long-horizon tasks."


def build_markdown(timeline: list[TimelineEntry], entries_by_title: dict[str, object]) -> str:
    counts = Counter(item.family for item in timeline)
    pre_method_pressure = [
        markdown_link("WebArena: Realistic Web Environment for Building Autonomous Agents", entries_by_title),
        markdown_link("Mind2Web: Towards a Generalist Agent for the Web", entries_by_title),
        markdown_link("Android in the Wild (AitW)", entries_by_title),
    ]

    lines = [
        "# Methods Timeline for Computer Use Agents",
        "",
        "Generated on 2026-03-28 (Asia/Tokyo) from the tracked method entries in `papers/methods/README.md`, then connected to benchmark, model, and safety reports already present in this repository.",
        "",
        "![Methods timeline](./figures/methods-timeline.svg)",
        "",
        "## How To Read This",
        "",
        "- The figure groups methods into five lanes: grounding, RL/post-training, data synthesis, planning/memory, and multi-agent orchestration.",
        "- Placement is based on when the work surfaced publicly, using preprint timing when available so the chronology stays comparable across later conference acceptances.",
        "- Each row in the timeline table links the method paper to the benchmark pressure, model wave, and safety lens that best explain why that method mattered.",
        "",
        "## Phase Shifts",
        "",
        f"- Before the method wave, benchmark pressure was set by {', '.join(pre_method_pressure)}. Those 2023 tasks explain why later methods obsess over web realism, mobile control, and long-horizon interaction.",
        "- 2024 is the first-control-loop phase: SeeAct, UFO, OS-Copilot, DigiRL, and Ponder & Press define the early playbook for grounding, mobile RL, and Windows/web interaction.",
        "- 2025 is the scaling phase: WebRL, AgentTrek, OS-Genesis, GUI-Reflection, PC Agent-E, Chain-of-Agents, and ComputerRL all try to solve the same bottleneck from different angles: too little high-quality interaction data and too little online adaptation.",
        "- 2026 pushes methods toward explicit structure: ActionEngine turns GUI execution into state-machine memory, GUI-GENESIS synthesizes verifiable training environments, and human-demonstration grounding pushes richer desktop supervision into the training loop.",
        "",
        "## Family Counts",
        "",
        "| Family | Count |",
        "| --- | --- |",
    ]

    for family in LANE_ORDER:
        lines.append(f"| {family} | {counts[family]} |")

    lines.extend(
        [
            "",
            "## Timeline Table",
            "",
            "| Phase | When | Method | Family | Key move | Benchmark pressure | Adjacent model wave | Safety lens | Report |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for item in timeline:
        benchmark_cell = "<br>".join(markdown_link(title, entries_by_title) for title in item.benchmark_context)
        model_cell = "<br>".join(markdown_link(title, entries_by_title) for title in item.model_context)
        safety_cell = "<br>".join(markdown_link(title, entries_by_title) for title in item.safety_context)
        report_link = f"[Open]({item.report_path.relative_to(REPORTS_ROOT)})"
        lines.append(
            f"| {phase_for(item)} | {item.time_label} | {markdown_link(item.title, entries_by_title)} | {item.family} | {item.key_move} | {benchmark_cell} | {model_cell} | {safety_cell} | {report_link} |"
        )

    lines.extend(["", "## Lane Notes", ""])
    family_titles: dict[str, list[str]] = defaultdict(list)
    for item in timeline:
        family_titles[item.family].append(item.title)
    for family in LANE_ORDER:
        if not family_titles[family]:
            continue
        lines.append(f"### {family}")
        lines.append(f"- {family_note(family, family_titles[family], entries_by_title)}")
        lines.append("")

    lines.extend(
        [
            "## Cross-Cutting Takeaways",
            "",
            "- Benchmark design and method design co-evolve. The timeline makes it clear that OSWorld, WebArena, AndroidWorld, and newer live-site or human-centric benchmarks are not side material; they are the pressure that explains the method wave.",
            "- The field broadens over time. Early methods are mostly about getting actions grounded at all; later methods care more about scaling data, stabilizing RL, building persistent memory, or coordinating multiple agents.",
            "- Safety lags capability but starts to intersect the method timeline in 2025-2026. AgentHarm, OS-Harm, RedTeamCUA, and VPI-Bench arrive after capability scaling is already underway, which suggests safety evaluation is becoming a co-equal axis only after strong capability pressure already exists.",
            "- The timeline also shows why later open models matter: works such as OpenCUA, ScaleCUA, Mobile-Agent-v3.5, and OmegaUse only make full sense when read against the method stack that improved grounding, trajectory generation, curriculum learning, and structured planning.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    timeline, entries_by_title = build_timeline_entries()
    TIMELINE_SVG.write_text(build_svg(timeline))
    TIMELINE_MD.write_text(build_markdown(timeline, entries_by_title))


if __name__ == "__main__":
    main()
