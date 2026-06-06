---
source_url: https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
source_type: blog-post
title: "How one Anthropic seller rebuilt his team's workflows with Claude Code"
author: Anthropic (first-party practitioner case study; subject: Jared Sires, GTM Product Manager, Anthropic)
date_published: 2026-06-05
date_extracted: 2026-06-06
last_checked: 2026-06-06
status: current
confidence_overall: anecdotal
issue: "#1080"
---

# How one Anthropic seller rebuilt his team's workflows with Claude Code

> First-party Anthropic case study of a non-programmer sales account executive who built a 4,300-line Gmail integration (CLAFTS) using Claude Code — introducing system prompt iteration as a style-matching methodology, model safety refusals as a quality signal, and the individual-tool-to-org-wide-plugin adoption arc as a replicable GTM automation pattern.

## Source Context

- **Type**: blog-post (first-party Anthropic practitioner case study, published June 5, 2026 on claude.com)
- **Author credibility**: Anthropic corporate blog; subject is Jared Sires, a named internal GTM Product Manager (formerly a sales account executive) who built and deployed the described tools. High credibility for workflow claims — first-party, named practitioner with specific metrics. The author has an obvious interest in demonstrating Claude Code value; treat time savings as directional rather than controlled measurements.
- **Scope**: Covers Jared Sires' path from overwhelmed account executive to GTM PM: building CLAFTS (email drafting), developing daily brief/recap skills, and packaging tools as a Claude Cowork plugin for the Anthropic sales organization. Focuses on individual-contributor augmentation, system prompt iteration for style matching, MCP server integration, and org-wide adoption. Does NOT cover: technical implementation details (CLAUDE.md configuration, hook setup, API keys), how Claude Code was configured as a non-programmer, whether CLAFTS went through security review, or pricing/cost tradeoffs.

## Extracted Claims

### Claim 1: A non-programmer with no coding background built a 4,300-line Gmail integration using Claude Code as the primary development tool

- **Evidence**: Jared Sires' explicit self-description as non-technical, combined with the specific line count and direct attribution to Claude Code.
- **Confidence**: anecdotal (single practitioner account, self-reported; code volume is specific and credible)
- **Quote**: "Claude Code, having the terminology 'code' at the end of it, made me feel a little bit intimidated just to even start."
- **Quote**: "But after a certain time frame, I understood the power of it being able to hook up to my computer and answer things about files on it."
- **Quote**: "I never had the technical chops to be in these conversations. With Claude, I'm able to design and build things that don't just improve my own day-to-day workflows, but also those of my broader team."
- **Our assessment**: This is the primary novelty claim in the source. The corpus previously documented Travis Bryant (`blog-anthropic-bryant-cowork-sales.md` Claim 8) as a GTM professional who tried Claude Code and "never got comfortable with working with the terminal," requiring Cowork's document-centric interface to adopt. Sires demonstrates the opposite path: he overcame the same initial intimidation and built production tooling directly with Claude Code. Together, these two first-party accounts establish that the CLI/terminal barrier is real but not universal — individual tolerance for it varies, and some non-technical users can clear it with persistence. The specific code metric (4,300 lines) is useful: it gives practitioners a sense of what Claude Code can produce for a non-technical user working on a real business problem over an extended period.

### Claim 2: Hundreds of system prompt iterations are the core methodology for matching an individual's writing style in AI-generated communications

- **Evidence**: Jared Sires' explicit description of his CLAFTS development process, with a specific iteration count.
- **Confidence**: anecdotal (single practitioner; the "hundreds of iterations" claim is self-reported and non-quantified, but the direction is credible)
- **Quote**: "I've probably gone through hundreds of iterations with CLAFTS in the system prompt to generate different pieces of writing for me."
- **Our assessment**: This is the most operationally replicable claim in the source. "Hundreds of iterations" is a high but credible number for a deeply personal task like voice/style matching — human writing style has subtle dimensions (word choice, hedging frequency, sentence rhythm, register shifts across audiences) that require extensive calibration. The practical implication for practitioners: style matching via system prompt is not a one-time setup task but an ongoing iterative refinement process, likely requiring more iterations than practitioners initially expect. The initial failure mode identified by the article — Claude's writing "tended to be longer and heavier on hedging phrases" — is a specific, commonly reported issue that practitioners can anticipate and address iteratively.

