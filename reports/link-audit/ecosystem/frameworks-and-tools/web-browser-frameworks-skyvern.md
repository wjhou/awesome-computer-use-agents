# Skyvern

Entry report generated on 2026-03-28 (Asia/Tokyo). This report is based on the repository entry, audit-time metadata, and cross-checks against adjacent repo context.

## Snapshot

| Field | Detail |
| --- | --- |
| Repo entry | Skyvern |
| Actual target | [GitHub](https://github.com/Skyvern-AI/skyvern) |
| Group | Frameworks & Tools |
| Category | Web/Browser Frameworks |
| Source location | `frameworks/README.md:103` |
| Primary link type | `repository` |
| Audit status | `ok` |
| GitHub stars | 20975 |
| Language | Python |
| License | AGPL-3.0 |
| Stars | 3k+ |

## Quick Read

| Lens | Read |
| --- | --- |
| Role in repo | repository |
| Novelty | Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims. |
| Operating frame | Repo language: Python; license: AGPL-3.0. |
| Main caution | Repository popularity is not the same thing as benchmark-verified reliability, maintenance quality, or deployment safety. |

## Visual Frame

```mermaid
flowchart LR
  Problem["Problem: Browser workflow automation using computer vision."] --> Value["Novelty: Its novelty is implementation availability: readers can..."]
  Value --> Surface["Framework: Repo language: Python; license: AGPL-3.0."]
  Surface --> Signal["Signal: GitHub stars: 20975."]
  Signal --> Risk["Risk: Repository popularity is not the same thing as..."]
  Risk --> Next["Next: Pair README claims with stronger benchmark references..."]
```

## Analysis Map

```mermaid
flowchart TB
  subgraph Adds["What This Entry Adds"]
    A1["Novelty: Its novelty is implementation availability: readers can..."]
    A2["Contribution: GitHub topic footprint: ai, api, automation, browser..."]
    A3["Signal: GitHub stars: 20975."]
  end
  subgraph Watch["What To Watch"]
    W1["Risk: Repository popularity is not the same thing as..."]
    W2["Improve: Pair README claims with stronger benchmark references..."]
  end
  A1 --> A2 --> A3 --> W1 --> W2
```

## Executive Summary

Browser workflow automation using computer vision. Automate browser based workflows with AI. Key local notes: Stars: 3k+.

## Novelty and Distinguishing Angle

- Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims.
- The entry is browser-first, matching the part of the ecosystem that currently looks most deployment-ready.
- Open-source adoption is non-trivial here: cached GitHub metadata records 20975 stars.

## Core Contributions or Offerings

- GitHub topic footprint: ai, api, automation, browser, browser-automation, computer.

## Operating Framework

- Repo language: Python; license: AGPL-3.0.
- Repository updated at audit time: 2026-03-27T15:02:37Z.

## Evidence and Adoption Signals

- GitHub stars: 20975.
- Open issues at audit time: 146.
- Open-source posture: Python, license AGPL-3.0.
- Topics: ai, api, automation, browser, browser-automation, computer.
- Recent maintenance timestamp in cached metadata: 2026-03-27T15:02:37Z.
- Audit-time page title: GitHub - Skyvern-AI/skyvern: Automate browser based workflows with AI · GitHub.

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

- [Browser Use](web-browser-frameworks-browser-use.md) - shared browser or web-agent operating surface.
- [Agent Browser (Vercel)](web-browser-frameworks-agent-browser-vercel.md) - shared browser or web-agent operating surface.
- [OpenAdapt](desktop-agent-frameworks-openadapt.md) - neighboring ecosystem entry in the same local cluster.
- [Stagehand](web-browser-frameworks-stagehand.md) - shared browser or web-agent operating surface.

## Source Basis

- Primary basis: repo-local notes, link-audit page metadata, GitHub repository metadata.
- Audit access note: link-audit status was `ok` for the primary URL.
- Maintenance note: repository metadata was current through 2026-03-27T15:02:37Z at audit time.
