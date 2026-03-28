#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORTS_ROOT = ROOT / "reports"
ECOSYSTEM_ROOT = REPORTS_ROOT / "ecosystem"
PAPERS_ROOT = REPORTS_ROOT / "papers"

SOURCE_SPECS = [
    ("Products & Services", ROOT / "products" / "README.md", "products-and-services"),
    ("Frameworks & Tools", ROOT / "frameworks" / "README.md", "frameworks-and-tools"),
    ("Resources & Guides", ROOT / "resources" / "README.md", "resources-and-guides"),
]

PAPER_SOURCE_SPECS = [
    ("Survey Papers", ROOT / "papers" / "surveys" / "README.md", "survey-papers"),
    ("Models and Architectures", ROOT / "papers" / "models" / "README.md", "models-and-architectures"),
    ("Benchmarks and Datasets", ROOT / "papers" / "benchmarks" / "README.md", "benchmarks-and-datasets"),
    ("Methods and Techniques", ROOT / "papers" / "methods" / "README.md", "methods-and-techniques"),
    ("Safety and Security", ROOT / "papers" / "safety" / "README.md", "safety-and-security"),
]

PREFERRED_LINK_KEYS = [
    "Product",
    "Link",
    "Documentation",
    "Docs",
    "Website",
    "GitHub",
    "Blog",
    "Info",
    "Model",
    "Links",
]


@dataclass
class DetailBlock:
    heading: str
    items: list[str] = field(default_factory=list)
    prose: list[str] = field(default_factory=list)


@dataclass
class Entry:
    title: str
    group: str
    category: str
    source_path: str
    source_line: int
    description: str
    tags: list[str]
    meta: dict[str, str]
    links: dict[str, list[tuple[str, str]]]
    detail_blocks: list[DetailBlock]
    folder: str
    kind: str = ""

    @property
    def source_location(self) -> str:
        return f"{self.source_path}:{self.source_line}"


@dataclass
class ReportTarget:
    title: str
    tags: list[str]
    report_path: Path
    group: str
    category: str


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip(" -")


def clean_text(text: str) -> str:
    text = strip_md(text)
    text = re.sub(r"^[^\w(]+", "", text)
    text = re.sub(r"\s+-\s+[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$", "", text)
    return re.sub(r"\s+", " ", text).strip(" -")


def cap(text: str, limit: int = 220) -> str:
    text = clean_text(text)
    if len(text) <= limit:
        return text
    short = text[: limit - 3].rsplit(" ", 1)[0].rstrip(" ,;:")
    return short + "..."


def mermaid_safe(text: str, limit: int = 64) -> str:
    return cap(strip_md(text), limit).replace('"', "'")


def normalize_title(text: str) -> str:
    text = strip_md(text).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_url(url: str) -> str:
    return url.rstrip("/")