### Claim 3: Web search integration allows AI-generated communications to reference current product documentation without manual synchronization

- **Evidence**: Jared Sires describes delegating the documentation-awareness problem to Claude's web search capability.
- **Confidence**: anecdotal (single practitioner; the mechanism is technically sound and the value proposition is clear)
- **Quote**: "Claude is able to use web search to understand our latest documentation from our website and reference that material when generating emails. I don't need to keep all of that in my head."
- **Our assessment**: This claim solves a practical AI-generated-communications problem: AI systems trained on static knowledge go stale as products evolve. By delegating documentation lookup to web search at draft-generation time, CLAFTS ensures emails reflect the current product state rather than training data state. The "I don't need to keep all of that in my head" framing is the practitioner-accessible version of the same pattern: reducing the cognitive load of maintaining knowledge currency by externalizing it to live retrieval. For guide chapters on communication automation: web search integration is a necessary component of any AI tool that needs to reference organizational knowledge that changes frequently.

### Claim 4: Model safety refusals during tone testing serve as a positive quality signal that voice-matching is working correctly

- **Evidence**: Jared Sires describes a deliberate edge-case test (writing increasingly angry emails to himself) that surfaced Claude's safety guardrails, which he interpreted as a validation signal.
- **Confidence**: anecdotal (single practitioner observation; the interpretive framework is creative and specific)
- **Quote**: "Claude started to mimic that, and at some point I started to have refusals because Claude didn't want to generate angry emails to customers. That was when I knew CLAFTS Tones was working."
- **Our assessment**: This is the most unexpected claim in the source and worth extracting carefully. Sires repurposes model safety behavior as a quality measurement: "the model refused to generate hostile content in my voice, therefore my voice matching is convincing enough to trigger safety evaluation." This is an indirect but clever quality test — the model has to successfully match the register before it can evaluate whether that register is safe to generate. For practitioners: a tone-matched safety refusal is evidence of successful voice calibration, not evidence of system failure. This also illustrates that deep personalization of AI communication tools surfaces safety model interactions that generic tools do not.

### Claim 5: CLAFTS saves 2–3 hours per day on email, and the overall workflow toolset saves 10–15 hours per week

- **Evidence**: Author characterization of Jared's time savings, with specific daily and weekly figures.
- **Confidence**: anecdotal (self-reported estimates from a single practitioner; no controlled baseline comparison; strong incentive to report high)
- **Quote**: (no direct quote from Jared on specific hours; article characterizes him as saving 2–3 hours per day on email)
- **Quote**: "Before CLAFTS, I felt like I was doing more administrative work than actually spending time with customers. After CLAFTS, I was actually able to do more of what I wanted to do, which is sales."
- **Our assessment**: The 10–15 hours/week savings claim is consistent with `blog-anthropic-bryant-cowork-sales.md` Claim 1 (Bryant estimates ~90 minutes/day on daily automation alone) and plausible for a role managing 600–700 accounts with 10–15 daily calls. The 2–3 hours/day on email specifically is high but credible given the described inbox volume ("It was almost impossible to manage my inbox"). Neither the before-state baseline nor the after-state are rigorously measured — treat these as directional evidence that email automation produces significant time savings for high-volume communication roles, not as a precise benchmark.

### Claim 6: Combining a daily brief skill (calendar + web research → talking points) with a daily recap skill (meeting notes → follow-up drafts) creates an agent that manages daily tasks

- **Evidence**: Jared Sires describes both skills in combination and names the agent pattern explicitly.
- **Confidence**: anecdotal (single practitioner; the mechanism is technically sound)
- **Quote**: "You couple those together and you get Claude managing your daily tasks, which essentially becomes an agent."
- **Our assessment**: The "essentially becomes an agent" framing is significant because it names the pattern explicitly: two coordinated skills that together cover the day's work cycle (preparation before meetings + follow-through after meetings) constitute a task management agent. The MCP server integration ("connect to Google Calendar and CRM data through MCP servers") makes both skills live rather than static — the brief uses real calendar data, the recap uses real meeting notes. For practitioners building communication workflows: the brief+recap skill pair is a replicable template applicable beyond sales (any role with recurring external meetings and follow-up obligations).

### Claim 7: Peer-to-peer sharing via Slack triggered adoption with equivalent results within 24 hours of completion

