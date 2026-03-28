#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[3]
REPORTS_ROOT = ROOT / "reports" / "link-audit"
PAPER_REPORTS_ROOT = REPORTS_ROOT / "papers"

README_SPECS = [
    ("Survey Papers", ROOT / "papers" / "surveys" / "README.md"),
    ("Models and Architectures", ROOT / "papers" / "models" / "README.md"),
    ("Benchmarks and Datasets", ROOT / "papers" / "benchmarks" / "README.md"),
    ("Methods and Techniques", ROOT / "papers" / "methods" / "README.md"),
    ("Safety and Security", ROOT / "papers" / "safety" / "README.md"),
]

GENERIC_TAGS = {
    "survey",
    "model",
    "benchmark",
    "dataset",
    "method",
    "safety",
    "security",
    "comprehensive",
    "unified",
    "evaluation",
}

SECTION_SLUGS = {
    "Survey Papers": "survey-papers",
    "Models and Architectures": "models-and-architectures",
    "Benchmarks and Datasets": "benchmarks-and-datasets",
    "Methods and Techniques": "methods-and-techniques",
    "Safety and Security": "safety-and-security",
}

ARXIV_ABS_RE = re.compile(r"https?://arxiv\.org/abs/([0-9]+\.[0-9]+)")
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}

KIND_BY_SECTION = {
    "Survey Papers": "survey",
    "Models and Architectures": "model",
    "Benchmarks and Datasets": "benchmark",
    "Methods and Techniques": "method",
    "Safety and Security": "safety",
}

