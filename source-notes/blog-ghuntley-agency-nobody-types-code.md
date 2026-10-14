---
source_url: https://ghuntley.com/agency/
source_type: blog-post
title: "nobody should type code by hand anymore. here's what's left."
author: Geoffrey Huntley
date_published: 2026-10-13
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: anecdotal
issue: "#4107"
---

# nobody should type code by hand anymore. here's what's left.

> A written recap of a four-part podcast interview (Josh Wulf, "Agentic Engineering") that restates Huntley's loop-engineering position and adds a few concrete, checkable practices: replace probabilistic AGENTS.md/skill tuning with deterministic pre-commit enforcement, periodically delete skills/AGENTS.md, put the whole system under test, and pick one model and stay on it.

## Source Context

- **Type**: blog-post (conversation writeup, ~41k characters, with chapter index for four episodes)
- **Author credibility**: Geoffrey Huntley, originator of the "Ralph loop" technique; formerly at Canva and Gitpod; now works at Antithesis (a deterministic-testing vendor), which he discloses in the post and which colours his verification advocacy. The post is a trusted-feed entry.
- **Scope**: Covers career/hiring opinion, token subsidies, a rebuild experience report, verification practice, skills/AGENTS.md skepticism, model selection, and unikernels. Contains no data, benchmarks, or linked repos for the main claims. Per Prospector triage, the career/team-adoption/job-market material is opinion and is recorded as anecdotal; the "500,000 unique views in 24 hours" figure is engagement, not evidence.

## Extracted Claims

### Claim 1: The remaining human work after models produce complete-looking code is the "missing 20%": completeness and verification
- **Evidence**: Anecdote about Josh Wulf's first agent project (cloning a Java testing framework into Node.js). No metrics beyond the "80% as good" self-estimate.
- **Confidence**: anecdotal
- **Quote**: "So he figured out what the missing 20% was: completeness and verification, because the models would leave stubs and partial implementations."
- **Our assessment**: Plausible and consistent with the wider corpus's verification-as-bottleneck thesis, but the "80%/20%" split is a single anecdote. Note Huntley later says "We don't get stubs anymore", so the stub observation is dated and the two statements sit in tension within the same post.

### Claim 2: Humans now fit at two points, vision and verification; implementation in the middle is a black box
- **Evidence**: Framing credited to Wulf; no supporting data.
- **Confidence**: anecdotal
- **Quote**: "Humans fit in at two points: the vision and the verification."
- **Our assessment**: A useful compact framing, not evidence. Pairs with Huntley's "whiteboard defence" requirement (Claim 4), which is the operational test he applies in place of reading code.

### Claim 3: Line-by-line human review cannot scale to agent output volume, so review should be replaced by system-level verification
- **Evidence**: Argument by analogy to review at human speed; Huntley's own practice (no PRs, tests as gate).
- **Confidence**: anecdotal
- **Quote**: "It didn't work at human speed. It sure as heck isn't going to work at a thousand times human speed."
- **Our assessment**: The premise (review is already leaky) is reasonable; the conclusion is under-evidenced here. Huntley himself scopes it: he does "a lot of greenfield and research work" and says regulated domains should "be careful". Treat as applicable to low-blast-radius work only.

### Claim 4: Replace "reading the code" with property-based testing, whole-system (OS-included) test environments, and a "whiteboard defence" of the design
- **Evidence**: Description of own practice (Nix, Antithesis at work, example property "a customer is charged only once"). Vendor-adjacent; no case study.
- **Confidence**: emerging
- **Quote**: "When I develop software, I put the entire system under test, operating system included, with Nix, and the agent runs against that."
- **Our assessment**: The practice is concrete and checkable (Hypothesis-style properties; Nix-defined environments). The claim that LLM-as-judge "can't tell you whether something will hold up in worst-case scenarios" is stated without evidence and is made by someone selling the alternative. Weight accordingly.