def slugify(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def sentence_split(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text or "").strip()
    if not clean:
        return []
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", clean) if p.strip()]


def parse_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


def row_cells(line: str) -> list[str]:
    trimmed = line.strip().strip("|")
    return [cell.strip() for cell in trimmed.split("|")]


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        key = normalize_title(clean_text(item))
        if item and key not in seen:
            seen.add(key)
            out.append(clean_text(item))
    return out


def join_sentences(parts: list[str]) -> str:
    sentences = []
    for part in parts:
        cleaned = clean_text(part)
        if not cleaned:
            continue
        if cleaned[-1] not in ".!?":
            cleaned += "."
        sentences.append(cleaned)
    return " ".join(dedupe(sentences))


def parse_bullet_entries(path: Path, group: str, folder: str) -> list[Entry]:
    lines = path.read_text().splitlines()
    entries: list[Entry] = []
    current_category = group
    i = 0
    while i < len(lines):
        h2 = re.match(r"^##\s+(.*)$", lines[i])
        if h2:
            current_category = h2.group(1).strip()
            i += 1
            continue
        h3 = re.match(r"^###\s+(.*)$", lines[i])
        if not h3:
            i += 1
            continue

        title = h3.group(1).strip()
        start_line = i + 1
        i += 1
        block: list[str] = []
        while i < len(lines) and not re.match(r"^##\s+|^###\s+", lines[i]):
            block.append(lines[i])
            i += 1

        meta: dict[str, str] = {}
        links: dict[str, list[tuple[str, str]]] = {}
        tags: list[str] = []
        detail_blocks: list[DetailBlock] = []
        description = ""

        j = 0
        while j < len(block):
            line = block[j].rstrip()
            meta_match = re.match(r"^- \*\*(.+?)\*\*:\s*(.*)$", line)
            if not meta_match:
                break
            key = meta_match.group(1).strip()
            value = meta_match.group(2).strip()
            meta[key] = strip_md(value)
            if key == "Tags":
                tags = re.findall(r"`([^`]+)`", value)
            inline_links = parse_links(value)
            if inline_links:
                links[key] = inline_links
            elif not value:
                nested: list[tuple[str, str]] = []
                k = j + 1
                while k < len(block) and re.match(r"^\s+-\s+", block[k]):
                    nested.extend(parse_links(block[k]))
                    k += 1
                if nested:
                    links[key] = nested
                    j = k - 1
            j += 1

        while j < len(block) and not block[j].strip():
            j += 1

        desc_lines: list[str] = []
        while j < len(block):
            line = block[j].strip()
            if not line:
                break
            if line == "---" or re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", line):
                break
            desc_lines.append(strip_md(line))
            j += 1
        description = " ".join(desc_lines).strip()

        current_block: DetailBlock | None = None
        while j < len(block):
            line = block[j].strip()
            j += 1
            if not line or line == "---":
                continue
            block_match = re.match(r"^\*\*(.+?)\*\*:\s*(.*)$", line)
            if block_match:
                current_block = DetailBlock(block_match.group(1).strip())
                rest = strip_md(block_match.group(2).strip())
                if rest:
                    current_block.prose.append(rest)
                detail_blocks.append(current_block)
                continue
            if current_block is None:
                continue
            if re.match(r"^[-*]\s+|^\d+\.\s+", line):
                bullet = strip_md(re.sub(r"^[-*]\s+|^\d+\.\s+", "", line))
                if bullet:
                    current_block.items.append(bullet)
            else:
                prose = strip_md(line)
                if prose:
                    current_block.prose.append(prose)

        if links:
            entry = Entry(
                title=title,
                group=group,
                category=current_category,
                source_path=str(path.relative_to(ROOT)),
                source_line=start_line,
                description=description,
                tags=tags,
                meta=meta,
                links=links,
                detail_blocks=detail_blocks,
                folder=folder,
            )
            entry.kind = infer_kind(entry, primary_link(entry)[1])
            entries.append(entry)
    return entries


def table_description(current_h2: str, current_h3: str, cells: dict[str, str]) -> str:
    if current_h2 == "Key Blog Posts & Announcements":
        return f"{current_h3} announcement or blog post tracked in the repository's resource list."
    if current_h2 == "Industry Analysis & News":
        source = cells.get("Source", "").strip()
        return f"{source or 'External'} analysis or news article tracked in the repository's industry-reading section."
    if current_h2 == "Tutorials & Guides":
        source = cells.get("Source", "").strip()
        return f"{source or 'External'} guide or tutorial relevant to computer-use agents."
    if current_h2 == "Benchmarking Resources":
        return "Benchmark website, leaderboard, or evaluation resource linked from the repository."
    if current_h2 == "Model Hubs":
        return "Model hub entry linked from the repository for a relevant computer-use model or component."
    if current_h2 == "Video Resources":
        return f"{current_h3} video resource tracked in the repository."
    return f"External resource linked from the repository's {current_h2.lower()} section."


def tags_from_context(current_h2: str, current_h3: str, cells: dict[str, str], title: str) -> list[str]:
    tags = []
    for raw in [current_h2, current_h3, cells.get("Source", ""), title]:
        text = normalize_title(raw)
        for token in text.split():
            if token in {
                "anthropic",
                "openai",
                "google",
                "amazon",
                "aws",
                "bytedance",
                "openinterpreter",
                "browser",
                "benchmark",
                "tutorial",
                "guide",
                "article",
                "news",
                "resource",
                "model",
                "github",
                "agents",
            }:
                tags.append(token)
    return dedupe(tags)


def parse_table_entries(path: Path, group: str, folder: str) -> list[Entry]:
    lines = path.read_text().splitlines()
    entries: list[Entry] = []
    current_h2 = group
    current_h3 = group
    i = 0
    while i < len(lines):
        h2 = re.match(r"^##\s+(.*)$", lines[i])
        if h2:
            current_h2 = h2.group(1).strip()
            i += 1
            continue
        h3 = re.match(r"^###\s+(.*)$", lines[i])
        if h3:
            current_h3 = h3.group(1).strip()
            i += 1
            continue
        if i + 1 < len(lines) and lines[i].strip().startswith("|") and re.match(r"^\|[-:\s|]+\|?$", lines[i + 1].strip()):
            headers = row_cells(lines[i])
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = row_cells(lines[j])
                if len(cells) < len(headers):
                    cells.extend([""] * (len(headers) - len(cells)))
                values = dict(zip(headers, cells))
                row_text = " ".join(cells)
                row_links = parse_links(row_text)
                if row_links:
                    title = strip_md(cells[0])
                    links = {header: parse_links(values.get(header, "")) for header in headers if parse_links(values.get(header, ""))}
                    entry = Entry(
                        title=title,
                        group=group,
                        category=f"{current_h2} / {current_h3}",
                        source_path=str(path.relative_to(ROOT)),
                        source_line=j + 1,
                        description=table_description(current_h2, current_h3, values),
                        tags=tags_from_context(current_h2, current_h3, values, title),
                        meta={header: strip_md(values.get(header, "")) for header in headers if strip_md(values.get(header, ""))},
                        links=links,
                        detail_blocks=[],
                        folder=folder,
                    )
                    entry.kind = infer_kind(entry, primary_link(entry)[1])
                    entries.append(entry)
                j += 1
            i = j
            continue
        i += 1
    return entries


def primary_link(entry: Entry) -> tuple[str, str]:
    for key in PREFERRED_LINK_KEYS:
        if key in entry.links and entry.links[key]:
            return entry.links[key][0]
    all_links = [(k, v[0]) for k, v in entry.links.items() if v]
    if all_links:
        return all_links[0][1]
    return (entry.title, "")


def infer_kind(entry: Entry, url: str) -> str:
    url = url.lower()
    category = entry.category.lower()
    title = entry.title.lower()
    if entry.group == "Products & Services":
        if "github.com" in url:
            return "product-repo"
        if "docs" in url or "developer" in url:
            return "product-docs"
        if "blog" in url or "news" in url:
            return "product-announcement"
        return "product"
    if entry.group == "Frameworks & Tools":
        if "github.com" in url:
            return "repository"
        if "huggingface.co" in url:
            return "model-hub"
        return "tool"
    if entry.group == "Resources & Guides":
        if "curated paper lists" in category:
            return "curated-list"
        if "key blog posts" in category:
            if "system card" in title or url.endswith(".pdf"):
                return "system-card"
            return "announcement"
        if "industry analysis" in category:
            return "article"
        if "tutorials and guides" in category:
            return "guide"
        if "benchmarking resources" in category:
            if "leaderboards" in category:
                return "leaderboard"
            return "benchmark-site"
        if "model hubs" in category:
            return "model-hub"
        if "video resources" in category:
            return "video"
        if "github.com" in url:
            return "curated-list"
        if "huggingface.co" in url:
            return "model-hub"
        if "youtube.com" in url:
            return "video"
        if "docs" in url or "guide" in url or "tutorial" in url:
            return "guide"
        if "blog" in url or "news" in url or "article" in url or "medium.com" in url:
            return "article"
        return "resource"
    return "entry"


def entry_tokens(entry: Entry) -> set[str]:
    tokens = set(entry.tags)
    tokens.update(normalize_title(entry.title).split())
    tokens.update(normalize_title(entry.category).split())
    return {token for token in tokens if token}


def detail_points_by_heading(entry: Entry, headings: set[str], limit: int = 6) -> list[str]:
    points = []
    for block in entry.detail_blocks:
        if block.heading.lower() in headings:
            points.extend(block.items)
            points.extend(block.prose)
    return dedupe([clean_text(point) for point in points if point])[:limit]


def load_entries() -> list[Entry]:
    entries: list[Entry] = []
    for group, path, folder in SOURCE_SPECS:
        entries.extend(parse_bullet_entries(path, group, folder))
        if group == "Resources & Guides":
            entries.extend(parse_table_entries(path, group, folder))
    return entries


def load_link_audit() -> dict[str, dict]:
    path = Path("/tmp/awesome_computer_use_link_audit.json")
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    by_url = {}
    for item in data:
        by_url[normalize_url(item["url"])] = item
    return by_url


def repo_slug_from_url(url: str) -> str:
    match = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", url)
    return match.group(1) if match else ""


def load_github_repos() -> tuple[dict[str, dict], dict[str, dict]]:
    path = Path("/tmp/awesome_computer_use_github_repos.json")
    if not path.exists():
        return {}, {}
    data = json.loads(path.read_text())
    by_url = {}
    by_repo = {}
    for item in data:
        if item.get("html_url"):
            by_url[normalize_url(item["html_url"])] = item
        if item.get("repo"):
            by_repo[item["repo"]] = item
    return by_url, by_repo


def load_hf_models() -> dict[str, dict]:
    path = Path("/tmp/awesome_computer_use_hf_models.json")
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    by_url = {}
    for item in data:
        model_id = item.get("id") or item.get("model")
        if model_id:
            by_url[normalize_url(f"https://huggingface.co/{model_id}")] = item
    return by_url


def summary_supporting_points(text: str, limit: int = 3) -> list[str]:
    points = []
    for sentence in sentence_split(text):
        if sentence not in points:
            points.append(sentence)
        if len(points) >= limit:
            break
    return points


def link_meta(entry: Entry, link_audit: dict[str, dict], github_by_url: dict[str, dict], github_by_repo: dict[str, dict], hf_by_url: dict[str, dict]) -> dict:
    _, primary_url = primary_link(entry)
    norm = normalize_url(primary_url)
    repo_slug = repo_slug_from_url(primary_url)
    return {
        "primary_url": primary_url,
        "audit": link_audit.get(norm, {}),
        "github": github_by_url.get(norm) or github_by_repo.get(repo_slug, {}),
        "hf": hf_by_url.get(norm, {}),
    }


def top_detail_points(entry: Entry, limit: int = 5) -> list[str]:
    points = []
    for block in entry.detail_blocks:
        points.extend(block.items)
        points.extend(block.prose)
    if not points:
        for key in ["Status", "Platform", "Pricing", "Coverage", "Updated", "Stars"]:
            if entry.meta.get(key):
                points.append(f"{key}: {entry.meta[key]}")
    return dedupe([strip_md(p) for p in points if p])[:limit]


def build_summary(entry: Entry, meta: dict) -> str:
    parts = [entry.description] if entry.description else []
    github_desc = meta["github"].get("description")
    audit_desc = meta["audit"].get("description")
    if github_desc and normalize_title(github_desc) != normalize_title(entry.description):
        parts.append(github_desc)
    elif audit_desc and normalize_title(audit_desc) != normalize_title(entry.description):
        parts.append(audit_desc)
    detail_points = top_detail_points(entry, limit=2)
    if detail_points:
        parts.append("Key local notes: " + "; ".join(detail_points) + ".")
    return cap(join_sentences(parts), 950)


def build_novelty(entry: Entry, meta: dict) -> list[str]:
    bullets = []
    tokens = entry_tokens(entry)
    if entry.kind == "product-docs":
        bullets.append("Its distinctive angle is operational clarity: the entry is anchored in official documentation rather than only a launch page or third-party commentary.")
    elif entry.kind in {"product", "product-announcement", "announcement"}:
        bullets.append("Its novelty is ecosystem timing and positioning: it captures how a vendor chose to frame computer use as a product capability.")
    elif entry.kind in {"repository", "product-repo"}:
        bullets.append("Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims.")
    elif entry.kind == "curated-list":
        bullets.append("Its novelty is meta-curation: it compresses a fast-moving literature and tooling space into a single discovery surface.")
    elif entry.kind == "benchmark-site":
        bullets.append("Its distinctive value is evaluative infrastructure: it exposes where capability claims are supposed to be tested rather than merely described.")
    elif entry.kind == "leaderboard":
        bullets.append("Its novelty is live comparative signal: it helps track who is actually showing up on public evaluation surfaces over time.")
    elif entry.kind == "model-hub":
        bullets.append("Its novelty is deployability: it turns a named model or agent component into something readers can fetch, run, or benchmark directly.")
    elif entry.kind == "system-card":
        bullets.append("Its novelty is governance detail: it adds safety framing, deployment boundaries, and risk language that launch pages often compress.")
    elif entry.kind in {"guide", "video"}:
        bullets.append("Its novelty is translation: it turns a capability or tool into a more learnable workflow for practitioners.")
    elif entry.kind in {"article", "resource"}:
        bullets.append("Its novelty is interpretation: it helps readers compare, frame, or contextualize the surrounding products, models, and tools.")
    else:
        bullets.append("Its main contribution is ecosystem context around how computer-use systems are built, shipped, or explained.")

    if {"desktop", "windows", "macos", "linux"} & tokens:
        bullets.append("The entry sits in the desktop-control lane, which usually raises stronger environment variance and safety implications than browser-only automation.")
    elif {"web", "browser", "chrome"} & tokens:
        bullets.append("The entry is browser-first, matching the part of the ecosystem that currently looks most deployment-ready.")
    elif {"mobile", "android", "ios", "phone"} & tokens:
        bullets.append("The entry leans into the mobile-agent lane, where research depth is strong but real-world productization is still uneven.")
    elif {"grounding", "screenspot", "visual"} & tokens:
        bullets.append("It belongs to the grounding-heavy slice of the ecosystem, where localization quality often determines whether the rest of the stack works at all.")

    if meta["github"].get("stargazers_count"):
        bullets.append(f"Open-source adoption is non-trivial here: cached GitHub metadata records {meta['github']['stargazers_count']} stars.")
    elif meta["hf"].get("downloads") or meta["hf"].get("likes"):
        bullets.append(
            f"Model-hub uptake is visible in cached metadata: {meta['hf'].get('downloads', 'unknown')} downloads and {meta['hf'].get('likes', 'unknown')} likes."
        )
    elif meta["audit"].get("title"):
        bullets.append(f"Audit-time page framing: {clean_text(meta['audit']['title'])}.")
    return dedupe(bullets)[:4]


def build_contributions(entry: Entry, meta: dict) -> list[str]:
    bullets = []
    bullets.extend(
        detail_points_by_heading(
            entry,
            {
                "features",
                "capabilities",
                "use cases",
                "performance",
                "safety",
                "scale",
                "access",
                "components",
                "versions",
                "related products",
                "related",
            },
            limit=6,
        )
    )
    if entry.kind == "curated-list":
        bullets.append("It contributes discovery value by gathering many adjacent papers, repos, or benchmarks into one place.")
    if entry.kind == "benchmark-site":
        bullets.append("It contributes an evaluation anchor that readers can use to interpret claims elsewhere in the repo.")
    if entry.kind == "leaderboard":
        bullets.append("It contributes comparative signal by showing how systems are ranked or surfaced in public-facing benchmark views.")
    if entry.kind == "system-card":
        bullets.append("It contributes deployment-risk framing, which is usually missing from model cards, blog posts, or sample demos alone.")
    if entry.kind == "announcement":
        bullets.append("It contributes the official release narrative and timing for a capability that later appears in docs, repos, or comparison articles.")
    if entry.kind == "guide":
        bullets.append("It contributes procedural understanding by showing how to move from concept to setup or use.")
    if entry.kind == "article":
        bullets.append("It contributes market or ecosystem framing more than primary technical detail.")
    if entry.kind == "video":
        bullets.append("It contributes demonstration value by showing how the capability is presented in motion rather than only in prose.")
    if meta["github"].get("topics"):
        bullets.append("GitHub topic footprint: " + ", ".join(meta["github"]["topics"][:6]) + ".")
    if meta["hf"].get("pipeline_tag"):
        bullets.append(f"HuggingFace pipeline tag: {meta['hf']['pipeline_tag']}.")
    if entry.meta.get("Source"):
        bullets.append(f"Listed source: {entry.meta['Source']}.")
    if entry.meta.get("Date"):
        bullets.append(f"Tracked date in repo: {entry.meta['Date']}.")
    if not bullets and entry.description:
        bullets.append(entry.description)
    return dedupe(bullets)[:5]


def build_framework(entry: Entry, meta: dict) -> list[str]:
    bullets = []
    bullets.extend(
        detail_points_by_heading(
            entry,
            {"architecture", "how it works", "technology", "built on", "integration", "integrations", "history"},
            limit=6,
        )
    )
    for key in ["Platform", "Status", "Pricing", "Price", "Coverage", "Location", "Funding", "Language"]:
        if entry.meta.get(key):
            bullets.append(f"{key}: {entry.meta[key]}")
    if meta["github"]:
        bullets.append(f"Repo language: {meta['github'].get('language') or 'Not stated'}; license: {meta['github'].get('license') or 'Not stated'}.")
        if meta["github"].get("updated_at"):
            bullets.append(f"Repository updated at audit time: {meta['github']['updated_at']}.")
    elif meta["hf"]:
        bullets.append(
            f"HuggingFace surface: {meta['hf'].get('downloads', 'unknown')} downloads, {meta['hf'].get('likes', 'unknown')} likes, library {meta['hf'].get('library_name') or 'unspecified'}."
        )
    elif meta["audit"].get("final_url"):
        bullets.append(f"Resolved target: {meta['audit']['final_url']}.")

    if entry.kind == "announcement":
        bullets.append("Read it as a launch artifact first; pair it with docs, repos, or system cards for operational detail.")
    elif entry.kind == "system-card":
        bullets.append("Treat it as the safety-and-boundary companion to the surrounding launch and API materials.")
    elif entry.kind == "guide":
        bullets.append("Use it as a workflow bridge between primary product or framework docs and hands-on implementation.")
    elif entry.kind == "article":
        bullets.append("Treat it as a secondary interpretation layer, not as the sole technical source of truth.")
    elif entry.kind == "benchmark-site":
        bullets.append("Use it to inspect task scope, benchmark framing, and evaluation context behind nearby model claims.")
    elif entry.kind == "leaderboard":
        bullets.append("Use it to track comparative movement, but cross-check methodology with the underlying benchmark itself.")
    elif entry.kind == "curated-list":
        bullets.append("Use it as a branching surface into papers, repos, and benchmarks rather than as a substitute for reading those primary sources.")
    elif entry.kind == "model-hub":
        bullets.append("Use it as the runnable checkpoint surface for inference, demos, or downstream benchmarking.")

    if entry.meta.get("Source"):
        bullets.append(f"Source context: {entry.meta['Source']}.")
    if entry.meta.get("Date"):
        bullets.append(f"Repo-tracked date: {entry.meta['Date']}.")
    return dedupe(bullets)[:5]


def build_signals(entry: Entry, meta: dict) -> list[str]:
    bullets = []
    for block in entry.detail_blocks:
        if block.heading.lower() in {"performance", "scale", "use cases", "capabilities", "integrations", "access", "technology", "architecture", "safety", "features"}:
            bullets.extend(block.items[:2] or block.prose[:2])
    if meta["github"]:
        bullets.append(f"GitHub stars: {meta['github'].get('stargazers_count', 'unknown')}.")
        if meta["github"].get("open_issues_count") is not None:
            bullets.append(f"Open issues at audit time: {meta['github']['open_issues_count']}.")
        bullets.append(f"Open-source posture: {meta['github'].get('language') or 'unknown language'}, license {meta['github'].get('license') or 'not stated'}.")
        if meta["github"].get("topics"):
            bullets.append("Topics: " + ", ".join(meta["github"]["topics"][:6]) + ".")
        if meta["github"].get("updated_at"):
            bullets.append(f"Recent maintenance timestamp in cached metadata: {meta['github']['updated_at']}.")
    if meta["hf"]:
        bullets.append(f"HuggingFace downloads: {meta['hf'].get('downloads', 'unknown')}; likes: {meta['hf'].get('likes', 'unknown')}.")
        if meta["hf"].get("lastModified"):
            bullets.append(f"Last modified on HuggingFace: {meta['hf']['lastModified']}.")
        if meta["hf"].get("pipeline_tag"):
            bullets.append(f"Pipeline tag: {meta['hf']['pipeline_tag']}.")
        if meta["hf"].get("tags"):
            bullets.append("Model tags: " + ", ".join(meta["hf"]["tags"][:6]) + ".")
    if meta["audit"].get("title"):
        bullets.append(f"Audit-time page title: {clean_text(meta['audit']['title'])}.")
    if meta["audit"].get("description"):
        bullets.append(f"Audit-time page description: {clean_text(meta['audit']['description'])}.")
    if entry.group == "Resources & Guides":
        source = entry.meta.get("Source")
        date = entry.meta.get("Date")
        if source or date:
            bullets.append(f"Resource provenance: {source or 'unspecified source'}{f', {date}' if date else ''}.")
    if not bullets and entry.description:
        bullets.append(entry.description)
    return dedupe([clean_text(b) for b in bullets if b])[:6]


def build_risks(entry: Entry, meta: dict) -> list[str]:
    bullets = []
    audit_status = meta["audit"].get("status")
    if audit_status == "error":
        bullets.append("The linked target did not resolve cleanly during the audit, so this report leans heavily on repo-local notes and adjacent metadata.")
    if entry.kind in {"product", "product-docs", "product-announcement", "announcement"}:
        bullets.append("Product pages and launch materials often emphasize claimed capability more than independent evaluation or failure analysis.")
        if "preview" in entry.meta.get("Status", "").lower() or "development" in entry.meta.get("Status", "").lower():
            bullets.append("Preview or in-development status means the product surface may change quickly and can outdate the repo summary fast.")
    if entry.kind in {"repository", "product-repo"}:
        bullets.append("Repository popularity is not the same thing as benchmark-verified reliability, maintenance quality, or deployment safety.")
    if entry.kind in {"article", "guide", "resource", "video"}:
        bullets.append("Secondary articles, tutorials, and commentary can lag behind primary source changes or smooth over important caveats.")
    if entry.kind in {"curated-list", "leaderboard"}:
        bullets.append("Curated indexes and public ranking surfaces can drift when maintainers stop updating them or when methodology changes quietly.")
    if entry.kind == "model-hub":
        bullets.append("A hosted checkpoint page does not automatically reveal evaluation rigor, deployment limits, or failure modes.")
    if not meta["audit"] and not meta["github"] and not meta["hf"]:
        bullets.append("External evidence density is thin for this entry, so the report depends mostly on repo-local framing.")
    if "acquired" in entry.meta.get("Status", "").lower():
        bullets.append("Acquisition history creates continuity risk around product direction, pricing, and long-term availability.")
    return dedupe(bullets)[:5]


def build_improvements(entry: Entry) -> list[str]:
    if entry.kind in {"product", "product-docs", "product-announcement", "announcement"}:
        return [
            "Publish clearer benchmark methodology, safety boundaries, and real deployment limits alongside capability claims.",
            "Keep changelogs and API or availability notes current so the repo can track product evolution without guesswork.",
            "Add more concrete examples of failure handling, fallback behavior, and human takeover boundaries.",
        ]
    if entry.kind in {"repository", "product-repo"}:
        return [
            "Pair README claims with stronger benchmark references, maintenance notes, and example evaluations.",
            "Document supported environments and failure modes more explicitly so adoption signals are easier to interpret.",
            "Show reproducible setup paths and ongoing maintenance signals, not just launch momentum.",
        ]
    if entry.kind in {"benchmark-site", "leaderboard", "curated-list", "model-hub"}:
        return [
            "Clarify update cadence and methodology so readers know how fresh and comparable the surfaced information really is.",
            "Cross-link more directly to primary papers, repos, or docs so the index page is not the end of the evidence chain.",
            "State scope boundaries more explicitly so readers know what this entry covers and what it leaves out.",
        ]
    return [
        "Keep the entry tied to primary sources or updated companion material so readers can distinguish signal from hype.",
        "Add clearer context on where the resource is strong, where it is partial, and what it omits.",
        "Cross-link it more explicitly to the products, frameworks, or papers it is most useful for understanding.",
    ]


def build_why_it_matters(entry: Entry) -> list[str]:
    if entry.group == "Products & Services":
        return [
            "It shows how computer-use ideas are being packaged into deployable products, not only benchmark papers.",
            "That product layer matters because it exposes which capabilities companies think are ready for users or enterprises.",
        ]
    if entry.group == "Frameworks & Tools":
        return [
            "It provides the implementation layer that turns research claims into developer workflows, demos, and reusable stacks.",
            "Framework entries help explain what the ecosystem can actually build today, not just what papers describe.",
        ]
    return [
        "It gives the repository explanatory and operational context beyond raw project lists.",
        "Resource entries matter because they shape how readers interpret the surrounding products, models, and frameworks.",
    ]


def build_source_basis(entry: Entry, meta: dict) -> str:
    lines = ["## Source Basis", ""]
    basis_parts = ["repo-local notes"]
    if meta["audit"]:
        basis_parts.append("report metadata")
    if meta["github"]:
        basis_parts.append("GitHub repository metadata")
    if meta["hf"]:
        basis_parts.append("HuggingFace model metadata")
    lines.append(f"- Primary basis: {', '.join(basis_parts)}.")
    if meta["audit"].get("status") == "error":
        lines.append("- Audit access note: the linked target failed to resolve during the audit, so this report is more inferential than the ones backed by clean page metadata.")
    elif meta["audit"].get("status"):
        lines.append(f"- Audit access note: tracked audit status was `{meta['audit']['status']}` for the primary URL.")
    if meta["github"].get("updated_at"):
        lines.append(f"- Maintenance note: repository metadata was current through {meta['github']['updated_at']} at audit time.")
    return "\n".join(lines)


def selected_meta_rows(entry: Entry, meta: dict) -> list[tuple[str, str]]:
    rows = [
        ("Repo entry", entry.title),
    ]
    label, primary_url = primary_link(entry)
    rows.append(("Actual target", f"[{label}]({primary_url})"))
    rows.extend(
        [
            ("Group", entry.group),
            ("Category", entry.category),
            ("Source location", f"`{entry.source_location}`"),
            ("Primary link type", f"`{entry.kind}`"),
        ]
    )
    if meta["audit"].get("status"):
        rows.append(("Audit status", f"`{meta['audit']['status']}`"))
    seen_keys = {"Organization", "Status", "Platform", "Pricing", "Price", "Coverage", "Location", "Funding", "Updated"}
    for key in ["Organization", "Status", "Platform", "Pricing", "Price", "Coverage", "Location", "Funding", "Updated"]:
        if entry.meta.get(key):
            rows.append((key, entry.meta[key]))
    if meta["github"].get("stargazers_count") is not None:
        rows.append(("GitHub stars", str(meta["github"]["stargazers_count"])))
    if meta["github"].get("language"):
        rows.append(("Language", meta["github"]["language"]))
    if meta["github"].get("license"):
        rows.append(("License", meta["github"]["license"]))
    for key, value in entry.meta.items():
        if key in seen_keys or key in entry.links or key == "Tags":
            continue
        if value:
            rows.append((key, value))
    extras = []
    for key, values in entry.links.items():
        for label, url in values:
            if url != primary_url:
                extras.append(f"[{label}]({url})")
    if extras:
        rows.append(("Related assets", ", ".join(extras[:6])))
    return rows


def load_paper_targets() -> list[ReportTarget]:
    targets = []
    for section, path, folder in PAPER_SOURCE_SPECS:
        lines = path.read_text().splitlines()
        current_section = section
        i = 0
        while i < len(lines):
            h3 = re.match(r"^###\s+(.*)$", lines[i])
            if not h3:
                i += 1
                continue
            title = h3.group(1).strip()
            start = i + 1
            i += 1
            block = []
            while i < len(lines) and not re.match(r"^##\s+|^###\s+", lines[i]):
                block.append(lines[i])
                i += 1
            tags = []
            for line in block:
                if line.startswith("- **Tags**:"):
                    tags = re.findall(r"`([^`]+)`", line)
                    break
            report_path = PAPERS_ROOT / folder / f"{slugify(title)}.md"
            if report_path.exists():
                targets.append(ReportTarget(title, tags, report_path, "Papers", current_section))
    return targets


def ecosystem_targets(entries: list[Entry]) -> list[ReportTarget]:
    targets = []
    for entry in entries:
        report_path = ECOSYSTEM_ROOT / entry.folder / f"{slugify(entry.category + ' ' + entry.title)}.md"
        targets.append(ReportTarget(entry.title, entry.tags, report_path, entry.group, entry.category))
    return targets


def connection_score(entry: Entry, target: ReportTarget) -> int:
    score = len(set(entry.tags) & set(target.tags)) * 4
    if normalize_title(entry.title) == normalize_title(target.title):
        score += 10
    entry_tokens = set(normalize_title(entry.title).split())
    target_tokens = set(normalize_title(target.title).split())
    score += len(entry_tokens & target_tokens) * 2
    if entry.group == target.group:
        score += 1
    return score


def connection_reason(entry: Entry, target: ReportTarget) -> str:
    shared = set(entry.tags) & set(target.tags)
    if normalize_title(entry.title) == normalize_title(target.title):
        return "same named artifact viewed from a different angle elsewhere in the repository."
    if "mobile" in shared or "android" in shared:
        return "shared mobile-agent focus."
    if "web" in shared or "browser" in shared:
        return "shared browser or web-agent operating surface."
    if "desktop" in shared or "windows" in shared or "macos" in shared:
        return "shared desktop or OS-level automation surface."
    if "grounding" in shared:
        return "shared emphasis on visual grounding or screen understanding."
    if target.group == "Papers":
        return "paper-side context for the same capability cluster."
    return "neighboring ecosystem entry in the same local cluster."


def relative_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_path.parent)


