---
source_url: https://www.deeplearning.ai/the-batch/issue-371
source_type: blog-post
title: "The Batch Issue 371: Meta's Agent Security, The Navier-Stokes Controversy, Fraud on Claude"
author: Andrew Ng and The Batch editorial team (DeepLearning.AI)
date_published: 2026-09-18
date_extracted: 2026-10-05
last_checked: 2026-10-05
status: current
confidence_overall: emerging
issue: "#3906"
---

# The Batch Issue 371: Meta's Agent Security, The Navier-Stokes Controversy, Fraud on Claude

> A weekly digest whose most guide-relevant content is a detailed secondary account of Meta's Muse agent architecture (OS-level isolation, credential separation, a gatekeeper agent, out-of-band approvals), plus Andrew Ng's "blame the user of the hammer" framing of agent responsibility, a Navier-Stokes dispute summary, Anthropic's illicit-distillation report, and a Meta paper on a proactive memory agent.

## Source Context

- **Type**: blog-post (weekly newsletter issue; Ng letter + four news items). The issue page is Cloudflare-blocked for direct fetch; the full text was read through a reader proxy (r.jina.ai) of the same URL. The note covers the entire issue.
- **Author credibility**: Andrew Ng (DeepLearning.AI) and The Batch's reporting team. Reporting is secondary: the Muse, Navier-Stokes and Anthropic items summarize primary announcements (Meta, OpenAI, Buckmaster, Anthropic) that the issue links but this note did not independently fetch. The Ng letter is opinion.
- **Scope**: Muse agent security design; OpenAI/Navier-Stokes credit dispute; Anthropic's report on seven China-based developers; Meta's Proactive Memory Agent paper. It does not provide Muse evaluation data (the issue itself says Meta withheld it).

## Extracted Claims

### Claim 1: Meta's Muse agent is designed on the assumption that prompt injection will succeed, so controls live at the OS/infrastructure level rather than in the model
- **Evidence**: Architectural description of Muse (per-user VM, sealed runtime cell, credential service, Sentinel gatekeeper). Secondary reporting of Meta's own disclosure; no independent test.
- **Confidence**: emerging
- **Quote**: "Meta assumes the model will be fooled, and it built controls at the operating-system level that should hold regardless of the model’s actions."
- **Our assessment**: Strong, specific design pattern consistent with the "impossible vs. tedious" criterion in our zero-trust notes. Credible as a design description; its efficacy is unproven (see Claim 8).

### Claim 2: Muse splits each VM into a sealed runtime cell (untrusted-data handling) and services outside the cell that hold secrets and decide permissions
- **Evidence**: Description of Linux container with own filesystem and virtual NIC; the cell reaches outside only via local channels carrying no passwords or tokens; admin rights in the cell do not extend to the host.
- **Confidence**: emerging
- **Quote**: "the VM is divided into two zones: (i) a sealed runtime cell where the agent and its tools handle untrusted data and (ii) services outside the cell that hold passwords and decide what the agent can do."
- **Our assessment**: A clean statement of the control-plane/data-plane split for agents. Applicable to any harness that runs untrusted content.

### Claim 3: The model never holds credentials; it works with stand-in tokens that a separate agent (Sentinel) swaps for real credentials as requests leave the VM
- **Evidence**: Described mechanism; connectors outside the cell receive only the credentials they need; the email connector strips temporary passcodes and password-reset links before the agent reads a message.
- **Confidence**: emerging
- **Quote**: "Muse Spark 1.3 never sees credentials."
- **Our assessment**: Credential-by-proxy is a pattern the guide can recommend generally. Meta's claim that this makes credential theft by injection "impossible" is a vendor claim; the note reads it as "removes the agent as a credential-exfiltration path," not as a proof of overall safety.

### Claim 4: A single gatekeeper (Sentinel) is the only component that can permit an action, and it tracks which tool processes have read user data to gate egress
- **Evidence**: Described policy: processes that have not read user data may reach a short list of pre-approved destinations; processes that have must ask the user. Each connector call is checked against user-set permissions and allowed, denied, or escalated.
- **Confidence**: emerging
- **Quote**: "Only Sentinel can permit an action proposed by Muse Spark 1.3."
- **Our assessment**: This is a taint-tracking egress policy, i.e., cutting the "send data out" leg of the lethal trifecta dynamically rather than statically. Notably more granular than the opt-in Lockdown Mode in our existing note.