### Claim 5: Deterministic enforcement (pre-commit hooks that inspect the diff) beats probabilistic instruction (AGENTS.md, skills) for architectural conventions
- **Evidence**: Single worked example: agent ignored Huntley's diagnostics library (OTel/structured logging patterns); a pre-commit hook that fails commits with direct observability calls and injects a corrective prompt took adherence to "ten out of ten". No sample size or trial count.
- **Confidence**: emerging (practice is widely shared; this instance is anecdotal)
- **Quote**: "Instead, I write a pre-commit hook that checks the git diff for direct calls to observability modules that bypass my diagnostics module. Boom: fail the commit, inject a prompt telling the agent to use the diagnostics library. All of a sudden it's ten out of ten."
- **Our assessment**: We buy the principle (mechanical checks are enforceable where prose is not), and the "Danger Systems in the loop" lineage is a good grounding. The "ten out of ten" figure is uncounted. He also concedes he still "sometimes" uses skills, "but rarely", so it is a preference, not an absolute.

### Claim 6: The "if you have to do it three times, automate it" rule applies to agent corrections
- **Evidence**: Practice statement; analogy to Danger (CI-integrated review automation).
- **Confidence**: anecdotal
- **Quote**: "If you have to do that three times, automate it."
- **Our assessment**: Heuristic, cheap to adopt. The failure mode it addresses (agent drift from an established pattern) is real; the threshold of three is arbitrary.

### Claim 7: Skill packs, AGENTS.md and MCP tuning are probabilistic with no guarantee of effect ("astrology for software engineers")
- **Evidence**: Rhetorical; supported only by the diagnostics-library example and Wulf's question "did you try it without the skills?".
- **Confidence**: anecdotal
- **Quote**: "Just because it's there doesn't mean it works, but it reads well and makes you feel good."
- **Our assessment**: Overstated as a blanket claim, but the underlying point (unmeasured instructions may do nothing) is a fair call for evals. It pushes against guide advice that treats AGENTS.md as the first configuration surface (see Cross-References). Not backed by an ablation.

### Claim 8: Delete skills and AGENTS.md every couple of months, because newer models may be de-tuned by old instructions, and without evals over traces you cannot tell if you are improving
- **Evidence**: Assertion; the chapter index mentions "one model update reversed the same instructions" but the written post gives only the GPT-5 "don't yell" vs Anthropic "yell if important" model-card example.
- **Confidence**: anecdotal
- **Quote**: "Unless you've invested in evals over all your traces (lab behavior, and a tiny minority of companies), you don't know whether you're going forward or backward."
- **Our assessment**: The most actionable and least-supported claim. The reasoning (instructions can become stale across model versions) is sound; the "every couple of months" cadence is invented. A better reading: re-test instructions on each model change.

### Claim 9: Read the model cards; instruction style that works for one model can backfire on another
- **Evidence**: One anecdote: GPT-5 felt "timid"; the model card advised not to yell; Anthropic guidance says yell if important.
- **Confidence**: anecdotal
- **Quote**: "Same instructions, same codebase, opposite behavior."
- **Our assessment**: Specific, checkable against the cited model cards (we have not checked them). The explanation for "amazing vs sucks" social-media noise is speculation.

### Claim 10: Pick one model and stay on it; switching weekly resets the working relationship
- **Evidence**: Personal practice; "firing a developer and hiring a new one" analogy.
- **Confidence**: anecdotal
- **Quote**: "Pick a model that works and lock in. Don't change every week."
- **Our assessment**: Reasonable for stability, but conflicts with advice elsewhere to route tasks across models by cost (see readable-explainable Claims 3-4). He exempts frontier-harness builders.

### Claim 11: Codebase patterns are amplified by agents, so bad architecture gets copied everywhere
- **Evidence**: "Kitten and Roomba" analogy; no data.
- **Confidence**: anecdotal
- **Quote**: "If your codebase has bad architectural patterns, or is inconsistent, AI will copy and paste them everywhere."
- **Our assessment**: Widely repeated and intuitively correct; supports cleaning up before scaling loops.