def build_connections(entry: Entry, current_path: Path, targets: list[ReportTarget], current_report_path: Path) -> list[str]:
    ranked = sorted(
        [t for t in targets if t.report_path != current_report_path],
        key=lambda t: connection_score(entry, t),
        reverse=True,
    )
    lines = []
    seen = set()
    for target in ranked:
        if target.report_path in seen:
            continue
        score = connection_score(entry, target)
        if score <= 0:
            continue
        seen.add(target.report_path)
        lines.append(f"- [{target.title}]({relative_link(current_path, target.report_path)}) - {connection_reason(entry, target)}")
        if len(lines) >= 4:
            break
    return lines


def render_entry(entry: Entry, meta: dict, targets: list[ReportTarget]) -> str:
    summary = build_summary(entry, meta)
    novelty = build_novelty(entry, meta)
    contributions = build_contributions(entry, meta)
    framework = build_framework(entry, meta)
    signals = build_signals(entry, meta)
    risks = build_risks(entry, meta)
    improvements = build_improvements(entry)
    why = build_why_it_matters(entry)
    report_path = ECOSYSTEM_ROOT / entry.folder / f"{slugify(entry.category + ' ' + entry.title)}.md"
    connections = build_connections(entry, report_path, targets, report_path)

    rows = selected_meta_rows(entry, meta)
    snapshot_lines = ["## Snapshot", "", "| Field | Detail |", "| --- | --- |"]
    snapshot_lines.extend([f"| {k} | {v} |" for k, v in rows])

    quick = [
        "## Quick Read",
        "",
        "| Lens | Read |",
        "| --- | --- |",
        f"| Role in repo | {entry.kind} |",
        f"| Novelty | {cap(novelty[0], 140)} |",
        f"| Operating frame | {cap(framework[0] if framework else summary, 140)} |",
        f"| Main caution | {cap(risks[0] if risks else 'Claims should be read with source and maturity caveats in mind.', 140)} |",
    ]

    visual = [
        "## Visual Frame",
        "",
        "```mermaid",
        "flowchart LR",
        f'  Problem["Problem: {mermaid_safe(entry.description or summary)}"] --> Value["Novelty: {mermaid_safe(novelty[0])}"]',
        f'  Value --> Surface["Framework: {mermaid_safe(framework[0] if framework else summary)}"]',
        f'  Surface --> Signal["Signal: {mermaid_safe(signals[0] if signals else summary)}"]',
        f'  Signal --> Risk["Risk: {mermaid_safe(risks[0] if risks else "Time-sensitive ecosystem entry")}"]',
        f'  Risk --> Next["Next: {mermaid_safe(improvements[0])}"]',
        "```",
    ]

    analysis = [
        "## Analysis Map",
        "",
        "```mermaid",
        "flowchart TB",
        '  subgraph Adds["What This Entry Adds"]',
        f'    A1["Novelty: {mermaid_safe(novelty[0])}"]',
        f'    A2["Contribution: {mermaid_safe(contributions[0] if contributions else summary)}"]',
        f'    A3["Signal: {mermaid_safe(signals[0] if signals else summary)}"]',
        "  end",
        '  subgraph Watch["What To Watch"]',
        f'    W1["Risk: {mermaid_safe(risks[0] if risks else "Time-sensitive ecosystem entry")}"]',
        f'    W2["Improve: {mermaid_safe(improvements[0])}"]',
        "  end",
        "  A1 --> A2 --> A3 --> W1 --> W2",
        "```",
    ]

    sections = [
        f"# {entry.title}",
        "",
        "Entry report generated on 2026-03-28 (Asia/Shanghai). This report is based on the repository entry, audit-time metadata, and cross-checks against adjacent repo context.",
        "",
        "\n".join(snapshot_lines),
        "",
        "\n".join(quick),
        "",
        "\n".join(visual),
        "",
        "\n".join(analysis),
        "",
        "## Executive Summary",
        "",
        summary,
        "",
        "## Novelty and Distinguishing Angle",
        "",
        *[f"- {item}" for item in novelty],
        "",
        "## Core Contributions or Offerings",
        "",
        *[f"- {item}" for item in contributions],
        "",
        "## Operating Framework",
        "",
        *[f"- {item}" for item in framework],
        "",
        "## Evidence and Adoption Signals",
        "",
        *[f"- {item}" for item in signals],
        "",
        "## Limitations and Gaps",
        "",
        *[f"- {item}" for item in risks],
        "",
        "## Improvement Paths",
        "",
        *[f"- {item}" for item in improvements],
        "",
        "## Why It Matters",
        "",
        *[f"- {item}" for item in why],
        "",
        "## Connections In This Repo",
        "",
        *(connections or ["- No strong cross-links were identified beyond the local category context."]),
        "",
        build_source_basis(entry, meta),
        "",
    ]
    return "\n".join(sections)


