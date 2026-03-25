# Models & Architectures for Computer Use Agents

Research papers on model architectures, visual language models, and agent systems.

## State-of-the-Art Models

### UI-TARS Series (ByteDance)

#### UI-TARS: Pioneering Automated GUI Interaction with Native Agents
- **Organization**: ByteDance Seed / Tsinghua University
- **Date**: January 2025
- **Link**: [arXiv:2501.12326](https://arxiv.org/abs/2501.12326)
- **Code**: [GitHub](https://github.com/bytedance/UI-TARS)
- **Tags**: `model` `bytedance` `sota` `end-to-end`

Native GUI agent model that solely perceives screenshots and performs human-like interactions.

**Key Innovations**:
1. **Enhanced Perception**: Large-scale dataset of GUI screenshots for context-aware understanding
2. **Unified Action Modeling**: Standardized actions across platforms
3. **System-2 Reasoning**: Deliberate reasoning with task decomposition, reflection, milestone recognition
4. **Iterative Training**: Reflective online traces collection on virtual machines

**Performance**:
- OSWorld: 24.6 (50 steps), 22.7 (15 steps) - outperforms Claude
- AndroidWorld: 46.6 - surpasses GPT-4o (34.5)

#### UI-TARS-2: Advancing GUI Agent with Multi-Turn RL
- **Date**: September 2025
- **Link**: [arXiv:2509.02544](https://arxiv.org/abs/2509.02544)
- **Tags**: `model` `reinforcement-learning` `multi-turn`

Extension using multi-turn reinforcement learning for improved performance.

---

### CogAgent: A Visual Language Model for GUI Agents
- **Organization**: Tsinghua/Zhipu AI
- **Date**: December 2023
- **Link**: [arXiv:2312.08914](https://arxiv.org/abs/2312.08914)
- **Tags**: `model` `vlm` `18b` `cross-platform`

18-billion-parameter VLM leveraging high-resolution image encoders to interpret complex GUI elements.

**Capabilities**:
- Leading performance on text-rich VQA
- GUI navigation benchmarks across PC and Android
- High-resolution image understanding (1120x1120)

---

### ShowUI: Vision-Language-Action Model for GUI Visual Agent
- **Venue**: CVPR 2025
- **Link**: [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.pdf)
- **Tags**: `model` `vla` `efficient`

Vision-Language-Action model with novel UI-guided visual token selection strategy.

**Features**:
- Efficient visual modeling through UI-guided token selection
- Interleaved vision-language-action streaming
- Unified handling of different GUI tasks

---

### ScreenAgent: A VLM-driven Computer Control Agent
- **Venue**: IJCAI 2024
- **Link**: [arXiv:2402.07945](https://arxiv.org/abs/2402.07945)
- **Code**: [GitHub](https://github.com/niuzaisheng/ScreenAgent)
- **Tags**: `model` `vlm` `control` `pipeline`

Environment for VLM agent to interact with real computer screens.

**Pipeline Phases**:
1. Planning
2. Acting
3. Reflecting

---

### OmniParser: Pure Vision Based GUI Agent
- **Organization**: Microsoft Research
- **Date**: August 2024
- **Link**: [arXiv:2408.00203](https://arxiv.org/abs/2408.00203)
- **Code**: [GitHub](https://github.com/microsoft/OmniParser)
- **Tags**: `model` `grounding` `microsoft` `parsing`

Screen parsing tool that converts UI screenshots to structured format.

**Components**:
- **Detection Module**: Fine-tuned YOLOv8 for interactive elements
- **Captioning Module**: Fine-tuned Florence-2 for element descriptions

**Performance**:
- OmniParser+GPT-4o: 39.6 on ScreenSpot Pro (vs GPT-4o's 0.8)

---

### SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents
- **Venue**: ACL 2024
- **Link**: [arXiv:2401.10935](https://arxiv.org/abs/2401.10935)
- **Code**: [GitHub](https://github.com/njucckevin/SeeClick)
- **Tags**: `model` `grounding` `screenspot`

Visual GUI agent with GUI grounding pre-training.

**Contributions**:
- ScreenSpot benchmark creation
- Automated GUI grounding data curation
- Cross-platform capabilities (mobile, desktop, web)

---

## Mobile-Focused Models

### AppAgent: Multimodal Agents as Smartphone Users
- **Organization**: Tencent
- **Venue**: CHI 2025
- **Link**: [arXiv:2312.13771](https://arxiv.org/abs/2312.13771)
- **Code**: [GitHub](https://github.com/TencentQQGYLab/AppAgent)
- **Tags**: `model` `mobile` `android` `learning`

LLM-based multimodal agent for smartphone operation.

**Approach**:
- Two phases: Exploration and Deployment
- Learns through autonomous exploration or human demonstrations
- Generates knowledge base for task execution

---

### Mobile-Agent-v3: Fundamental Agents for GUI Automation
- **Organization**: Alibaba X-PLUG
- **Date**: August 2025
- **Link**: [arXiv:2508.15144](https://arxiv.org/abs/2508.15144)
- **Code**: [GitHub](https://github.com/X-PLUG/MobileAgent)
- **Tags**: `model` `mobile` `multi-agent` `sota`

GUI-Owl foundational model achieving SOTA among open-source models.

**Performance**:
- AndroidWorld: 73.3
- OSWorld-Verified: 37.7

---

### AutoGLM: Autonomous Foundation Agents for GUIs
- **Organization**: Tsinghua/ChatGLM
- **Date**: November 2024
- **Link**: [arXiv:2411.00820](https://arxiv.org/abs/2411.00820)
- **Code**: [GitHub](https://github.com/THUDM/AutoGLM)
- **Model**: [HuggingFace](https://huggingface.co/THUDM/AutoGLM-Phone-9B)
- **Tags**: `model` `mobile` `chatglm` `open-source`

Open-source phone agent framework built on ChatGLM family.

**Supported Apps**: Gmail, Google Maps, WeChat, Taobao, Meituan (English & Chinese)

---

### AgentCPM-GUI: On-device Mobile Agent
- **Organization**: OpenBMB
- **Date**: 2025
- **Code**: [GitHub](https://github.com/OpenBMB/AgentCPM-GUI)
- **Tags**: `model` `mobile` `on-device` `8b`

8B-parameter on-device GUI agent for Android.

**Training Pipeline**:
1. Grounding-aware pre-training (12M samples)
2. Supervised fine-tuning (55K trajectories)
3. RL fine-tuning with GRPO

---

### Ferret-UI: Grounded Mobile UI Understanding
- **Organization**: Apple
- **Date**: April 2024
- **Link**: [arXiv:2404.05719](https://arxiv.org/abs/2404.05719)
- **Tags**: `model` `mobile` `grounding` `apple`

Mobile UI understanding with grounding capabilities.

---

## Vision-Language Models with Agent Capabilities

### Qwen2.5-VL Technical Report
- **Organization**: Alibaba Qwen Team
- **Date**: February 2025
- **Link**: [arXiv:2502.13923](https://arxiv.org/abs/2502.13923)
- **Model**: [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct)
- **Tags**: `model` `vlm` `agent-capable` `reasoning`

Visual agent capable of reasoning and dynamically directing tools.

**Agent Capabilities**:
- Computer use and phone use
- Tool usage in real-world scenarios
- Operating computers and mobile devices

---

### AGUVIS: Unified Pure Vision Agents for GUI Interaction
- **Date**: December 2024
- **Link**: [arXiv:2412.04454](https://arxiv.org/abs/2412.04454)
- **Tags**: `model` `vision-only` `unified` `cross-platform`

Pure vision-based framework for autonomous GUI agents.

**Features**:
- Image-based observations only
- Consistent action space across platforms
- Large-scale trajectory dataset

---

### R-VLM: Region-Aware VLM for Precise GUI Grounding
- **Date**: July 2025
- **Link**: [arXiv:2507.05673](https://arxiv.org/abs/2507.05673)
- **Tags**: `model` `grounding` `region-aware`

Addresses GUI element grounding across diverse platforms by reducing irrelevant information processing.

---

### GUI-Actor: Coordinate-Free Visual Grounding
- **Organization**: Microsoft
- **Date**: June 2025
- **Link**: [Project](https://microsoft.github.io/GUI-Actor/)
- **Tags**: `model` `grounding` `coordinate-free` `microsoft`

Novel approach to GUI grounding without explicit coordinates.