MANUAL_METADATA = {
    "AgentCPM-GUI: On-device Mobile Agent": {
        "title": "AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning",
        "summary": (
            "The paper targets practical on-device mobile control, where training data quality, "
            "cross-lingual diversity, and generalization remain major bottlenecks. It introduces "
            "an 8B mobile GUI agent trained with grounding-aware pre-training, supervised "
            "fine-tuning on curated Chinese and English trajectories, and reinforcement "
            "fine-tuning with GRPO. The design also uses a compact action space to keep output "
            "efficient on-device while aiming to improve planning and grounding in unfamiliar "
            "interfaces."
        ),
        "authors": [
            "Zhong Zhang",
            "Yaxi Lu",
            "Yikun Fu",
            "Yupeng Huo",
            "Shenzhi Yang",
            "Yesai Wu",
            "Han Si",
            "Xin Cong",
            "Haotian Chen",
            "Yankai Lin",
            "Jie Xie",
            "Wei Zhou",
        ],
        "published": "2025-06-02T07:30:29Z",
        "source_note": "Companion arXiv abstract used to deepen the code-only entry.",
    },
    "ShowUI: Vision-Language-Action Model for GUI Visual Agent": {
        "title": "ShowUI: One Vision-Language-Action Model for GUI Visual Agent",
        "summary": (
            "The paper argues that GUI assistants need a visual-first action model rather than a "
            "language-only layer on top of HTML or accessibility trees. ShowUI introduces three "
            "core ideas: UI-guided visual token selection to cut compute by exploiting screen "
            "structure, interleaved vision-language-action streaming to manage action history, "
            "and a carefully curated GUI instruction-following dataset with resampling to handle "
            "data imbalance. The overall goal is a single model that can perceive, reason, and "
            "act across GUI tasks with lower cost."
        ),
        "authors": [
            "Kevin Qinghong Lin",
            "Linjie Li",
            "Difei Gao",
            "Zhengyuan Yang",
            "Shiwei Wu",
            "Zechen Bai",
            "Weixian Lei",
            "Lijuan Wang",
            "Mike Zheng Shou",
        ],
        "published": "2024-11-26T14:29:47Z",
        "source_note": "Companion arXiv abstract used to complement the CVPR PDF link.",
    },
    "GUI-Actor: Coordinate-Free Visual Grounding": {
        "title": "GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents",
        "summary": (
            "The paper focuses on GUI grounding, a core weak point for VLM-based agents. Instead "
            "of predicting screen coordinates as text, GUI-Actor introduces a coordinate-free "
            "action head that aligns a dedicated ACTOR token with relevant visual patch tokens, "
            "allowing the model to propose one or more action regions in one pass. A grounding "
            "verifier then scores the candidates and selects the most plausible region for "
            "execution."
        ),
        "authors": [
            "Qianhui Wu",
            "Kanzhi Cheng",
            "Rui Yang",
            "Chaoyun Zhang",
            "Jianwei Yang",
            "Huiqiang Jiang",
            "Jian Mu",
            "Baolin Peng",
            "Bo Qiao",
            "Reuben Tan",
            "Si Qin",
            "Lars Liden",
        ],
        "published": "2025-06-03T17:59:08Z",
        "source_note": "Companion arXiv abstract used to complement the project-page entry.",
    },
    "GUI-Reflection: Self-Reflection for GUI Agents": {
        "title": "GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior",
        "summary": (
            "GUI-Reflection addresses a training blind spot in GUI automation: most multimodal "
            "GUI models learn from nearly error-free traces and therefore rarely learn recovery "
            "behavior. The framework adds explicit self-reflection and error-correction behavior "
            "across GUI-specific pre-training, supervised fine-tuning, and online reflection "
            "tuning. It also builds automated reflection data pipelines and a task suite aimed at "
            "reflection-oriented abilities rather than only grounding accuracy."
        ),
        "authors": [
            "Penghao Wu",
            "Shengnan Ma",
            "Bo Wang",
            "Jiaheng Yu",
            "Lewei Lu",
            "Ziwei Liu",
        ],
        "published": "2025-06-09T17:59:57Z",
        "source_note": "Companion arXiv abstract used because the project page was unstable during audit.",
    },
    "AI Agents Under Threat: Key Security Challenges and Future Pathways": {
        "title": "AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways",
        "summary": (
            "This survey studies AI-agent security through four knowledge gaps: unpredictable "
            "multi-step inputs, opaque internal execution, variable operating environments, and "
            "interaction with untrusted external entities. Its value is not a new defense but a "
            "structured threat map that explains why agent security is harder than single-turn "
            "LLM safety. The survey also highlights how existing defenses remain incomplete once "
            "agents begin planning, tool use, and long-horizon interaction."
        ),
        "authors": [
            "Zehang Deng",
            "Yongjian Guo",
            "Changzhou Han",
            "Wanlun Ma",
            "Junwu Xiong",
            "Sheng Wen",
            "Yang Xiang",
        ],
        "published": "2024-06-04T01:22:31Z",
        "source_note": "Companion arXiv survey metadata used to deepen the ACM entry.",
    },
    "Large Reasoning Models are Autonomous Jailbreak Agents": {
        "title": "Large Reasoning Models Are Autonomous Jailbreak Agents",
        "summary": (
            "The paper studies large reasoning models as autonomous jailbreak operators rather "
            "than only as target systems. It evaluates four reasoning models that receive a "
            "single system prompt and then plan and execute multi-turn jailbreaks without further "
            "supervision against nine target models. The reported result is an overall attack "
            "success rate of 97.14 percent across a 70-prompt harmful benchmark, framing "
            "reasoning capability itself as a safety regression if left unchecked."
        ),
        "authors": [
            "Thilo Hagendorff",
            "Erik Derner",
            "Nuria Oliver",
        ],
        "published": "2025-08-04T18:27:26Z",
        "source_note": "Companion arXiv abstract used to complement the Nature page.",
    },
    "GUI Odyssey: Cross-app Mobile Navigation": {
        "title": "GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices",
        "summary": (
            "GUIOdyssey pushes mobile evaluation beyond single-app tasks by building a cross-app "
            "dataset with 8,334 episodes, 212 apps, 1,357 app combinations, and an average of "
            "15.3 steps per episode. Each step includes semantic reasoning annotations to help "
            "agents learn long-horizon decision processes. The paper also introduces OdysseyAgent "
            "with a history resampler so the model can reuse prior screenshots and actions "
            "without letting context grow uncontrollably."
        ),
        "authors": [
            "Quanfeng Lu",
            "Wenqi Shao",
            "Zitao Liu",
            "Lingxiao Du",
            "Fanqing Meng",
            "Boxuan Li",
            "Botong Chen",
            "Siyuan Huang",
            "Kaipeng Zhang",
            "Ping Luo",
        ],
        "published": "2024-06-12T17:44:26Z",
        "source_note": "Replacement arXiv paper used because the repo URL resolves to the wrong target.",
    },
    "Ponder & Press: Advancing VLM Grounding": {
        "title": "Ponder & Press: Advancing Visual GUI Agent towards General Computer Control",
        "summary": (
            "Ponder & Press splits visual GUI control into two roles: an interpreter that turns "
            "user intent into a detailed action description and a GUI-specific locator that "
            "grounds the action precisely on screen. The framework is fully visual, avoiding HTML "
            "or accessibility-tree dependence, and it is positioned as a general computer control "
            "method across web, desktop, and mobile. The paper reports a 22.5 percent gain on "
            "ScreenSpot for the locator and strong results across offline and interactive GUI "
            "benchmarks."
        ),
        "authors": [
            "Yiqin Wang",
            "Haoji Zhang",
            "Jingqi Tian",
            "Yansong Tang",
        ],
        "published": "2024-12-02T08:35:31Z",
        "source_note": "Replacement arXiv paper used because the repo URL resolves to an unrelated paper.",
    },
    "EIA: Environmental Injection Attack": {
        "title": "EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage",
        "summary": (
            "EIA studies privacy leakage in generalist web agents when they interact with "
            "compromised websites. The paper defines a realistic threat model with two attacker "
            "goals, stealing specific personally identifiable information or exfiltrating the "
            "entire user request, and introduces an environmental injection attack tailored to "
            "the agent's visual and behavioral context. On realistic web tasks involving 177 "
            "PII-relevant steps, the paper reports up to 70 percent attack success for targeted "
            "PII leakage and 16 percent for leaking the full user request."
        ),
        "authors": [
            "Zeyi Liao",
            "Lingbo Mo",
            "Chejian Xu",
            "Mintong Kang",
            "Jiawei Zhang",
            "Chaowei Xiao",
            "Yuan Tian",
            "Bo Li",
            "Huan Sun",
        ],
        "published": "2024-09-17T15:49:44Z",
        "source_note": "Replacement arXiv paper used because the repo URL resolves to an unrelated paper.",
    },
    "AgentTrek Trajectories": {
        "title": "AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials",
        "summary": (
            "The linked artifact is the trajectory dataset side of AgentTrek. The paired method "
            "paper uses public web tutorials to synthesize high-quality trajectories by "
            "harvesting tutorial text, converting it into structured tasks, replaying the tasks "
            "in real environments with a VLM agent, and verifying outputs with a VLM evaluator. "
            "The dataset matters because it turns tutorial-like procedural knowledge into "
            "reusable training traces at low cost."
        ),
        "source_note": "Method-paper arXiv abstract used to deepen the project-page trajectory entry.",
    },
    "OS-Genesis Trajectories": {
        "title": "OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis",
        "summary": (
            "The linked artifact is the trajectory set produced by OS-Genesis. The paired method "
            "paper introduces reverse task synthesis, where agents first interact with the "
            "environment and only then derive high-quality task descriptions retrospectively. "
            "That reversal makes the data pipeline more scalable because it avoids depending on "
            "humans to author tasks before every trajectory is collected."
        ),
        "source_note": "Method-paper arXiv abstract used to deepen the project-page trajectory entry.",
    },
    "A Survey on Benchmarks of LLM-based GUI Agents": {
        "title": "A Survey on Benchmarks of LLM-based GUI Agents",
        "summary": (
            "This survey narrows in on benchmark design rather than the full GUI-agent stack. It "
            "organizes evaluation resources into three major families: grounding and question "
            "answering tasks, navigation and multi-step reasoning tasks, and open-world computer "
            "environments. That focus makes it a useful companion to broader surveys because it "
            "surfaces how different benchmarks reward different capabilities and where current "
            "evaluation still misses real deployment complexity."
        ),
        "source_note": "Accessible abstract-level signals were limited, so the report leans on repo notes and public index metadata.",
    },
    "ScreenSuite (HuggingFace)": {
        "title": "ScreenSuite",
        "summary": (
            "ScreenSuite positions itself as a unified benchmark suite rather than a single new "
            "dataset. Its value comes from packaging major GUI evaluation assets, including "
            "ScreenSpot variants and OSWorld, into one maintained interface so model and method "
            "papers can compare against a broader spread of tasks without assembling every "
            "benchmark by hand."
        ),
        "source_note": "GitHub repository metadata and repo-local notes were the main basis because no primary paper was linked.",
    },
    "Computer Agent Arena: Toward Human-Centric Evaluation and Analysis of Computer-Use Agents": {
        "title": "Computer Agent Arena: Toward Human-Centric Evaluation and Analysis of Computer-Use Agents",
        "summary": (
            "Computer Agent Arena studies the gap between benchmark scores and actual user preference by building a "
            "human-centric evaluation arena for computer-use agents. The benchmark collects 2,201 high-quality human "
            "votes comparing 12 agents and shows that rankings based on user preference can differ sharply from "
            "rankings on static capability benchmarks. The paper argues that correctness dominates preference, but "
            "self-correction behavior and the quality of agent-human interaction materially shape which agent people "
            "would actually choose."
        ),
        "authors": [
            "Ameesh Shah",
            "Jiaxin Cui",
            "Tianbao Xie",
            "Ari Holtzman",
            "Caiming Xiong",
            "Mohit Bansal",
            "Robin Jia",
        ],
        "published": "2026-01-15T00:00:00Z",
        "source_note": "Primary OpenReview abstract and metadata were used because this entry is not available through the arXiv API.",
    },
    "CUA-Suite: Expert Trajectories and Pixel-Precise Grounding for Computer-use Agents": {
        "title": "CUA-Suite: Expert Trajectories and Pixel-Precise Grounding for Computer-use Agents",
        "summary": (
            "CUA-Suite packages dense desktop supervision for computer-use agents by combining UI understanding, "
            "grounding, and trajectory data into one suite. It spans 87 applications, 56K screenshots, and more "
            "than 5 million UI-element annotations, plus roughly 10,000 expert-demonstrated tasks with detailed "
            "reasoning traces. The paper positions this expert-driven corpus as a way to push current action models "
            "beyond consumer-style interfaces toward professional desktop software."
        ),
        "authors": [
            "Dongxu Li",
            "Yizheng Pan",
            "Guangchen Song",
            "Yu-Qing Xie",
            "Zeyi Li",
            "Weixin Chen",
            "Yizhe Yang",
            "Tong Xiao",
            "Jianmin Bao",
        ],
        "published": "2026-03-01T00:00:00Z",
        "source_note": "Primary OpenReview abstract and metadata were used because this entry is not available through the arXiv API.",
    },
}


@dataclass
class DetailBlock:
    heading: str
    items: list[str] = field(default_factory=list)
    prose: list[str] = field(default_factory=list)


