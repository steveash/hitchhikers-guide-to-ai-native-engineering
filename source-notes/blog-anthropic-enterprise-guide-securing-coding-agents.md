---
source_url: https://claude.com/resources/articles/enterprise-guide-to-securing-coding-agents
source_type: blog-post
title: "The enterprise guide to securing coding agents"
author: Anthropic (Claude Resources; Best practices, Claude Code)
date_published: 2026-11-23
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: emerging
issue: "#4919"
---

# The enterprise guide to securing coding agents

> Anthropic's 18-minute vendor guide gives a six-question enterprise-readiness rubric, a two-layer (judgment vs. fixed-boundary) defense model, and named managed-settings knobs for locking Claude Code policy. It adds new, vendor-reported prompt-injection numbers.

## Source Context

- **Type**: blog-post (vendor guide, "Best practices" / Claude Code, ~18 min read; companion to the AI-Native SDLC Playbook)
- **Author credibility**: Published by Anthropic, the vendor of the product it secures. It quotes Jason Clinton (Deputy CISO). No individual byline is shown on the page. Controls described are first-hand product behavior, but every effectiveness figure is vendor-published or vendor-funded. The Salesforce footnote discloses "Salesforce Ventures is an investor in Anthropic."
- **Scope**: Six chapters: (1) six-question rubric and SaaS-style requirements, (2) four AI-specific risks, (3) judgment layer, (4) fixed boundaries (permission rules, Bash parsing, hooks, sandbox, cloud sessions), (5) central policy enforcement, (6) pilot checklist. It is Claude-Code-specific in its mechanisms. It does not cover other vendors' controls except in the Trajectory Labs comparison.

## Extracted Claims

### Claim 1: Enterprises can evaluate any coding agent with six questions, each with a "good" and a "weak" answer
- **Evidence**: A table (refusal; external action inspection; environment-bounded blast radius; central policy lock; secure code output; incident reconstruction). Each row has a "why care", "good answer" and "weak answer" column. Authority only, no data.
- **Confidence**: emerging
- **Quote**: "Here are six questions leaders can ask when evaluating coding agents to verify they are enterprise ready."
- **Our assessment**: Useful, checkable procurement rubric. The "weak answers" ("Our system prompt instructs the model to decline.", "The agent is instructed not to leave the working directory.") name the prompt-only-control anti-pattern. The rubric is vendor-authored, so the "good answers" describe Anthropic's own feature set (e.g. "Prompt injection probes", "audit API (Enterprise)"). The guide is also internally inconsistent: the pilot checklist says "Score the pilot against Chapter 1's five questions" although the table has six.

### Claim 2: Defense is two layers: a probabilistic judgment layer and a deterministic fixed-boundary layer
- **Evidence**: Architectural framing. Judgment layer = alignment training, prompt-injection probes, auto-mode classifier. Fixed layer = permission rules, command analysis, hooks, sandbox, egress allowlists.
- **Confidence**: emerging
- **Quote**: "The fixed boundary layer can be made deterministic and sets an agent’s blast radius."
- **Our assessment**: Consistent with the "environment first" thesis in other Anthropic notes. The guide states the limitation of each layer symmetrically: judgment controls "have the chance of being beaten", while fixed boundaries "only block what you tell them to block". Worth adopting as the guide's organizing frame.

### Claim 3: Alignment training reduces the likelihood of harm but does not bound its severity
- **Evidence**: Anthropic testing "without production safeguards": 81–85% refusal of malicious requests, 98–100% completion of dual-use/benign ones. No methodology is given on the page.
- **Confidence**: emerging
- **Quote**: "Keep in mind, model alignment training makes a bad outcome less likely, but it doesn’t limit how bad that outcome can be."
- **Our assessment**: The principle is sound and widely corroborated. The refusal rates are self-reported and a 15–19% non-refusal rate on malicious requests supports the claim that the model alone is insufficient.

### Claim 4: Gray Swan's indirect-prompt-injection benchmark scores Opus 5.5 at 1.0% and Fable 5.2 at 4.1% with probes off, at up to 15 attempts per scenario
- **Evidence**: Third-party benchmark (Gray Swan), run by or reported by Anthropic. The guide notes most successful Fable 5.2 attacks "hit requests a safety classifier had rerouted to an older model (system card)".
- **Confidence**: emerging
- **Quote**: "With prompt injection probes off, Claude Opus 5.5 scored 1.0% and Claude Fable 5.2 scored 4.1%."
- **Our assessment**: Low single-digit rates under a bounded 15-try attacker. The "rerouted to an older model" caveat matters: the headline rate depends on routing behavior, not just the model.