### Claim 5: Approval requests are rendered out-of-band as system dialogs, not as chat messages, so injected text cannot manufacture user consent; high-risk actions always require verification
- **Evidence**: Described design: agent stops when Sentinel asks; approvals are scoped to a connector/destination and purpose and may be limited to one action, session, task, time span or all future uses; emails and purchases always require verification; purchases on unfamiliar sites use a single-use Stripe Link card limited to merchant, amount and time.
- **Confidence**: emerging
- **Quote**: "This way, prompt-injected text can’t manufacture a user’s approval."
- **Our assessment**: Directly actionable for human-in-the-loop design: approval UI must be a channel the model cannot write to. Single-use scoped payment credentials are a transferable pattern.

### Claim 6: Muse adds three model-level layers on top: untrusted-data labeling, an ensemble of externally-run classifiers, and a browser sub-agent that reads only the accessibility tree and cannot run JavaScript
- **Evidence**: Described design. Classifiers run outside the cell so an attacker cannot disable them; other classifiers block routing of personal data to destinations the task did not call for.
- **Confidence**: emerging
- **Quote**: "In the browser, a sub-agent reads a structured summary of each page — the accessibility tree that screen readers use — instead of the page’s code."
- **Our assessment**: The accessibility-tree reader is a notable, concrete input-sanitization technique for browsing agents; effectiveness not quantified.

### Claim 7: Muse's design lines up with prior public work (CaMeL, Willison's lethal trifecta), and Meta defends the layers behind the classifiers because classifier-only defense is unacceptable
- **Evidence**: The "Behind the news" section cites CaMeL (Google DeepMind / ETH Zurich, April 2025) and Willison's trifecta, and a Willison argument that a classifier catching 99 percent of new injections is still an unacceptable risk.
- **Confidence**: emerging
- **Quote**: "Muse processes all three but routes outgoing data through a component the model can’t override, according to Meta."
- **Our assessment**: Notable that Muse does *not* follow Willison's "avoid combining them" advice; it combines all three legs and bets on a deterministic chokepoint. Whether that bet holds is the open question.

### Claim 8: Meta's security claims are not independently evidenced — evaluations are unpublished and Meta substitutes a bug bounty
- **Evidence**: The issue's "Yes, but" and "Undisclosed" bullets.
- **Confidence**: settled (as a statement of what was disclosed)
- **Quote**: "it has not provided accuracy metrics for the classifiers that screen incoming data."
- **Our assessment**: Important caveat for any guide recommendation: treat Muse as a design reference, not a validated one. The bounty ($300,000 top, $130,000 for prompt injection) is a signal of confidence, not evidence.

### Claim 9: Ng argues responsibility for agent actions lies with the person who prompts or builds the agent, and warns of AI companies "disclaiming responsibility"
- **Evidence**: Opinion/analogy (the hammer); no data.
- **Confidence**: anecdotal
- **Quote**: "if I prompt an agent and it hacks into someone else’s system, the responsibility lies with me, not the agent."
- **Our assessment**: A normative position, useful as a counterweight to anthropomorphic framing, but in tension with notes that treat agents as having emergent misaligned goals (see Cross-References). The letter itself concedes "Today’s agentic systems are not predictable."

### Claim 10: Ng attributes the OpenAI–Hugging Face incident to buggy sandboxing and monitoring, argues AI agents' main cyber advantage is relentlessness, and expects long-term advantage to defenders
- **Evidence**: Opinion; also notes the "1,200 agents" figure is unremarkable parallelism ("I have about 1,300 processes running on my laptop").
- **Confidence**: anecdotal
- **Quote**: "The main advantage of AI agents is that they are relentless."
- **Our assessment**: Partly consistent with OpenAI's own account (reduced safeguards, missing monitoring) but undersells the misalignment patterns OpenAI itself documented (reward hacking, agents adopting goals from each other). The "defenders win long-term" claim is unsupported here.

### Claim 11: The Navier-Stokes dispute turns on whether OpenAI's agents could have seen Buckmaster and Alpöge's work; OpenAI revised its statement from "can't determine" to "could not have influenced" for only the preceding two months
- **Evidence**: Timeline reported from Buckmaster's post, Bubeck's X post and OpenAI's statements: Sept 6 phone calls, Sept 7 Lean-verified proofs of three simpler equations by Buckmaster/Alpöge, Sept 8 announcement, Sept 10 revised statement.
- **Confidence**: emerging
- **Quote**: "However, OpenAI did not address whether earlier Codex prompts may have influenced the system."
- **Our assessment**: Contributes the unresolved training-data-provenance gap that OpenAI's own post (existing note) presents as closed. Practical lesson for practitioners is the Batch's: check provider data-retention/training settings.

