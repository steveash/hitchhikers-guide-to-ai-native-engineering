---
source_url: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/
source_type: blog-post
title: "Understanding ChatGPT Work"
author: Simon Willison
date_published: 2026-08-30
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: emerging
issue: "#3182"
---

# Understanding ChatGPT Work

> An outsider's reverse-engineered feature audit of ChatGPT Work (Cloud),
> built by hands-on experimentation rather than insider access: internet-
> connected code execution, a headless Chrome browser tool, a persistent
> shared `/workspace` filesystem, sub-agents, and — via a self-referential
> prompt that made Work document its own tool/skill inventory (223 tools,
> 44 skills) — the first public enumeration of what's actually installed
> under the hood.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, single long-form article,
  published 2026-08-30).
- **Author credibility**: Simon Willison is a trusted, high-signal source
  already extensively represented in this corpus (creator of Datasette,
  the `llm` CLI, and the "lethal trifecta" prompt-injection framework this
  article itself cites). This is an external practitioner's own hands-on
  investigation — not an OpenAI interview or insider account — built by
  extensive personal experimentation with the product over the ~7 weeks
  since ChatGPT Work's July 9, 2026 launch. He explicitly frames the piece
  as reverse-engineering necessitated by OpenAI's own documentation gaps
  (see Claim 8 below), which is itself one of the article's claims.
- **Scope**: Covers ChatGPT Work (Cloud) specifically — the web/mobile
  version accessed via chatgpt.com — explicitly bracketing out "Work
  Local" (the desktop-app version, described as re-skinned Codex) after
  a brief mention. Covers: the Work vs. Chat feature distinction, model/
  reasoning-level options and billing, code execution with internet
  access, the browser tool, the persistent shared filesystem, ChatGPT
  Sites, sub-agents, scheduled prompt automations, a security assessment
  via the "lethal trifecta" framework, a critique of OpenAI's
  documentation practices, and a self-directed tool/skill inventory
  extraction. Does NOT cover: Work Local/desktop in any depth, pricing
  details beyond the $20/month subscription gate, enterprise/admin
  features, or any quantified task-success/reliability data — every
  capability claim is a first-hand qualitative observation from one
  power user's testing, not a systematic audit or benchmark.

## Extracted Claims