### Claim 5: Prompt-injection probes cut successful attacks by roughly two-thirds to four-fifths in a harder 200-try Shade benchmark
- **Evidence**: Gray Swan Shade, 40 scenarios × 200 tries, "In the November 2026 system card". Fable 5.2: 89.8% → 28.2%. Opus 5.5: 54.6% → 11.1%.
- **Confidence**: emerging
- **Quote**: "Claude Fable 5.2: probes cut successful attacks by about two-thirds, from 89.8% to 28.2%."
- **Our assessment**: Strong signal that persistent attackers beat the model alone (89.8% / 54.6%) and that the probe reduces but does not remove risk (28.2% / 11.1% residual). Anthropic-run, so treat as self-reported. Together with Claim 4 it shows success rate depends heavily on attacker budget (15 vs 200 tries), which is a reconciling variable for C-007-style comparisons.

### Claim 6: In an Anthropic-paid Trajectory Labs study, 0 of 720 injection attempts succeeded against Claude Code auto mode, versus 5.83% / 19.03% against Codex
- **Evidence**: 72 scenarios × 10 runs, agent versions as of July 17, 2026. Codex (GPT-5.6 Sol): 5.83% in its automated review mode, 19.03% in full-access mode. Explicitly "paid for by Anthropic".
- **Confidence**: anecdotal
- **Quote**: "Zero of 720 attempts succeeded against Claude Code in auto mode, across Claude Fable 5, Opus 5, and Sonnet 5."
- **Our assessment**: Sponsored comparative benchmark against a competitor; not independently replicated. Zero of 720 bounds the rate only loosely (the 95% upper bound is roughly 0.4%). The study covered "the agents themselves, not browser extensions or other product safeguards". Cite as attributed, not as a settled ranking.

### Claim 7: Auto mode is now the default because the classifier catches more dangerous commands than human approval does
- **Evidence**: Anthropic-published August 2026 controlled study: 1,053 paid testers, blind to the behavior under test, caught 13.6% of dangerous commands. Auto mode blocked 89% of the same commands.
- **Confidence**: emerging
- **Quote**: "in a controlled study Anthropic published in August 2026, 1,053 paid testers caught 13.6% of dangerous commands, and auto mode blocked 89% of the same commands."
- **Our assessment**: Extends the approval-fatigue evidence (93% of prompts approved) with a direct human-vs-classifier measurement. Paid testers in a study differ from real developers; still a useful data point. The guide still says "Auto mode relies on classification systems and does not eliminate all risk."

### Claim 8: Require human approval for actions that are both irreversible and costlier than reviewing every instance
- **Evidence**: A two-part test plus a list (production DB migrations, IAM policy changes and credential rotation, infrastructure-definition edits). No data.
- **Confidence**: emerging
- **Quote**: "is this action irreversible, and would a single mistake cost more than having a person review every instance?"
- **Our assessment**: A concrete, portable heuristic for deciding what stays outside auto mode. Not Claude-specific.

### Claim 9: Permission rules evaluate deny → ask → allow, and Bash commands are parsed so compound commands cannot slip past
- **Evidence**: Product-behavior description. Deny and ask rules apply "to each part of a command in every permission mode, including bypassPermissions". Subagents inherit the parent's rules and mode. Warns against broad allow rules such as `Bash(python:*)`.
- **Confidence**: settled (documented product behavior; verify against current docs)
- **Quote**: "Without parsing, a permission rule allowing git status would also approve git status && curl attacker.example, and wrapping a denied command in a subshell would get it past the rule."
- **Our assessment**: Good concrete failure example for why string-prefix allow rules are unsafe. The guide also admits "Command rules match what the agent types, so back them with the sandbox and egress allowlist."

### Claim 10: Hooks fail open by default, and a hook cannot approve past a deny/ask rule
- **Evidence**: Product behavior. `onFailure` set to `"block"` makes a failing or timed-out hook block the call. `allowManagedHooksOnly` stops user, project and plugin hooks. `ConfigChange` hooks can reject mid-session settings loosening.
- **Confidence**: settled (documented behavior; verify in docs)
- **Quote**: "By default, a hook that fails or times out lets the call through."
- **Our assessment**: A high-value gotcha: a security hook that crashes silently becomes no control. This is not stated in the existing hook-related notes (see Cross-References).