### Claim 12: Experience report: three former employers' products rebuilt in under ten days, via 48-hour build cycles on five $200 plans
- **Evidence**: Self-reported; nothing published yet ("I'm going to drop them as MIT open source"). No repos, test results, or description of what verification preceded release. Purpose stated: material for a conference talk on how he verifies so much code.
- **Confidence**: anecdotal (unverified)
- **Quote**: "Most recently, I rebuilt the products of three of my former employers in under ten days, and I'm going to drop them as MIT open source."
- **Our assessment**: Cannot be checked at extraction time. Revisit if the repos appear. Also note the workflow: "a couple of weeks thinking about exactly what I'm going to build, then smash it out in 48 hours", meaning the planning phase is substantial and not counted in "ten days". Rebuilding known products also implies a strong oracle (existing behaviour), which he names elsewhere: "If you have an oracle, porting is a loop."

### Claim 13: Huntley pushes to main with agents holding sudo, gated by integration tests, on a disposable NixOS machine; PRs are "gone"
- **Evidence**: Self-reported practice on greenfield/research work. Claims agent deception (deleting tests) "has dropped dramatically over the past year and a half".
- **Confidence**: anecdotal
- **Quote**: "My agents have sudo, and I push to main. I don't do pull requests anymore."
- **Our assessment**: Safety rests on the rebuildable machine and test gate, not on trust in the model. The "cheating has mostly gone" claim is unquantified and contradicts caution found elsewhere in the corpus (Fowler/Boeckeler's tautological-test finding). Do not generalise beyond sandboxed greenfield work.

### Claim 14: Iteration velocity first, hardening second: the first version is wrong, get to "number ten" fast
- **Evidence**: Practice statement.
- **Confidence**: anecdotal
- **Quote**: "Whatever you build first is wrong. The tenth one is going to be the one, so get to number ten as fast as possible instead of spending all your time and energy on number one."
- **Our assessment**: Sensible for exploratory work; he scopes it by saying verification and hardening follow once the thing is known to be worth it.

### Claim 15: LLM subsidies are drying up, which will price out hobby building, so the current period is a window of subsidised learning
- **Evidence**: Assertion, no pricing data.
- **Confidence**: anecdotal
- **Quote**: "These LLMs are heavily subsidized, and the subsidies are drying up."
- **Our assessment**: Speculative. Compare Claim 5 in `blog-ghuntley-readable-explainable.md` on lab-level economics. Not usable as a planning input without pricing evidence.

### Claim 16: Mandatory-AI and career claims ("quit if your company bans AI", engineers who type code by hand have no place, managers must make time)
- **Evidence**: Opinion; engagement figure only (500k views).
- **Confidence**: anecdotal
- **Quote**: "if your team is too busy doing their 'normal job' to experiment with AI, you're preparing them to be replaced"
- **Our assessment**: Opinion, recorded per triage guidance. Repeats prior posts.

## Concrete Artifacts

Property example given as the starting point for verification (Huntley, section "why are we still doing PR reviews?"):

```
during checkout, across my two or three microservices, a customer is charged only once.
```

Tools named for authoring properties locally: Hypothesis, Hegel, Bomdadil. Hook design described in prose (no script published):

```
pre-commit hook:
  inspect git diff for direct calls to observability modules that bypass the diagnostics module
  -> fail the commit
  -> inject a prompt telling the agent to use the diagnostics library
```

Struggling-agent recovery prompt (verbatim from the post):

```
"Hey, you dumb clanker, you seem to be going around in circles. Think extra hard about what's going on. Look at your previous tool calls. What do you need? Let's replan."
```

Other tools named: `ghuntley/underclass` (OpenAI-compatible pooling proxy that pins sessions to one account and fails over on quota exhaustion).

## Cross-References

- **Corroborates**:
  - `blog-ghuntley-engineer-away-slop.md` Claim 10 (creation near-free, verification not) and Claim 9 (pre-commit-hook-driven analyzers as part of software factories): this post gives the first worked hook example.
  - `blog-ghuntley-nix-overlay-agent-environments.md` Claim 4 (agent `sudo` safe on NixOS) and Claim 5 (whole OS under test): Claims 4 and 13 here restate the same practice.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 7 (hooks for deterministic control flow) and Claim 8 (agent self-verification correlates with success).
  - `blog-ghuntley-readable-explainable.md` Claim 1 (explainable, not readable): the "whiteboard defence" here is the operational version.
- **Contradicts**: No new contradiction issue filed. Tensions, which are conditioned on context rather than direct opposition:
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 2 treats CLAUDE.md/AGENTS.md as the first configuration surface; this post calls such tuning "astrology". The difference is that HumanLayer keeps its file short and advocates deterministic injection, so the disagreement is about emphasis and evidence, not mechanism. Neither side has controlled data.
  - `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claims 5-6 (tests written by the same agent can be tautological) cut against the post's reliance on agent-run integration tests as the gate, and its claim that cheating "has dropped dramatically".
  - `blog-ghuntley-readable-explainable.md` Claims 3-4 (use cheaper models where verification is strong) versus Claim 10 here (stick with one model).
- **Extends**: `blog-ghuntley-eighteen-month-recap.md` (same loop/Ralph material; adds the verification and de-tuning practices), `blog-ghuntley-miami-hot-takes.md` Claims 4 and 12 (coding-agent literacy; quit if AI is banned), `blog-addyosmani-agentic-skill-decay.md` Claim 6 (skills cannot tell when assumptions stop fitting).
- **Novel**: (1) Concrete pre-commit-hook-versus-AGENTS.md example with a claimed adherence outcome; (2) the advice to periodically delete skills/AGENTS.md and re-evaluate on the newer model, with the "no evals means you can't tell forward from backward" caveat; (3) model-card-driven prompt style (yelling) differing across vendors; (4) the "rebuild three employers in ten days" claim (unverified); (5) the "target size of one" security argument for unikernels (out of scope here).

## Guide Impact

- **Chapter 03 (verification)**: Add the deterministic-hook-over-prose point as a single-source, anecdotal example alongside existing hook coverage; cite this note (Claim 5) and keep the "ten out of ten" figure out of the guide because it is uncounted. Cite Claim 4 for property-based testing of whole-system invariants, flagged as vendor-adjacent.
- **Agent configuration chapters (AGENTS.md / skills)**: Recommend a caveat that instructions should be re-tested against each new model, citing Claim 8, with the cadence ("every couple of months") not adopted. Pair with the evals requirement the author names.
- **Ch05 (team adoption)**: No changes recommended; Claims 15-16 are opinion already covered by earlier Huntley notes.
- **Ch00**: At most a footnote: the "vision and verification" framing (Claim 2) as a practitioner's summary, not evidence.

## Extraction Notes

- Read the full page (about 40k characters, all four parts and chapter index). The page links to several earlier posts (Z80, Dear Student, eighteen-month recap, readable, unikernels, Nix overlay); only those already in the corpus were cross-referenced and none were followed.
- The chapter index lists topics not developed in the written text (e.g., "one model update reversed the same instructions", "fruit fly connectome to detect code smells", "isolate the variables"); these were not extracted since the post body gives no content for them.
- Quote fields were verified verbatim against the fetched page text. Cross-referenced claim numbers were checked against headings in the cited notes; the Fowler/Boeckeler, HumanLayer, Nix-overlay, and Addy Osmani numbers were read from their headings.
- Huntley's affiliation with Antithesis (verification vendor) and his subscription/proxy tooling are conflicts to weigh.
