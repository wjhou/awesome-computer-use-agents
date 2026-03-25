# Commercial Products & Solutions

Comprehensive list of commercial computer use agent products and services.

## Major Tech Companies

### Anthropic - Claude Computer Use
- **Status**: Generally Available (March 2025)
- **Platform**: Desktop (macOS, Windows, Linux), Web
- **Link**: [Documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
- **Tags**: `desktop` `api` `claude` `mac` `windows`

**Features**:
- Full desktop control via Claude
- Dispatch feature for mobile-to-desktop control
- App integrations (Slack, Calendar, etc.)
- Falls back to mouse/keyboard when no integration available

**Access**:
- Claude Pro ($20/month)
- Claude Max ($100/month)

**How It Works**:
1. User messages Claude from phone or desktop
2. Claude executes tasks on desktop
3. Results sent back to user

---

### OpenAI - Operator / CUA
- **Status**: Research Preview (January 2025)
- **Platform**: Web/Browser
- **Links**:
  - [Product](https://openai.com/index/introducing-operator/)
  - [CUA Model](https://openai.com/index/computer-using-agent/)
  - [System Card](https://cdn.openai.com/operator_system_card.pdf)
  - [API Docs](https://developers.openai.com/api/docs/guides/tools-computer-use)
  - [Sample App](https://github.com/openai/openai-cua-sample-app)
- **Tags**: `web` `browser` `api` `research-preview`

**Architecture**:
- CUA model combines GPT-4o vision with RL-based reasoning
- Trained on GUI interaction
- Multi-step planning with self-correction

**Performance**:
- OSWorld: 38.1% (vs Human 72.4%)
- WebArena: 58.1% (vs Human 78.2%)

**Safety**:
- 97% refusal rate on illicit activity tasks
- Proactive user takeover for logins, payments, CAPTCHAs

---

### Google - Project Mariner
- **Status**: Preview (May 2025)
- **Platform**: Chrome Browser, Web
- **Links**:
  - [Product](https://deepmind.google/models/project-mariner/)
  - [Computer Use Model](https://blog.google/technology/google-deepmind/gemini-computer-use-model/)
- **Tags**: `web` `chrome` `gemini` `browser`

**Technology**:
- Powered by Gemini 2.5 Computer Use model
- Takes frequent screenshots
- Identifies interactive elements via spatial reasoning
- Generates clicks and keystrokes

**Related Products**:
- Firebase Testing Agent
- AI Mode in Search

---

### Amazon AWS - Nova Act
- **Status**: Generally Available (2025)
- **Platform**: Web/Browser
- **Links**:
  - [Product](https://aws.amazon.com/nova/act/)
  - [SDK](https://github.com/aws/nova-act)
  - [Bedrock AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-quickstart-nova-act.html)
- **Tags**: `web` `enterprise` `aws` `production`

**Key Features**:
- 90% reliability for production workflows
- Custom computer use model for complex UI automation
- Scales to hundreds of thousands of workflows/month

**Use Cases**:
- Form filling across multiple sites
- Payment reconciliation
- Shipment coordination
- Medical records updating

**Integration**:
- Works with AgentCore Browser Tool
- Secure cloud-based browser environment

---

### Apple - Siri Agent (Apple Intelligence)
- **Status**: In Development (Expected WWDC 2026)
- **Platform**: iOS, macOS
- **Link**: [Apple Intelligence](https://www.apple.com/apple-intelligence/)
- **Tags**: `mobile` `on-device` `privacy` `ios` `macos`

**Reported Features**:
- On-device AI agent for iPhone apps
- 90%+ success rate in controlled conditions
- Runs on Apple Silicon locally
- No cloud data transmission

---

## Startups

### Manus (Butterfly Effect)
- **Location**: Wuhan, China (with Beijing office)
- **Status**: Acquired by Meta (December 2025, $2-3B)
- **Link**: [Website](https://manus.bot)
- **Tags**: `general` `multi-model` `acquired-meta`

**Architecture**:
- Uses multiple AI models (Claude 3.5 Sonnet, Qwen variants)
- Multiple independently operating agents
- General-purpose task completion

**Capabilities**:
- Trip itinerary planning
- Stock analysis
- Real estate recommendations
- Code writing and deployment

**History**:
- Founded by Xiao Hong (33-year-old serial entrepreneur)
- Launched March 6, 2025
- ~Few dozen employees

---

### Rabbit Inc - Rabbit R1
- **Price**: $199 (one-time hardware purchase)
- **Link**: [Website](https://www.rabbit.tech/rabbit-r1)
- **Tags**: `hardware` `mobile` `lam` `consumer`

**Key Innovation**:
- Large Action Model (LAM) - learns by observing humans
- Standalone device (not reliant on APIs)
- Co-designed with Teenage Engineering

**Capabilities**:
- Order DoorDash
- Call Uber
- Book vacations
- Operate apps via voice

---

### Twin Labs - Twin
- **Location**: Paris, France
- **Funding**: €12M from LocalGlobe + unicorn founders
- **Link**: [Website](https://twin.so/)
- **Tags**: `enterprise` `workflow` `browser` `non-technical`

**Technology**:
- Chromium-based browser on server
- Uses OpenAI CUA model
- Schedule or trigger-based execution

**Scale**:
- 1,000,000 workflows automated
- 100,000 agents deployed
- 60,000 users

**Use Case**: Invoice retrieval (partnership with Qonto)

---

### HyperWrite - Personal Assistant
- **Platform**: Chrome Extension
- **Pricing**: Free tier, Premium (~$20/month), Ultra (~$45/month)
- **Link**: [Website](https://www.hyperwriteai.com/personal-assistant)
- **Tags**: `browser` `personal-assistant` `chrome`

**Capabilities**:
- Browser automation
- Form filling
- Web navigation
- Task execution

---

### MultiOn
- **Link**: [Website](https://www.multion.ai/)
- **Docs**: [Documentation](https://docs.multion.ai/)
- **Tags**: `browser` `automation` `api` `enterprise`

**Features**:
- Millions of concurrent AI agents
- Natural language task specification
- End-to-end web task completion

**Use Cases**:
- Booking reservations
- Ordering products
- Managing online forms
- Social media automation
- Competitor tracking

---

### Adept AI - ACT-1
- **Status**: Talent acquired by Amazon (2024)
- **Link**: [Blog](https://www.adept.ai/blog/act-1/)
- **Tags**: `enterprise` `acquired-amazon` `action-transformer`

**Technology**:
- Action Transformer (ACT-1)
- Trained on 50B+ tokens
- Natural language to software actions

**Post-Acquisition**:
- Founders joined Amazon's AGI SF Lab
- Adept continues independently

---

### H Company - Runner H
- **Link**: [Website](https://www.hcompany.ai/)
- **Tags**: `enterprise` `web` `real-world`

Advanced real-world application agent.

---

## Browser Infrastructure Services

### Browserbase
- **Link**: [Website](https://www.browserbase.com/)
- **Tags**: `infrastructure` `cloud` `api`

Cloud-native browser automation platform for AI agents.

**Features**:
- Playwright, Puppeteer, Selenium compatible
- Sessions API for browser state control
- Built-in framework: Stagehand

---

### Browserless
- **Link**: [Website](https://www.browserless.io/)
- **Tags**: `infrastructure` `cloud` `playwright`

Headless browser service for AI agents.

**Integrations**:
- Browser Use
- LangChain
- Vercel AI SDK

---

### Amazon Bedrock AgentCore Browser
- **Link**: [Docs](https://docs.aws.amazon.com/bedrock-agentcore/)
- **Tags**: `infrastructure` `enterprise` `aws`

Secure cloud-based browser for AI agents.

---

## Comparison Matrix

| Product | Platform | Target | Pricing | Status |
|---------|----------|--------|---------|--------|
| Claude Computer Use | Desktop/Web | Developers/Enterprise | $20-100/mo | GA |
| OpenAI Operator | Web | Developers | API pricing | Preview |
| Project Mariner | Chrome | Consumers | Free (Preview) | Preview |
| Nova Act | Web | Enterprise | AWS pricing | GA |
| Manus | General | Enterprise | Enterprise | Acquired |
| Rabbit R1 | Hardware | Consumers | $199 | Available |
| Twin | Web | Enterprise | Enterprise | Available |
| HyperWrite | Browser | Consumers | Free-$45/mo | Available |
| MultiOn | Web | Enterprise | API pricing | Available |