### Claim 11: Sandbox enforcement needs `failIfUnavailable`, or an unstartable sandbox silently leaves commands uncontained
- **Evidence**: Product behavior. Sandbox runs on macOS, Linux, WSL2, not native Windows (so with `failIfUnavailable` Claude Code won't start there). Admins can add Read deny rules for credential paths and set credential masking.
- **Confidence**: settled (documented behavior)
- **Quote**: "Without it, a sandbox that can’t start leaves commands running uncontained instead of refusing to run them."
- **Our assessment**: Same fail-open-versus-fail-closed lesson as Claim 10. Recommend fail-closed defaults for every boundary control.

### Claim 12: A domain allowlist cannot distinguish your account from an attacker's, and DNS is a second exfiltration route
- **Evidence**: Reasoned example (allow github.com → push to attacker-owned repo). Mitigations: per-agent destinations "down to the organization or path where it can", filtered and logged DNS resolver, DLP on uploads, storage restricted by role and IP. Stolen tokens bypass egress filtering entirely.
- **Confidence**: emerging
- **Quote**: "The challenge is a domain allowlist can't tell your account from an attacker's account."
- **Our assessment**: Corroborates the Files-API exfiltration incident in the containment note with a general rule. The DNS-encoding route and "token used from anywhere" point are new to the corpus. The guide admits cloud sessions' allowlist "works by domain", so finer control needs self-hosted environments.

### Claim 13: MCP servers, plugins, skills, subagent definitions and CLAUDE.md are dependencies that act on load, not on call
- **Evidence**: Argument by contrast with libraries. Mitigations: internal registry as the only reachable one, pinning with automated upgrade PRs, marketplace allowlisting, and (Enterprise) scanning of third-party skills/plugins on upload or edit.
- **Confidence**: emerging
- **Quote**: "Unlike a compromised library, which waits to be called, they reach the agent as soon as they load."
- **Our assessment**: Reframes agent configuration as supply chain. Useful for Ch06. The scanning feature is Enterprise-only and its detection quality is not reported.

### Claim 14: Agents run under the developer's identity by default, so incident response needs a separate agent identity and telemetry
- **Evidence**: Product defaults. Recommends least agency, short-lived scoped tokens, OIDC/workload identity, OpenTelemetry export, and CI use of the GitHub Action, which "runs as its own GitHub App".
- **Confidence**: emerging
- **Quote**: "By default, an agent in Claude Code runs under the identity of the developer who oversees it."
- **Our assessment**: Matches the identity-spectrum discussion in the CISO guide and the agent-identity note. Practical consequence: attribution of agent vs human actions is lost by default.

### Claim 15: Managed settings apply only from the highest-ranked source by default, silently ignoring others
- **Evidence**: Product behavior. Sources: server-managed, MDM/OS-level, managed file. `managedSourcesBehavior: "merge"` combines them. Verify with `/status`.
- **Confidence**: settled (documented behavior; verify in docs)
- **Quote**: "By default, Claude Code applies only the highest-ranked source and ignores the others, in that order, with no warning."
- **Our assessment**: A silent-misconfiguration trap (e.g. MDM turns on sandbox, file holds the allowlist, allowlist never applies). Concrete and checkable.

### Claim 16: A two-week, single-repo pilot with a frozen policy and a denial review is the recommended rollout path
- **Evidence**: A six-step checklist (tier repos, central baseline, turn on telemetry, run two weeks unchanged, review denials, score against the rubric). Advice to add allowlist entries rather than relax deny rules.
- **Confidence**: anecdotal
- **Quote**: "Run for two weeks without changing the policy, so every result traces back to one configuration."
- **Our assessment**: Sensible and cheap, but no evidence is given for the two-week duration. Tool-agnostic practice.

### Claim 17: Salesforce reported 79% more merged PRs per developer and 5% fewer incidents after standardizing on Claude Code
- **Evidence**: Single customer, no methodology, investor-disclosure footnote.
- **Confidence**: anecdotal
- **Quote**: "79%" / "more pull requests merged per developer at Salesforce"
- **Our assessment**: Marketing framing. Do not cite as an effect size. The "5% fewer total incidents" figure is notably small and unqualified.

## Concrete Artifacts

Managed-settings keys named in the guide (Chapter 5 table, attributed to the source; values not shown in the source):

```
sandbox.enabled                         # baseline: sandbox on for local sessions
failIfUnavailable                       # locked: refuse to run if sandbox can't start
allowUnsandboxedCommands: false         # locked: no unsandboxed retries
sandbox.network.allowedDomains          # baseline: managed approved sites
allowManagedDomainsOnly                 # locked: only the managed list counts
permissions.deny                        # Read deny rules for sensitive paths
permissions.blockReadsOutsideWorkingDirectories
sandbox.filesystem.denyRead
sandbox.credentials                     # credential masking
allowedMcpServers / allowManagedMcpServersOnly
allowManagedPermissionRulesOnly
allowManagedHooksOnly
permissions.disableBypassPermissionsMode
managedSourcesBehavior: "merge"         # default: only highest-ranked source applies
disableDesktopLocalSessions             # desktop-app only
hook onFailure: "block"                 # default: hook failure lets call through
```

Six-question rubric (source: Chapter 1 table, condensed): refusal trained into weights with published rates; external inspection (static analysis + separate evaluator + probes); blast radius via kernel sandbox (fail-closed) or per-session VM plus network egress allowlist; central hard-deny policy; automated security review with human approval of high-risk changes; incident reconstruction via telemetry export, audit API and named known gaps.

Pilot checklist (source: Chapter 6): tier repos → baseline policy (strict sandbox, credential deny rules, masking, egress allowlist, auto mode, default cloud environment, security-guidance plugin, hooks) → OpenTelemetry export with tool content (beta) → two weeks unchanged → review classifier denials, sandbox blocks, unsandboxed retries, refused egress → score against the rubric.

Stripe example (source, Chapter 4): agents get "a fresh one for every task"; Patrick Collison: "The boxes don’t have access to any kind of production data, or indeed production services at all".

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` Claim 3 and Claim 4 (environment containment is primary; limit blast radius independent of intent). This guide gives the same thesis as the two-layer model.
  - `blog-anthropic-how-contain-claude.md` Claim 12 (exfiltration through Anthropic's own Files API despite a domain allowlist). Claim 12 here generalizes it ("a domain allowlist can't tell your account from an attacker's account").
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 1 (make agentic risk "legible and bounded"; the same Clinton quote appears here) and Claim 3 (least agency).
  - `blog-anthropic-ai-native-sdlc-playbook.md` Claim 7 and Claim 9 (hooks as deterministic enforcement behind advisory controls; managed-settings hooks engineers cannot override).
  - `blog-anthropic-claude-code-auto-mode.md` Claim 1 (users approve 93% of prompts) and Claim 3 (the classifier does not see the agent's own reasoning). This guide adds that tool results are stripped from classifier input, and a human-vs-classifier study.
- **Contradicts**: None filed. The new Gray Swan / Trajectory Labs figures (Claims 4–6) are not a contradiction of `blog-anthropic-how-contain-claude.md` Claim 11 (24 of 25 phishing-injection successes) or of C-007. Both come from different attacker budgets, targets and agent configurations, which is a conditioning variable rather than an opposing claim. See Extraction Notes.
- **Extends**:
  - `blog-anthropic-claude-code-auto-mode.md` Claim 12 (server-side injection probe): adds quantified probe efficacy (Claim 5 here).
  - `blog-anthropic-claude-code-self-hosted-environments.md` (cited here as the way to lock network boundaries and run own proxy/DNS filtering for cloud sessions).
- **Novel**:
  - The six-question rubric with good/weak answers (Claim 1).
  - Fail-open defaults for hooks and sandbox, and silent single-source managed settings (Claims 10, 11, 15). These are checkable pitfalls.
  - DNS-encoded exfiltration and the stolen-token-bypasses-egress point (Claim 12).
  - Dependency framing for MCP/plugin/skill/CLAUDE.md as load-time attack surface (Claim 13).
  - Probe-on/off and attacker-budget numbers (Claims 4–5) and the sponsored comparative study (Claim 6).

## Guide Impact

- **Chapter 06 (Security and Threat Model)**: Add the two-layer framing (probabilistic judgment vs deterministic boundary) and the "weak answer" list (system prompt says decline, agent told not to leave the directory, honor-system policy doc) as anti-patterns. Add DNS exfiltration and "allowlisted domain, attacker's account" to the egress discussion, citing this source with `blog-anthropic-how-contain-claude.md` Claim 12.
- **Chapter 06**: In the prompt-injection section, add the Gray Swan figures with the attacker-budget conditioning (1.0%/4.1% at 15 tries with probes off vs 54.6–89.8% at 200 tries, falling to 11.1–28.2% with probes). Label all as vendor-reported. Label the Trajectory Labs 0/720 result as Anthropic-commissioned.
- **Chapter 02 (Harness Engineering)**: Add "security controls must fail closed": hooks default to fail-open (`onFailure: "block"`), sandbox needs `failIfUnavailable`, and managed settings take only the highest-ranked source unless `managedSourcesBehavior` is `"merge"`. Recommend verifying with `/status` and current docs before adopting the key names.
- **Chapter 05 (Team Adoption)**: Add the two-week frozen-policy pilot and the "add allowlist entries rather than relax deny rules" review rule as a rollout recipe, noting the evidence is practitioner guidance only.
- **Do not cite**: Salesforce 79%/5% as an effect size.

## Extraction Notes

- Fetched and read the full article HTML (rendered text, ~330 lines of body). Did not follow linked pages (companion SDLC playbook is already in the corpus as a separate note; system card and studies are referenced but not linked in the page text I extracted).
- Quotes copied from the fetched page text. Page-level images/diagrams (e.g. defense-layer diagram, cloud session anatomy) carry only captions, which were not extracted as claims.
- Setting names are as printed in the guide's table. They were not checked against current product docs, and the triage comment asks that they be verified before the guide recommends them.
- Internal inconsistency: Chapter 1 has six questions, Chapter 6 says "five questions".
- No contradiction issue filed: the nearest candidates (injection success rates across sources) differ by attacker budget and target, so they are conditioning variables rather than opposed claims.
