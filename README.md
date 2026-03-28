# Awesome Computer Use Agents

A comprehensive collection of research papers, products, frameworks, and resources for AI agents that can interact with computers through graphical user interfaces (GUIs).

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Table of Contents

- [Overview](#overview)
- [Reports & Audits](#reports--audits)
- [Papers](#papers)
  - [Survey Papers](#survey-papers)
  - [Models & Architectures](#models--architectures)
  - [Benchmarks & Datasets](#benchmarks--datasets)
  - [Methods & Techniques](#methods--techniques)
  - [Safety & Security](#safety--security)
- [Products & Commercial Solutions](#products--commercial-solutions)
- [Open Source Frameworks](#open-source-frameworks)
- [Infrastructure & Tools](#infrastructure--tools)
- [Related Resources](#related-resources)

## Overview

Computer Use Agents (CUAs) are AI systems capable of interacting with digital interfaces just like humans do - clicking, typing, scrolling, and navigating through GUIs. This field has seen rapid advancement with the emergence of Vision-Language Models (VLMs) and Large Language Models (LLMs).

### Key Capabilities

- **GUI Grounding**: Locating and identifying UI elements from screenshots
- **Action Prediction**: Determining what actions to take (click, type, scroll)
- **Task Planning**: Breaking down complex tasks into actionable steps
- **Cross-Platform**: Operating across web, desktop (Windows/macOS/Linux), and mobile (Android/iOS)

## Reports & Audits

The repository also includes generated audit artifacts so readers can move from a curated link list to deeper entry-by-entry analysis.

- [Link Audit Summary](reports/link-audit/README.md) - high-level findings, cross-link patterns, and audit insights across the repository.
- [Per-Paper Report Portal](reports/link-audit/per-paper-report.md) - entry point to the full paper-level report set.
- [Ecosystem Report Portal](reports/link-audit/ecosystem-report.md) - entry point to the non-paper reports covering products, frameworks, tools, and resources.
- [Post-2024 Research Refresh](reports/link-audit/post-2024-research-refresh.md) - targeted 2025-2026 research expansion covering newly added papers and why they matter.
- [Paper Reports Coverage Index](reports/link-audit/papers/README.md) - shows every paper entry and marks report availability with `[x]`; entries without reports are intentionally left blank.
- [Ecosystem Reports Coverage Index](reports/link-audit/ecosystem/README.md) - shows every non-paper link-bearing entry and marks report availability with `[x]`; entries without reports are intentionally left blank.
- [Link Inventory](reports/link-audit/inventory.md) - raw URL inventory and resolution status.
- [Maintenance Findings](reports/link-audit/maintenance-findings.md) - confirmed link mismatches and follow-up fixes to make in the source lists.

## Papers

The `Report` column links to the generated per-entry paper report when one is available.

### Survey Papers

| Title | Venue/Date | Tags | Link | Report |
|-------|------------|------|------|--------|
| Large Language Model-Brained GUI Agents: A Survey | arXiv 2024 | `survey` `llm` `gui` | [Paper](https://arxiv.org/abs/2411.18279) | [Report](reports/link-audit/papers/survey-papers/large-language-model-brained-gui-agents-a-survey.md) |
| GUI Agents: A Survey | ACL 2025 | `survey` `comprehensive` | [Paper](https://arxiv.org/abs/2412.13501) | [Report](reports/link-audit/papers/survey-papers/gui-agents-a-survey.md) |
| GUI Agents with Foundation Models: A Comprehensive Survey | arXiv 2024 | `survey` `foundation-models` | [Paper](https://arxiv.org/abs/2411.04890) | [Report](reports/link-audit/papers/survey-papers/gui-agents-with-foundation-models-a-comprehensive-survey.md) |
| LLM-Powered GUI Agents in Phone Automation | arXiv 2025 | `survey` `mobile` | [Paper](https://arxiv.org/abs/2504.19838) | [Report](reports/link-audit/papers/survey-papers/llm-powered-gui-agents-in-phone-automation.md) |
| A Survey on Benchmarks of LLM-based GUI Agents | TechRxiv 2025 | `survey` `benchmarks` | [Paper](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176591818.87526814) | [Report](reports/link-audit/papers/survey-papers/a-survey-on-benchmarks-of-llm-based-gui-agents.md) |
| JARVIS or Ultron? Safety and Security Threats of CUAs | arXiv 2025 | `survey` `safety` `security` | [Paper](https://arxiv.org/abs/2505.10924) | [Report](reports/link-audit/papers/survey-papers/jarvis-or-ultron-safety-and-security-threats-of-computer-using-agents.md) |
| AI Agents: Evolution, Architecture, and Real-World Applications | arXiv 2025 | `survey` `architecture` | [Paper](https://arxiv.org/abs/2503.12687) | [Report](reports/link-audit/papers/survey-papers/ai-agents-evolution-architecture-and-real-world-applications.md) |
| How Smart Is Your GUI Agent? A Framework for the Future of Software Interaction | arXiv 2026 | `survey` `autonomy` `framework` | [Paper](https://arxiv.org/abs/2602.11514) | [Report](reports/link-audit/papers/survey-papers/how-smart-is-your-gui-agent-a-framework-for-the-future-of-software-interaction.md) |

See [papers/surveys/](papers/surveys/) for detailed information.

### Models & Architectures

| Title | Venue/Date | Tags | Link | Report |
|-------|------------|------|------|--------|
| UI-TARS: Pioneering Automated GUI Interaction with Native Agents | arXiv 2025 | `model` `bytedance` `sota` | [Paper](https://arxiv.org/abs/2501.12326) | [Report](reports/link-audit/papers/models-and-architectures/ui-tars-pioneering-automated-gui-interaction-with-native-agents.md) |
| UI-TARS-2: Advancing GUI Agent with Multi-Turn RL | arXiv 2025 | `model` `reinforcement-learning` | [Paper](https://arxiv.org/abs/2509.02544) | [Report](reports/link-audit/papers/models-and-architectures/ui-tars-2-advancing-gui-agent-with-multi-turn-rl.md) |
| CogAgent: A Visual Language Model for GUI Agents | arXiv 2024 | `model` `vlm` `18b` | [Paper](https://arxiv.org/abs/2312.08914) | [Report](reports/link-audit/papers/models-and-architectures/cogagent-a-visual-language-model-for-gui-agents.md) |
| ShowUI: Vision-Language-Action Model for GUI Visual Agent | CVPR 2025 | `model` `vla` | [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.pdf) | [Report](reports/link-audit/papers/models-and-architectures/showui-vision-language-action-model-for-gui-visual-agent.md) |
| ScreenAgent: A VLM-driven Computer Control Agent | IJCAI 2024 | `model` `vlm` `control` | [Paper](https://arxiv.org/abs/2402.07945) | [Report](reports/link-audit/papers/models-and-architectures/screenagent-a-vlm-driven-computer-control-agent.md) |
| SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents | ACL 2024 | `model` `grounding` | [Paper](https://arxiv.org/abs/2401.10935) | [Report](reports/link-audit/papers/models-and-architectures/seeclick-harnessing-gui-grounding-for-advanced-visual-gui-agents.md) |
| OmniParser: Pure Vision Based GUI Agent | arXiv 2024 | `model` `grounding` `microsoft` | [Paper](https://arxiv.org/abs/2408.00203) | [Report](reports/link-audit/papers/models-and-architectures/omniparser-pure-vision-based-gui-agent.md) |
| AGUVIS: Unified Pure Vision Agents for GUI Interaction | arXiv 2024 | `model` `vision-only` | [Paper](https://arxiv.org/abs/2412.04454) | [Report](reports/link-audit/papers/models-and-architectures/aguvis-unified-pure-vision-agents-for-gui-interaction.md) |
| AppAgent: Multimodal Agents as Smartphone Users | CHI 2025 | `model` `mobile` `android` | [Paper](https://arxiv.org/abs/2312.13771) | [Report](reports/link-audit/papers/models-and-architectures/appagent-multimodal-agents-as-smartphone-users.md) |
| Mobile-Agent-v3: Fundamental Agents for GUI Automation | arXiv 2025 | `model` `mobile` `multi-agent` | [Paper](https://arxiv.org/abs/2508.15144) | [Report](reports/link-audit/papers/models-and-architectures/mobile-agent-v3-fundamental-agents-for-gui-automation.md) |
| AutoGLM: Autonomous Foundation Agents for GUIs | arXiv 2024 | `model` `mobile` `chatglm` | [Paper](https://arxiv.org/abs/2411.00820) | [Report](reports/link-audit/papers/models-and-architectures/autoglm-autonomous-foundation-agents-for-guis.md) |
| AgentCPM-GUI: On-device Mobile Agent | GitHub 2025 | `model` `mobile` `on-device` | [GitHub](https://github.com/OpenBMB/AgentCPM-GUI) | [Report](reports/link-audit/papers/models-and-architectures/agentcpm-gui-on-device-mobile-agent.md) |
| Ferret-UI: Grounded Mobile UI Understanding | arXiv 2024 | `model` `mobile` `grounding` | [Paper](https://arxiv.org/abs/2404.05719) | [Report](reports/link-audit/papers/models-and-architectures/ferret-ui-grounded-mobile-ui-understanding.md) |
| Qwen2.5-VL Technical Report | arXiv 2025 | `model` `vlm` `agent-capable` | [Paper](https://arxiv.org/abs/2502.13923) | [Report](reports/link-audit/papers/models-and-architectures/qwen2-5-vl-technical-report.md) |
| R-VLM: Region-Aware VLM for Precise GUI Grounding | arXiv 2025 | `model` `grounding` | [Paper](https://arxiv.org/abs/2507.05673) | [Report](reports/link-audit/papers/models-and-architectures/r-vlm-region-aware-vlm-for-precise-gui-grounding.md) |
| GUI-Actor: Coordinate-Free Visual Grounding | Microsoft 2025 | `model` `grounding` | [Project](https://microsoft.github.io/GUI-Actor/) | [Report](reports/link-audit/papers/models-and-architectures/gui-actor-coordinate-free-visual-grounding.md) |
| Step-GUI Technical Report | arXiv 2025 | `model` `training-pipeline` `mcp` | [Paper](https://arxiv.org/abs/2512.15431) | [Report](reports/link-audit/papers/models-and-architectures/step-gui-technical-report.md) |
| OpenCUA: Open Foundations for Computer-Use Agents | arXiv 2025 | `model` `open-source` `foundation-model` | [Paper](https://arxiv.org/abs/2508.09123) | [Report](reports/link-audit/papers/models-and-architectures/opencua-open-foundations-for-computer-use-agents.md) |
| ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data | arXiv 2025 | `model` `data-scaling` `cross-platform` | [Paper](https://arxiv.org/abs/2509.15221) | [Report](reports/link-audit/papers/models-and-architectures/scalecua-scaling-open-source-computer-use-agents-with-cross-platform-data.md) |
| Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents | arXiv 2026 | `model` `mobile` `desktop` `cross-platform` | [Paper](https://arxiv.org/abs/2602.16855) | [Report](reports/link-audit/papers/models-and-architectures/mobile-agent-v3-5-multi-platform-fundamental-gui-agents.md) |
| ShowUI-Aloha: Human-Taught GUI Agent | arXiv 2026 | `model` `human-demonstrations` `desktop` | [Paper](https://arxiv.org/abs/2601.07181) | [Report](reports/link-audit/papers/models-and-architectures/showui-aloha-human-taught-gui-agent.md) |
| OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution | arXiv 2026 | `model` `moe` `desktop` `mobile` | [Paper](https://arxiv.org/abs/2601.20380) | [Report](reports/link-audit/papers/models-and-architectures/omegause-building-a-general-purpose-gui-agent-for-autonomous-task-execution.md) |

See [papers/models/](papers/models/) for detailed information.

### Benchmarks & Datasets

| Title | Venue/Date | Tags | Link | Report |
|-------|------------|------|------|--------|
| OSWorld: Multimodal Agents for Open-Ended Tasks in Real Computer Environments | NeurIPS 2024 | `benchmark` `desktop` `multimodal` | [Paper](https://arxiv.org/abs/2404.07972) | [Report](reports/link-audit/papers/benchmarks-and-datasets/osworld-multimodal-agents-for-open-ended-tasks-in-real-computer-environments.md) |
| WebArena: Realistic Web Environment for Building Autonomous Agents | arXiv 2023 | `benchmark` `web` | [Paper](https://arxiv.org/abs/2307.13854) | [Report](reports/link-audit/papers/benchmarks-and-datasets/webarena-realistic-web-environment-for-building-autonomous-agents.md) |
| Mind2Web: Towards a Generalist Agent for the Web | NeurIPS 2023 | `benchmark` `dataset` `web` | [Paper](https://arxiv.org/abs/2306.06070) | [Report](reports/link-audit/papers/benchmarks-and-datasets/mind2web-towards-a-generalist-agent-for-the-web.md) |
| VisualWebArena: Multimodal Web Tasks | arXiv 2024 | `benchmark` `web` `multimodal` | [Paper](https://arxiv.org/abs/2401.13649) | [Report](reports/link-audit/papers/benchmarks-and-datasets/visualwebarena-multimodal-web-tasks.md) |
| WebVoyager: End-to-End Web Agent with LMMs | arXiv 2024 | `benchmark` `web` `evaluation` | [Paper](https://arxiv.org/abs/2401.13919) | [Report](reports/link-audit/papers/benchmarks-and-datasets/webvoyager-end-to-end-web-agent-with-lmms.md) |
| ScreenSpot / ScreenSpot-Pro | arXiv 2024/2025 | `benchmark` `grounding` `high-res` | [Paper](https://arxiv.org/abs/2401.10935) | [Report](reports/link-audit/papers/benchmarks-and-datasets/screenspot-screenspot-pro.md) |
| Windows Agent Arena (WAA) | arXiv 2024 | `benchmark` `windows` `desktop` | [Paper](https://arxiv.org/abs/2409.08264) | [Report](reports/link-audit/papers/benchmarks-and-datasets/windows-agent-arena-waa.md) |
| AndroidWorld: Dynamic Benchmarking Environment | arXiv 2024 | `benchmark` `android` `mobile` | [Paper](https://arxiv.org/abs/2405.14573) | [Report](reports/link-audit/papers/benchmarks-and-datasets/androidworld-dynamic-benchmarking-environment.md) |
| Android in the Wild (AitW) | arXiv 2023 | `dataset` `android` `real-world` | [Paper](https://arxiv.org/abs/2307.10088) | [Report](reports/link-audit/papers/benchmarks-and-datasets/android-in-the-wild-aitw.md) |
| AMEX: Android Multi-annotation EXpo | arXiv 2024 | `dataset` `android` `annotations` | [Paper](https://arxiv.org/abs/2407.17490) | [Report](reports/link-audit/papers/benchmarks-and-datasets/amex-android-multi-annotation-expo.md) |
| A3: Android Agent Arena | arXiv 2025 | `benchmark` `android` `evaluation` | [Paper](https://arxiv.org/abs/2501.01149) | [Report](reports/link-audit/papers/benchmarks-and-datasets/a3-android-agent-arena.md) |
| macOSWorld | arXiv 2025 | `benchmark` `macos` `desktop` | [Paper](https://arxiv.org/abs/2506.04135) | [Report](reports/link-audit/papers/benchmarks-and-datasets/macosworld.md) |
| GUI Odyssey: Cross-app Mobile Navigation | arXiv 2024 | `benchmark` `mobile` `cross-app` | [Paper](https://arxiv.org/abs/2411.00820) | [Report](reports/link-audit/papers/benchmarks-and-datasets/gui-odyssey-cross-app-mobile-navigation.md) |
| WebCanvas: Online Web Agent Benchmarking | arXiv 2024 | `benchmark` `web` `online` | [Paper](https://arxiv.org/abs/2406.12373) | [Report](reports/link-audit/papers/benchmarks-and-datasets/webcanvas-online-web-agent-benchmarking.md) |
| Online-Mind2Web | arXiv 2025 | `benchmark` `web` `live-sites` | [Paper](https://arxiv.org/abs/2504.01382) | [Report](reports/link-audit/papers/benchmarks-and-datasets/online-mind2web.md) |
| MobileAgentBench | arXiv 2024 | `benchmark` `mobile` `efficiency` | [Paper](https://arxiv.org/abs/2406.08184) | [Report](reports/link-audit/papers/benchmarks-and-datasets/mobileagentbench.md) |
| OmniACT | arXiv 2024 | `benchmark` `desktop` `web` | [Paper](https://arxiv.org/abs/2402.17553) | [Report](reports/link-audit/papers/benchmarks-and-datasets/omniact.md) |
| ScreenSuite (HuggingFace) | GitHub 2025 | `benchmark` `comprehensive` | [GitHub](https://github.com/huggingface/screensuite) | [Report](reports/link-audit/papers/benchmarks-and-datasets/screensuite-huggingface.md) |
| MMBench-GUI: Hierarchical Multi-Platform Evaluation Framework for GUI Agents | arXiv 2025 | `benchmark` `cross-platform` `efficiency` | [Paper](https://arxiv.org/abs/2507.19478) | [Report](reports/link-audit/papers/benchmarks-and-datasets/mmbench-gui-hierarchical-multi-platform-evaluation-framework-for-gui-agents.md) |
| OS-MAP: How Far Can Computer-Using Agents Go in Breadth and Depth? | arXiv 2025 | `benchmark` `desktop` `taxonomy` | [Paper](https://arxiv.org/abs/2507.19132) | [Report](reports/link-audit/papers/benchmarks-and-datasets/os-map-how-far-can-computer-using-agents-go-in-breadth-and-depth.md) |
| OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents | arXiv 2025 | `benchmark` `mcp` `tool-calling` | [Paper](https://arxiv.org/abs/2510.24563) | [Report](reports/link-audit/papers/benchmarks-and-datasets/osworld-mcp-benchmarking-mcp-tool-invocation-in-computer-use-agents.md) |
| Computer Agent Arena: Toward Human-Centric Evaluation and Analysis of Computer-Use Agents | ICLR 2026 | `benchmark` `human-centric` `evaluation` | [Paper](https://openreview.net/forum?id=3x4SDbXbgl) | [Report](reports/link-audit/papers/benchmarks-and-datasets/computer-agent-arena-toward-human-centric-evaluation-and-analysis-of-computer-use-agents.md) |
| CUA-Suite: Expert Trajectories and Pixel-Precise Grounding for Computer-use Agents | LLA 2026 | `dataset` `grounding` `desktop` | [Paper](https://openreview.net/forum?id=IgTUGrZfMr) | [Report](reports/link-audit/papers/benchmarks-and-datasets/cua-suite-expert-trajectories-and-pixel-precise-grounding-for-computer-use-agents.md) |
| Spider2-V: Data Science Workflows | arXiv 2024 | `benchmark` `data-science` `specialized` | [Paper](https://arxiv.org/abs/2407.10956) | [Report](reports/link-audit/papers/benchmarks-and-datasets/spider2-v-data-science-workflows.md) |
| VideoGUI: Instructional Video Automation | arXiv 2024 | `benchmark` `video` `instructions` | [Paper](https://arxiv.org/abs/2406.10227) | [Report](reports/link-audit/papers/benchmarks-and-datasets/videogui-instructional-video-automation.md) |
| GUICourse: Vision-Language to Agents | arXiv 2024 | `benchmark` `training` `curriculum` | [Paper](https://arxiv.org/abs/2406.11317) | [Report](reports/link-audit/papers/benchmarks-and-datasets/guicourse-vision-language-to-agents.md) |
| AgentTrek Trajectories | Project 2024 | `dataset` `trajectories` `web` | [Project](https://agenttrek.github.io/) | [Report](reports/link-audit/papers/benchmarks-and-datasets/agenttrek-trajectories.md) |
| OS-Genesis Trajectories | Project 2024 | `dataset` `trajectories` `reverse-synthesis` | [Project](https://qiushisun.github.io/OS-Genesis-Home/) | [Report](reports/link-audit/papers/benchmarks-and-datasets/os-genesis-trajectories.md) |

See [papers/benchmarks/](papers/benchmarks/) for detailed information.

### Methods & Techniques

| Title | Venue/Date | Tags | Link | Report |
|-------|------------|------|------|--------|
| ComputerRL: End-to-End Online RL for Computer Use Agents | arXiv 2025 | `method` `reinforcement-learning` | [Paper](https://arxiv.org/abs/2508.14040) | [Report](reports/link-audit/papers/methods-and-techniques/computerrl-end-to-end-online-rl-for-computer-use-agents.md) |
| WebRL: Self-Evolving Online Curriculum RL for Web Agents | arXiv 2024 | `method` `reinforcement-learning` `web` | [Paper](https://arxiv.org/abs/2411.02337) | [Report](reports/link-audit/papers/methods-and-techniques/webrl-self-evolving-online-curriculum-rl-for-web-agents.md) |
| DigiRL: Training In-The-Wild Device-Control | NeurIPS 2024 | `method` `reinforcement-learning` `mobile` | [Paper](https://arxiv.org/abs/2406.11896) | [Report](reports/link-audit/papers/methods-and-techniques/digirl-training-in-the-wild-device-control.md) |
| AgentTrek: Agent Trajectory Synthesis via Web Tutorials | arXiv 2024 | `method` `data-synthesis` `trajectories` | [Paper](https://arxiv.org/abs/2412.09605) | [Report](reports/link-audit/papers/methods-and-techniques/agenttrek-agent-trajectory-synthesis-via-web-tutorials.md) |
| OS-Genesis: Automating GUI Agent Trajectory Construction | arXiv 2024 | `method` `data-synthesis` `reverse-task` | [Paper](https://arxiv.org/abs/2412.19723) | [Report](reports/link-audit/papers/methods-and-techniques/os-genesis-automating-gui-agent-trajectory-construction.md) |
| PC Agent-E: Efficient Agent Training for Computer Use | arXiv 2025 | `method` `efficient-training` | [Paper](https://arxiv.org/abs/2505.13909) | [Report](reports/link-audit/papers/methods-and-techniques/pc-agent-e-efficient-agent-training-for-computer-use.md) |
| SeeAct: GPT-4V Web Agent via Visual Grounding | arXiv 2024 | `method` `grounding` `web` | [Paper](https://arxiv.org/abs/2401.01614) | [Report](reports/link-audit/papers/methods-and-techniques/seeact-gpt-4v-web-agent-via-visual-grounding.md) |
| UFO: Windows OS UI Agent via GPT-4V | arXiv 2024 | `method` `windows` `gpt-4v` | [Paper](https://arxiv.org/abs/2402.07939) | [Report](reports/link-audit/papers/methods-and-techniques/ufo-windows-os-ui-agent-via-gpt-4v.md) |
| Ponder & Press: Advancing VLM Grounding | arXiv 2024 | `method` `grounding` `dual-model` | [Paper](https://arxiv.org/abs/2409.04566) | [Report](reports/link-audit/papers/methods-and-techniques/ponder-press-advancing-vlm-grounding.md) |
| Chain-of-Agents: Multi-Agent Collaboration | arXiv 2025 | `method` `multi-agent` | [Paper](https://arxiv.org/abs/2508.13167) | [Report](reports/link-audit/papers/methods-and-techniques/chain-of-agents-multi-agent-collaboration.md) |
| GUI-Reflection: Self-Reflection for GUI Agents | arXiv 2025 | `method` `self-reflection` | [Project](https://penghao-wu.github.io/GUI_Reflection) | [Report](reports/link-audit/papers/methods-and-techniques/gui-reflection-self-reflection-for-gui-agents.md) |
| Magentic-One: Multi-Agent with Human-in-Loop | arXiv 2024 | `method` `multi-agent` `microsoft` | [Paper](https://arxiv.org/abs/2411.04468) | [Report](reports/link-audit/papers/methods-and-techniques/magentic-one-multi-agent-with-human-in-loop.md) |
| Grounding Computer Use Agents on Human Demonstrations | arXiv 2025 | `method` `grounding` `human-demonstrations` | [Paper](https://arxiv.org/abs/2511.07332) | [Report](reports/link-audit/papers/methods-and-techniques/grounding-computer-use-agents-on-human-demonstrations.md) |
| ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory | arXiv 2026 | `method` `program-synthesis` `memory` | [Paper](https://arxiv.org/abs/2602.20502) | [Report](reports/link-audit/papers/methods-and-techniques/actionengine-from-reactive-to-programmatic-gui-agents-via-state-machine-memory.md) |
| GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training | arXiv 2026 | `method` `data-synthesis` `post-training` | [Paper](https://arxiv.org/abs/2602.14093) | [Report](reports/link-audit/papers/methods-and-techniques/gui-genesis-automated-synthesis-of-efficient-environments-with-verifiable-rewards-for-gui-agent-post-training.md) |
| OS-Copilot: Towards Generalist Computer Agents | arXiv 2024 | `method` `desktop` `self-improvement` | [Paper](https://arxiv.org/abs/2402.07456) | [Report](reports/link-audit/papers/methods-and-techniques/os-copilot-towards-generalist-computer-agents.md) |

See [papers/methods/](papers/methods/) for detailed information.

### Safety & Security

| Title | Venue/Date | Tags | Link | Report |
|-------|------------|------|------|--------|
| AgentHarm: LLM Agent Safety Benchmark | arXiv 2024 | `safety` `benchmark` `jailbreak` | [Paper](https://arxiv.org/abs/2410.09024) | [Report](reports/link-audit/papers/safety-and-security/agentharm-llm-agent-safety-benchmark.md) |
| RedTeamCUA: Security Testing for Computer Use Agents | arXiv 2025 | `safety` `red-team` | [Paper](https://arxiv.org/abs/2505.21936) | [Report](reports/link-audit/papers/safety-and-security/redteamcua-security-testing-for-computer-use-agents.md) |
| WebGuard: Safety Dataset for Web Agents | arXiv 2025 | `safety` `dataset` `web` | [Paper](https://arxiv.org/abs/2507.14293) | [Report](reports/link-audit/papers/safety-and-security/webguard-safety-dataset-for-web-agents.md) |
| Attacking Vision-Language Computer Agents via Pop-ups | arXiv 2024 | `security` `adversarial` `vlm` | [Paper](https://arxiv.org/abs/2411.02391) | [Report](reports/link-audit/papers/safety-and-security/attacking-vision-language-computer-agents-via-pop-ups.md) |
| EIA: Environmental Injection Attack | arXiv 2024 | `security` `privacy` `attack` | [Paper](https://arxiv.org/abs/2409.02453) | [Report](reports/link-audit/papers/safety-and-security/eia-environmental-injection-attack.md) |
| OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents | arXiv 2025 | `safety` `benchmark` `prompt-injection` | [Paper](https://arxiv.org/abs/2506.14866) | [Report](reports/link-audit/papers/safety-and-security/os-harm-a-benchmark-for-measuring-safety-of-computer-use-agents.md) |
| VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | arXiv 2025 | `security` `prompt-injection` `visual` | [Paper](https://arxiv.org/abs/2506.02456) | [Report](reports/link-audit/papers/safety-and-security/vpi-bench-visual-prompt-injection-attacks-for-computer-use-agents.md) |
| HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities | arXiv 2025 | `security` `cybersecurity` `web` | [Paper](https://arxiv.org/abs/2510.12200) | [Report](reports/link-audit/papers/safety-and-security/hackworld-evaluating-computer-use-agents-on-exploiting-web-application-vulnerabilities.md) |
| GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents | arXiv 2026 | `safety` `privacy` `benchmark` | [Paper](https://arxiv.org/abs/2601.18842) | [Report](reports/link-audit/papers/safety-and-security/guiguard-toward-a-general-framework-for-privacy-preserving-gui-agents.md) |
| When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents | arXiv 2026 | `security` `unintended-behavior` `red-team` | [Paper](https://arxiv.org/abs/2602.08235) | [Report](reports/link-audit/papers/safety-and-security/when-benign-inputs-lead-to-severe-harms-eliciting-unsafe-unintended-behaviors-of-computer-use-agents.md) |
| Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible | arXiv 2026 | `privacy` `mobile` `defense` | [Paper](https://arxiv.org/abs/2602.10139) | [Report](reports/link-audit/papers/safety-and-security/anonymization-enhanced-privacy-protection-for-mobile-gui-agents-available-but-invisible.md) |
| Infectious Jailbreaks in Multi-Agent Systems | arXiv 2024 | `security` `jailbreak` `multi-agent` | [Paper](https://arxiv.org/abs/2402.08567) | [Report](reports/link-audit/papers/safety-and-security/infectious-jailbreaks-in-multi-agent-systems.md) |
| Large Reasoning Models are Autonomous Jailbreak Agents | Nature 2026 | `security` `jailbreak` `lrm` | [Paper](https://www.nature.com/articles/s41467-026-69010-1) | [Report](reports/link-audit/papers/safety-and-security/large-reasoning-models-are-autonomous-jailbreak-agents.md) |
| AI Agents Under Threat: Key Security Challenges and Future Pathways | ACM Computing Surveys 2025 | `survey` `security` | [Paper](https://dl.acm.org/doi/10.1145/3716628) | [Report](reports/link-audit/papers/safety-and-security/ai-agents-under-threat-key-security-challenges-and-future-pathways.md) |

See [papers/safety/](papers/safety/) for detailed information.

## Products & Commercial Solutions

The non-paper tables below now include a `Report` column that links to the generated ecosystem dossier for each tracked entry.

### Major Tech Companies

| Product | Company | Platform | Status | Tags | Link | Report |
|---------|---------|----------|--------|------|------|--------|
| Computer Use | Anthropic | Desktop/Web | GA (Mar 2025) | `desktop` `api` `claude` | [Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | [Report](reports/link-audit/ecosystem/products-and-services/major-tech-companies-anthropic-claude-computer-use.md) |
| Operator / CUA | OpenAI | Web | Preview (Jan 2025) | `web` `browser` `api` | [Product](https://openai.com/index/introducing-operator/) | [Report](reports/link-audit/ecosystem/products-and-services/major-tech-companies-openai-operator-cua.md) |
| Project Mariner | Google DeepMind | Web/Chrome | Preview (May 2025) | `web` `chrome` `gemini` | [Product](https://deepmind.google/models/project-mariner/) | [Report](reports/link-audit/ecosystem/products-and-services/major-tech-companies-google-project-mariner.md) |
| Gemini 2.5 Computer Use | Google | Desktop/Web | Preview (2025) | `desktop` `gemini` | [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model/) | [Report](reports/link-audit/ecosystem/resources-and-guides/key-blog-posts-and-announcements-google-gemini-2-5-computer-use.md) |
| Nova Act | Amazon AWS | Web | GA (2025) | `web` `enterprise` `aws` | [Product](https://aws.amazon.com/nova/act/) | [Report](reports/link-audit/ecosystem/products-and-services/major-tech-companies-amazon-aws-nova-act.md) |
| Apple Intelligence (Siri Agent) | Apple | iOS/macOS | Development | `mobile` `on-device` | [Info](https://www.apple.com/apple-intelligence/) | [Report](reports/link-audit/ecosystem/products-and-services/major-tech-companies-apple-siri-agent-apple-intelligence.md) |

### Startups & Products

| Product | Company | Focus | Tags | Link | Report |
|---------|---------|-------|------|------|--------|
| Manus | Butterfly Effect | General-purpose Agent | `general` `multi-model` `acquired-meta` | [Website](https://manus.bot) | [Report](reports/link-audit/ecosystem/products-and-services/startups-manus-butterfly-effect.md) |
| Rabbit R1 | Rabbit Inc | Hardware Device + LAM | `hardware` `mobile` `lam` | [Website](https://www.rabbit.tech/rabbit-r1) | [Report](reports/link-audit/ecosystem/products-and-services/startups-rabbit-inc-rabbit-r1.md) |
| Twin | Twin Labs | Workflow Automation | `enterprise` `workflow` `browser` | [Website](https://twin.so/) | [Report](reports/link-audit/ecosystem/products-and-services/startups-twin-labs-twin.md) |
| HyperWrite | HyperWrite AI | Browser Assistant | `browser` `personal-assistant` | [Website](https://www.hyperwriteai.com/personal-assistant) | [Report](reports/link-audit/ecosystem/products-and-services/startups-hyperwrite-personal-assistant.md) |
| MultiOn | MultiOn | Browser Automation | `browser` `automation` `api` | [Website](https://www.multion.ai/) | [Report](reports/link-audit/ecosystem/products-and-services/startups-multion.md) |
| ACT-1 | Adept AI | Action Transformer | `enterprise` `acquired-amazon` | [Blog](https://www.adept.ai/blog/act-1/) | [Report](reports/link-audit/ecosystem/products-and-services/startups-adept-ai-act-1.md) |
| Runner H | H Company | Real-world Applications | `enterprise` `web` | [Website](https://www.hcompany.ai/) | [Report](reports/link-audit/ecosystem/products-and-services/startups-h-company-runner-h.md) |

### Browser Infrastructure

| Product | Company | Focus | Tags | Link | Report |
|---------|---------|-------|------|------|--------|
| Browserbase | Browserbase | Cloud Browser for Agents | `infrastructure` `cloud` `api` | [Website](https://www.browserbase.com/) | [Report](reports/link-audit/ecosystem/products-and-services/browser-infrastructure-services-browserbase.md) |
| Browserless | Browserless | Headless Browser Service | `infrastructure` `cloud` `playwright` | [Website](https://www.browserless.io/) | [Report](reports/link-audit/ecosystem/products-and-services/browser-infrastructure-services-browserless.md) |
| AgentCore Browser | Amazon AWS | Enterprise Browser Tool | `infrastructure` `enterprise` `aws` | [Docs](https://docs.aws.amazon.com/bedrock-agentcore/) | [Report](reports/link-audit/ecosystem/products-and-services/browser-infrastructure-services-amazon-bedrock-agentcore-browser.md) |

## Open Source Frameworks

### Agent Frameworks

| Name | Organization | Focus | Stars | Tags | Link | Report |
|------|--------------|-------|-------|------|------|--------|
| UI-TARS Desktop | ByteDance | Desktop Agent Stack | 15k+ | `desktop` `multimodal` `sota` | [GitHub](https://github.com/bytedance/UI-TARS-desktop) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/desktop-agent-frameworks-ui-tars-desktop.md) |
| Browser Use | Browser Use | Web Automation | 10k+ | `web` `python` `llm` | [GitHub](https://github.com/browser-use/browser-use) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/web-browser-frameworks-browser-use.md) |
| Stagehand | Browserbase | Web Agent Control | 5k+ | `web` `typescript` `playwright` | [GitHub](https://github.com/browserbase/stagehand) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/web-browser-frameworks-stagehand.md) |
| LaVague | LaVague | Modular Web Agent | 5k+ | `web` `modular` `python` | [GitHub](https://github.com/lavague-ai/lavague) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/web-browser-frameworks-lavague.md) |
| Skyvern | Skyvern | Browser Workflow | 3k+ | `web` `vision` `automation` | [GitHub](https://github.com/Skyvern-AI/skyvern) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/web-browser-frameworks-skyvern.md) |
| OpenInterpreter | Open Interpreter | General Computer Control | 50k+ | `general` `code` `desktop` | [GitHub](https://github.com/OpenInterpreter/open-interpreter) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/desktop-agent-frameworks-openinterpreter.md) |
| OpenAdapt | OpenAdapt | Process Automation | 1k+ | `desktop` `rpa` `ai-first` | [GitHub](https://github.com/OpenAdaptAI/OpenAdapt) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/desktop-agent-frameworks-openadapt.md) |
| AutoGLM | Tsinghua/ChatGLM | Mobile Agent | 2k+ | `mobile` `android` `open-source` | [GitHub](https://github.com/THUDM/AutoGLM) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/mobile-agent-frameworks-autoglm.md) |
| AppAgent | Tencent | Smartphone Agent | 5k+ | `mobile` `android` `multimodal` | [GitHub](https://github.com/TencentQQGYLab/AppAgent) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/mobile-agent-frameworks-appagent.md) |
| Mobile-Agent | Alibaba X-PLUG | Mobile GUI Family | 3k+ | `mobile` `multi-agent` | [GitHub](https://github.com/X-PLUG/MobileAgent) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/mobile-agent-frameworks-mobile-agent.md) |

### Multi-Agent Frameworks

| Name | Organization | Focus | Tags | Link | Report |
|------|--------------|-------|------|------|--------|
| AutoGen | Microsoft | Multi-Agent Systems | `multi-agent` `conversation` | [GitHub](https://github.com/microsoft/autogen) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/multi-agent-frameworks-autogen.md) |
| CrewAI | CrewAI | Team-based Agents | `multi-agent` `orchestration` | [GitHub](https://github.com/joaomdmoura/crewAI) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/multi-agent-frameworks-crewai.md) |
| LangGraph | LangChain | Graph-based Agents | `multi-agent` `workflow` | [GitHub](https://github.com/langchain-ai/langgraph) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/multi-agent-frameworks-langgraph.md) |

### Grounding & Parsing Tools

| Name | Organization | Focus | Tags | Link | Report |
|------|--------------|-------|------|------|--------|
| OmniParser | Microsoft | Screen Parsing | `grounding` `yolo` `florence` | [GitHub](https://github.com/microsoft/OmniParser) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/grounding-and-parsing-tools-omniparser.md) |
| SeeClick | Nanjing Univ | GUI Grounding | `grounding` `vlm` | [GitHub](https://github.com/njucckevin/SeeClick) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/grounding-and-parsing-tools-seeclick.md) |

## Infrastructure & Tools

### Desktop Automation

| Name | Language | Platform | Tags | Link | Report |
|------|----------|----------|------|------|--------|
| PyAutoGUI | Python | Cross-platform | `automation` `python` | [GitHub](https://github.com/asweigart/pyautogui) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/desktop-automation-libraries-pyautogui.md) |
| nut.js | TypeScript | Cross-platform | `automation` `nodejs` | [GitHub](https://github.com/nut-tree/nut.js) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/desktop-automation-libraries-nut-js.md) |

### Sandbox Environments

| Name | Purpose | Tags | Link | Report |
|------|---------|------|------|--------|
| E2B Desktop Sandbox | Secure Agent Evaluation | `sandbox` `cloud` | [GitHub](https://github.com/e2b-dev/desktop) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/sandbox-and-testing-environments-e2b-desktop-sandbox.md) |
| Windows in Docker | Windows VM Containers | `windows` `docker` | [GitHub](https://github.com/dockur/windows) | [Report](reports/link-audit/ecosystem/frameworks-and-tools/sandbox-and-testing-environments-windows-in-docker.md) |

## Related Resources

### Curated Lists

| Name | Focus | Link | Report |
|------|-------|------|--------|
| GUI-Agents-Paper-List | Comprehensive Paper Collection | [GitHub](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-gui-agents-paper-list-osu-nlp-group.md) |
| Awesome-GUI-Agent | Showlab's Collection | [GitHub](https://github.com/showlab/Awesome-GUI-Agent) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-awesome-gui-agent-showlab.md) |
| Awesome-GUI-Agents | ZJU Collection | [GitHub](https://github.com/ZJU-REAL/Awesome-GUI-Agents) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-awesome-gui-agents-zju-real.md) |
| ACU (AI for Computer Use) | Papers, Projects, Tools | [GitHub](https://github.com/trycua/acu) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-acu-ai-for-computer-use.md) |
| ai-agent-papers | Biweekly Updated Papers | [GitHub](https://github.com/masamasa59/ai-agent-papers) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-ai-agent-papers.md) |
| awesome-mobile-agents | Mobile & PC GUI Agents | [GitHub](https://github.com/aialt/awesome-mobile-agents) | [Report](reports/link-audit/ecosystem/resources-and-guides/curated-paper-lists-awesome-mobile-agents.md) |

### Key Blog Posts & Articles

| Title | Source | Date | Link | Report |
|-------|--------|------|------|--------|
| Introducing Computer Use | Anthropic | Oct 2024 | [Blog](https://www.anthropic.com/news/3-5-models-and-computer-use) | [Report](reports/link-audit/ecosystem/resources-and-guides/key-blog-posts-and-announcements-anthropic-introducing-computer-use.md) |
| Computer-Using Agent | OpenAI | Jan 2025 | [Blog](https://openai.com/index/computer-using-agent/) | [Report](reports/link-audit/ecosystem/resources-and-guides/key-blog-posts-and-announcements-openai-computer-using-agent.md) |
| Operator System Card | OpenAI | Jan 2025 | [PDF](https://cdn.openai.com/operator_system_card.pdf) | [Report](reports/link-audit/ecosystem/resources-and-guides/key-blog-posts-and-announcements-openai-operator-system-card.md) |
| Introducing Gemini 2.5 Computer Use | Google | 2025 | [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model/) | [Report](reports/link-audit/ecosystem/resources-and-guides/key-blog-posts-and-announcements-google-gemini-2-5-computer-use.md) |
| AI is about to completely change how you use computers | Bill Gates | Nov 2024 | [Blog](https://www.gatesnotes.com/AI-agents) | [Report](reports/link-audit/ecosystem/resources-and-guides/industry-analysis-and-news-major-articles-ai-is-about-to-completely-change-how-you-use-computers.md) |

---

## Tags Reference

### Category Tags
- `survey` - Review/survey papers
- `model` - Model architecture papers
- `benchmark` - Evaluation benchmarks
- `dataset` - Training/evaluation datasets
- `method` - Techniques and methods
- `safety` - Safety research
- `security` - Security research

### Platform Tags
- `web` - Web/browser agents
- `desktop` - Desktop OS agents
- `mobile` - Mobile device agents
- `android` - Android-specific
- `ios` - iOS-specific
- `windows` - Windows-specific
- `macos` - macOS-specific
- `cross-platform` - Multiple platforms

### Technical Tags
- `vlm` - Vision-Language Model
- `llm` - Large Language Model
- `grounding` - UI element grounding
- `reinforcement-learning` - RL-based training
- `multi-agent` - Multi-agent systems
- `on-device` - On-device inference

### Organization Tags
- `microsoft` - Microsoft Research
- `google` - Google/DeepMind
- `anthropic` - Anthropic
- `openai` - OpenAI
- `bytedance` - ByteDance
- `alibaba` - Alibaba
- `tencent` - Tencent

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This repository is licensed under MIT License.

## Acknowledgments

This collection draws from multiple excellent resources including:
- [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) by OSU NLP Group
- [Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) by ShowLab
- [ACU](https://github.com/trycua/acu) by trycua

---

*Last updated: March 2026*
