# Browser Use

Entry report generated on 2026-03-28 (Asia/Tokyo). This report is based on the repository entry, audit-time metadata, and cross-checks against adjacent repo context.

## Snapshot

| Field | Detail |
| --- | --- |
| Repo entry | Browser Use |
| Actual target | [GitHub](https://github.com/browser-use/browser-use) |
| Group | Frameworks & Tools |
| Category | Web/Browser Frameworks |
| Source location | `frameworks/README.md:60` |
| Primary link type | `repository` |
| Audit status | `ok` |
| GitHub stars | 84728 |
| Language | Python |
| License | MIT |
| Stars | 10k+ |

## Quick Read

| Lens | Read |
| --- | --- |
| Role in repo | repository |
| Novelty | Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims. |
| Operating frame | Repo language: Python; license: MIT. |
| Main caution | Repository popularity is not the same thing as benchmark-verified reliability, maintenance quality, or deployment safety. |

## Visual Frame

```mermaid
flowchart LR
  Problem["Problem: Connect LLMs to browsers with vision and HTML extraction."] --> Value["Novelty: Its novelty is implementation availability: readers can..."]
  Value --> Surface["Framework: Repo language: Python; license: MIT."]
  Surface --> Signal["Signal: Full LLM control of browser"]
  Signal --> Risk["Risk: Repository popularity is not the same thing as..."]
  Risk --> Next["Next: Pair README claims with stronger benchmark references..."]
```

## Analysis Map

```mermaid
flowchart TB
  subgraph Adds["What This Entry Adds"]
    A1["Novelty: Its novelty is implementation availability: readers can..."]
    A2["Contribution: Full LLM control of browser"]
    A3["Signal: Full LLM control of browser"]
  end
  subgraph Watch["What To Watch"]
    W1["Risk: Repository popularity is not the same thing as..."]
    W2["Improve: Pair README claims with stronger benchmark references..."]
  end
  A1 --> A2 --> A3 --> W1 --> W2
```

## Executive Summary

Connect LLMs to browsers with vision and HTML extraction. Make websites accessible for AI agents. Automate tasks online with ease. Key local notes: Full LLM control of browser; Autonomous step determination.

## Novelty and Distinguishing Angle

- Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims.
- The entry is browser-first, matching the part of the ecosystem that currently looks most deployment-ready.
- Open-source adoption is non-trivial here: cached GitHub metadata records 84728 stars.

## Core Contributions or Offerings

- Full LLM control of browser
- Autonomous step determination
- Vision-based interaction
- GitHub topic footprint: ai-agents, ai-tools, browser-automation, browser-use, llm, playwright.

## Operating Framework

- Repo language: Python; license: MIT.
- Repository updated at audit time: 2026-03-27T15:34:17Z.

## Evidence and Adoption Signals

- Full LLM control of browser
- Autonomous step determination
- GitHub stars: 84728.
- Open issues at audit time: 190.
- Open-source posture: Python, license MIT.
- Topics: ai-agents, ai-tools, browser-automation, browser-use, llm, playwright.

## Limitations and Gaps

- Repository popularity is not the same thing as benchmark-verified reliability, maintenance quality, or deployment safety.

## Improvement Paths

- Pair README claims with stronger benchmark references, maintenance notes, and example evaluations.
- Document supported environments and failure modes more explicitly so adoption signals are easier to interpret.
- Show reproducible setup paths and ongoing maintenance signals, not just launch momentum.

## Why It Matters

- It provides the implementation layer that turns research claims into developer workflows, demos, and reusable stacks.
- Framework entries help explain what the ecosystem can actually build today, not just what papers describe.

## Connections In This Repo

- [LaVague](web-browser-frameworks-lavague.md) - shared browser or web-agent operating surface.
- [Skyvern](web-browser-frameworks-skyvern.md) - shared browser or web-agent operating surface.
- [Agent Browser (Vercel)](web-browser-frameworks-agent-browser-vercel.md) - shared browser or web-agent operating surface.
- [Stagehand](web-browser-frameworks-stagehand.md) - shared browser or web-agent operating surface.

## Source Basis

- Primary basis: repo-local notes, link-audit page metadata, GitHub repository metadata.
- Audit access note: link-audit status was `ok` for the primary URL.
- Maintenance note: repository metadata was current through 2026-03-27T15:34:17Z at audit time.
