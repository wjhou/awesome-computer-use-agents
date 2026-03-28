# Safety & Security Research for Computer Use Agents

Research on safety, security, adversarial attacks, and defensive measures.

## Safety Benchmarks

### AgentHarm: LLM Agent Safety Benchmark
- **Venue**: ICLR 2025
- **Link**: [arXiv:2410.09024](https://arxiv.org/abs/2410.09024)
- **Tags**: `safety` `benchmark` `jailbreak` `multi-step`

Benchmark assessing LLM agents' capacity to resist harmful tasks.

**Metrics**:
- HarmScore
- RefusalRate

**Key Findings**:
- Exposes vulnerabilities in multi-turn agentic settings
- Single-turn chatbot defenses don't transfer well

---

### WebGuard: Safety Dataset for Web Agents
- **Date**: July 2025
- **Link**: [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)
- **Tags**: `safety` `dataset` `web`

Safety-focused dataset for web agent evaluation.

---

## Security Research

### JARVIS or Ultron? Safety and Security Threats of CUAs
- **Date**: May 2025
- **Link**: [arXiv:2505.10924](https://arxiv.org/abs/2505.10924)
- **Tags**: `survey` `safety` `security` `comprehensive`

Comprehensive survey on CUA-specific threats.

**Vulnerability Categories**:
1. Visual grounding errors
2. Response delays
3. UI interpretation pitfalls

**Attack Types**:
- Adversarial attacks adapted to GUI environments
- Jailbreak strategies with heightened severity
- Goal misdirection
- Data leakage

---

### RedTeamCUA: Security Testing for Computer Use Agents
- **Venue**: ICLR 2026 Oral
- **Link**: [arXiv:2505.21936](https://arxiv.org/abs/2505.21936)
- **Tags**: `safety` `red-team` `testing`

Framework for red-teaming computer use agents.

---

### Attacking Vision-Language Computer Agents via Pop-ups
- **Venue**: ACL 2025
- **Link**: [arXiv:2411.02391](https://arxiv.org/abs/2411.02391)
- **Tags**: `security` `adversarial` `vlm` `pop-ups`

Adversarial attacks through malicious pop-up injection.

---

### EIA: Environmental Injection Attack
- **Date**: September 2024
- **Link**: [arXiv:2409.02453](https://arxiv.org/abs/2409.02453)
- **Tags**: `security` `privacy` `attack` `injection`

Privacy leakage study through environmental injection.

---

### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents
- **Venue**: NeurIPS 2025 D&B Spotlight
- **Link**: [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)
- **Tags**: `safety` `benchmark` `desktop` `prompt-injection`

Safety benchmark for computer-use agents built on top of the OSWorld environment.

**Statistics**:
- 150 tasks spanning deliberate misuse, prompt injection, and model misbehavior.

**Metrics**:
- Automated judge with reported 0.76 and 0.79 F1 agreement against human annotations.

**Key Findings**:
- Frontier models often comply with misuse requests, remain vulnerable to static prompt injections, and occasionally take unsafe actions.

---

### VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents
- **Venue**: ICLR 2026
- **Link**: [arXiv:2506.02456](https://arxiv.org/abs/2506.02456)
- **Tags**: `security` `prompt-injection` `visual` `benchmark`

Benchmark for visually embedded prompt injection attacks against computer-use and browser-use agents.

**Statistics**:
- 306 interactive test cases across five widely used platforms.

**Key Findings**:
- Reports deception rates up to 51% for computer-use agents and 100% for browser-use agents on some platforms.
- System-prompt defenses only provide limited robustness improvements.

---

### HackWorld: Evaluating Computer-Use Agents on Exploiting Web Application Vulnerabilities
- **Date**: October 2025
- **Link**: [arXiv:2510.12200](https://arxiv.org/abs/2510.12200)
- **Tags**: `security` `cybersecurity` `web` `benchmark`

CTF-style evaluation framework for whether computer-use agents can exploit web application vulnerabilities through visual interaction.

**Statistics**:
- 36 real-world applications across 11 frameworks and 7 programming languages.

**Key Findings**:
- Reported exploitation rates stay below 12%.
- Current agents struggle with multi-step attack planning and effective use of security tooling.

---

### GUIGuard: Toward a General Framework for Privacy-Preserving GUI Agents
- **Date**: January 2026
- **Link**: [arXiv:2601.18842](https://arxiv.org/abs/2601.18842)
- **Tags**: `safety` `privacy` `benchmark` `cross-platform`

Privacy-preserving GUI agent framework coupled with a benchmark for recognition, protection, and task completion.

**Framework Components**:
- Privacy recognition.
- Privacy protection.
- Task execution under protection.

**Statistics**:
- GUIGuard-Bench contains 630 trajectories and 13,830 screenshots with region-level privacy annotations.

**Key Findings**:
- Reported privacy recognition remains weak, reaching only 13.3% on Android and 1.4% on PC for the strongest tested models.

---

### When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents
- **Date**: February 2026
- **Link**: [arXiv:2602.08235](https://arxiv.org/abs/2602.08235)
- **Tags**: `security` `unintended-behavior` `red-team` `elicitation`

Framework for surfacing unsafe unintended CUA behaviors that emerge even from benign-looking inputs.

**Approach**:
- AutoElicit iteratively perturbs benign instructions using agent execution feedback while keeping them realistic.

**Key Findings**:
- Surfaces hundreds of harmful unintended behaviors across frontier computer-use agents.
- Human-verified perturbations transfer across multiple different CUA stacks.

---

### Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible
- **Date**: February 2026
- **Link**: [arXiv:2602.10139](https://arxiv.org/abs/2602.10139)
- **Tags**: `privacy` `mobile` `defense` `security`

Available-but-invisible privacy framework for cloud-backed mobile GUI agents.

**Framework Components**:
- PII Detector.
- UI Transformer.
- Secure Interaction Proxy.
- Privacy Gatekeeper.

**Key Findings**:
- Preserves task utility while substantially reducing privacy leakage on AndroidLab and PrivScreen.
- Reports the best privacy-utility trade-off among the compared protection methods.

---

## Jailbreak Research

### Large Reasoning Models are Autonomous Jailbreak Agents
- **Venue**: Nature Communications 2026
- **Link**: [Nature](https://www.nature.com/articles/s41467-026-69010-1)
- **Tags**: `security` `jailbreak` `lrm` `autonomous`

Large reasoning models as jailbreak vectors.

**Findings**:
- LRMs simplify and scale jailbreaking
- Makes jailbreaking accessible to non-experts
- 97.14% overall jailbreak success rate across 4 LRMs tested

---

### Infectious Jailbreaks in Multi-Agent Systems
- **Venue**: ICML 2024
- **Link**: [arXiv:2402.08567](https://arxiv.org/abs/2402.08567)
- **Tags**: `security` `jailbreak` `multi-agent` `spreading`

**Finding**: Adversarial image in one agent's memory can spread infection to ~100% of agents.

---

## AI Agents Security Survey

### AI Agents Under Threat: Key Security Challenges and Future Pathways
- **Venue**: ACM Computing Surveys 2025
- **Link**: [ACM](https://dl.acm.org/doi/10.1145/3716628)
- **Tags**: `survey` `security` `comprehensive`

Comprehensive survey on AI agent security challenges.

---

## Defense Strategies

### Certified Defenses
- Analyzing toxicity of all possible input substrings

### Multi-Agent Debate
- Language models self-evaluate through discussion
- Improves robustness against jailbreak

### Layered Safety Approach
Example from OpenAI Operator:
1. Model-level safeguards
2. System-level safeguards
3. Post-deployment monitoring

**Results**: 97% refusal rate on illicit activity evaluation set.

---

## Industry Safety Practices

### Anthropic Computer Use
- Built with safeguards minimizing risk
- Permission requests before accessing new apps
- Research preview with safety monitoring

### OpenAI Operator
- Three-class safety risk mitigation:
  1. Misuse
  2. Model mistakes
  3. Frontier risks
- Proactive user takeover for:
  - Login tasks
  - Payment details
  - CAPTCHAs

### Amazon Nova Act
- 90% reliability target for production workflows
- Enterprise-grade safety measures

---

## Key Security Considerations

### Threat Categories for CUAs

1. **Visual Manipulation**
   - Adversarial UI elements
   - Malicious pop-ups
   - Misleading visual content

2. **Prompt Injection**
   - Environmental injection
   - Cross-agent infection
   - Instruction hijacking

3. **Privacy Risks**
   - Data exfiltration
   - Credential exposure
   - Unintended information sharing

4. **Autonomy Risks**
   - Goal misalignment
   - Unintended actions
   - Lack of human oversight

### Recommended Mitigations

1. Human-in-the-loop for sensitive actions
2. Action confirmation for irreversible operations
3. Sandboxed execution environments
4. Continuous monitoring and logging
5. Rate limiting and scope restrictions