@dataclass
class RepoEntry:
    title: str
    section: str
    source_path: str
    source_line: int
    description: str
    tags: list[str]
    meta: dict[str, str]
    links: dict[str, tuple[str, str]]
    detail_blocks: list[DetailBlock]

    @property
    def source_location(self) -> str:
        return f"{self.source_path}:{self.source_line}"


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip().strip("-").strip()


def normalize_title(text: str) -> str:
    text = strip_md(text).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def sentence_split(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if not clean:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", clean)
    return [part.strip() for part in parts if part.strip()]


def cap(text: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    clipped = text[: limit - 3].rsplit(" ", 1)[0].rstrip(" ,;:")
    return f"{clipped}..."


def sentence_fragment(text: str) -> str:
    return strip_md(text).rstrip(" .;:")


def markdown_cell_text(raw: str) -> str:
    return strip_md(raw).strip()


def link_markdown(link: tuple[str, str]) -> str:
    label, url = link
    return f"[{label}]({url})"


def primary_link_markdown(entry: RepoEntry) -> str:
    for key in ["Link", "Code", "Website", "Model"]:
        link = entry.links.get(key)
        if link:
            return link_markdown(link)
    return ""


def primary_link_type(entry: RepoEntry, snapshot: dict[str, str]) -> str:
    existing = markdown_cell_text(snapshot.get("Primary link type", ""))
    if existing:
        return existing
    for key, kind in [("Link", "link"), ("Code", "code"), ("Website", "website"), ("Model", "model")]:
        if key in entry.links:
            return kind
    return "unknown"


def date_or_venue(entry: RepoEntry) -> str:
    return entry.meta.get("Venue") or entry.meta.get("Date") or "Not stated in local entry"


def focus_tags(entry: RepoEntry) -> str:
    if not entry.tags:
        return "Not stated in local entry"
    return " ".join(f"`{tag}`" for tag in entry.tags)


def report_center_of_gravity(entry: RepoEntry, snapshot: dict[str, str]) -> str:
    existing = markdown_cell_text(snapshot.get("Center of gravity", ""))
    if existing:
        return existing
    terms = feature_terms(entry)
    if terms:
        return ", ".join(terms[:3])
    return "repo-curated summary"


def supporting_artifact_rows(entry: RepoEntry) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    if entry.links.get("Code"):
        rows.append(("Code repo", link_markdown(entry.links["Code"])))
    if entry.links.get("Website"):
        rows.append(("Project page", link_markdown(entry.links["Website"])))
    if entry.links.get("Model"):
        rows.append(("Model hub", link_markdown(entry.links["Model"])))

    extras = []
    for key, link in entry.links.items():
        if key in {"Link", "Code", "Website", "Model"}:
            continue
        extras.append(link_markdown(link))
    if extras:
        rows.append(("Related assets", "; ".join(extras[:6])))
    return rows


def build_artifact_section(entry: RepoEntry) -> str:
    lines = ["## Code and Supporting Artifacts", ""]
    code_link = entry.links.get("Code")
    website_link = entry.links.get("Website")
    model_link = entry.links.get("Model")

    if code_link:
        lines.append(f"- Code repository: {link_markdown(code_link)}")
    else:
        lines.append("- Code repository: no dedicated code link is currently tracked in the repo entry.")

    if website_link:
        lines.append(f"- Project page or benchmark site: {link_markdown(website_link)}")
    if model_link:
        lines.append(f"- Model weights or hub: {link_markdown(model_link)}")

    extra_assets = []
    for key, link in entry.links.items():
        if key in {"Link", "Code", "Website", "Model"}:
            continue
        extra_assets.append(f"{key}: {link_markdown(link)}")
    if extra_assets:
        lines.append(f"- Other tracked assets: {'; '.join(extra_assets[:6])}")

    primary_kind = primary_link_type(entry, {})
    if primary_kind == "code":
        lines.append("- Primary source note: this repo entry points first to code rather than to a paper landing page.")

    return "\n".join(lines)


def parse_readme_block(path: Path, section: str) -> list[RepoEntry]:
    lines = path.read_text().splitlines()
    entries: list[RepoEntry] = []
    i = 0
    while i < len(lines):
        heading_match = re.match(r"^(#{3,4})\s+(.*)$", lines[i])
        if not heading_match:
            i += 1
            continue

        level = len(heading_match.group(1))
        title = heading_match.group(2).strip()
        start_line = i + 1
        i += 1
        block: list[str] = []
        while i < len(lines):
            next_heading = re.match(r"^(#{3,4})\s+(.*)$", lines[i])
            if next_heading:
                break
            block.append(lines[i])
            i += 1

        if not any("**Tags**" in line for line in block):
            continue
        entries.append(parse_entry(title, section, path, start_line, block))
    return entries


def parse_entry(
    title: str, section: str, path: Path, start_line: int, block: list[str]
) -> RepoEntry:
    meta: dict[str, str] = {}
    links: dict[str, tuple[str, str]] = {}
    tags: list[str] = []
    detail_blocks: list[DetailBlock] = []
    description = ""

    i = 0
    while i < len(block):
        line = block[i].rstrip()
        meta_match = re.match(r"^- \*\*(.+?)\*\*:\s*(.*)$", line)
        if not meta_match:
            break
        key = meta_match.group(1).strip()
        value = meta_match.group(2).strip()
        meta[key] = strip_md(value)
        if key == "Tags":
            tags = re.findall(r"`([^`]+)`", value)
        link_match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", value)
        if link_match:
            links[key] = (link_match.group(1), link_match.group(2))
        i += 1

    while i < len(block) and not block[i].strip():
        i += 1

    description_lines: list[str] = []
    while i < len(block):
        line = block[i].strip()
        if not line:
            break
        if line == "---" or line.startswith("## "):
            break
        if re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", line):
            break
        description_lines.append(strip_md(line))
        i += 1
    description = " ".join(description_lines).strip()

    current: DetailBlock | None = None
    while i < len(block):
        line = block[i].strip()
        i += 1
        if not line or line == "---":
            continue
        block_match = re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", line)
        if block_match:
            current = DetailBlock(block_match.group(1).strip())
            rest = strip_md(block_match.group(2).strip())
            if rest:
                current.prose.append(rest)
            detail_blocks.append(current)
            continue
        if current is None:
            continue
        bullet = re.sub(r"^[-*]\s+", "", line)
        bullet = re.sub(r"^\d+\.\s+", "", bullet)
        bullet = strip_md(bullet)
        if not bullet:
            continue
        if re.match(r"^[-*]\s+|^\d+\.\s+", line):
            current.items.append(bullet)
        else:
            current.prose.append(bullet)

    return RepoEntry(
        title=title,
        section=section,
        source_path=str(path.relative_to(ROOT)),
        source_line=start_line,
        description=description,
        tags=tags,
        meta=meta,
        links=links,
        detail_blocks=detail_blocks,
    )


def load_repo_entries() -> dict[str, RepoEntry]:
    entries: dict[str, RepoEntry] = {}
    for section, path in README_SPECS:
        for entry in parse_readme_block(path, section):
            entries[entry.source_location] = entry
    return entries


def parse_snapshot(text: str) -> dict[str, str]:
    match = re.search(
        r"## Snapshot\n\n\| Field \| Detail \|\n\| --- \| --- \|\n(.*?)(?:\n## |\Z)",
        text,
        re.S,
    )
    if not match:
        return {}
    snapshot: dict[str, str] = {}
    for line in match.group(1).splitlines():
        row_match = re.match(r"^\| (.*?) \| (.*?) \|$", line.strip())
        if row_match:
            snapshot[row_match.group(1).strip()] = row_match.group(2).strip()
    return snapshot


def load_current_reports() -> list[dict]:
    reports = []
    for path in sorted(PAPER_REPORTS_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        title_match = re.search(r"^# (.+)$", text, re.M)
        if not title_match or "## Snapshot" not in text:
            continue
        cut_points = [pos for pos in (text.find("## Quick Read"), text.find("## Visual Frame")) if pos != -1]
        cut_at = min(cut_points) if cut_points else len(text)
        prefix = text[:cut_at].rstrip() + "\n\n"
        note_match = re.search(r"(^> Link mismatch:.*(?:\n>.*)*)", prefix, re.M)
        reports.append(
            {
                "path": path,
                "title": title_match.group(1).strip(),
                "text": text,
                "snapshot": parse_snapshot(text),
                "mismatch_note": note_match.group(1).strip() if note_match else "",
            }
        )
    return reports


def load_metadata() -> dict[str, dict]:
    arxiv_path = Path("/tmp/awesome_computer_use_arxiv.json")
    items = json.loads(arxiv_path.read_text()) if arxiv_path.exists() else []
    by_title: dict[str, dict] = {}
    for item in items:
        by_title[normalize_title(item["title"])] = item
    for title, extra in MANUAL_METADATA.items():
        if "authors" not in extra:
            extra["authors"] = []
        by_title[normalize_title(title)] = {
            "title": extra.get("title", title),
            "summary": extra.get("summary", ""),
            "authors": extra.get("authors", []),
            "published": extra.get("published", ""),
            "source_note": extra.get("source_note", ""),
        }
    return by_title


def arxiv_id_from_text(text: str) -> str | None:
    match = ARXIV_ABS_RE.search(text or "")
    return match.group(1) if match else None


def fetch_arxiv_metadata(arxiv_id: str) -> dict:
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        root = ET.fromstring(urllib.request.urlopen(url, timeout=30).read())
    except Exception:
        return {}

    entry = root.find("atom:entry", ARXIV_NS)
    if entry is None:
        return {}

    title = entry.findtext("atom:title", default="", namespaces=ARXIV_NS)
    summary = entry.findtext("atom:summary", default="", namespaces=ARXIV_NS)
    published = entry.findtext("atom:published", default="", namespaces=ARXIV_NS)
    authors = [
        author.findtext("atom:name", default="", namespaces=ARXIV_NS)
        for author in entry.findall("atom:author", ARXIV_NS)
    ]
    return {
        "title": " ".join(title.split()),
        "summary": " ".join(summary.split()),
        "authors": [author for author in authors if author],
        "published": published,
        "source_note": "Primary arXiv abstract metadata was fetched live from the linked paper page.",
    }


def pick_metadata(entry: RepoEntry, title: str, snapshot: dict[str, str], metadata: dict[str, dict]) -> dict:
    candidates = [
        title,
        markdown_cell_text(snapshot.get("Actual target", "")),
        markdown_cell_text(snapshot.get("Intended paper", "")),
        markdown_cell_text(snapshot.get("Repo entry", "")),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        item = metadata.get(normalize_title(candidate))
        if item:
            return item

    urls = [link[1] for link in entry.links.values()]
    actual_target = snapshot.get("Actual target", "")
    actual_target_match = re.search(r"\((https?://[^)]+)\)", actual_target)
    if actual_target_match:
        urls.append(actual_target_match.group(1))
    for url in urls:
        arxiv_id = arxiv_id_from_text(url)
        if not arxiv_id:
            continue
        item = fetch_arxiv_metadata(arxiv_id)
        if item:
            metadata[normalize_title(item["title"])] = item
            metadata.setdefault(normalize_title(title), item)
            return item
    return {}


def all_detail_items(entry: RepoEntry) -> list[str]:
    items: list[str] = []
    for block in entry.detail_blocks:
        items.extend(block.items)
        items.extend(block.prose)
    return [item for item in items if item]


def select_detail_items(entry: RepoEntry, headings: Iterable[str], limit: int = 4) -> list[str]:
    selected: list[str] = []
    heading_lookup = {block.heading.lower(): block for block in entry.detail_blocks}
    for heading in headings:
        block = heading_lookup.get(heading.lower())
        if not block:
            continue
        for item in block.items + block.prose:
            if item not in selected:
                selected.append(item)
            if len(selected) >= limit:
                return selected
    return selected


def summary_evidence(summary: str, limit: int = 4) -> list[str]:
    evidence = []
    for sentence in sentence_split(summary):
        if re.search(r"\d", sentence) or "%" in sentence:
            evidence.append(sentence)
        if len(evidence) >= limit:
            break
    return evidence


def summary_supporting_points(summary: str, limit: int = 3) -> list[str]:
    points = []
    for sentence in sentence_split(summary):
        cleaned = restyle_sentence(sentence)
        if cleaned not in points:
            points.append(cleaned)
        if len(points) >= limit:
            break
    return points


def feature_terms(entry: RepoEntry) -> list[str]:
    terms = [tag for tag in entry.tags if tag not in GENERIC_TAGS]
    for block in entry.detail_blocks:
        if block.heading.lower() not in {"statistics", "performance", "results", "metrics"}:
            terms.append(block.heading.lower())
    seen = set()
    ordered = []
    for term in terms:
        clean = strip_md(term)
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            ordered.append(clean)
    return ordered


def lower_lead(text: str) -> str:
    if not text:
        return text
    if len(text) > 1 and text[:2].isupper():
        return text
    return text[0].lower() + text[1:]


def restyle_sentence(sentence: str) -> str:
    sentence = sentence.strip()
    replacements = {
        "This paper introduces": "The paper introduces",
        "In this work, we develop": "The paper develops",
        "In this work, we present": "The paper presents",
        "In this work, we propose": "The paper proposes",
        "We propose": "The authors propose",
        "We present": "The authors present",
        "We develop": "The authors develop",
        "Experiments demonstrate": "The reported experiments indicate",
        "Extensive experiments show": "The reported evaluation shows",
    }
    for old, new in replacements.items():
        if sentence.startswith(old):
            return new + sentence[len(old) :]
    return sentence


def build_executive_summary(entry: RepoEntry, paper: dict, section_kind: str) -> str:
    parts = []
    if entry.description:
        parts.append(entry.description)
    summary = paper.get("summary", "")
    sentences = [restyle_sentence(s) for s in sentence_split(summary)]
    for sentence in sentences[:3]:
        if sentence not in parts:
            parts.append(sentence)
    if section_kind == "benchmark" and not any("benchmark" in p.lower() for p in parts):
        parts.append("The benchmark or dataset is the main contribution rather than a new agent policy.")
    if section_kind == "survey" and not any("survey" in p.lower() for p in parts):
        parts.append("Its main contribution is a field map, taxonomy, and synthesis rather than a new model.")
    text = " ".join(parts)
    return cap(text, 950)


def build_quick_read(entry: RepoEntry, novelty: str, evidence: str, gap: str) -> str:
    problem = cap(entry.description or "The paper targets a concrete bottleneck in computer-use agents.", 140)
    return "\n".join(
        [
            "## Quick Read",
            "",
            "| Lens | Read |",
            "| --- | --- |",
            f"| Problem pressure | {problem} |",
            f"| Most novel move | {cap(novelty, 140)} |",
            f"| Strongest evidence | {cap(evidence, 140)} |",
            f"| Main caveat | {cap(gap, 140)} |",
        ]
    )


def build_novelty(entry: RepoEntry, paper: dict, section_kind: str) -> list[str]:
    terms = feature_terms(entry)
    summary = paper.get("summary", "")
    evidence = summary_evidence(summary, limit=2)
    top_items = select_detail_items(
        entry,
        [
            "Key Innovations",
            "Contributions",
            "Features",
            "Components",
            "Approach",
            "Pipeline",
            "Training Pipeline",
            "Framework Components",
            "Agent Capabilities",
        ],
        limit=3,
    )
    bullets: list[str] = []
    if section_kind == "survey":
        focus = ", ".join(terms[:3]) if terms else "benchmarks, architectures, and training"
        bullets.append(
            f"The novelty is synthetic rather than model-side: the paper tries to stabilize a fast-moving literature around {focus}."
        )
    elif section_kind == "benchmark":
        focus = ", ".join(terms[:3]) if terms else "task design, coverage, and evaluation protocol"
        bullets.append(
            f"The main novelty sits in the evaluation surface itself, especially its emphasis on {focus}."
        )
    elif section_kind == "method":
        focus = top_items[0] if top_items else entry.description
        bullets.append(
            f"The method's clearest new move is {lower_lead(sentence_fragment(focus)) if focus else 'a new training or inference recipe'}."
        )
    elif section_kind == "safety":
        focus = ", ".join(terms[:3]) if terms else "agent threat models and misuse evaluation"
        bullets.append(
            f"The paper turns general security concern into an operational agent-risk story centered on {focus}."
        )
    else:
        focus = top_items[0] if top_items else (terms[0] if terms else entry.description)
        bullets.append(
            f"The architecture-level novelty is most visible in {lower_lead(sentence_fragment(focus)) if focus else 'how perception, reasoning, and action are combined'}."
        )

    for item in top_items[1:3]:
        bullets.append(f"It also stands out for {lower_lead(sentence_fragment(item))}.")
    if len(bullets) < 3:
        for point in summary_supporting_points(summary, limit=3):
            if point not in bullets:
                bullets.append(point)
            if len(bullets) >= 3:
                break
    if evidence:
        bullets.append(
            f"The novelty claim is not only conceptual; the summary ties it to reported evidence such as {cap(evidence[0], 120).lower()}."
        )
    return bullets[:3]


def build_contributions(entry: RepoEntry, paper: dict, section_kind: str) -> list[str]:
    items = select_detail_items(
        entry,
        [
            "Key Innovations",
            "Contributions",
            "Features",
            "Capabilities",
            "Components",
            "Approach",
            "Training Pipeline",
            "Pipeline Phases",
            "Framework Components",
            "Threat Categories",
            "Metrics",
            "Key Findings",
            "Includes",
            "Statistics",
        ],
        limit=6,
    )
    if not items:
        items = all_detail_items(entry)[:6]

    bullets = []
    for item in items[:5]:
        bullets.append(item)

    if not bullets and entry.description:
        bullets.append(entry.description)
    if len(bullets) < 4:
        for point in summary_supporting_points(paper.get("summary", ""), limit=4):
            if point not in bullets:
                bullets.append(point)
            if len(bullets) >= 4:
                break

    if section_kind == "benchmark" and not any("task" in bullet.lower() or "benchmark" in bullet.lower() for bullet in bullets):
        bullets.append("Defines a reusable benchmark surface that later model and method papers can optimize against.")
    if section_kind == "survey" and not any("taxonomy" in bullet.lower() or "survey" in bullet.lower() for bullet in bullets):
        bullets.append("Provides a structured taxonomy that helps compare papers that would otherwise look incomparable.")
    if section_kind == "safety" and not any("attack" in bullet.lower() or "benchmark" in bullet.lower() for bullet in bullets):
        bullets.append("Turns agent safety into concrete scenarios, attack surfaces, or measurable guardrail objectives.")
    return bullets[:5]


def build_framework(entry: RepoEntry, paper: dict, section_kind: str) -> list[str]:
    items = select_detail_items(
        entry,
        [
            "Framework Components",
            "Components",
            "Pipeline",
            "Training Pipeline",
            "Pipeline Phases",
            "Approach",
            "Features",
            "Agent Capabilities",
        ],
        limit=5,
    )
    summary = paper.get("summary", "")
    bullets: list[str] = []
    for item in items[:4]:
        bullets.append(item)

    if not bullets:
        if section_kind == "survey":
            bullets.append("The framework is conceptual: organize prior work into categories, then compare assumptions, metrics, and open problems.")
        elif section_kind == "benchmark":
            bullets.append("The framework is benchmark-centric: define tasks, environments, and success criteria so later agent work can be evaluated on common ground.")
        elif section_kind == "safety":
            bullets.append("The framework centers on a threat model, an evaluation setup, and a concrete criterion for attack or defense success.")
        else:
            bullets.append("The framework combines visual observation, decision making, and action execution into a reusable control loop.")

    if summary and section_kind == "method" and not any("training" in bullet.lower() or "pipeline" in bullet.lower() for bullet in bullets):
        bullets.append("The abstract indicates that the method should be read as a pipeline change rather than only a bigger base model.")
    if len(bullets) < 3:
        for point in summary_supporting_points(summary, limit=3):
            if point not in bullets:
                bullets.append(point)
            if len(bullets) >= 3:
                break
    return bullets[:4]


def build_evidence(entry: RepoEntry, paper: dict, section_kind: str) -> list[str]:
    bullets = select_detail_items(
        entry,
        [
            "Performance",
            "Statistics",
            "Results",
            "Current SOTA",
            "Metrics",
            "Key Findings",
            "Improvements over Mind2Web",
        ],
        limit=5,
    )
    for sentence in summary_evidence(paper.get("summary", ""), limit=4):
        if sentence not in bullets:
            bullets.append(sentence)
        if len(bullets) >= 5:
            break
    if len(bullets) < 2:
        for sentence in summary_supporting_points(paper.get("summary", ""), limit=3):
            if sentence not in bullets:
                bullets.append(sentence)
            if len(bullets) >= 3:
                break

    if not bullets:
        if section_kind == "survey":
            bullets.append("Evidence here is mostly comparative coverage, taxonomy quality, and how clearly the survey surfaces unresolved tensions in the literature.")
        elif section_kind == "benchmark":
            bullets.append("The evidence is the benchmark design itself: coverage, realism, evaluation protocol, and how hard current agents find the task surface.")
        elif section_kind == "safety":
            bullets.append("Safety evidence is typically attack success rate, refusal behavior, or guardrail performance rather than raw task completion.")
        else:
            bullets.append("The evidence is mainly benchmark performance plus qualitative signs that the proposed design improves control reliability.")
    return bullets[:5]


def platform_phrase(entry: RepoEntry) -> str:
    tags = set(entry.tags)
    if {"mobile", "android", "phone"} & tags:
        return "mobile interfaces, app transitions, and version drift"
    if {"web", "live-sites"} & tags:
        return "live websites, layout drift, and prompt-injection exposure"
    if {"desktop", "windows", "macos"} & tags:
        return "desktop heterogeneity, long workflows, and OS-level side effects"
    if {"grounding", "screenspot"} & tags:
        return "precise element localization and recovery after grounding misses"
    return "long-horizon transfer, recovery behavior, and distribution shift"


def build_gaps(entry: RepoEntry, snapshot: dict[str, str], section_kind: str) -> list[str]:
    audit_status = markdown_cell_text(snapshot.get("Audit status", "")).lower()
    bullets = []
    if audit_status in {"code-only", "project-page", "pdf-light-read", "script-blocked"}:
        bullets.append(
            "The accessible source basis is thinner than a full paper review, so some claims rest on project metadata, repo notes, or abstract-level evidence rather than a complete methods read."
        )
    if section_kind == "benchmark":
        bullets.append(
            f"Benchmarks can overstate progress if agents learn the evaluator rather than the underlying task skill, especially around {platform_phrase(entry)}."
        )
        bullets.append("Even a strong benchmark can miss interruptions, login drift, or real user messiness if the environment is too clean.")
    elif section_kind == "survey":
        bullets.append("As a survey, it depends on literature coverage and taxonomy quality more than on new experimental validation.")
        bullets.append("Fast-moving agent releases can age the benchmark map or architecture taxonomy quickly.")
    elif section_kind == "safety":
        bullets.append("One attack family or benchmark never exhausts the deployment threat surface for computer-use agents.")
        bullets.append(f"Transfer remains uncertain across stacks, especially once the interface shifts toward {platform_phrase(entry)}.")
    elif section_kind == "method":
        bullets.append("Method gains can be entangled with data quality, environment choice, or evaluator assumptions if ablations are thin.")
        bullets.append(f"Better grounding or reflection does not automatically solve {platform_phrase(entry)}.")
    else:
        bullets.append(f"Strong model-side results still leave open whether the gains survive {platform_phrase(entry)}.")
        bullets.append("A stronger agent core does not by itself guarantee safer planning, error recovery, or tool-use discipline.")
    return bullets[:4]


def build_improvements(entry: RepoEntry, section_kind: str) -> list[str]:
    phrase = platform_phrase(entry)
    bullets = []
    if section_kind == "survey":
        bullets.extend(
            [
                "Turn the survey into a living benchmark matrix or updateable appendix so it stays useful as the field changes.",
                "Separate capability, safety, and deployment-readiness lenses more sharply so the taxonomy can guide applied system design.",
                "Add clearer links between benchmark choice and the failure modes practitioners should expect in real deployments.",
            ]
        )
    elif section_kind == "benchmark":
        bullets.extend(
            [
                f"Broaden environment drift and task diversity so agents cannot overfit a narrow evaluator or a fixed slice of {phrase}.",
                "Add richer partial-credit and failure-taxonomy reporting, not only binary success.",
                "Pair benchmark scores with human-grounded difficulty and usability checks so the suite better reflects real workflows.",
            ]
        )
    elif section_kind == "safety":
        bullets.extend(
            [
                "Expand the threat coverage beyond one attack family into cross-platform, human-in-the-loop, and defense-cost scenarios.",
                "Connect the benchmark or analysis to deployable mitigations such as takeover triggers, isolation policies, and audit logging.",
                "Measure the usability cost of safety controls so defenses can be judged as systems decisions, not only as refusals.",
            ]
        )
    elif section_kind == "method":
        bullets.extend(
            [
                "Run stronger ablations so each training or inference component carries a clearly attributable gain.",
                f"Stress-test the method on longer workflows and harder transfer settings involving {phrase}.",
                "Publish sharper failure analyses for the cases where the method improves one stage of control but still fails end-to-end.",
            ]
        )
    else:
        bullets.extend(
            [
                "Test the model under longer-horizon and more safety-sensitive workloads rather than only narrow benchmark slices.",
                f"Separate perception gains from planning gains with clearer studies over {phrase}.",
                "Report richer failure modes, especially around recovery after an early grounding or reasoning error.",
            ]
        )
    return bullets[:4]


def build_why_it_matters(entry: RepoEntry, section_kind: str) -> list[str]:
    if section_kind == "survey":
        return [
            "This entry matters because the repository is large enough that a good field map saves readers from rediscovering the same bottlenecks paper by paper.",
            "It also helps turn the repo from a list of links into a navigable research landscape.",
        ]
    if section_kind == "benchmark":
        return [
            "This entry matters because benchmarks decide what the rest of the repo gets rewarded for improving.",
            "It is part of the evaluative scaffolding that lets model and method papers claim progress in a comparable way.",
        ]
    if section_kind == "safety":
        return [
            "This entry matters because stronger computer-use capability without a matching safety story creates an immediate operational risk.",
            "It gives the repo a concrete threat or guardrail lens instead of only capability metrics.",
        ]
    if section_kind == "method":
        return [
            "This entry matters because training and inference design often determine whether a capable base model can actually become a useful agent.",
            "It usually connects high-level capability claims to the data, tuning, or orchestration choices that make them work.",
        ]
    return [
        "This entry matters because architecture choices determine whether GUI understanding becomes reliable control rather than passive description.",
        "It also acts as a capability anchor that other benchmark and method papers in the repo can be read against.",
    ]


def shared_theme(entry: RepoEntry, other: RepoEntry) -> str:
    tags = set(entry.tags) & set(other.tags)
    if "grounding" in tags:
        return "shared emphasis on precise UI localization and action placement."
    if {"mobile", "android", "phone"} & tags:
        return "shared focus on mobile GUI control and cross-app interaction constraints."
    if {"web", "live-sites"} & tags:
        return "shared focus on web-agent realism, dynamic pages, or browser-side risk."
    if {"desktop", "windows", "macos"} & tags:
        return "shared desktop or OS-level interaction surface."
    if {"safety", "security", "jailbreak", "attack"} & tags:
        return "shared concern with adversarial behavior, guardrails, or deployment risk."
    if {"benchmark", "dataset"} & tags:
        return "shared evaluative role in defining what progress means."
    if KIND_BY_SECTION[entry.section] == "survey":
        return f"this report helps frame the {other.section.lower()} side of the repo."
    if KIND_BY_SECTION[other.section] == "survey":
        return f"the survey provides context for the {entry.section.lower()} issues highlighted here."
    if entry.section != other.section:
        if KIND_BY_SECTION[entry.section] == "model" and KIND_BY_SECTION[other.section] == "benchmark":
            return "benchmark pressure here is a natural proving ground for the model."
        if KIND_BY_SECTION[entry.section] == "method" and KIND_BY_SECTION[other.section] in {"model", "benchmark"}:
            return "the method complements the model or benchmark side of the same research cluster."
        if KIND_BY_SECTION[entry.section] == "safety" and KIND_BY_SECTION[other.section] in {"model", "benchmark", "method"}:
            return "it gives a safety read on the capability work happening in the neighboring entry."
    if entry.section == other.section:
        return f"neighbor entry in the same {entry.section.lower()} cluster."
    return "the papers sit in the same local research cluster in this repository."


def connection_score(entry: RepoEntry, other: RepoEntry) -> int:
    if entry.title == other.title:
        return -10
    score = 0
    shared = set(entry.tags) & set(other.tags)
    score += len(shared) * 4
    if entry.section == other.section:
        score += 1
    if KIND_BY_SECTION[entry.section] != KIND_BY_SECTION[other.section]:
        score += 2
    focus_overlap = {"mobile", "android", "web", "desktop", "windows", "macos", "grounding", "safety", "security"} & shared
    score += len(focus_overlap) * 3
    return score


def build_connections(current: RepoEntry, all_entries: list[RepoEntry]) -> list[tuple[RepoEntry, str]]:
    ranked = sorted(
        (other for other in all_entries if other.title != current.title),
        key=lambda other: connection_score(current, other),
        reverse=True,
    )
    picked: list[tuple[RepoEntry, str]] = []
    seen_titles = set()
    for other in ranked:
        if other.title in seen_titles:
            continue
        reason = shared_theme(current, other)
        picked.append((other, reason))
        seen_titles.add(other.title)
        if len(picked) >= 4:
            break
    return picked


def relative_report_link(from_path: Path, target_path: Path) -> str:
    return os.path.relpath(target_path, start=from_path.parent)


def slug_for_title(title: str) -> str:
    text = title.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def mermaid_safe(text: str, limit: int = 64) -> str:
    text = cap(strip_md(text), limit)
    return text.replace('"', "'")


def build_visual_frame(problem: str, novelty: str, framework: str, evidence: str, gap: str, improve: str) -> str:
    return "\n".join(
        [
            "## Visual Frame",
            "",
            "```mermaid",
            "flowchart LR",
            f'  Problem["Problem: {mermaid_safe(problem)}"] --> Novelty["Novelty: {mermaid_safe(novelty)}"]',
            f'  Novelty --> Framework["Framework: {mermaid_safe(framework)}"]',
            f'  Framework --> Evidence["Evidence: {mermaid_safe(evidence)}"]',
            f'  Evidence --> Gap["Gap: {mermaid_safe(gap)}"]',
            f'  Gap --> Next["Next: {mermaid_safe(improve)}"]',
            "  classDef insight fill:#dbeafe,stroke:#2563eb,color:#0f172a;",
            "  classDef risk fill:#fee2e2,stroke:#dc2626,color:#7f1d1d;",
            "  classDef next fill:#dcfce7,stroke:#16a34a,color:#14532d;",
            "  class Problem,Novelty,Framework insight;",
            "  class Evidence insight;",
            "  class Gap risk;",
            "  class Next next;",
            "```",
        ]
    )


def build_analysis_map(contrib: str, framework: str, evidence: str, gap: str, improve: str) -> str:
    return "\n".join(
        [
            "## Analysis Map",
            "",
            "```mermaid",
            "flowchart TB",
            '  subgraph Adds["What This Work Adds"]',
            f'    C1["Contribution: {mermaid_safe(contrib)}"]',
            f'    C2["Mechanism: {mermaid_safe(framework)}"]',
            f'    C3["Evidence: {mermaid_safe(evidence)}"]',
            "  end",
            '  subgraph Watch["What Still Needs Work"]',
            f'    W1["Gap: {mermaid_safe(gap)}"]',
            f'    W2["Improve: {mermaid_safe(improve)}"]',
            "  end",
            "  C1 --> C2 --> C3 --> W1 --> W2",
            "  classDef add fill:#ecfccb,stroke:#65a30d,color:#365314;",
            "  classDef watch fill:#fff7ed,stroke:#ea580c,color:#7c2d12;",
            "  class C1,C2,C3 add;",
            "  class W1,W2 watch;",
            "```",
        ]
    )


def bullet_section(title: str, bullets: list[str]) -> str:
    lines = [f"## {title}", ""]
    for bullet in bullets:
        lines.append(f"- {bullet}")
    return "\n".join(lines)


def build_source_basis(snapshot: dict[str, str], paper: dict, entry: RepoEntry) -> str:
    audit_status = markdown_cell_text(snapshot.get("Audit status", ""))
    basis = []
    if paper.get("summary"):
        if paper.get("source_note"):
            basis.append(f"- Primary basis: {paper['source_note']}")
        else:
            basis.append("- Primary basis: abstract-level paper metadata plus the repo-local notes in the source Markdown file.")
    else:
        basis.append("- Primary basis: repo-local notes, link-audit metadata, and project/repository metadata available during the audit.")
    if audit_status:
        if audit_status == "limited-access":
            basis.append("- Audit access note: The linked source had limited direct readability during the audit, so the report leans more heavily on accessible metadata and repo context.")
        elif audit_status == "code-only":
            basis.append("- Audit access note: The repo links code rather than a primary paper page, so evidence quality depends on repository documentation and companion metadata.")
        elif audit_status == "project-page":
            basis.append("- Audit access note: The repo points to a project page, so the report blends page metadata with repo-local notes and, where available, companion abstract-level metadata.")
        elif audit_status == "pdf-light-read":
            basis.append("- Audit access note: The PDF was resolved, but this report favors abstract-level metadata and repo-curated notes instead of pretending to be a full manual paper review.")
        elif audit_status == "script-blocked":
            basis.append("- Audit access note: The linked page was script-blocked, so the report relies on repo notes and accessible public metadata.")
        else:
            basis.append("- Audit access note: Metadata resolved cleanly during the audit.")
    if "Current broken target" in snapshot:
        basis.append("- Integrity note: The repository entry currently points to the wrong paper; this report is intentionally written against the confirmed intended target.")
    return "\n".join(["## Source Basis", "", *basis])


def generate_report_body(
    report: dict,
    entry: RepoEntry,
    paper: dict,
    all_entries: list[RepoEntry],
    report_paths_by_title: dict[str, Path],
) -> str:
    section_kind = KIND_BY_SECTION[entry.section]
    summary = build_executive_summary(entry, paper, section_kind)
    novelty = build_novelty(entry, paper, section_kind)
    contributions = build_contributions(entry, paper, section_kind)
    framework = build_framework(entry, paper, section_kind)
    evidence = build_evidence(entry, paper, section_kind)
    gaps = build_gaps(entry, report["snapshot"], section_kind)
    improvements = build_improvements(entry, section_kind)
    why_it_matters = build_why_it_matters(entry, section_kind)
    connections = build_connections(entry, all_entries)

    quick_read = build_quick_read(entry, novelty[0], evidence[0], gaps[0])
    visual_frame = build_visual_frame(
        entry.description or summary,
        novelty[0],
        framework[0],
        evidence[0],
        gaps[0],
        improvements[0],
    )
    analysis_map = build_analysis_map(
        contributions[0],
        framework[0],
        evidence[0],
        gaps[0],
        improvements[0],
    )
    summary_section = "\n".join(["## Executive Summary", "", summary])
    connections_lines = ["## Connections In This Repo", ""]
    for other, reason in connections:
        target_path = report_paths_by_title.get(other.title)
        if not target_path:
            continue
        rel = relative_report_link(report["path"], target_path)
        connections_lines.append(f"- [{other.title}]({rel}) - {reason}")

    sections = [
        quick_read,
        visual_frame,
        analysis_map,
        summary_section,
        build_artifact_section(entry),
        bullet_section("Novelty", novelty),
        bullet_section("Core Contributions", contributions),
        bullet_section("Framework and Operating Logic", framework),
        bullet_section("Evidence and Claimed Results", evidence),
        bullet_section("Gaps and Limitations", gaps),
        bullet_section("How To Improve", improvements),
        bullet_section("Why It Matters", why_it_matters),
        "\n".join(connections_lines),
        build_source_basis(report["snapshot"], paper, entry),
    ]
    return "\n\n".join(section.rstrip() for section in sections).rstrip() + "\n"


def build_report_prefix(report: dict, entry: RepoEntry, paper: dict) -> str:
    snapshot = report["snapshot"]
    rows: list[tuple[str, str]] = [
        ("Repo entry", entry.title),
        ("Actual target", snapshot.get("Actual target", "") or primary_link_markdown(entry)),
        ("Section", entry.section),
        ("Source location", f"`{entry.source_location}`"),
        ("Primary link type", f"`{primary_link_type(entry, snapshot)}`"),
    ]
    if snapshot.get("Audit status"):
        rows.append(("Audit status", snapshot["Audit status"]))
    rows.append(("Date / venue", date_or_venue(entry)))

    authors = ", ".join(paper.get("authors", [])) if paper.get("authors") else markdown_cell_text(snapshot.get("Authors", ""))
    if authors:
        rows.append(("Authors", authors))
    rows.append(("Focus tags", focus_tags(entry)))
    rows.append(("Center of gravity", report_center_of_gravity(entry, snapshot)))
    rows.extend(supporting_artifact_rows(entry))

    seen = {key for key, _ in rows}
    stale_artifact_keys = {"Code repo", "Project page", "Model hub", "Related assets"}
    for key, value in snapshot.items():
        if key in seen or key in stale_artifact_keys:
            continue
        rows.append((key, value))

    snapshot_lines = ["## Snapshot", "", "| Field | Detail |", "| --- | --- |"]
    snapshot_lines.extend([f"| {key} | {value} |" for key, value in rows if value])

    lines = [
        f"# {report['title']}",
        "",
        "Entry report generated on 2026-03-28 (Asia/Tokyo). This report is based on the repository entry, linked source metadata, and audit-time cross-checks.",
        "",
    ]
    if report["mismatch_note"]:
        lines.extend([report["mismatch_note"], ""])
    lines.extend(snapshot_lines)
    return "\n".join(lines).rstrip() + "\n\n"


def rewrite_reports() -> tuple[dict[str, Path], dict[str, dict], dict[str, RepoEntry]]:
    metadata = load_metadata()
    repo_entries = load_repo_entries()
    all_entries = list(repo_entries.values())
    reports = load_current_reports()
    report_paths_by_title = {report["title"]: report["path"] for report in reports}
    report_snapshots_by_title = {report["title"]: report["snapshot"] for report in reports}

    for report in reports:
        entry = next((item for item in all_entries if item.title == report["title"]), None)
        if not entry:
            source_location = markdown_cell_text(report["snapshot"].get("Source location", ""))
            candidate = repo_entries.get(source_location)
            if candidate and candidate.title == report["title"]:
                entry = candidate
            else:
                entry = candidate
        if not entry:
            continue
        paper = pick_metadata(entry, report["title"], report["snapshot"], metadata)
        body = generate_report_body(report, entry, paper, all_entries, report_paths_by_title)
        prefix = build_report_prefix(report, entry, paper)
        report["path"].write_text(prefix + body)
    return report_paths_by_title, report_snapshots_by_title, repo_entries


def rewrite_index(
    repo_entries: dict[str, RepoEntry],
    report_paths_by_title: dict[str, Path],
    report_snapshots_by_title: dict[str, dict],
) -> None:
    rows_by_section: dict[str, list[str]] = {section: [] for section, _ in README_SPECS}
    total_entries = 0
    total_reports = 0

    for section, _ in README_SPECS:
        section_entries = [entry for entry in repo_entries.values() if entry.section == section]
        section_entries.sort(key=lambda item: item.source_line)
        for entry in section_entries:
            total_entries += 1
            report_path = report_paths_by_title.get(entry.title)
            report_mark = "[x]" if report_path and report_path.exists() else ""
            if report_mark:
                total_reports += 1
            report_link = f"[Open]({report_path.relative_to(PAPER_REPORTS_ROOT)})" if report_mark else ""
            primary = (
                entry.links.get("Link")
                or entry.links.get("Code")
                or entry.links.get("Website")
                or entry.links.get("Model")
            )
            primary_link = f"[Source]({primary[1]})" if primary else ""
            snapshot = report_snapshots_by_title.get(entry.title, {})
            audit_status = markdown_cell_text(snapshot.get("Audit status", ""))
            audit_cell = f"`{audit_status}`" if audit_status else ""
            notes = []
            if "Current broken target" in snapshot:
                notes.append("Confirmed link mismatch.")
            if snapshot.get("Primary link type") and markdown_cell_text(snapshot.get("Primary link type", "")) in {"code", "website"}:
                notes.append(f"Primary source is `{markdown_cell_text(snapshot['Primary link type'])}`.")
            note_cell = " ".join(notes) if notes else "-"
            rows_by_section[section].append(
                f"| {entry.title} | {report_mark} | {report_link} | {primary_link} | {audit_cell} | {note_cell} |"
            )

    missing_reports = total_entries - total_reports
    index = PAPER_REPORTS_ROOT / "README.md"
    lines = [
        "# Paper Reports Index",
        "",
        "This index is generated from the repository's `papers/*/README.md` files. The `Report Included` column is a coverage checkbox: entries with a generated report are marked `[x]`, and future entries without reports stay blank until a report is added.",
        "",
        "```mermaid",
        "flowchart LR",
        "  Surveys[Survey Papers] --> Benchmarks[Benchmarks and Datasets]",
        "  Benchmarks --> Methods[Methods and Techniques]",
        "  Methods --> Models[Models and Architectures]",
        "  Safety[Safety and Security] --> Methods",
        "  Safety --> Models",
        "```",
        "",
        "```mermaid",
        "pie showData",
        "    title Report Coverage",
        f'    "Reports present" : {total_reports}',
        f'    "Reports missing" : {missing_reports}',
        "```",
        "",
        f"Coverage: `{total_reports}/{total_entries}` entries currently have a paper report.",
        "",
    ]

    for section, _ in README_SPECS:
        lines.extend(
            [
                f"## {section}",
                "",
                "| Entry | Report Included | Report | Primary URL | Audit status | Notes |",
                "| --- | --- | --- | --- | --- | --- |",
                *rows_by_section[section],
                "",
            ]
        )
    index.write_text("\n".join(lines).rstrip() + "\n")


def rewrite_portal(repo_entries: dict[str, RepoEntry]) -> None:
    counts = {
        section: sum(1 for entry in repo_entries.values() if entry.section == section)
        for section, _ in README_SPECS
    }
    portal = REPORTS_ROOT / "per-paper-report.md"
    portal.write_text(
        "\n".join(
            [
                "# Per-Paper Report Portal",
                "",
                "The comprehensive paper-level reports now live in [papers/README.md](./papers/README.md).",
                "A generated methods chronology now lives in [methods-timeline.md](./methods-timeline.md).",
                "",
                "## What Is New",
                "",
                "- One dedicated markdown report per entry in `papers/*/README.md`.",
                "- The index now shows a `Report Included` checkbox for every source entry, so future papers without reports stay visible but unmarked.",
                "- Every report now includes a `Quick Read`, two Mermaid figures, and paper-level sections for `code and supporting artifacts`, `novelty`, `core contributions`, `framework and operating logic`, `evidence`, `gaps and limitations`, `how to improve`, and `connections`.",
                "- Confirmed link mismatches are called out inside the affected entry reports as well as in [maintenance-findings.md](./maintenance-findings.md).",
                "- The methods timeline organizes the method wave by grounding, RL/post-training, data synthesis, memory/planning, and multi-agent orchestration.",
                "",
                "```mermaid",
                "flowchart LR",
                "  Index[papers/README.md] --> Surveys[survey-papers/]",
                "  Index --> Models[models-and-architectures/]",
                "  Index --> Benchmarks[benchmarks-and-datasets/]",
                "  Index --> Methods[methods-and-techniques/]",
                "  Index --> Safety[safety-and-security/]",
                "  Methods --> Timeline[methods-timeline.md]",
                "```",
                "",
                "## Counts",
                "",
                "| Section | Count |",
                "| --- | --- |",
                f"| Survey Papers | {counts['Survey Papers']} |",
                f"| Models and Architectures | {counts['Models and Architectures']} |",
                f"| Benchmarks and Datasets | {counts['Benchmarks and Datasets']} |",
                f"| Methods and Techniques | {counts['Methods and Techniques']} |",
                f"| Safety and Security | {counts['Safety and Security']} |",
            ]
        )
        + "\n"
    )


def main() -> None:
    report_paths_by_title, report_snapshots_by_title, repo_entries = rewrite_reports()
    rewrite_index(repo_entries, report_paths_by_title, report_snapshots_by_title)
    rewrite_portal(repo_entries)


if __name__ == "__main__":
    main()