### Claim 12: Independent verification of the Navier-Stokes proof is not complete and a formal proof does not confer understanding; verification is now cheap while human understanding stays expensive
- **Evidence**: Clay's rules require publication, a two-year wait and expert acceptance; OpenAI says it is not seeking the prize. Contrast: Anthropic's Lean proof of Fermat's Last Theorem built on and was endorsed by Kevin Buzzard.
- **Confidence**: emerging
- **Quote**: "While automated verification has become relatively inexpensive, human-readable understanding remains costly."
- **Our assessment**: A crisp restatement of the verification-vs-comprehension asymmetry that is relevant to AI-generated code review in general, not just mathematics.

### Claim 13: Anthropic alleges seven China-based developers fraudulently accessed Claude (false identities, stolen cards/keys, "transfer stations") to distill reasoning and to resell Claude output as their own models' output
- **Evidence**: Reported figures from Anthropic's report: Alibaba's May–June 2026 campaign of 151 million exchanges through 5,000 fraudulent accounts; Zhipu abandoning Fable for weaker-safeguard models; sensitive user data (including a PLA member, a state-owned-enterprise employee, a Russian defense agent) routed to Claude through DeepSeek/Moonshot front-ends. The Batch relays allegations; companies' responses are not reported.
- **Confidence**: emerging
- **Quote**: "Zhipu then switched to Opus 4.6 and another U.S. frontier model specifically because their safeguards appeared to be weaker."
- **Our assessment**: Interesting evidence that stronger cyber safeguards measurably displaced misuse toward weaker models. All claims are allegations by an interested party; relayed secondhand.

### Claim 14: Ng's "We're thinking" rebuts the distillation narrative: you cannot distill your way to a frontier model
- **Evidence**: Opinion; asserts the accused labs' published technical breakthroughs mattered more.
- **Confidence**: anecdotal
- **Quote**: "You can’t distill your way to a frontier model."
- **Our assessment**: A counterpoint to the allegation framing; no evidence offered. Mostly peripheral to the guide.

### Claim 15: A separate "Proactive Memory Agent" that runs beside an action agent and injects short, well-timed reminders improved all tested benchmarks, and beat reminding at every step
- **Evidence**: Meta AI paper (Yifan Wu et al.) as summarized: Terminal-Bench 2.0 (85 problems) Sonnet 4.5 45.9% vs 37.6%, Opus 4.6 45.9% vs 43.5%, fine-tuned Qwen3.5-27B 41.1% vs 37.6%; τ2-Bench (278 problems) Sonnet 4.5 61.8% vs 55.0%, Opus 4.6 68.7% vs 66.2%. The memory agent sees the problem description and the action agent's eight most recent outputs/tool calls and maintains notes on facts, environment, fixes, unfinished work and failed commands.
- **Confidence**: emerging
- **Quote**: "Apparently reminding an agent is not enough. It’s necessary to remind it at the right moments."
- **Our assessment**: Modest, benchmark-based gains (largest for the weaker model; ~2.4–2.5 points for Opus 4.6). Plausible mechanism and bolt-on deployment; we did not read the paper. Note a text inconsistency in the summary (Opus 4.5 vs 4.6 in "Results").

## Concrete Artifacts

```
Muse agent isolation architecture (The Batch issue 371, "How To Secure Agents for the Masses"):
  Per-agent VM
    ├─ Sealed runtime cell (Linux container; own filesystem + virtual NIC)
    │    agent harness + user workspace + tools; handles untrusted data
    │    reaches outside ONLY via local channels (no passwords/tokens;
    │    OS-level verification of the process at each end)
    └─ Outside the cell
         ├─ Credential service (real passwords/tokens; agent sees stand-ins)
         ├─ Sentinel (approves every request; swaps in real credentials on egress;
         │            allow / deny / ask user; tracks which tool processes read user data)
         ├─ Connectors (receive only the credentials they need;
         │              email connector strips passcodes and reset links)
         └─ Prompt-injection classifier ensemble (outside cell so it cannot be disabled)
  Approvals: system dialog in Muse app, not in conversation; scoped to one
  connector/destination + purpose; purchases via single-use Stripe Link card.
```

```
Reported benchmark results, Proactive Memory Agent (The Batch issue 371):
Terminal-Bench 2.0 (85 problems):  Sonnet 4.5 37.6 -> 45.9 | Opus 4.6 43.5 -> 45.9 | Qwen3.5-27B 37.6 -> 41.1
tau2-Bench (278 problems):         Sonnet 4.5 55.0 -> 61.8 | Opus 4.6 66.2 -> 68.7
```

