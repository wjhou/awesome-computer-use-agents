# Benchmarks & Datasets for Computer Use Agents

Comprehensive collection of evaluation benchmarks and training datasets.

## Desktop Benchmarks

### OSWorld: Multimodal Agents for Open-Ended Tasks in Real Computer Environments
- **Venue**: NeurIPS 2024
- **Link**: [arXiv:2404.07972](https://arxiv.org/abs/2404.07972)
- **Website**: [os-world.github.io](https://os-world.github.io/)
- **Code**: [GitHub](https://github.com/xlang-ai/OSWorld)
- **Tags**: `benchmark` `desktop` `multimodal` `open-ended`

First-of-its-kind scalable, real computer environment for multimodal agents.

**Statistics**:
- 369 computer tasks
- Supports Ubuntu, Windows, macOS
- Real web and desktop apps
- OS file I/O and multi-app workflows

**Performance Gap**:
- Human: 72.36%
- Best Model: 12.24%

---

### Windows Agent Arena (WAA)
- **Organization**: Microsoft Research
- **Venue**: ICML 2025 Poster
- **Link**: [arXiv:2409.08264](https://arxiv.org/abs/2409.08264)
- **Website**: [microsoft.github.io/WindowsAgentArena](https://microsoft.github.io/WindowsAgentArena/)
- **Code**: [GitHub](https://github.com/microsoft/WindowsAgentArena)
- **Tags**: `benchmark` `windows` `desktop` `scalable`

Reproducible environment focusing on Windows OS.

**Statistics**:
- 154 diverse tasks
- 10+ applications (LibreOffice, Edge, VS Code, VLC, etc.)

**Performance Gap**:
- Human: 74.5%
- Best AI Agent: 19.5%

**Features**:
- Cloud parallelization via Azure
- Docker containers with Windows 11 VMs

---

### macOSWorld
- **Date**: June 2025
- **Link**: [arXiv:2506.04135](https://arxiv.org/abs/2506.04135)
- **Tags**: `benchmark` `macos` `desktop`

Benchmark specifically for macOS desktop environment.

---

## Web Benchmarks

### WebArena: Realistic Web Environment for Building Autonomous Agents
- **Venue**: ICLR 2024 Poster
- **Link**: [arXiv:2307.13854](https://arxiv.org/abs/2307.13854)
- **Website**: [webarena.dev](https://webarena.dev/)
- **Tags**: `benchmark` `web` `realistic`

**Current SOTA**:
- CUA (OpenAI): 58.1% (vs Human 78.2%)

---

### Mind2Web: Towards a Generalist Agent for the Web
- **Venue**: NeurIPS 2023 Spotlight
- **Link**: [arXiv:2306.06070](https://arxiv.org/abs/2306.06070)
- **Website**: [osu-nlp-group.github.io/Mind2Web](https://osu-nlp-group.github.io/Mind2Web/)
- **Code**: [GitHub](https://github.com/OSU-NLP-Group/Mind2Web)
- **Tags**: `benchmark` `dataset` `web` `generalist`

First dataset for developing generalist web agents.

**Statistics**:
- 2,000+ open-ended tasks
- 137 websites
- 31 domains
- Crowdsourced action sequences

---

### Online-Mind2Web
- **Venue**: COLM 2025
- **Link**: [arXiv:2504.01382](https://arxiv.org/abs/2504.01382)
- **Tags**: `benchmark` `web` `live-sites`

**Improvements over Mind2Web**:
- 300 diverse tasks across 136 websites
- Live website evaluation (vs cached pages)
- Handles cookies, pop-ups, changing layouts

---

### VisualWebArena: Multimodal Web Tasks
- **Venue**: ACL 2024
- **Link**: [arXiv:2401.13649](https://arxiv.org/abs/2401.13649)
- **Tags**: `benchmark` `web` `multimodal` `visual`

Extends WebArena with multimodal visual tasks.

---

### WebVoyager: End-to-End Web Agent with LMMs
- **Venue**: ACL 2024
- **Link**: [arXiv:2401.13919](https://arxiv.org/abs/2401.13919)
- **Tags**: `benchmark` `web` `evaluation` `end-to-end`

**Known Limitations**:
- Limited task/website coverage
- Shortcut solutions possible (51% via Google Search)
- Low LLM-as-Judge agreement with humans

---

### WebCanvas: Online Web Agent Benchmarking
- **Date**: June 2024
- **Link**: [arXiv:2406.12373](https://arxiv.org/abs/2406.12373)
- **Tags**: `benchmark` `web` `online` `dynamic`

Real-time web benchmarking with live sites.

---

## Mobile Benchmarks

### AndroidWorld: Dynamic Benchmarking Environment
- **Venue**: ICLR 2025 Poster
- **Link**: [arXiv:2405.14573](https://arxiv.org/abs/2405.14573)
- **Tags**: `benchmark` `android` `mobile` `dynamic`

Dynamic benchmarking environment for Android agents.

**Current SOTA**:
- UI-TARS: 46.6
- Mobile-Agent-v3: 73.3

---

### Android in the Wild (AitW)
- **Venue**: NeurIPS 2023 D&B
- **Link**: [arXiv:2307.10088](https://arxiv.org/abs/2307.10088)
- **Tags**: `dataset` `android` `real-world`

Real-world device control scenarios for Android.

---

### AMEX: Android Multi-annotation EXpo
- **Date**: July 2024
- **Link**: [arXiv:2407.17490](https://arxiv.org/abs/2407.17490)
- **Tags**: `dataset` `android` `annotations` `comprehensive`

**Statistics**:
- 104K+ high-resolution screenshots
- 110 popular mobile applications
- Multi-level annotations:
  - GUI element grounding
  - Functionality descriptions
  - Complex NL instructions

---

### A3: Android Agent Arena
- **Date**: January 2025
- **Link**: [arXiv:2501.01149](https://arxiv.org/abs/2501.01149)
- **Tags**: `benchmark` `android` `evaluation` `practical`

**Features**:
- 21 widely used third-party apps
- 201 representative user tasks
- Automated LLM-based evaluation

---

### MobileAgentBench
- **Date**: June 2024
- **Link**: [arXiv:2406.08184](https://arxiv.org/abs/2406.08184)
- **Tags**: `benchmark` `mobile` `efficiency`

**Statistics**:
- 100 tasks across 10 open-source apps
- Systematic comparison of AppAgent, MobileAgent, etc.

---

### GUI Odyssey: Cross-app Mobile Navigation
- **Date**: 2024
- **Link**: [arXiv:2411.00820](https://arxiv.org/abs/2411.00820)
- **Tags**: `benchmark` `mobile` `cross-app` `navigation`

Cross-application navigation benchmark for mobile.

---

## Grounding Benchmarks

### ScreenSpot / ScreenSpot-Pro
- **Date**: 2024/2025
- **Link**: [arXiv:2401.10935](https://arxiv.org/abs/2401.10935)
- **Tags**: `benchmark` `grounding` `high-res` `professional`

**ScreenSpot**: First realistic GUI grounding dataset
- Mobile, desktop, web environments

**ScreenSpot-Pro**:
- 1,581 tasks across 23 applications
- Professional, high-resolution environments
- Industry-focused

---

## Cross-Platform Benchmarks

### OmniACT
- **Date**: February 2024
- **Link**: [arXiv:2402.17553](https://arxiv.org/abs/2402.17553)
- **Tags**: `benchmark` `desktop` `web` `cross-platform`

Benchmark for desktop and web agents.

---

### ScreenSuite (HuggingFace)
- **Organization**: HuggingFace
- **Code**: [GitHub](https://github.com/huggingface/screensuite)
- **Tags**: `benchmark` `comprehensive` `unified`

Most comprehensive benchmarking suite for GUI agents.

**Includes**:
- ScreenSpot-v1, v2, Pro
- OSWorld

---

### MMBench-GUI: Hierarchical Multi-Platform Evaluation Framework for GUI Agents
- **Date**: July 2025
- **Link**: [arXiv:2507.19478](https://arxiv.org/abs/2507.19478)
- **Tags**: `benchmark` `cross-platform` `hierarchical` `efficiency`

Hierarchical benchmark for GUI agents spanning desktop, mobile, and web platforms.

**Statistics**:
- Covers Windows, macOS, Linux, iOS, Android, and Web.
- Evaluates four levels: content understanding, element grounding, task automation, and task collaboration.

**Metrics**:
- Efficiency-Quality Area (EQA) measures both task success and execution efficiency.

**Key Findings**:
- Accurate visual grounding is a primary determinant of end-to-end task success.
- Existing agents remain highly inefficient, often taking many redundant steps.

---

### OS-MAP: How Far Can Computer-Using Agents Go in Breadth and Depth?
- **Date**: July 2025
- **Link**: [arXiv:2507.19132](https://arxiv.org/abs/2507.19132)
- **Code**: [GitHub](https://github.com/OS-Copilot/OS-Map)
- **Tags**: `benchmark` `desktop` `taxonomy` `generalization`

Benchmark for daily computer-use automation organized by autonomy level and generalization scope.

**Statistics**:
- 416 realistic tasks across 15 applications.
- Five automation levels combined with a user-demand hierarchy form a performance-generalization matrix.

**Key Findings**:
- Even frontier VLM-based agents struggle on higher-level tasks requiring perception, reasoning, and coordination.

---

### OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents
- **Date**: October 2025
- **Link**: [arXiv:2510.24563](https://arxiv.org/abs/2510.24563)
- **Website**: [osworld-mcp.github.io](https://osworld-mcp.github.io/)
- **Tags**: `benchmark` `tool-calling` `desktop` `mcp`

Benchmark for fair evaluation of GUI control, MCP tool invocation, and decision-making in shared environments.

**Statistics**:
- 158 manually validated tools spanning 7 common applications.

**Key Findings**:
- Reported task success improves with tools, such as o3 from 8.3% to 20.4% at 15 steps.
- Even strong models invoke tools infrequently, with the paper reporting only 36.3% tool usage at best.

---

### Computer Agent Arena: Toward Human-Centric Evaluation and Analysis of Computer-Use Agents
- **Venue**: ICLR 2026 Poster
- **Link**: [OpenReview](https://openreview.net/forum?id=3x4SDbXbgl)
- **Tags**: `benchmark` `human-centric` `evaluation` `preference`

Human-preference arena for measuring how computer-use agents actually feel in realistic use.

**Statistics**:
- 2,201 high-quality human preference votes comparing 12 different agents.

**Key Findings**:
- Human rankings can invert relative to static benchmark rankings.
- Correctness matters most, but self-correction behavior and agent-human interaction quality also shape preference.

---

### CUA-Suite: Expert Trajectories and Pixel-Precise Grounding for Computer-use Agents
- **Venue**: LLA 2026 Poster
- **Link**: [OpenReview](https://openreview.net/forum?id=IgTUGrZfMr)
- **Tags**: `dataset` `grounding` `desktop` `human-demonstrations`

Desktop CUA benchmark and training suite built from expert trajectories and dense grounding annotations.

**Statistics**:
- 56K screenshots with more than 5 million element annotations across 87 desktop applications.
- Roughly 10,000 expert-demonstrated tasks with lengthy step-level reasoning annotations.

**Includes**:
- UI-Vision benchmark for desktop GUI understanding.
- GroundCUA grounding data and ActCUA expert trajectory data.

**Key Findings**:
- Current foundation action models still struggle on professional desktop software despite the richer supervision.
- Multiple other benchmarks

---

## Specialized Benchmarks

### Spider2-V: Data Science Workflows
- **Date**: 2024
- **Link**: [arXiv:2407.10956](https://arxiv.org/abs/2407.10956)
- **Tags**: `benchmark` `data-science` `specialized`

Benchmark for data science workflow automation.

---

### VideoGUI: Instructional Video Automation
- **Date**: 2024
- **Link**: [arXiv:2406.10227](https://arxiv.org/abs/2406.10227)
- **Tags**: `benchmark` `video` `instructions`

Automation from instructional video content.

---

### GUICourse: Vision-Language to Agents
- **Date**: 2024
- **Link**: [arXiv:2406.11317](https://arxiv.org/abs/2406.11317)
- **Tags**: `benchmark` `training` `curriculum`

Curriculum-based benchmark for agent development.

---

## Trajectory Datasets

### AgentTrek Trajectories
- **Link**: [agenttrek.github.io](https://agenttrek.github.io/)
- **Tags**: `dataset` `trajectories` `web`

Cost: $0.55 per high-quality trajectory (fully automated).

---

### OS-Genesis Trajectories
- **Link**: [Project](https://qiushisun.github.io/OS-Genesis-Home/)
- **Tags**: `dataset` `trajectories` `reverse-synthesis`

Reverse task synthesis for trajectory generation.
