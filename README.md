# Awesome Computer Use Agents

A comprehensive collection of research papers, products, frameworks, and resources for AI agents that can interact with computers through graphical user interfaces (GUIs).

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Table of Contents

- [Overview](#overview)
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

## Papers

### Survey Papers

| Title | Venue/Date | Tags | Link |
|-------|------------|------|------|
| Large Language Model-Brained GUI Agents: A Survey | arXiv 2024 | `survey` `llm` `gui` | [Paper](https://arxiv.org/abs/2411.18279) |
| GUI Agents: A Survey | ACL 2025 | `survey` `comprehensive` | [Paper](https://arxiv.org/abs/2412.13501) |
| GUI Agents with Foundation Models: A Comprehensive Survey | arXiv 2024 | `survey` `foundation-models` | [Paper](https://arxiv.org/abs/2411.04890) |
| LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects | arXiv 2025 | `survey` `mobile` | [Paper](https://arxiv.org/abs/2504.19838) |
| A Survey on Benchmarks of LLM-based GUI Agents | TechRxiv 2025 | `survey` `benchmarks` | [Paper](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176591818.87526814) |
| JARVIS or Ultron? Safety and Security Threats of Computer-Using Agents | arXiv 2025 | `survey` `safety` `security` | [Paper](https://arxiv.org/abs/2505.10924) |
| AI Agents: Evolution, Architecture, and Real-World Applications | arXiv 2025 | `survey` `architecture` | [Paper](https://arxiv.org/abs/2503.12687) |

See [papers/surveys/](papers/surveys/) for detailed information.

### Models & Architectures

| Title | Venue/Date | Tags | Link |
|-------|------------|------|------|
| UI-TARS: Pioneering Automated GUI Interaction with Native Agents | arXiv 2025 | `model` `bytedance` `sota` | [Paper](https://arxiv.org/abs/2501.12326) |
| UI-TARS-2: Advancing GUI Agent with Multi-Turn RL | arXiv 2025 | `model` `reinforcement-learning` | [Paper](https://arxiv.org/abs/2509.02544) |
| CogAgent: A Visual Language Model for GUI Agents | arXiv 2024 | `model` `vlm` `18b` | [Paper](https://arxiv.org/abs/2312.08914) |
| ShowUI: Vision-Language-Action Model for GUI Visual Agent | CVPR 2025 | `model` `vla` | [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.pdf) |
| ScreenAgent: A VLM-driven Computer Control Agent | IJCAI 2024 | `model` `vlm` `control` | [Paper](https://arxiv.org/abs/2402.07945) |
| SeeClick: Harnessing GUI Grounding for Visual GUI Agents | ACL 2024 | `model` `grounding` | [Paper](https://arxiv.org/abs/2401.10935) |
| OmniParser: Pure Vision Based GUI Agent | arXiv 2024 | `model` `grounding` `microsoft` | [Paper](https://arxiv.org/abs/2408.00203) |
| AGUVIS: Unified Pure Vision Agents for GUI Interaction | arXiv 2024 | `model` `vision-only` | [Paper](https://arxiv.org/abs/2412.04454) |
| AppAgent: Multimodal Agents as Smartphone Users | CHI 2025 | `model` `mobile` `android` | [Paper](https://arxiv.org/abs/2312.13771) |
| Mobile-Agent-v3: Fundamental Agents for GUI Automation | arXiv 2025 | `model` `mobile` `multi-agent` | [Paper](https://arxiv.org/abs/2508.15144) |
| AutoGLM: Autonomous Foundation Agents for GUIs | arXiv 2024 | `model` `mobile` `chatglm` | [Paper](https://arxiv.org/abs/2411.00820) |
| AgentCPM-GUI: On-device Mobile Agent | GitHub 2025 | `model` `mobile` `on-device` | [GitHub](https://github.com/OpenBMB/AgentCPM-GUI) |
| Ferret-UI: Grounded Mobile UI Understanding | arXiv 2024 | `model` `mobile` `grounding` | [Paper](https://arxiv.org/abs/2404.05719) |
| Qwen2.5-VL Technical Report | arXiv 2025 | `model` `vlm` `agent-capable` | [Paper](https://arxiv.org/abs/2502.13923) |
| R-VLM: Region-Aware VLM for Precise GUI Grounding | arXiv 2025 | `model` `grounding` | [Paper](https://arxiv.org/abs/2507.05673) |
| GUI-Actor: Coordinate-Free Visual Grounding | Microsoft 2025 | `model` `grounding` | [Project](https://microsoft.github.io/GUI-Actor/) |

See [papers/models/](papers/models/) for detailed information.

### Benchmarks & Datasets

| Title | Venue/Date | Tags | Link |
|-------|------------|------|------|
| OSWorld: Multimodal Agents for Open-Ended Tasks in Real Computer Environments | NeurIPS 2024 | `benchmark` `desktop` `multimodal` | [Paper](https://arxiv.org/abs/2404.07972) |
| WebArena: Realistic Web Environment for Building Autonomous Agents | arXiv 2023 | `benchmark` `web` | [Paper](https://arxiv.org/abs/2307.13854) |
| Mind2Web: Towards a Generalist Agent for the Web | NeurIPS 2023 | `benchmark` `dataset` `web` | [Paper](https://arxiv.org/abs/2306.06070) |
| VisualWebArena: Multimodal Web Tasks | arXiv 2024 | `benchmark` `web` `multimodal` | [Paper](https://arxiv.org/abs/2401.13649) |
| WebVoyager: End-to-End Web Agent with LMMs | arXiv 2024 | `benchmark` `web` `evaluation` | [Paper](https://arxiv.org/abs/2401.13919) |
| ScreenSpot / ScreenSpot-Pro | arXiv 2024/2025 | `benchmark` `grounding` `high-res` | [Paper](https://arxiv.org/abs/2401.10935) |
| Windows Agent Arena | arXiv 2024 | `benchmark` `windows` `desktop` | [Paper](https://arxiv.org/abs/2409.08264) |
| AndroidWorld: Dynamic Benchmarking Environment | arXiv 2024 | `benchmark` `android` `mobile` | [Paper](https://arxiv.org/abs/2405.14573) |
| Android in the Wild (AitW) | arXiv 2023 | `dataset` `android` `real-world` | [Paper](https://arxiv.org/abs/2307.10088) |
| AMEX: Android Multi-annotation EXpo | arXiv 2024 | `dataset` `android` `annotations` | [Paper](https://arxiv.org/abs/2407.17490) |
| A3: Android Agent Arena | arXiv 2025 | `benchmark` `android` `evaluation` | [Paper](https://arxiv.org/abs/2501.01149) |
| macOSWorld | arXiv 2025 | `benchmark` `macos` `desktop` | [Paper](https://arxiv.org/abs/2506.04135) |
| GUI Odyssey: Cross-app Mobile Navigation | arXiv 2024 | `benchmark` `mobile` `cross-app` | [Paper](https://arxiv.org/abs/2411.00820) |
| WebCanvas: Online Web Agent Benchmarking | arXiv 2024 | `benchmark` `web` `online` | [Paper](https://arxiv.org/abs/2406.12373) |
| Online-Mind2Web | arXiv 2025 | `benchmark` `web` `live-sites` | [Paper](https://arxiv.org/abs/2504.01382) |
| MobileAgentBench | arXiv 2024 | `benchmark` `mobile` `efficiency` | [Paper](https://arxiv.org/abs/2406.08184) |
| OmniACT | arXiv 2024 | `benchmark` `desktop` `web` | [Paper](https://arxiv.org/abs/2402.17553) |
| ScreenSuite (HuggingFace) | GitHub 2025 | `benchmark` `comprehensive` | [GitHub](https://github.com/huggingface/screensuite) |

See [papers/benchmarks/](papers/benchmarks/) for detailed information.

### Methods & Techniques

| Title | Venue/Date | Tags | Link |
|-------|------------|------|------|
| ComputerRL: End-to-End Online RL for Computer Use Agents | arXiv 2025 | `method` `reinforcement-learning` | [Paper](https://arxiv.org/abs/2508.14040) |
| WebRL: Self-Evolving Online Curriculum RL for Web Agents | arXiv 2024 | `method` `reinforcement-learning` `web` | [Paper](https://arxiv.org/abs/2411.02337) |
| DigiRL: Training In-The-Wild Device-Control | NeurIPS 2024 | `method` `reinforcement-learning` `mobile` | [Paper](https://arxiv.org/abs/2406.11896) |
| AgentTrek: Agent Trajectory Synthesis via Web Tutorials | arXiv 2024 | `method` `data-synthesis` `trajectories` | [Paper](https://arxiv.org/abs/2412.09605) |
| OS-Genesis: Automating GUI Agent Trajectory Construction | arXiv 2024 | `method` `data-synthesis` `reverse-task` | [Paper](https://arxiv.org/abs/2412.19723) |
| PC Agent-E: Efficient Agent Training for Computer Use | arXiv 2025 | `method` `efficient-training` | [Paper](https://arxiv.org/abs/2505.13909) |
| SeeAct: GPT-4V Web Agent via Visual Grounding | arXiv 2024 | `method` `grounding` `web` | [Paper](https://arxiv.org/abs/2401.01614) |
| UFO: Windows OS UI Agent via GPT-4V | arXiv 2024 | `method` `windows` `gpt-4v` | [Paper](https://arxiv.org/abs/2402.07939) |
| Ponder & Press: Advancing VLM Grounding | arXiv 2024 | `method` `grounding` `dual-model` | [Paper](https://arxiv.org/abs/2409.04566) |
| Chain-of-Agents: Multi-Agent Collaboration | arXiv 2025 | `method` `multi-agent` | [Paper](https://arxiv.org/abs/2508.13167) |
| GUI-Reflection: Self-Reflection for GUI Agents | arXiv 2025 | `method` `self-reflection` | [Project](https://penghao-wu.github.io/GUI_Reflection) |
| Magentic-One: Multi-Agent with Human-in-Loop | arXiv 2024 | `method` `multi-agent` `microsoft` | [Paper](https://arxiv.org/abs/2411.04468) |

See [papers/methods/](papers/methods/) for detailed information.

### Safety & Security

| Title | Venue/Date | Tags | Link |
|-------|------------|------|------|
| AgentHarm: LLM Agent Safety Benchmark | arXiv 2024 | `safety` `benchmark` `jailbreak` | [Paper](https://arxiv.org/abs/2410.09024) |
| RedTeamCUA: Security Testing for Computer Use Agents | arXiv 2025 | `safety` `red-team` | [Paper](https://arxiv.org/abs/2505.21936) |
| WebGuard: Safety Dataset for Web Agents | arXiv 2025 | `safety` `dataset` `web` | [Paper](https://arxiv.org/abs/2507.14293) |
| Attacking Vision-Language Computer Agents via Pop-ups | arXiv 2024 | `security` `adversarial` `vlm` | [Paper](https://arxiv.org/abs/2411.02391) |
| EIA: Environmental Injection Attack | arXiv 2024 | `security` `privacy` `attack` | [Paper](https://arxiv.org/abs/2409.02453) |
| Large Reasoning Models are Autonomous Jailbreak Agents | Nature 2026 | `security` `jailbreak` `lrm` | [Paper](https://www.nature.com/articles/s41467-026-69010-1) |
| AI Agents Under Threat: Key Security Challenges | ACM Computing Surveys 2025 | `survey` `security` | [Paper](https://dl.acm.org/doi/10.1145/3716628) |

See [papers/safety/](papers/safety/) for detailed information.

## Products & Commercial Solutions

### Major Tech Companies

| Product | Company | Platform | Status | Tags | Link |
|---------|---------|----------|--------|------|------|
| Computer Use | Anthropic | Desktop/Web | GA (Mar 2025) | `desktop` `api` `claude` | [Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) |
| Operator / CUA | OpenAI | Web | Preview (Jan 2025) | `web` `browser` `api` | [Product](https://openai.com/index/introducing-operator/) |
| Project Mariner | Google DeepMind | Web/Chrome | Preview (May 2025) | `web` `chrome` `gemini` | [Product](https://deepmind.google/models/project-mariner/) |
| Gemini 2.5 Computer Use | Google | Desktop/Web | Preview (2025) | `desktop` `gemini` | [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model/) |
| Nova Act | Amazon AWS | Web | GA (2025) | `web` `enterprise` `aws` | [Product](https://aws.amazon.com/nova/act/) |
| Apple Intelligence (Siri Agent) | Apple | iOS/macOS | Development | `mobile` `on-device` | [Info](https://www.apple.com/apple-intelligence/) |

### Startups & Products

| Product | Company | Focus | Tags | Link |
|---------|---------|-------|------|------|
| Manus | Butterfly Effect | General-purpose Agent | `general` `multi-model` `acquired-meta` | [Website](https://manus.bot) |
| Rabbit R1 | Rabbit Inc | Hardware Device + LAM | `hardware` `mobile` `lam` | [Website](https://www.rabbit.tech/rabbit-r1) |
| Twin | Twin Labs | Workflow Automation | `enterprise` `workflow` `browser` | [Website](https://twin.so/) |
| HyperWrite | HyperWrite AI | Browser Assistant | `browser` `personal-assistant` | [Website](https://www.hyperwriteai.com/personal-assistant) |
| MultiOn | MultiOn | Browser Automation | `browser` `automation` `api` | [Website](https://www.multion.ai/) |
| ACT-1 | Adept AI | Action Transformer | `enterprise` `acquired-amazon` | [Blog](https://www.adept.ai/blog/act-1/) |
| Runner H | H Company | Real-world Applications | `enterprise` `web` | [Website](https://www.hcompany.ai/) |

### Browser Infrastructure

| Product | Company | Focus | Tags | Link |
|---------|---------|-------|------|------|
| Browserbase | Browserbase | Cloud Browser for Agents | `infrastructure` `cloud` `api` | [Website](https://www.browserbase.com/) |
| Browserless | Browserless | Headless Browser Service | `infrastructure` `cloud` `playwright` | [Website](https://www.browserless.io/) |
| AgentCore Browser | Amazon AWS | Enterprise Browser Tool | `infrastructure` `enterprise` `aws` | [Docs](https://docs.aws.amazon.com/bedrock-agentcore/) |

## Open Source Frameworks

### Agent Frameworks

| Name | Organization | Focus | Stars | Tags | Link |
|------|--------------|-------|-------|------|------|
| UI-TARS Desktop | ByteDance | Desktop Agent Stack | 15k+ | `desktop` `multimodal` `sota` | [GitHub](https://github.com/bytedance/UI-TARS-desktop) |
| Browser Use | Browser Use | Web Automation | 10k+ | `web` `python` `llm` | [GitHub](https://github.com/browser-use/browser-use) |
| Stagehand | Browserbase | Web Agent Control | 5k+ | `web` `typescript` `playwright` | [GitHub](https://github.com/browserbase/stagehand) |
| LaVague | LaVague | Modular Web Agent | 5k+ | `web` `modular` `python` | [GitHub](https://github.com/lavague-ai/lavague) |
| Skyvern | Skyvern | Browser Workflow | 3k+ | `web` `vision` `automation` | [GitHub](https://github.com/Skyvern-AI/skyvern) |
| OpenInterpreter | Open Interpreter | General Computer Control | 50k+ | `general` `code` `desktop` | [GitHub](https://github.com/OpenInterpreter/open-interpreter) |
| OpenAdapt | OpenAdapt | Process Automation | 1k+ | `desktop` `rpa` `ai-first` | [GitHub](https://github.com/OpenAdaptAI/OpenAdapt) |
| AutoGLM | Tsinghua/ChatGLM | Mobile Agent | 2k+ | `mobile` `android` `open-source` | [GitHub](https://github.com/THUDM/AutoGLM) |
| AppAgent | Tencent | Smartphone Agent | 5k+ | `mobile` `android` `multimodal` | [GitHub](https://github.com/TencentQQGYLab/AppAgent) |
| Mobile-Agent | Alibaba X-PLUG | Mobile GUI Family | 3k+ | `mobile` `multi-agent` | [GitHub](https://github.com/X-PLUG/MobileAgent) |

### Multi-Agent Frameworks

| Name | Organization | Focus | Tags | Link |
|------|--------------|-------|------|------|
| AutoGen | Microsoft | Multi-Agent Systems | `multi-agent` `conversation` | [GitHub](https://github.com/microsoft/autogen) |
| CrewAI | CrewAI | Team-based Agents | `multi-agent` `orchestration` | [GitHub](https://github.com/joaomdmoura/crewAI) |
| LangGraph | LangChain | Graph-based Agents | `multi-agent` `workflow` | [GitHub](https://github.com/langchain-ai/langgraph) |

### Grounding & Parsing Tools

| Name | Organization | Focus | Tags | Link |
|------|--------------|-------|------|------|
| OmniParser | Microsoft | Screen Parsing | `grounding` `yolo` `florence` | [GitHub](https://github.com/microsoft/OmniParser) |
| SeeClick | Nanjing Univ | GUI Grounding | `grounding` `vlm` | [GitHub](https://github.com/njucckevin/SeeClick) |

## Infrastructure & Tools

### Desktop Automation

| Name | Language | Platform | Tags | Link |
|------|----------|----------|------|------|
| PyAutoGUI | Python | Cross-platform | `automation` `python` | [GitHub](https://github.com/asweigart/pyautogui) |
| nut.js | TypeScript | Cross-platform | `automation` `nodejs` | [GitHub](https://github.com/nut-tree/nut.js) |

### Sandbox Environments

| Name | Purpose | Tags | Link |
|------|---------|------|------|
| E2B Desktop Sandbox | Secure Agent Evaluation | `sandbox` `cloud` | [GitHub](https://github.com/e2b-dev/desktop) |
| Windows in Docker | Windows VM Containers | `windows` `docker` | [GitHub](https://github.com/dockur/windows) |

## Related Resources

### Curated Lists

| Name | Focus | Link |
|------|-------|------|
| GUI-Agents-Paper-List | Comprehensive Paper Collection | [GitHub](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) |
| Awesome-GUI-Agent | Showlab's Collection | [GitHub](https://github.com/showlab/Awesome-GUI-Agent) |
| Awesome-GUI-Agents | ZJU Collection | [GitHub](https://github.com/ZJU-REAL/Awesome-GUI-Agents) |
| ACU (AI for Computer Use) | Papers, Projects, Tools | [GitHub](https://github.com/trycua/acu) |
| ai-agent-papers | Biweekly Updated Papers | [GitHub](https://github.com/masamasa59/ai-agent-papers) |
| awesome-mobile-agents | Mobile & PC GUI Agents | [GitHub](https://github.com/aialt/awesome-mobile-agents) |

### Key Blog Posts & Articles

| Title | Source | Date | Link |
|-------|--------|------|------|
| Introducing Computer Use | Anthropic | Oct 2024 | [Blog](https://www.anthropic.com/news/3-5-models-and-computer-use) |
| Computer-Using Agent | OpenAI | Jan 2025 | [Blog](https://openai.com/index/computer-using-agent/) |
| Operator System Card | OpenAI | Jan 2025 | [PDF](https://cdn.openai.com/operator_system_card.pdf) |
| Introducing Gemini 2.5 Computer Use | Google | 2025 | [Blog](https://blog.google/technology/google-deepmind/gemini-computer-use-model/) |
| AI is about to completely change how you use computers | Bill Gates | Nov 2024 | [Blog](https://www.gatesnotes.com/AI-agents) |

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