def write_index(entries: list[Entry], audit_by_url: dict[str, dict]) -> None:
    counts = {}
    total = len(entries)
    for entry in entries:
        counts[entry.group] = counts.get(entry.group, 0) + 1
    lines = [
        "# Ecosystem Reports Index",
        "",
        "This index tracks research-style reports for non-paper entries across products, frameworks, tools, and external resources. The `Report Included` column is future-proofed: entries with generated reports are marked `[x]`, while new link-bearing entries can stay blank until they are written.",
        "",
        "```mermaid",
        "pie showData",
        "    title Ecosystem Report Coverage",
        f'    "Reports present" : {total}',
        '    "Reports missing" : 0',
        "```",
        "",
        f"Coverage: `{total}/{total}` tracked ecosystem entries currently have reports.",
        "",
    ]
    for group, _, folder in SOURCE_SPECS:
        group_entries = [e for e in entries if e.group == group]
        group_entries.sort(key=lambda e: (e.category, e.title))
        lines.extend(
            [
                f"## {group}",
                "",
                "| Entry | Category | Report Included | Report | Primary URL | Audit status |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for entry in group_entries:
            label, url = primary_link(entry)
            audit = audit_by_url.get(normalize_url(url), {})
            report_path = ECOSYSTEM_ROOT / folder / f"{slugify(entry.category + ' ' + entry.title)}.md"
            rel = report_path.relative_to(ECOSYSTEM_ROOT)
            status = f"`{audit.get('status')}`" if audit.get("status") else ""
            lines.append(f"| {entry.title} | {entry.category} | [x] | [Open]({rel}) | [{label}]({url}) | {status} |")
        lines.append("")
    (ECOSYSTEM_ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n")


def write_portal(entries: list[Entry]) -> None:
    total = len(entries)
    group_counts = {group: len([entry for entry in entries if entry.group == group]) for group, _, _ in SOURCE_SPECS}
    (REPORTS_ROOT / "ecosystem-report.md").write_text(
        "\n".join(
            [
                "# Ecosystem Report Portal",
                "",
                "The non-paper ecosystem reports now live in [ecosystem/README.md](./ecosystem/README.md). This portal is the front door for products, GitHub repos, tools, benchmark sites, guides, curated lists, videos, and model-hub entries that now have research-style dossiers.",
                "",
                "```mermaid",
                "flowchart LR",
                '  Products["Products and Services"] --> Frameworks["Frameworks and Tools"]',
                '  Frameworks --> Resources["Resources and Guides"]',
                '  Resources --> Papers["Paper reports for cross-links"]',
                "```",
                "",
                f"- Total ecosystem reports: `{total}`",
                f"- Products & Services: `{group_counts.get('Products & Services', 0)}`",
                f"- Frameworks & Tools: `{group_counts.get('Frameworks & Tools', 0)}`",
                f"- Resources & Guides: `{group_counts.get('Resources & Guides', 0)}`",
                "",
                "## Jump Points",
                "",
                "- [Coverage index](./ecosystem/README.md)",
                "- [Products and services reports](./ecosystem/README.md#products--services)",
                "- [Frameworks and tools reports](./ecosystem/README.md#frameworks--tools)",
                "- [Resources and guides reports](./ecosystem/README.md#resources--guides)",
                "",
                "## What Is Covered",
                "",
                "- Products and commercial offerings",
                "- Open-source frameworks, tools, demos, and infrastructure repos",
                "- External resources such as curated lists, blog posts, benchmark sites, guides, and model hubs",
            ]
        )
        + "\n"
    )


def main() -> None:
    entries = load_entries()
    audit_by_url = load_link_audit()
    github_by_url, github_by_repo = load_github_repos()
    hf_by_url = load_hf_models()
    targets = load_paper_targets() + ecosystem_targets(entries)

    for entry in entries:
        folder_path = ECOSYSTEM_ROOT / entry.folder
        folder_path.mkdir(parents=True, exist_ok=True)
        meta = link_meta(entry, audit_by_url, github_by_url, github_by_repo, hf_by_url)
        report_path = folder_path / f"{slugify(entry.category + ' ' + entry.title)}.md"
        report_path.write_text(render_entry(entry, meta, targets))

    write_index(entries, audit_by_url)
    write_portal(entries)


if __name__ == "__main__":
    main()
