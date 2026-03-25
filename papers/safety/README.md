# Safety & Security Research for Computer Use Agents

Research on safety, security, adversarial attacks, and defensive measures.

## Safety Benchmarks

### AgentHarm: LLM Agent Safety Benchmark
- **Date**: October 2024
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
- **Date**: May 2025
- **Link**: [arXiv:2505.21936](https://arxiv.org/abs/2505.21936)
- **Tags**: `safety` `red-team` `testing`

Framework for red-teaming computer use agents.

---

### Attacking Vision-Language Computer Agents via Pop-ups
- **Date**: November 2024
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
