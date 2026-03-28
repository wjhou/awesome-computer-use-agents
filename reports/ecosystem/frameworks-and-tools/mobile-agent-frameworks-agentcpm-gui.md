# AgentCPM-GUI

Entry report generated on 2026-03-28 (Asia/Shanghai). This report is based on the repository entry, audit-time metadata, and cross-checks against adjacent repo context.

## Snapshot

| Field | Detail |
| --- | --- |
| Repo entry | AgentCPM-GUI |
| Actual target | [GitHub](https://github.com/OpenBMB/AgentCPM-GUI) |
| Group | Frameworks & Tools |
| Category | Mobile Agent Frameworks |
| Source location | `frameworks/README.md:168` |
| Primary link type | `repository` |
| Audit status | `ok` |
| Organization | OpenBMB |
| GitHub stars | 1341 |
| Language | Python |
| License | Apache-2.0 |

## Quick Read

| Lens | Read |
| --- | --- |
| Role in repo | repository |
| Novelty | Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims. |
| Operating frame | Repo language: Python; license: Apache-2.0. |
| Main caution | Repository popularity is not the same thing as benchmark-verified reliability, maintenance quality, or deployment safety. |

## Visual Frame

```mermaid
flowchart LR
  Problem["Problem: 8B-parameter on-device mobile agent."] --> Value["Novelty: Its novelty is implementation availability: readers can..."]
  Value --> Surface["Framework: Repo language: Python; license: Apache-2.0."]
  Surface --> Signal["Signal: GitHub stars: 1341."]
  Signal --> Risk["Risk: Repository popularity is not the same thing as..."]
  Risk --> Next["Next: Pair README claims with stronger benchmark references..."]
```

## Analysis Map

```mermaid
flowchart TB
  subgraph Adds["What This Entry Adds"]
    A1["Novelty: Its novelty is implementation availability: readers can..."]
    A2["Contribution: 8B-parameter on-device mobile agent."]
    A3["Signal: GitHub stars: 1341."]
  end
  subgraph Watch["What To Watch"]
    W1["Risk: Repository popularity is not the same thing as..."]
    W2["Improve: Pair README claims with stronger benchmark references..."]
  end
  A1 --> A2 --> A3 --> W1 --> W2
```

## Executive Summary

8B-parameter on-device mobile agent. AgentCPM-GUI: An on-device GUI agent for operating Android apps, enhancing reasoning ability with reinforcement fine-tuning for efficient task execution.

## Novelty and Distinguishing Angle

- Its novelty is implementation availability: readers can inspect, run, and adapt the actual stack rather than only reading paper claims.
- The entry leans into the mobile-agent lane, where research depth is strong but real-world productization is still uneven.
- Open-source adoption is non-trivial here: cached GitHub metadata records 1341 stars.

## Core Contributions or Offerings

- 8B-parameter on-device mobile agent.

## Operating Framework

- Repo language: Python; license: Apache-2.0.
- Repository updated at audit time: 2026-03-26T05:39:07Z.

## Evidence and Adoption Signals

- GitHub stars: 1341.
- Open issues at audit time: 3.
- Open-source posture: Python, license Apache-2.0.
- Recent maintenance timestamp in cached metadata: 2026-03-26T05:39:07Z.
- Audit-time page title: GitHub - OpenBMB/AgentCPM-GUI: AgentCPM-GUI: An on-device GUI agent for operating Android apps, enhancing reasoning ability with reinforcement fine-tuning for efficient task execution. · GitHub.
- Audit-time page description: AgentCPM-GUI: An on-device GUI agent for operating Android apps, enhancing reasoning ability with reinforcement fine-tuning for efficient task execution..

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

- [AgentCPM-GUI: On-device Mobile Agent](../../papers/models-and-architectures/agentcpm-gui-on-device-mobile-agent.md) - shared mobile-agent focus.
- [AppAgent](mobile-agent-frameworks-appagent.md) - shared mobile-agent focus.
- [Mobile-Agent](mobile-agent-frameworks-mobile-agent.md) - shared mobile-agent focus.
- [AutoGLM](mobile-agent-frameworks-autoglm.md) - shared mobile-agent focus.

## Source Basis

- Primary basis: repo-local notes, report metadata, GitHub repository metadata.
- Audit access note: tracked audit status was `ok` for the primary URL.
- Maintenance note: repository metadata was current through 2026-03-26T05:39:07Z at audit time.
