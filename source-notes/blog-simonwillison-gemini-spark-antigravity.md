---
source_url: https://simonwillison.net/2026/May/20/google-io/
source_type: blog-post
title: "Google I/O, Gemini Spark, Antigravity"
author: Simon Willison
date_published: 2026-05-20
date_extracted: 2026-05-29
last_checked: 2026-05-29
status: current
confidence_overall: emerging
issue: "#985"
---

# Google I/O, Gemini Spark, Antigravity

> Simon Willison's May 2026 analysis of two Google I/O announcements documents a commercial agent security isolation pattern — ephemeral VM per task, Agent Gateway, DLP enforcement, credential opacity — and a vendor lock-in transition from open-source (Apache 2.0) to closed-source CLI tooling, with Willison explicitly flagging Gemini Spark as a top prompt injection risk candidate.

## Source Context

- **Type**: blog-post (Willison link-blog / notes format; ~600 words; published May 20, 2026, the day after Google I/O. Contains one large verbatim blockquote from Google Cloud's enterprise documentation. Willison explicitly states he only writes about things he can try himself — this post is commentary on vendor announcements, not hands-on evaluation, because neither Gemini Spark nor Antigravity was available for testing at time of writing.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI, one of the most widely-cited independent practitioners on LLM tooling. His stated policy of only writing about things he can try himself gives his omissions equal signal to his coverage. He is unaffiliated with Google. Security observations are practitioner intuition, not formal threat analysis — but he has a track record of identifying risks before they materialize.
- **Scope**: Covers (1) Gemini Spark as a product category with its security isolation architecture sourced from Google Cloud's enterprise blog; (2) Antigravity as the underlying agent runtime and its component stack; (3) the transition from open-source Gemini CLI to closed-source Antigravity CLI. Does NOT cover: hands-on evaluation of either product, model capability comparisons, Gemini 3.5 Flash details (covered in a separate simonwillison.net post, see blog-simonwillison-gemini35-flash-pricing), or broader Google I/O announcements.

## Extracted Claims

### Claim 1: Gemini Spark is a personal AI agent that connects natively with Gmail, Calendar, Drive, Docs, Sheets, Slides, YouTube, and Maps

- **Evidence**: Willison citing Google's published product description directly.
- **Confidence**: settled (factual product announcement; Google's own published description)
- **Quote**: "described as 'your personal AI agent' which can 'connect natively with your favorite Google apps like Gmail, Calendar, Drive, Docs, Sheets, Slides, YouTube, and Google Maps'"
- **Our assessment**: The native Workspace integration list (8 apps) establishes Gemini Spark's threat surface. An agent with read/write access to email, calendar, documents, and spreadsheets processes extremely sensitive personal and enterprise data. Willison frames this as Google's competitor to OpenAI's personal agent offerings. This is the commercial reference architecture for what a production-grade personal AI agent harness integrates with at launch.

### Claim 2: Gemini Spark's own FAQ states it runs on Gemini 3.5 Flash and Antigravity

- **Evidence**: Direct verbatim reproduction of the Gemini Spark FAQ by Willison, who found the detail "confusing."
- **Confidence**: settled (first-party Google FAQ content reproduced by Willison)
- **Quote**: "Gemini Spark runs on Gemini 3.5 Flash and Antigravity."
- **Our assessment**: The FAQ naming "Antigravity" alongside the model as a co-runtime is the clearest evidence that Antigravity is a production-scale agent execution framework, not just a developer SDK. The Go binary that ships in the Antigravity developer SDK appears to be the same runtime powering a major consumer-facing agentic product. Willison notes he is "not sure why that's worth mentioning in the FAQ" — but for practitioners the implication is significant: the Antigravity SDK is not a toy wrapper.

### Claim 3: Gemini Spark executes every task in a fresh, strictly isolated, ephemeral VM, preventing data overlap between sessions

- **Evidence**: Google Cloud enterprise blog blockquote, as directly quoted by Willison. This is from "Everything Google Cloud customers need to know coming out of Google I/O," an enterprise-facing post from Google Cloud.
- **Confidence**: emerging (first-party Google marketing claim; no independent verification; Willison explicitly expresses skepticism about whether the implementation is bulletproof)
- **Quote**: "Every task executes in a fresh, strictly isolated, ephemeral VM to help ensure data never overlaps between sessions."
- **Our assessment**: Ephemeral VMs (fresh per task, no persistent state) are the strongest documented form of commercial agent session isolation: state cannot accumulate between sessions by architectural design, not just policy. This aligns with the Advanced tier isolation pattern in `blog-anthropic-zero-trust-ai-agents.md` (microVM architectures). As of May 2026, this is the first corpus example of a major commercial consumer agent product publicly claiming VM-level per-task isolation — establishing it as a production standard, not just a framework recommendation.

### Claim 4: All Gemini Spark traffic routes through a secure Agent Gateway that enforces DLP policies

- **Evidence**: Google Cloud enterprise blog blockquote reproduced by Willison.
- **Confidence**: emerging (first-party Google marketing claim; no independent verification of implementation)
- **Quote**: "all traffic routes through our secure Agent Gateway that enforces Data Loss Prevention (DLP) policies"
- **Our assessment**: The Agent Gateway as a DLP enforcement point is architecturally significant: a dedicated component interposed between the agent runtime and all external services, enforcing policy controls that the agent itself cannot bypass. This is the commercial implementation of the network-enforcement-layer pattern from `blog-anthropic-zero-trust-ai-agents.md` Claim 4 (controls that remove capabilities rather than throttle them). DLP at the gateway (rather than at the agent prompt level) means a prompt-injected agent cannot exfiltrate data that the gateway blocks — the enforcement is structural, not instructional.

### Claim 5: Gemini Spark user credentials are fully encrypted and never exposed directly to the agent

- **Evidence**: Google Cloud enterprise blog blockquote reproduced by Willison.
- **Confidence**: emerging (first-party Google marketing claim; no independent verification of the encryption mechanism or the "never exposed" guarantee)
- **Quote**: "user credentials remain fully encrypted and are never exposed directly to the agent"
- **Our assessment**: "Never exposed directly to the agent" is the critical isolation claim: if an attacker achieves prompt injection and attempts credential exfiltration, the agent never had the credentials to exfiltrate — they are opaque at the agent execution layer. This extends the Zero Trust credential protection pattern (`blog-anthropic-zero-trust-ai-agents.md` Claim 12, which specifies credentials should never appear in code or config files) further: not just hidden from code, but structurally absent from the agent's context. Verification would require independent security research, which is not yet available.

### Claim 6: The Antigravity ecosystem consists of a desktop app, a Go-written CLI agent tool, an open-source Python SDK wrapping a closed-source Go binary, and a VS Code fork IDE

- **Evidence**: Willison's direct reading of the antigravity.google product page.
- **Confidence**: settled (first-person observation of the product page at time of writing; product website is the authoritative source for component listing)
- **Quote**: "The antigravity.google website currently lists Antigravity as a desktop app, a CLI agent tool (written in Go), the Antigravity SDK (an open source Python wrapper around a bundled closed source Go binary), and the original Antigravity IDE (a VS Code fork)."
- **Our assessment**: The SDK architecture — open-source Python wrapper around a closed-source Go binary — is a notable pattern: it provides developer-visible tooling (inspectable Python wrapper, GitHub-hosted) while protecting the proprietary runtime (compiled Go binary, closed source) from inspection or modification. Practitioners building on the Antigravity SDK have a transparent interface but an opaque execution core. The IDE being a VS Code fork is consistent with the broader industry pattern (Cursor, Windsurf, GitHub Copilot) of forking VS Code as the developer agent IDE base.

### Claim 7: Google is forcing a transition from the open-source Gemini CLI (Apache 2.0 TypeScript) to a closed-source Antigravity CLI, with the old tool stopped on June 18th

- **Evidence**: Willison cites the Google developer blog announcement "Transitioning Gemini CLI to Antigravity CLI."
- **Confidence**: settled (official Google developer blog announcement directly cited; hard deadline is explicit)
- **Quote**: "Google announce that the open source Gemini CLI tool (Apache 2.0 licensed TypeScript) will stop working with their AI subscription plans on June 18th, replaced by the new closed source Antigravity CLI."
- **Our assessment**: This is a direct open-source-to-closed-source forced migration. The Gemini CLI had Apache 2.0 community transparency (inspectable TypeScript on GitHub); the Antigravity CLI has none. The June 18th hard deadline leaves no room for continued open-source use with AI subscription plans. For practitioners who have integrated the open-source Gemini CLI into workflows, this is a case study in the vendor lock-in risk of CLI agent tooling: a tool can be Apache 2.0 today and deprecated next month.

### Claim 8: Willison identifies Gemini Spark as a top candidate for an "agent security challenger disaster" due to the sensitivity of data it will process

- **Evidence**: Willison's first-person editorial assessment, referencing his earlier January 2026 LLM prediction.
- **Confidence**: anecdotal (practitioner editorial; no empirical security analysis; Willison is flagging a risk hypothesis, not documenting a known failure)
- **Quote**: "Given how many people are going to be piping _very_ sensitive data through Gemini Spark in the near future I hope they've made this bullet-proof, or this could be a top candidate for the agent security challenger disaster that we still haven't seen."
- **Our assessment**: The "challenger disaster" reference is to Willison's January 2026 prediction about a high-profile agent security failure. His concern here is structurally specific: Gemini Spark processes Gmail, Calendar, Drive, and Docs — a uniquely broad and sensitive data surface. A successful prompt injection (via a malicious email, calendar invite, or shared document) could cascade across all integrated apps simultaneously. Willison's concern should be read as an identification of the attack surface, not a claim about existing failures. The question his framing raises for guide purposes: what would practitioners need to see to trust the ephemeral VM and Agent Gateway claims?

### Claim 9: Willison has a policy of only writing about things he can try himself, which constrained his Google I/O coverage

- **Evidence**: Willison's direct statement of his editorial policy.
- **Confidence**: settled (first-person disclosure of his writing standards; consistent with his documented approach across other posts)
- **Quote**: "It's hard to find much to write about Google I/O this year because I have a policy of not writing about anything that I can't try out myself, and a lot of the big announcements are 'coming soon'."
- **Our assessment**: This context shapes the entire source. Willison's coverage of Gemini Spark and Antigravity is based on publicly available vendor documentation, not hands-on evaluation. His security observations are practitioner inference from vendor claims, not penetration test results. The "coming soon" policy means his analysis here is necessarily secondary: he is synthesizing Google's own published information rather than providing independent verification.

## Concrete Artifacts

### Gemini Spark Security Architecture (from Google Cloud enterprise blog, via Willison)

```
Gemini Spark Security Architecture (Google Cloud, May 2026)
Source: Google Cloud blog "Everything Google Cloud customers need to know
coming out of Google I/O", reproduced in simonwillison.net/2026/May/20/google-io/

Session isolation:    "Every task executes in a fresh, strictly isolated,
                       ephemeral VM to help ensure data never overlaps
                       between sessions."

Traffic routing:      "all traffic routes through our secure Agent Gateway
                       that enforces Data Loss Prevention (DLP) policies"

Credential handling:  "user credentials remain fully encrypted and are
                       never exposed directly to the agent"

Runtime description:  "a fully managed, secure runtime on Google Cloud,
                       meaning you get enterprise-grade security without
                       ever having to manage the underlying infrastructure"
```

### Antigravity Stack Components (from antigravity.google, via Willison)

```
Antigravity Ecosystem (Google, May 2026)
Source: antigravity.google product page,
        via simonwillison.net/2026/May/20/google-io/

Component            Description
-----------          -----------
Desktop app          Standalone application
CLI agent tool       Written in Go (closed source)
                     GitHub: google-antigravity/antigravity-cli
Antigravity SDK      Open-source Python wrapper around bundled
                     closed-source Go binary
                     GitHub: google-antigravity/antigravity-sdk-python
Antigravity IDE      VS Code fork

Production use:      Gemini Spark FAQ: "Gemini Spark runs on Gemini 3.5
                     Flash and Antigravity" — Go binary powers both
                     developer tooling and the consumer product runtime
```

### Gemini CLI to Antigravity CLI Transition

```
Gemini CLI → Antigravity CLI Forced Migration (Google, May 2026)
Source: Google developer blog "Transitioning Gemini CLI to Antigravity CLI",
        cited in simonwillison.net/2026/May/20/google-io/

Old tool:   Gemini CLI
            License: open source, Apache 2.0
            Language: TypeScript
            GitHub: google-gemini/gemini-cli

New tool:   Antigravity CLI
            License: closed source
            GitHub: google-antigravity/antigravity-cli

Hard deadline: June 18, 2026
               Gemini CLI stops working with AI subscription plans
               No continued open-source alternative for subscription users
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-muse-spark.md` Claim 1: Meta's Muse Spark is also a hosted personal AI agent (not open weights). This source documents Google Gemini Spark in the same category. Two major vendors (Meta, Google) launched hosted personal AI agents with native platform integrations in the same period, corroborating cross-vendor convergence on personal AI agent as a product category.
  - `blog-simonwillison-muse-spark.md` Claim 5: meta.ai's Python execution environment is sandboxed with persistent `/mnt/data/` storage — a per-session container isolation model. Gemini Spark's ephemeral VMs (fresh per task) represent a stricter isolation model: no cross-session persistence at all, compared to meta.ai's session-persistent sandbox. Together these two sources document the range of commercial isolation designs: persistent container (Meta) vs. ephemeral VM (Google).
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 4: That note documents Gemini 3.5 Flash deployed across multiple Google products "including Google Antigravity." This source confirms Gemini Spark explicitly runs on Gemini 3.5 Flash (per the Spark FAQ), completing the picture of Gemini 3.5 Flash's production deployment at scale.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 3: The "impossible vs. tedious" test is the design criterion for security controls. Gemini Spark's ephemeral VM isolation passes this test: session state structurally cannot persist between tasks (impossible), not just hard to access (tedious). The Agent Gateway DLP enforcement similarly removes capability rather than throttling it.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5: "Least agency" restricts what each agent tool can do, how often, and where. The Gemini Spark Agent Gateway with DLP enforcement is a commercial implementation of least agency at the network level — a dedicated component enforcing constraints the agent itself cannot bypass.

- **Contradicts**: None identified. The security architecture claims here are vendor marketing that corroborates Zero Trust patterns rather than contradicting them. No existing source note makes a claim materially opposed by this source.

- **Extends**:
  - `blog-simonwillison-muse-spark.md`: That source documented Meta's personal AI agent architecture. This source adds Google's equivalent. Together they provide a two-vendor dataset for commercial personal AI agent security isolation: Meta uses session-persistent containers (`/mnt/data/`), Google uses ephemeral VMs per task. The Google approach is more aggressive in session isolation.
  - `blog-anthropic-zero-trust-ai-agents.md`: That note provides Anthropic's prescriptive Zero Trust framework (three tiers, eight phases, threat taxonomy). This source provides a commercial vendor implementation example: Gemini Spark's isolation architecture matches the Advanced tier's microVM pattern, and the Agent Gateway matches the DLP enforcement pattern. The Zero Trust note prescribes; this source documents a commercial product that ships those prescriptions.
  - `blog-simonwillison-gemini35-flash-pricing.md`: That source covered Gemini 3.5 Flash as a model (pricing, deployment targets). This source shows Gemini 3.5 Flash in production as the model layer inside Gemini Spark, with Antigravity as the runtime layer — a dimension not covered in the pricing note.

- **Novel**:
  - **Ephemeral VM per agent task as a documented commercial production pattern**: No prior source in the corpus documents "fresh, strictly isolated, ephemeral VM per task" as an explicit commercial security architecture at consumer scale. The Zero Trust note prescribes microVMs for the Advanced tier; this source documents Google claiming to ship it in a major consumer product. First corpus evidence this pattern has moved from framework recommendation to commercial production practice.
  - **Agent Gateway as a named DLP enforcement layer**: The specific architecture — a dedicated "Agent Gateway" that intercepts all agent traffic and enforces DLP policies — is new to the corpus. Prior notes discuss DLP conceptually; this is the first documentation of a named dedicated gateway component in a commercial agent product.
  - **Forced open-source-to-closed-source CLI tool transition with hard deadline**: The Gemini CLI → Antigravity CLI migration is the first documented instance in the corpus of a major AI vendor replacing an open-source (Apache 2.0) developer CLI tool with a closed-source replacement under a hard cutoff. This establishes vendor lock-in via tooling transitions as a concrete risk pattern.
  - **"Challenger disaster" framing for agent security**: Willison's specific risk hypothesis — that a high-profile agent security failure in a data-rich personal AI agent has not yet occurred but is overdue, with Gemini Spark as a top candidate — is the most pointed forward-looking security risk assessment in the corpus. No prior source identifies a specific commercial product as a concrete high-risk prompt injection target with this framing.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Execution isolation**: Gemini Spark's ephemeral VM per task is the first corpus evidence of commercial VM-level agent isolation deployed at consumer scale. Update any harness section on execution isolation to cite this: "As of May 2026, Google's Gemini Spark explicitly uses 'fresh, strictly isolated, ephemeral VM[s]' per task — establishing VM-level isolation as a production-grade commercial standard for high-sensitivity agent tasks, not just an architectural recommendation."

- **Chapter 02 (Harness Engineering) / Policy enforcement architecture**: The Agent Gateway pattern (dedicated gateway enforcing DLP before data exits the agent runtime) is a new architectural primitive for outbound data controls. Add to harness engineering guidance: "DLP enforcement belongs at a gateway layer between the agent runtime and external services, not in the agent prompt. A prompt-injected agent cannot bypass a gateway that structurally blocks the data path."

- **Chapter 04 or Ch05 (Agent Security / Prompt Injection)**: Willison's Claim 8 is the strongest practitioner-articulated risk statement about personal AI agents and prompt injection in the corpus. Add to any prompt injection section: "Production personal AI agents with native access to email, calendar, and documents represent a uniquely concentrated attack surface. A single prompt injection — via a malicious email, calendar invite, or shared document — can cascade across all integrated apps simultaneously."

- **Chapter 05 (Vendor Selection / Lock-in Risks)**: The Gemini CLI → Antigravity CLI forced migration (Claim 7) is a concrete case study for vendor lock-in risk in CLI agent tooling. Add: "When integrating CLI agent tools, verify license durability: Apache 2.0 today is not a guarantee of open-source access tomorrow. Google's June 2026 transition from the open-source Gemini CLI to the closed-source Antigravity CLI demonstrates that 'currently open source' is an insufficient lock-in risk assessment."

- **Chapter 06 (Production Deployment / Security reference architectures)**: Gemini Spark's full security stack (ephemeral VMs + Agent Gateway + DLP + credential opacity) is the most complete documented commercial implementation of production agent security architecture in the corpus. Reference alongside the Anthropic Zero Trust framework (blog-anthropic-zero-trust-ai-agents.md) as a cross-vendor production benchmark.

## Extraction Notes

- **Short source (~600 words) with concentrated high-signal content**: The article's value is in four distinct areas: (1) the Google Cloud enterprise blockquote on security architecture; (2) the Antigravity component inventory; (3) the CLI transition announcement; (4) Willison's editorial risk assessment. All four are fully extracted above.
- **Security architecture quotes are from Google Cloud's enterprise blog, not from Gemini Spark directly**: The blockquote about ephemeral VMs, Agent Gateway, and credential handling comes from Google Cloud's enterprise-facing I/O recap post, not from the Spark product page or Antigravity documentation. These are Google marketing claims aimed at enterprise procurement decision-makers. They should be treated as vendor assertions pending independent verification.
- **Neither Gemini Spark nor Antigravity was available to try at time of writing**: Willison explicitly states this; his coverage is based on published documentation only. Claims about Spark security properties and Antigravity capabilities are vendor-announced, not practitioner-verified.
- **"OpenClaw competitor" in source text**: The WebFetch of the source returned "Google's upcoming OpenClaw competitor" as Willison's competitive framing. "OpenClaw" is not a product name verifiable from this extraction (training data cutoff August 2025). The Assayer should verify the exact wording against the live source URL. The substantive claims about Gemini Spark do not depend on this label.
- **No sub-pages followed**: The post links to the Gemini Spark product page, Google Cloud enterprise blog, antigravity.google, Google developer blog (CLI transition), and a prior simonwillison.net post. All substantive content was captured through the blockquotes and component lists Willison reproduced directly in the article.
- **Confidence calibration**: Claims from the Google Cloud enterprise blockquote are rated "emerging" — first-party vendor claims without independent security verification. The CLI transition announcement is "settled" — official Google developer blog with a hard deadline. Willison's editorial risk assessment is "anecdotal." The overall note confidence is "emerging" because the most novel and actionable claims (isolation architecture) are vendor-stated, not independently validated.