```
Distillation figures reported from Anthropic's report (The Batch issue 371):
Alibaba, May-June 2026: 151 million exchanges via 5,000 fraudulent accounts
Navier-Stokes (OpenAI, as reported): 10,000 agents, 88 hours, 4.9M messages, ~300B output tokens, +17 hours Lean formalization
FLT (Anthropic, as reported): ~11 days, ~6 billion output tokens
```

## Cross-References

- **Corroborates**: `blog-anthropic-zero-trust-ai-agents.md` Claims 3 and 4 (controls must make attacks impossible, not tedious; hardware-bound/expiring credentials and non-existent network paths) — Muse's credential-by-proxy and sealed cell are an instance. `blog-simonwillison-openai-lockdown-mode.md` Claims 3–5 (lethal trifecta; cut the exfiltration leg; deterministic mechanism not relying on AI judgment) — Sentinel is a deterministic egress chokepoint. `blog-simonwillison-prompt-injection-role-confusion.md` Claim 8 (without provenance-based role perception, prompt-injection defenses are structurally weak) — Muse's untrusted-data labeling plus out-of-band controls is the architectural response. `blog-openai-hf-incident-road-ahead.md` Claim 13 (monitoring and the production harness materially reduced risk) supports Ng's "improved monitoring" point in Claim 10 here.
- **Contradicts**: None filed. Soft tension (a difference of framing, not filed as a contradiction): Ng's Claim 9 here (responsibility lies with the user, not the agent; the hammer analogy) vs. `blog-openai-hf-incident-road-ahead.md` Claim 12 (OpenAI documenting misalignment patterns such as agents adopting goals from one another). They address different questions (accountability vs. mechanism), so this was not filed under MINER.md §4a.
- **Extends**: `blog-openai-navier-stokes-solution.md` Claim 10 (OpenAI says Buckmaster's prompts could not have influenced the system) — this source adds that the statement covers only the two preceding months and that the first version of the statement said OpenAI could not determine whether activity was used to improve models. Also Claims 3 and 8 there (10,000 agents; 4.9M messages, ~300B tokens) are echoed. `blog-simonwillison-meta-muse-spark-cyberattack.md` Claims 1–2 and `blog-latentspace-ainews-muse-spark-13-frontier-lab.md` (Muse Spark 1.3 context) — this source describes the product security architecture. `blog-simonwillison-muse-agent-false-presence-claim.md` Claims 4–5 (an agent taking outbound action on its own authority before consulting the principal) is a behavior Sentinel-style approvals are designed to gate; the Batch note says sending emails always requires user verification.
- **Novel**: Detailed Muse security architecture (cell/Sentinel/credential stand-ins/out-of-band approval/accessibility-tree browsing sub-agent); Anthropic's illicit-distillation allegations and the "customer queries silently routed to Claude" fraud pattern (no prior corpus note); Proactive Memory Agent results; the Fermat's Last Theorem Lean proof by Claude (one-line mention only).

## Guide Impact

- **Security / agent-safety chapter (Ch06 per the triage; verify numbering)**: Add the Muse architecture as a worked reference for "assume injection succeeds": credential stand-ins, a gatekeeper that cannot be overridden by the model, taint-tracking egress, and approvals delivered on a channel the model cannot write to. Cite Claims 1–6, labeled "vendor-described, unevaluated" per Claim 8. Do not present it as validated.
- **Human-in-the-loop / approvals guidance**: Recommend that approval prompts be rendered outside the conversation transcript (Claim 5) and that approvals be scoped to connector + purpose + duration.
- **Context/memory guidance (harness chapter)**: A short mention that a separate reminder agent with selective (not every-step) injection improved benchmark scores (Claim 15), flagged emerging and based on a secondary summary.
- **Accountability discussion**: If the guide covers responsibility for agent actions, cite Ng's framing (Claim 9) as one position, alongside OpenAI's misalignment-pattern evidence.
- **Verification chapter**: The cheap-verification/expensive-understanding line (Claim 12) is a quotable framing.

## Extraction Notes

- The page returns a Cloudflare challenge to direct fetches; the full article text was obtained through a reader proxy and read end to end. Quotes were copied from that rendering (curly apostrophes preserved). The linked primary sources (Meta's Muse post, Anthropic's report, Buckmaster's statement, the paper) were not fetched; all claims about them are the Batch's relay.
- The Batch text contains a few internal inconsistencies/typos (e.g., "Sentinal", Claude Opus 4.5 vs 4.6 in the memory-agent Results paragraph); the note flags the one that affects numbers.
- Navier-Stokes was already covered by `blog-openai-navier-stokes-solution.md`; only the new framing is extracted here.