- **Evidence**: The article describes Jared's sharing behavior and the immediate uptake by colleagues.
- **Confidence**: anecdotal (single event; direction of adoption is credible given reported time savings)
- **Quote**: (no direct Jared quote for this event; article describes the pattern)
- **Our assessment**: The 24-hour viral adoption pattern is consistent with what other corpus sources document about tool proliferation via word-of-mouth channels in the same workspace. The mechanism is straightforward: Jared posted in Slack, teammates with the same inbox problem recognized it immediately, and time savings replicated. The parallel to `blog-anthropic-claude-code-skills-lessons.md` Claim 15 (peer curation: "point people to it in Slack or forums" before promoting to marketplace) is direct: informal Slack sharing is the natural first step in the peer distribution pattern that eventually scales to org-wide adoption.

### Claim 8: Packaging individual tools as a Claude Cowork plugin achieved approximately 80% sales organization adoption within months

- **Evidence**: Specific adoption percentage from the article, with timeline descriptor.
- **Confidence**: anecdotal (self-reported by Anthropic; no independent corroboration; percentage is specific but unaudited)
- **Quote**: (no direct Jared quote; article states approximately 80% of Anthropic's sales organization adopted the plugin within months)
- **Our assessment**: 80% adoption within months is high for any internal tool. The packaging step — wrapping individual Claude Code tools as a Cowork plugin — is the key organizational enabler: it moves from "Jared helps each teammate manually" to "any sales rep can install the plugin in minutes." The MCP integrations (Salesforce, Intercom, Gong, Google Calendar, Gmail, Google Drive, BigQuery) that are hard to configure individually become bundled infrastructure. For practitioners: the plugin packaging pattern is how individual productivity wins become team-wide adoption. The Claude Cowork plugin format provides the distribution mechanism that the Claude Code CLI cannot — a one-click installation experience suitable for non-technical users. This is the same Cowork interface accessibility dynamic that Bryant described (`blog-anthropic-bryant-cowork-sales.md` Claim 8), but here applied as a packaging and distribution strategy rather than a primary usage mode.

### Claim 9: The /customer-context skill delivers a 360-degree account view across Salesforce, Intercom, Gong, Google Calendar, Gmail, Google Drive, and BigQuery in approximately 90 seconds

- **Evidence**: Direct quote from Jared about the capability and specific tool integrations.
- **Confidence**: anecdotal (single practitioner claim; the 7-system integration and 90-second timeframe are specific and verifiable in principle)
- **Quote**: "a 360-degree account view across all those sources in about 90 seconds"
- **Our assessment**: The 7-system integration scope is the most operationally concrete claim in the source. Assembling context from Salesforce (CRM), Intercom (support), Gong (calls), Google Calendar (scheduling), Gmail (email history), Google Drive (shared docs), and BigQuery (usage data) into a single 90-second synthesis was previously an analyst-hours task requiring manual lookup across each system. The 90-second figure is consistent with parallel MCP tool calls across multiple systems. This is the same cross-system data pull pattern documented in `blog-anthropic-bryant-cowork-sales.md` Claims 1–2 (BigQuery + Salesforce briefing), but applied to a richer 7-system integration with a broader account context scope.

### Claim 10: AI tools can transform a knowledge worker's professional trajectory from executor to builder, enabling non-technical practitioners to design and deploy tools for their entire team

- **Evidence**: Jared Sires' description of his career transformation from sales account executive to GTM Product Manager.
- **Confidence**: anecdotal (single practitioner account; high narrative impact but narrow evidence base)
- **Quote**: "The most empowering thing I've ever experienced."
- **Quote**: "I never had the technical chops to be in these conversations. With Claude, I'm able to design and build things that don't just improve my own day-to-day workflows, but also those of my broader team."
- **Our assessment**: The career transformation claim is the most speculative and most impactful claim in the source. Sires moved from AE (executor role) to GTM PM (builder/architect role) as a direct result of building Claude Code tools. Whether this trajectory is broadly replicable or context-specific to Anthropic's culture and Sires' particular initiative is unknown. The claim is nonetheless high-value for the guide: it establishes that AI tool building can be a career-differentiating activity for non-technical knowledge workers, not just for engineers. The "design and build things for my broader team" framing is the outcome that transforms individual augmentation into organizational contribution.

## Concrete Artifacts

### CLAFTS Technical Profile (from article)

```
CLAFTS (Claude Drafts) — Gmail Email Drafting Integration
Subject: Jared Sires, GTM PM, Anthropic (formerly AE)
Published: June 5, 2026

IMPLEMENTATION:
  Size:          ~4,300 lines of code, "almost all of it written by Claude Code"
  Language/platform: Gmail integration (exact stack not described)
  API:           Claude API

CORE FUNCTION:
  Input:   Incoming customer emails
  Context: Shared Google Drive folders + third-party tools + Anthropic
           public documentation (via web search)
  Output:  Drafted reply in Jared's voice for review

STYLE MATCHING METHODOLOGY:
  Approach:      Iterative system prompt refinement
  Iterations:    "hundreds of iterations"
  Initial issue: Claude's writing "tended to be longer and heavier
                 on hedging phrases"
  Resolution:    Extended iteration to calibrate length, hedging,
                 and register

CLAFTS TONES FEATURE:
  Purpose:       Audience-specific voice matching
  Mechanism:     Pattern matching to mirror voice across
                 different relationship types
  Relationship types: customers, peers, family threads
  Quality test:  Escalating-tone test to self — feature "worked"
                 when model safety refusals appeared (model declined
                 to generate hostile customer emails in the matched voice)

PERFORMANCE:
  Email time savings: 2–3 hours/day
  Total weekly savings (all tools): 10–15 hours/week
```

### Daily Workflow Skills Stack (from article)

```
Jared Sires' Daily Workflow Skills — Claude Code + MCP
Published: June 5, 2026

DAILY BRIEF SKILL:
  Trigger: Pre-call / start of day
  Sources: Google Calendar (via MCP), web search (on meeting contacts)
  Output:  Talking points for upcoming calls
  Pattern: Context assembly → synthesis → briefing

DAILY RECAP SKILL:
  Trigger: Post-meeting
  Sources: Google Docs (meeting notes), call notes
  Output:  Drafted follow-up emails
  Pattern: Note ingestion → draft generation

COMBINED PATTERN (Jared's framing):
  "You couple those together and you get Claude managing your daily
   tasks, which essentially becomes an agent."
  Infrastructure: "connect to Google Calendar and CRM data through
                  MCP servers"
```

### Cowork Plugin Architecture (from article)

```
Anthropic Sales Claude Cowork Plugin
Published: June 5, 2026; adoption described as within months of launch

INTEGRATED SYSTEMS (7 total):
  Salesforce     — CRM (accounts, pipeline, contacts)
  Intercom       — Customer support history
  Gong           — Call recordings and transcripts
  Google Calendar — Scheduling and meeting history
  Gmail          — Email history
  Google Drive   — Shared documents and assets
  BigQuery       — Product usage data and analytics

CORE SKILLS:
  /customer-context
    Output: 360-degree account view across all above sources
    Time:   ~90 seconds
    Use:    Pre-call research and account understanding

  /pipeline-management
    Output: At-risk deal identification, forecasting guidance,
            progression recommendations
    Use:    Weekly pipeline management and forecasting

ADOPTION:
  Distribution: Claude Cowork plugin (install in minutes)
  Scale:        ~80% of Anthropic's sales organization within months
```

### Individual-to-Org Adoption Arc (from article)

```
Jared Sires' Tool Adoption Pattern — June 5, 2026

STAGE 1: Individual pain point identification
  Problem:  "It was almost impossible to manage my inbox" —
            600-700 accounts, 10-15 daily calls, answering emails
            until 9-10 PM
  Action:   Built CLAFTS with Claude Code (non-programmer)
  Result:   2–3 hours/day saved on email

STAGE 2: Peer discovery via Slack
  Action:   Shared CLAFTS in Slack the morning after completing it
  Result:   Other sales team members adopted within 24 hours,
            reporting similar time savings

STAGE 3: Career transition
  Recognition: Tool adoption → Jared transitions from AE to GTM PM
  New scope:   Building tools for the full sales organization

STAGE 4: Org-wide packaging
  Tools built: Daily brief skill, daily recap skill,
               /customer-context skill, /pipeline-management skill
  Distribution: Packaged as Claude Cowork plugin
  Result:       ~80% of sales org adoption within months
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-bryant-cowork-sales.md` Claim 10 — Bryant's "Before Claude Cowork, data assembly, report formatting, and the rebaseline when a number changes used to fill my week. Now, I have the hours back to dedicate to the strategic and customer-relationship work that pushes the needle." is the same time-reallocation dynamic that Sires describes: "Before CLAFTS, I felt like I was doing more administrative work than actually spending time with customers. After CLAFTS, I was actually able to do more of what I wanted to do, which is sales." Two independent first-party Anthropic GTM practitioners arrive at the same framing about reclaiming time for relationship work.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 5 — Fung's automation reflex ("Is there a way to automate it?") is exactly the pattern Sires embodies operationally: he identified one painful recurring task (email drafting), automated it, then systematically extended the approach to adjacent tasks (daily brief, daily recap, pipeline management). Sires' path from CLAFTS → daily skills → Cowork plugin is a step-by-step instantiation of the "always ask: can this be automated?" behavioral norm.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 15 — The peer-curation distribution pattern: "If someone has a skill that they want people to try out, they can upload it to a sandbox folder in GitHub and point people to it in Slack or other forums." Sires' Slack sharing of CLAFTS is the identical pattern applied before any formal plugin infrastructure existed: informal word-of-mouth as the initial distribution mechanism, leading to adoption that justified packaging as a formal plugin.

- **Contradicts**:
  - The Sires source presents a partial tension with `blog-anthropic-bryant-cowork-sales.md` Claim 8: Bryant explicitly states he "tried Claude Code, but never got comfortable with working with the terminal" and needed Cowork's document-centric interface to adopt. Sires is also a non-technical GTM professional, yet did adopt Claude Code directly (Claim 1 here). The tension is not a factual contradiction — they are different individuals with different tolerance for CLI tools — but the two accounts together provide a more nuanced picture than either alone: the terminal/CLI interface is a real adoption barrier for non-technical users, but some non-technical users can clear it with persistence. This is a conditioning variable (individual tolerance for CLI friction), not a genuine contradiction. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-bryant-cowork-sales.md` — Extends the corpus of first-party Anthropic GTM automation case studies with a Claude Code (rather than Cowork) primary usage path. Bryant uses Cowork throughout; Sires builds with Claude Code and later packages in Cowork. Together they document the full adoption spectrum: CLI-native builder (Sires) and GUI-native user (Bryant) are both valid paths to the same outcome (sales workflow automation), and they can interoperate (Sires packages Claude Code tools into a Cowork plugin that Bryant-type users can install).
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 2 (nine-category skills taxonomy) — extends the Business Process and Team Automation category with a concrete real-world implementation from a non-engineering role. Sires' daily brief, daily recap, and CLAFTS map directly to the "standup-post, create-ticket, weekly-recap" examples in the taxonomy, but for a GTM/sales context. The voice-matching dimension (CLAFTS Tones) adds a category-specific sub-pattern not represented in the engineering examples.
  - `blog-anthropic-claude-code-routines.md` Claim 3 and Claim 9 — Sires' daily brief and daily recap skills, invoked via Cowork scheduling, are concrete practitioner examples of the scheduled routine pattern for non-engineering roles. The routines announcement described backlog management and documentation drift as primary patterns; Sires' tools demonstrate the same scheduling model applied to communication and context assembly tasks.

- **Novel**:
  - **System prompt iteration as a named methodology for personal style matching**: No prior corpus source describes "hundreds of iterations" of system prompt development for voice/tone calibration as a specific, expected development timeline for personalization tasks. The corpus covers system prompts extensively but not the iteration depth required for individual-specific style matching.
  - **Model safety refusals as a quality signal for tone calibration** (Claim 4): The interpretation of a model safety refusal as evidence that voice-matching succeeded (rather than as an error to be worked around) is entirely novel to the corpus. No prior source documents this inverted reading of safety behavior as a calibration validator.
  - **Claude Code adoption path for non-technical GTM roles** (Claim 1): While the corpus includes non-technical Cowork usage (`blog-anthropic-bryant-cowork-sales.md`) and engineering-focused Claude Code usage throughout, this is the first documented case of a non-programmer GTM professional building a production system with Claude Code directly.
  - **Individual-to-org-wide adoption arc as a four-stage replicable pattern** (Concrete Artifacts → Individual-to-Org Adoption Arc): The specific sequence — personal pain point → iterative build → peer Slack sharing → viral adoption → role transition → packaged deployment → org-wide rollout — is a new reusable template for how individual AI tool building becomes organizational capability. No prior corpus source names or operationalizes this arc explicitly.
  - **/customer-context as a 7-system 90-second synthesis pattern** (Claim 9): The specific combination of Salesforce + Intercom + Gong + Google Calendar + Gmail + Google Drive + BigQuery into a 90-second account view is a concrete integration scope benchmark not documented elsewhere in the corpus.

## Guide Impact

- **Chapter on Individual-Contributor Augmentation (Ch02)**: Add the individual-to-org adoption arc (Concrete Artifacts → Individual-to-Org Adoption Arc) as a reusable four-stage template. The pattern — identify one painful recurring task, build with Claude Code, share in Slack, package for team — is replicable across non-engineering roles and should be presented as the standard path from individual automation to team capability. Pair with `blog-anthropic-ai-native-engineering-org.md` Claim 5 (automation reflex) as the behavioral norm that initiates the arc.

- **Chapter on System Prompt Engineering / Style Matching (Ch03)**: Add "hundreds of iterations for voice-matched communications" as an expected benchmark for personal style calibration tasks. Frame as: style matching is qualitatively different from task performance prompting — it requires calibrating subtle dimensions of voice that a user may not be able to articulate in advance. Practitioners attempting email drafting tools should expect extended iterative development cycles, with the initial Claude tendency toward "longer and heavier on hedging phrases" as a common first-pass failure mode.

- **Chapter on Verification and Quality (Ch03)**: Add the model safety refusal as quality signal pattern (Claim 4). Frame as: for tone-matching tools, successfully triggering a model safety refusal through an edge-case test is evidence that the voice calibration has reached sufficient fidelity for the model to evaluate safety in context. This is a non-obvious positive signal that practitioners should recognize and not treat as a bug.

- **Chapter on Non-Engineering Roles and AI Adoption (Ch05)**: Add the Sires/Bryant contrast as evidence for interface stratification in non-technical adoption. Some non-technical users can clear the CLI barrier with persistence (Sires); others cannot and need a document-centric wrapper (Bryant). Guide advice: for teams deploying AI tools to non-technical roles, offer both paths — a Claude Code path for motivated builders and a Cowork/plugin path for users who need GUI interfaces. The Cowork plugin packaging model (Claim 8) bridges the two: Sires builds with Code; Bryant-type users install the resulting plugin in Cowork.

- **Chapter on Context Assembly / MCP Integration (Ch04)**: Add /customer-context as a concrete 7-system integration benchmark. The pattern — parallel MCP tool calls across Salesforce, Intercom, Gong, Google Calendar, Gmail, Google Drive, BigQuery → synthesized 90-second account briefing — is a reusable architecture for any role requiring multi-system context assembly before customer interactions.

## Extraction Notes

- The source URL returns marketing content from Anthropic's blog. WebFetch declined to reproduce the full article verbatim. All quotes in this note were extracted through multiple targeted WebFetch prompts requesting specific quotes, technical details, and section-by-section content. All quotes attributed to Jared Sires were presented by the WebFetch model with explicit quotation marks and direct attribution to Sires in the response.
- The time savings figures (2–3 hours/day email, 10–15 hours/week total) were presented in one WebFetch response as "CLAFTS was saving him two to three hours a day (estimated by the author, not a direct quote)." No verbatim Jared quote was extractable for the specific hourly figures; the Claim 5 section notes this absence.
- The 80% adoption figure and 24-hour adoption timeline were presented in the WebFetch responses but no verbatim quote from Jared was recoverable for these claims. They are treated as article-stated facts rather than direct Jared quotations.
- Three separate Prospector triage comments provide extraction guidance; all three identify the same core claims (style matching, CLAFTS Tones, 10–15 hours, 80% adoption, MCP integration). This consensus increases confidence that the key claims were captured.
- No contradiction with existing corpus notes was found that rises to a filing threshold (see Contradicts section for the Sires/Bryant tension, which is a conditioning variable, not a contradiction). No contradiction issue filed.
- Confidence is set to `anecdotal`: single named practitioner account from a credible first-party Anthropic source, with specific metrics that are self-reported and not independently validated. The source is high-quality as anecdotal evidence goes — named, specific, first-party — but remains a single case study without controlled measurement.