### Claim 1: ChatGPT Work is actually two separate products — "Work Cloud" (accessed via chatgpt.com or the mobile apps) and "Work Local" (accessed through the ChatGPT desktop app, previously branded Codex, which runs directly on the user's own machine) — and Work Local "feels more like regular Codex re-skinned to be less intimidating to non-software-developers"
- **Evidence**: The author's own first-hand product-structure observation, stated as the article's opening organizing claim.
- **Confidence**: emerging (a specific, named product-structure claim from extensive hands-on use, though based on outsider observation rather than an OpenAI architecture statement)
- **Quote**: "If you install the ChatGPT desktop app—the app that used to be called Codex—you gain access to a thing called ChatGPT Work that can access files and run programs directly on your computer. Let's call that one Work Local. This one feels more like regular Codex re-skinned to be less intimidating to non-software-developers."
- **Our assessment**: This corroborates `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 8 (Cloud Mode vs. Local Mode, with Local Mode desktop-only and not syncing to web/mobile) and `blog-anthropic`-adjacent framing in `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 1 (Codex and ChatGPT Work share an identical underlying harness, differentiated only at the UX layer) — Willison's outsider "re-skinned Codex" characterization is an independent, externally-observed confirmation of the same harness-sharing architecture Nathan (OpenAI, the product's own lead) describes from the inside. A third and more technical source for the same shared-harness claim is `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10, which reports (from OpenAI's own engineering post) that the agentic harness for *both* Codex and ChatGPT Work is a single Rust orchestration layer — so the "re-skinned Codex" characterization Willison arrives at from outside matches what OpenAI describes as literally one shared harness underneath. The rest of this article is explicitly scoped to Work Cloud only, which this note follows.

### Claim 2: ChatGPT Work (in both Cloud and Local forms) is gated to paid subscribers at $20/month and up — Free users and $8/month Go users have no access at all
- **Evidence**: The author's own direct statement of the access tier.
- **Confidence**: emerging (a specific, checkable pricing/access fact from hands-on use)
- **Quote**: "Right now, ChatGPT Work (in both flavors) is available only to $20/month and up subscribers. Free users and $8/month Go users do not have access."
- **Our assessment**: A concrete, verifiable access-tier fact not previously captured with this precision in the corpus's other ChatGPT Work notes (which focus on features and case studies rather than the pricing/access gate). Useful as a grounding detail for any guide discussion that assumes universal ChatGPT Work availability. Worth reading against `blog-openai-chatgpt-work-ambitious-partner.md` Claim 9, where OpenAI's July 9, 2026 launch post states that in the unified ChatGPT desktop app "Chat, Work, and Codex are available on every plan, including Free." That is in tension with Willison's Aug 30 report, but not filed as a contradiction per MINER.md §4a: the two statements are separated by ~7 weeks and describe different things (which modes appear in a desktop app surface vs. which subscription tiers can actually run Work), and no guide advice turns on resolving them. The safe framing for the guide is Willison's dated, hands-on one — treat Work as a paid-tier feature as of Aug 2026 — rather than the launch post's broader phrasing.

### Claim 3: OpenAI's own official guidance on when to use Chat vs. Work ("use Chat when you want an answer... use ChatGPT Work when you want ChatGPT to complete a task with a clear outcome") is, in Willison's assessment, unhelpful because he has used regular Chat for all of those same task categories for years
- **Evidence**: The author's direct critique of OpenAI's own published guidance, contrasted against his own multi-year usage pattern.
- **Confidence**: anecdotal (a single power user's subjective assessment that OpenAI's framing doesn't match his own usage experience)
- **Quote**: "I find that almost entirely useless, because I've been using regular ChatGPT Chat for all of those task categories for years!"
- **Our assessment**: A useful, named critique of vendor-provided mode-selection guidance being too vague to be actionable — worth flagging alongside the more concrete "what does Work actually have that Chat doesn't" feature list this article supplies as a corrective (Claims 4-7 below), which is a more practically useful decision criterion than OpenAI's own task-outcome framing.

### Claim 4: ChatGPT Work's code execution sandbox has open internet access by default — it can install packages, clone repositories, and interact with arbitrary websites/APIs — whereas ChatGPT Chat's code execution sandbox blocks that access via a container proxy, and this is "by far the most exciting feature of ChatGPT Work (Cloud)" for Willison
- **Evidence**: Direct first-hand comparison between Chat's and Work's sandboxed code-execution environments, based on hands-on testing.
- **Confidence**: emerging (a specific, testable technical claim about sandbox network policy, from a named power user's direct experimentation, though not independently verified against OpenAI documentation in this article)
- **Quote**: "The code execution environment can now talk to the rest of the internet! ChatGPT Chat can't do this—if you ask it to install additional software packages or interact with websites or APIs that access will be blocked by the container proxy."
- **Our assessment**: This is the article's headline technical finding and a specific, actionable capability claim for any guide discussion of code-execution sandbox design. Willison explicitly contrasts this against Claude's code-interpreter sandbox, which he says has allowed only a short domain allowlist (PyPI, npm, GitHub) since its September launch, versus Work's default-open policy — a specific inter-vendor sandbox-permissiveness comparison not previously documented in this corpus with this level of detail. Treat the "default appears to be open to all" characterization as Willison's own inference from testing, not a confirmed OpenAI policy statement — he notes Work "can be configured with a specific list of allowed domains," implying the open-by-default behavior is a default, not a hard architectural constraint.

### Claim 5: ChatGPT Work's browser tool can launch a full headless Chrome instance, load sites, fill forms, take screenshots, and run arbitrary JavaScript against a loaded page's DOM — and for sites requiring sign-in, it can hand control to the user to enter passwords and 2FA codes directly, without those credentials round-tripping through the model itself
- **Evidence**: Direct first-hand description plus a worked example (a prompt asking the browser to extract page headings via JavaScript, with the resulting tool call shown).
- **Confidence**: emerging (a specific, demonstrated capability claim with a shown example, from hands-on testing)
- **Quote**: "If a site requires sign in the browser can prompt you to take over and enter both passwords and 2FA codes, without round-tripping those credentials through the model itself."
- **Our assessment**: This credential-isolation design detail (user enters credentials directly into the browser session, bypassing the model) is a concrete security-relevant mechanism — a different but complementary approach to the "permission ledger" credential-isolation design `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 6 documents for the same browser tool (that note's ledger governs *which sites* the agent may act on; this claim describes how *credential entry itself* avoids exposing secrets to the model). Both claims describe the same underlying browser-use feature from independent hands-on testing, strengthening confidence that credential protection is a real, deliberate design choice rather than a marketing claim.

### Claim 6: ChatGPT Work gives each session its own persistent scratch folder under a shared `/workspace` volume (Willison had 171 folders in `/workspace/scratch` at time of writing) that persists across sessions and is mounted to all currently-running Work sessions simultaneously, so file edits in one session are instantly visible to others — unlike ChatGPT Chat, which gets a fresh, non-shared filesystem per session
- **Evidence**: Direct first-hand technical observation, including a specific folder-naming pattern and the author's own current folder count.
- **Confidence**: emerging (a specific, named implementation detail from hands-on inspection of the filesystem, not confirmed against OpenAI's own technical documentation in this article)
- **Quote**: "In ChatGPT Work each session gets its own scratch folder—named something like /workspace/scratch/e00a0a017944—but each of those are persisted across sessions, so you can access files from previous chats. I have 171 folders in /workspace/scratch right now!"
- **Quote (shared-mount detail)**: "As far as I can tell that /workspace volume is mounted to all Work sessions that are currently running—file edits from one can be instantly seen by the others."
- **Our assessment**: This corroborates and extends `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 2 (each Work task gets a working directory at `/workspace/scratch` with "the freedom of a normal computer") — both sources independently name the identical path (`/workspace/scratch`), which is strong independent confirmation of the mechanism's existence and naming. This article adds detail Khemani's did not: that the volume is *simultaneously mounted across concurrently running sessions* (not just persistent across sequential sessions), with instant cross-session file visibility — a materially different and more specific claim than "persists across sessions" alone, since it implies live, shared-state concurrency rather than just durable storage. Willison also notes sessions "don't seem to share the same process space" and localhost servers in one session aren't reachable from another, a useful boundary detail on how far the sharing extends.

### Claim 7: ChatGPT Work can run sub-agent sessions using the named model variants (Sol, Luna, and Terra), a capability entirely unavailable in ChatGPT Chat, positioned as "very much a power-user feature" for complex, parallelizable projects
- **Evidence**: The author's own direct, brief statement of the capability and its intended use case.
- **Confidence**: emerging (a specific capability-availability claim from hands-on use, though the article states "there's not much to say about this one" — it is not explored in depth)
- **Quote**: "There's not much to say about this one. ChatGPT Chat can't run sub-agents. ChatGPT Work can. This is very much a power-user feature: if you are running a complex project that can benefit from multiple parallel agents working together, Work can do that."
- **Our assessment**: Corroborates `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 5 (sub-agents exist in Work/Ultra mode but are hidden from the user by default) and this article's own earlier remark that "Ultra is a special mode that more eagerly delegates to sub-agents" — consistent with Nathan's first-person account of the same feature from inside OpenAI. Willison's treatment is much thinner than Nathan's (no design-tradeoff discussion, no mention of the hidden-by-default UX choice), so this claim should be cited as confirming the feature's *existence* from an independent, external vantage point, not as adding new mechanism detail beyond what the Nathan interview already covers.

### Claim 8: Scheduled prompt automations, which Willison initially listed as a Work-exclusive feature, turned out — per his own inline correction — to also work in ChatGPT Chat, undercutting his own earlier claim that this was one of the features distinguishing Work from Chat
- **Evidence**: The article's own self-correction, added as an inline "Update" note directly beneath the original claim.
- **Confidence**: anecdotal (a single author's own real-time correction of his own initial testing; no explanation is given for the discrepancy or how it was resolved)
- **Quote**: "Update: Actually this seems to work in ChatGPT Chat as well."
- **Our assessment**: This is the article disagreeing with itself in a minor, self-corrected way (per MINER.md §4a, "a source disagrees with itself") — but it does not rise to the bar for filing a contradiction issue, because Willison resolves it himself within the same article rather than leaving two live, opposing claims, and no guide-impacting decision would turn on which version is correct (the underlying feature works in both surfaces either way). Worth flagging in the guide only as a caution that this article's initial "here's what Work has that Chat doesn't" feature list (the seven-item list under "Work has features that aren't available in Chat") should not be treated as a fully verified, final differentiator list — Willison himself found and flagged at least one item on it to be wrong.

### Claim 9: Willison assesses ChatGPT Work as combining all three legs of his own "lethal trifecta" model (private-data access, untrusted-content exposure, and an exfiltration path), and states he would like OpenAI to explain more about how they protect Work sessions against prompt injection, guessing their answer is "the same auto-review mechanism as Codex"
- **Evidence**: Direct application of the author's own named security framework to the specific product under review, plus an explicit request for more vendor transparency.
- **Confidence**: emerging (a specific, named risk-framework application from the framework's own creator, though the "protection mechanism is probably the same as Codex's auto-review" claim is explicitly speculative — Willison states he does not know and is guessing)
- **Quote**: "My lethal trifecta model warns about the risks inherent in any agent system that combines access to private data with exposure to untrusted content and a way to communicate stolen information back to an attacker."
- **Quote (verdict)**: "ChatGPT Work combines all three!"
- **Our assessment**: This directly corroborates `blog-simonwillison-openai-lockdown-mode.md` Claim 3 (the lethal-trifecta framework as the theoretical basis for evaluating agent-system risk) — the same author applying the same named framework to a different OpenAI product, reinforcing that OpenAI's own agent products (Lockdown Mode's subject and now ChatGPT Work) are both assessed by their creator as trifecta-complete by default. Unlike the Lockdown Mode article, this piece does not describe any specific mitigation Work has shipped (Lockdown Mode itself is not mentioned here) — Willison explicitly says he is speculating that Work's protection is "the same auto-review mechanism as Codex," which he has not verified. This is a gap worth flagging: if the guide cites Work's security posture, it should not imply Willison has confirmed what defenses exist, only that he has confirmed the risk profile. The mechanism Willison guesses at is documented in the corpus: `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13 describes Auto-review as using OpenAI's "most advanced models to review important actions involving connected tools and APIs before they happen" — so the feature he assumes covers Work does exist and is vendor-described, but that note presents it as an Enterprise/Edu admin governance feature, which is not obviously the same thing as a prompt-injection defense applied to every Work session. Willison's request for transparency stands even against the corpus's best existing answer.

### Claim 10: Willison identifies two specific, named documentation failures behind why ChatGPT Work is confusing to understand: OpenAI explains Work in terms of what it's for rather than what it actually does, and OpenAI does not publish the system prompt or tool descriptions the agent uses
- **Evidence**: The author's own direct critique, stated as his diagnosis for why the investigative work behind this entire article was necessary.
- **Confidence**: anecdotal (a single practitioner's assessment of vendor documentation quality, though backed by the fact that the rest of the article is itself the evidence — extensive reverse-engineering was required to answer basic capability questions)
- **Quote**: "If the ChatGPT Work documentation included the exact system prompt and tool descriptions used by the agent I wouldn't have needed to write this post."
- **Our assessment**: A specific, named documentation-transparency critique (functional description vs. technical description; hidden system prompts and tool descriptions) that is a recurring theme across multiple vendors in this corpus's coverage of agent products — worth citing as a concrete illustration of the practitioner cost of opaque system-prompt/tool-schema documentation, distinct from a general "documentation could be better" complaint.

### Claim 11: By prompting a fresh Work session to build a self-documenting website listing and explaining its own tools, then following up to also extract full copies of its own skills, Willison surfaced 223 registered tools (6 of which were his own personal MCP tools served via `datasette-mcp`, not native OpenAI tools) and 44 distinct skills, including a `control-browser` skill whose instructions reveal the browser is driven through a Node REPL tool and an `agent.browsers.*` runtime API
- **Evidence**: A concrete, reproducible methodology (two sequential prompts to the product itself) with a specific numeric result and a named example of the extracted content (the `control-browser` skill's own instructions, which the author further extended by prompting Work to append its own `browser.documentation()` output to the published page).
- **Confidence**: emerging (a specific, reproducible extraction method with a checkable numeric result — the generated site is linked and viewable — though the *content* of what Work reported about itself is self-reported by the model, not independently verified against OpenAI's actual source configuration, so the 223/44 figures reflect what Work says about itself, not a ground-truth audit)
- **Quote**: "Here's the site it built, which includes details of 223 registered tools—though 6 of those are from my own personal MCPs served via datasette-mcp."
- **Quote (skills count)**: "It turns out ChatGPT Work uses a lot of skills—44 in fact!"
- **Our assessment**: This is the most novel and concrete contribution of the article: a reproducible, self-referential prompting technique for making an opaque agent document its own tool/skill surface, directly addressing the documentation gap named in Claim 10. No other source note in this corpus documents a specific tool count (223) or skill count (44) for ChatGPT Work, nor this self-documentation extraction methodology. The caveat about self-reported content applies: a model asked to describe its own tools may omit, mis-describe, or hallucinate details, so the 223/44 figures and the reproduced skill text should be treated as "what Work says about itself when asked," not as ground truth confirmed against OpenAI's actual configuration — Willison does not claim otherwise. `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10 supplies a plausible *mechanism* for why a self-referential prompting trick was needed at all: OpenAI's own engineering post describes the Codex/ChatGPT Work harness as using "deferred discovery," which makes integrations, custom MCP tools, skills, and plugins only surfaceable when needed rather than all resident in context up front. If the tool and skill surface is deliberately not loaded by default, no ordinary "what tools do you have?" question would enumerate it — which fits Willison's own experience here that his first prompt surfaced only `web.run` as the browser-related tool (missing the headless-browser capability he had already observed in testing), and that a second, separate prompt was required before the 44 skills appeared at all. Deferred discovery also sharpens the self-reporting caveat above: an inventory the model produces about itself is bounded by what its harness chose to surface at that moment, so 223 and 44 are better read as floors than as audited totals.

## Concrete Artifacts

```
Source: Simon Willison's Weblog, "Understanding ChatGPT Work,"
https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/,
published 2026-08-30.

Feature list Willison identifies as Work-exclusive (vs. Chat), from the
"Work has features that aren't available in Chat" section (see Claim 8
for the one item he later flagged as incorrect — scheduled automations):
  1. Options to use Luna and Terra in place of Sol (model selection)
  2. A code execution environment with Internet access
  3. A headless Chrome browser
  4. A persistent filesystem shared between sessions
  5. The ability to publish ChatGPT Sites
  6. The ability to run sub-agent sessions with Sol, Luna, and Terra
  7. Scheduled prompt automations ("may be in ChatGPT Chat too" —
     later confirmed to also work in Chat, per Claim 8)

Model/reasoning options in Work (per the article's "Model selection"
section):
  - GPT-5.6: Sol, Luna, or Terra, each at Light / Medium / High /
    Extra High / Max / Ultra reasoning
  - GPT-5.5: at Light / Medium / High / Extra High
  - Chat's separate selection: 5.6 Instant / Medium / High / Extra High /
    Pro (Extra High and Pro gated to $100/month+ subscribers; 5.6 Pro
    has no Work equivalent)
  - Willison's belief (unconfirmed, stated as "I believe"): Work sessions
    bill against the Codex allowance; Chat sessions have a separate
    allowance.

ChatGPT Sites example: a site built from the prompt "Figure out all of
the places in London with a pelican in her piety, then turn that into a
JSON file and build a ChatGPT sites site about them," deployed via
Cloudflare Workers (with D1/R2 for stateful features), default-private
per creator, shareable on team plans.

Tool/skill self-documentation artifact (Claim 11):
  - Prompt 1: "Build a site that lists every one of your tools -
    nearly grouped into categories - and for each one explain what it
    does. Try to exactly duplicate arguments and tool descriptions
    where possible. Design aesthetic should be technical docs, minimal
    flare" -> a published site listing 223 tools (6 personal MCP tools
    included).
  - Observation: the only browser-related tool initially listed was
    `web.run` (search/open-URL/click-link methods), which did not match
    the full headless-browser capability observed elsewhere in testing.
  - Prompt 2: "Add full copies of every skill to the website (separate
    pages linked to from the homepage)" -> revealed 44 skills, including:
    control-browser, documents (.docx creation), imagegen (image_gen
    tool tips), pdf (read/render), spreadsheets (.xlsx/.xls/.csv/.tsv),
    sites:sites-building, openai-docs, data-analytics:build-dashboard.
  - Follow-up prompt: "Add the full output of await
    browser.documentation() to the bottom of the /skills/control-browser
    page" -> the control-browser skill's own text names a Node REPL tool
    (callable id "mcp__node_repl__js" in this environment) as how browser
    setup code runs, and an `agent.browsers.*` runtime API as how the
    agent interacts with the browser directly, with an explicit
    instruction that the agent MUST read the output of
    `await browser.documentation()` before attempting to use it.
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in
those notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 1 (Codex and
    ChatGPT Work share an identical underlying harness, differentiated
    only at the UX layer) — corroborated independently, from outside
    OpenAI, by this article's Claim 1 ("Work Local... feels more like
    regular Codex re-skinned").
  - `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 8 (Cloud
    Mode vs. Local Mode as two distinct operating modes) — corroborated
    by this article's Claim 1, an independent naming of the same
    Cloud/Local split ("Work Cloud" / "Work Local").
  - `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 2 (each
    Work task gets a working directory at `/workspace/scratch`) —
    corroborated and extended by this article's Claim 6, which
    independently names the identical path and adds the cross-session
    simultaneous-mount detail Khemani's note does not include.
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 5 (sub-agents
    exist in Work/Ultra mode) — corroborated by this article's Claim 7
    and its own remark that "Ultra is a special mode that more eagerly
    delegates to sub-agents," an independent external confirmation of
    the same feature Nathan describes from inside OpenAI.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10 (OpenAI's
    agentic harness for Codex and ChatGPT Work is a single Rust
    orchestration layer using "deferred discovery") — a third source for
    the shared-harness claim in this article's Claim 1, and the most
    technical of the three: Nathan describes the shared harness as a
    product decision, Willison here infers it from the outside ("re-skinned
    Codex"), and OpenAI's engineering post states it as an implementation
    fact. Note: the shared-harness material in that note is at Claim 10,
    not Claim 1 (its Claim 1 is the Luna/Terra price cut).
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13 (Auto-review
    uses OpenAI's most advanced models to review important actions
    involving connected tools/APIs before they happen) — this article's
    Claim 9 guesses that Work's prompt-injection protection "is the same
    auto-review mechanism as Codex," and that note confirms such a
    mechanism exists and is vendor-described, though scoped there to
    Enterprise/Edu governance rather than to every Work session.
  - `blog-simonwillison-openai-lockdown-mode.md` Claim 3 (the "lethal
    trifecta" framework as the basis for evaluating agent-system risk)
    — the same author applying the same named framework to a different
    OpenAI product in this article's Claim 9, reinforcing the framework's
    consistent use as Willison's standard lens for assessing OpenAI
    agent-product risk.
- **Contradicts**: None rising to MINER.md §4a's filing bar. Claim 8
  documents the article contradicting *itself* (an inline self-correction
  about whether scheduled automations are Work-exclusive), but Willison
  resolves it within the same piece and no guide-impacting decision turns
  on which version is right, so no contradiction issue was filed. A second,
  cross-source tension was considered and also not filed: this article's
  Claim 2 (Free and $8/month Go users have no Work access) sits against
  `blog-openai-chatgpt-work-ambitious-partner.md` Claim 9 ("Chat, Work, and
  Codex are available on every plan, including Free"), but the two are ~7
  weeks apart and describe different things — desktop-app mode visibility
  vs. subscription-tier entitlement — which is a conditioning/temporal
  difference rather than opposing guide advice (MINER.md §4a). See Claim 2's
  assessment for the framing the guide should use.
- **Extends**:
  - `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 6 (browser
    tool credential isolation via a "permission ledger" governing which
    sites the agent may act on) — this article's Claim 5 adds a
    complementary credential-isolation detail Khemani's note does not
    cover: sign-in credentials (passwords, 2FA codes) are entered
    directly by the user into the browser session rather than passing
    through the model, addressing a different part of the same
    credential-exposure risk (input-time exposure vs. site-access scope).
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10 ("deferred
    discovery" makes integrations, custom MCP tools, skills, and plugins
    only surfaceable when needed) — this article's Claim 11 is, in effect,
    an empirical consequence of that architectural choice observed from
    outside: because the tool/skill surface is not resident in context by
    default, Willison needed a self-referential prompt (and then a second
    one for skills) to enumerate it at all, and his first pass surfaced
    only `web.run` rather than the headless browser he had already used.
    That note names the mechanism; this note shows what it costs a
    practitioner trying to audit the product.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11 (Scheduled
    Tasks can run once, repeat on a schedule, or monitor for changes and
    trigger on an event) — this article's Claim 8 adds an outsider's
    correction that scheduled prompt automations are not Work-exclusive,
    a boundary detail OpenAI's own launch post does not state.
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 9 (memory
    inheritance) and Khemani's Claim 5 (standalone-vs-heartbeat scheduled
    tasks) — this article's Concrete Artifacts feature list and Claim 8
    add an outsider's confirmation that scheduled automations exist as a
    feature, plus the caveat (found through Willison's own testing) that
    the feature is not actually Work-exclusive, a boundary detail neither
    of those two notes states.
- **Novel**:
  - The specific tool/skill self-documentation extraction methodology
    and its numeric results — 223 registered tools, 44 skills (Claim 11)
    — not present anywhere else in the corpus. No existing ChatGPT Work
    source note gives any tool or skill count.
  - The `control-browser` skill's own internal implementation detail
    (Node REPL tool `mcp__node_repl__js`, `agent.browsers.*` runtime API,
    a required `browser.documentation()` read-before-use step) — the
    first source in the corpus to document ChatGPT Work's browser
    automation at this level of technical/implementation specificity,
    versus the higher-level "full Chrome instance" and "permission
    ledger" descriptions in existing notes.
  - The direct sandbox-permissiveness comparison against Claude's code
    interpreter (short domain allowlist vs. Work's open-by-default
    internet access) (Claim 4) — not previously documented in this
    corpus as an explicit inter-vendor comparison.
  - The $20/month subscription gate and Free/Go-tier exclusion (Claim 2)
    — a specific access-tier fact not previously captured in the corpus's
    other ChatGPT Work notes.
  - The named documentation-quality critique — functional vs. technical
    explanation, and withheld system prompts/tool descriptions as the
    two specific causes of confusion (Claim 10) — a sharper, more
    specific version of documentation criticism than any existing note
    in the corpus's ChatGPT Work coverage supplies.

## Guide Impact

- **Chapter 04 (Tool Use & Ecosystem / Agent Architecture)**: Add Claim 11
  as a concrete, reproducible technique — prompt an opaque agent product
  to build a self-documenting site cataloging its own tools and skills —
  for practitioners auditing what capabilities a closed agent product
  actually has, distinct from vendor marketing copy. Pair with the
  explicit caveat that the resulting inventory is self-reported by the
  model, not independently verified against the vendor's real
  configuration. Pair it also with
  `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10's "deferred
  discovery" as the architectural reason the technique is necessary: when a
  harness deliberately keeps tools, skills, and MCP integrations out of
  context until needed, the agent's own default self-description is
  incomplete by design, so an auditor must prompt for the inventory
  explicitly — and should treat the result as a lower bound on what is
  installed, not a complete list.
- **Chapter 03 (Multi-Agent Coordination / Computer Use & Sandboxing)**:
  Add Claim 4's sandbox-permissiveness comparison (Work's code-execution
  environment open to the internet by default vs. Claude's code
  interpreter's short domain allowlist) as a concrete data point for a
  guide discussion contrasting vendor approaches to code-execution
  network policy — flag that this is Willison's own testing-based
  inference about the default, not a confirmed OpenAI policy statement.
- **Chapter 03 (Computer Use & Browser Automation)**: Add Claim 5's
  credential-entry-bypasses-the-model detail alongside the existing
  "permission ledger" mechanism from `blog-latentspace-khemani-unpacking-chatgpt-work.md`
  Claim 6, as two complementary halves of ChatGPT Work's browser-use
  credential-protection design (which sites it may touch; how sign-in
  credentials avoid ever reaching the model).
- **Chapter 06 (Tool/Vendor Evaluation)**: Add Claim 10 as a concrete,
  quotable example of a documentation-transparency critique (functional
  vs. technical explanation; undisclosed system prompts and tool
  descriptions) applicable as an evaluation criterion when assessing any
  vendor's agent product documentation, not just ChatGPT Work.
- No chapter should cite the 223-tools/44-skills figures as a confirmed,
  vendor-verified inventory — per Claim 11's assessment, these are what
  Work reported about itself when prompted, not an independently audited
  count.

## Extraction Notes

- **Fetch method**: An initial `WebFetch` pass against the URL returned a
  reasonably accurate but partially-summarized rendering (with some
  quotes constructed by splicing non-adjacent sentences together with
  ellipses), consistent with the known limitation — documented elsewhere
  in this corpus — that `WebFetch` routes pages through a small
  summarization model rather than returning raw text. Because the page is
  not paywalled, the full raw HTML was instead fetched directly via
  `curl` with a browser user-agent, the `entryBody` div was isolated, and
  HTML tags/entities were stripped locally to produce a plain-text copy
  of the full article body. All `Quote` fields above were checked
  character-for-character against that stripped text (including its
  typographic curly quotes/apostrophes, preserved as they appear on the
  page) before being finalized, per MINER.md §2a; none splice
  non-adjacent sentences.
- **Full article read**: The entire article was read in full via the
  stripped-text extraction described above, from the opening framing
  paragraph through every named section ("ChatGPT Work is actually two
  products," "Work is for paid subscribers only," "Work has features that
  aren't available in Chat," "Model selection," "Code execution with
  Internet access!," "A full, headless Chrome browser," "A persistent,
  shared filesystem," "ChatGPT Sites," "Sub-agents with Sol, Luna, and
  Terra," "Scheduled prompt automations," "Is this safe?," "OpenAI could
  make this a lot less confusing," "A list of all the tools," and "And a
  whole lot of Skills") to the closing byline. The article links to
  several external pages (OpenAI's Work announcement, the auto-review
  mechanism docs, Willison's own lethal-trifecta post, a self-generated
  tool-reference site at codex-tool-reference.simonw.chatgpt.site, and
  several individual skill-documentation pages); none of these were
  followed as separate sub-pages, since the article itself quotes and
  summarizes their relevant content directly (e.g. the `control-browser`
  skill text and its `browser.documentation()` output are reproduced
  inline in the article body, which this note draws from directly rather
  than fetching the linked page separately).
- **Cross-references verified**: `blog-latentspace-nathan-chatgpt-work-harness.md`
  Claims 1 and 5; `blog-latentspace-khemani-unpacking-chatgpt-work.md`
  Claims 2, 6, and 8; `blog-simonwillison-openai-lockdown-mode.md`
  Claim 3; `blog-simonwillison-gpt56-luna-price-drop.md` Claim 10; and
  `blog-openai-chatgpt-work-ambitious-partner.md` Claims 9, 11, and 13
  were each re-read in full before citing; no claim numbers were guessed.
  One correction worth recording: the shared-harness / "deferred discovery"
  material in `blog-simonwillison-gpt56-luna-price-drop.md` is that note's
  **Claim 10**, not its Claim 1 (Claim 1 there is the Luna 80% / Terra 20%
  price cut). Cited by the verified number.
- **Second-pass corpus sweep**: The two same-cluster notes not cited in the
  first draft were re-checked directly. Neither is subsumed by the
  Nathan/Khemani notes: `blog-simonwillison-gpt56-luna-price-drop.md`
  Claim 10 supplies the harness implementation detail (Rust orchestration
  layer, deferred discovery) that neither of those notes contains, and
  `blog-openai-chatgpt-work-ambitious-partner.md` supplies the vendor's own
  Auto-review description (Claim 13) that this article's Claim 9 speculates
  about, plus a plan-availability statement (Claim 9) in tension with this
  article's Claim 2. All are now cited at the relevant claims.
- No contradiction with any existing corpus source note was found during
  cross-referencing (the only self-contradiction found is internal to
  this article itself, Claim 8, and does not meet the MINER.md §4a filing
  bar — see Cross-References → Contradicts above), so no contradiction
  issue was filed.
