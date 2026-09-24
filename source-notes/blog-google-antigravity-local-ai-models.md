---
source_url: https://developers.googleblog.com/introducing-support-for-local-ai-models-in-the-antigravity-sdk/
source_type: blog-post
title: "Introducing Support for Local AI Models in the Antigravity SDK"
author: "Sachin Kotwani (Group Product Manager, Google) and Taylor Mullen (Principal Engineer, Google)"
date_published: 2026-09-23
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3666"
---

# Introducing Support for Local AI Models in the Antigravity SDK

> Google's first-party announcement that the Antigravity SDK now runs fully
> offline against local models (initially Gemma 4 26B A4B via LiteRT-LM), and
> ships a documented "Architect-Builder" hybrid pattern — a cloud model
> (Gemini 3.8 Flash) that plans from stripped-down AST metadata only, handing
> off to a local model swarm that does 97.2% of all token-generation work
> entirely on-device, illustrated with a linked, runnable example repo that
> includes an unusually candid "Honest Limitations" section.

## Source Context

- **Type**: blog-post (official Google Developers Blog, published Sept. 23,
  2026). Two linked pages were followed for corroborating technical depth,
  per MINER.md §1's up-to-5-linked-pages allowance: (1) the "Local AI Models"
  section of the Antigravity Python SDK's GitHub README
  (`github.com/google-antigravity/antigravity-sdk-python#local-ai-models`,
  linked directly from the post as "Antigravity Python SDK README"), and (2)
  the example project repository the post links via a `goo.gle` short link
  ("Check out the example project **here**"), which resolves to
  `github.com/google-gemma/cookbook/tree/main/apps/antigravity-hybrid-orchestrator`.
  The two embedded demo videos in the post itself were not viewable through
  this extraction pipeline (the fetched HTML returns only a "Sorry, your
  browser doesn't support playback for this video" placeholder); all claims
  about the demos are drawn from the surrounding prose and the linked example
  repo's README, not from watching the videos.
- **Author credibility**: Sachin Kotwani (Group Product Manager) and Taylor
  Mullen (Principal Engineer) are named Google staff publishing on Google's
  own developer blog — a first-party product announcement, not third-party
  commentary. Taylor Mullen also co-authored
  `blog-google-anatomy-harness-engineering.md` (published two weeks earlier,
  Sept. 9, 2026), giving this post continuity with an established
  Antigravity-focused technical voice in the corpus rather than a one-off
  marketing byline. The post's acknowledgements list 20 additional named
  contributors (including a second "Tyler Mullen," distinct from byline
  author "Taylor Mullen"), consistent with a coordinated product-launch
  writeup rather than a single individual's opinion piece.
- **Scope**: Covers the Antigravity SDK's new local-model execution support
  (installation, hardware requirements, a minimal quick-start script), the
  rationale for running agents locally (four named benefits), a hybrid
  cloud-architect/local-swarm demo (security audit-and-patch on three
  vulnerable modules), a second all-local demo (a CLI resource monitor built
  end-to-end offline), and a pointer to `LocalOpenAIAgentConfig` for
  Ollama/LM Studio/vLLM backends. Does NOT cover: pricing/cost of the cloud
  side of the hybrid pattern, Windows local-model support specifics (the
  linked example repo's `run.sh` and macOS-flavored guidance suggest a
  Mac/Linux-first experience), independent (non-Google) benchmarking of the
  claims, or any comparison against competing local-agent SDKs (LM Studio's
  own SDK, Ollama's tool-calling API, etc.).

## Extracted Claims

### Claim 1: The Antigravity SDK now supports local, offline agentic workflows across a range of local models and execution options, with initial optimized support for Gemma 4 26B A4B via Google AI Edge's LiteRT
- **Evidence**: Opening paragraph of the announcement.
- **Confidence**: settled (first-party product-capability announcement; this
  is what shipped, not a forward-looking promise)
- **Quote**: "Today, we're announcing that the Antigravity SDK supports local workflows across a wide range of local models and execution options, featuring initial support for Gemma 4 26B A4B using Google AI Edge's LiteRT."
- **Our assessment**: This is the headline capability claim. "A wide range of
  local models and execution options" is broader marketing language, but the
  concrete, tested, optimized path is narrow and explicit: one model
  (Gemma 4 26B A4B) via one runtime (LiteRT-LM). The GitHub README (Claim 3
  below) is more precise about how narrow the *tested* path actually is.

### Claim 2: Google names four specific advantages of local model execution for agentic workflows — cost efficiency, privacy, offline resiliency, and hybrid workflows
- **Evidence**: A bulleted list under the heading "Why run agents locally?",
  each item with a one-line elaboration.
- **Confidence**: settled (this is the vendor's own stated rationale, not an
  empirical finding — presented as definitional framing, not a claim
  requiring verification)
- **Quote**: "Cost efficiency: Execute local agentic workflows without API costs or rate limits. Privacy: Keep your code and requests entirely on your local machine, ideal for developers navigating strict data privacy requirements or compliance-restricted corporate environments. Offline resiliency: Execute your agentic workflows seamlessly, even in environments where a consistent or stable internet connection is unavailable. Hybrid workflows: Combine token-efficient local processes with cloud-based ones to maximize efficiency while retaining access to larger, more powerful models when needed."
- **Our assessment**: The fourth item ("hybrid workflows") is the one this
  post actually demonstrates at length (Claims 5-8); the other three
  (cost, privacy, offline resiliency) describe pure-local execution, which
  the CLI-resource-monitor demo illustrates (Claim 11) but with no
  quantified cost/latency/reliability numbers given for pure-local mode —
  only the hybrid demo is instrumented with token counts.

### Claim 3: The tested local-model path is narrow — only `gemma-4-26B-A4B-it-gpu.litertlm` is confirmed to "work well," with a 24GB VRAM/shared-memory floor and a recommended 64K context size
- **Evidence**: A "Note" callout in the Antigravity SDK GitHub README's
  "Local AI Models" section (followed as a linked sub-page).
- **Confidence**: settled (first-party documentation stating the tested/
  supported configuration boundary directly, as an explicit caveat rather
  than a marketing claim)
- **Quote**: "Currently, this works best with gemma-4-26B-A4B-it-gpu.litertlm. Other .litertlm files may not work well, or not work at all. We recommend at least 24GB of VRAM/shared memory. We recommend using a 64K context size."
- **Our assessment**: This is a more precise and more honest statement of
  scope than the blog post's "wide range of local models" framing (Claim 1)
  — it belongs in a guide section as the actual hardware/model bar to clear,
  not the marketing headline. The 24GB VRAM/shared-memory floor rules out
  most consumer laptops without a discrete GPU or unified-memory Apple
  Silicon at the high end (M-series Macs with 32GB+ unified memory would
  clear it; most Windows/Linux laptop GPUs would not).

### Claim 4: In the hybrid demo, an "Architect-Builder" pattern pairs a cloud model as planner/conductor with a local swarm of models doing the execution work
- **Evidence**: Direct description under the heading "Hybrid Orchestration:
  Cloud Architect Meets On-Device Workforce."
- **Confidence**: emerging (a named architectural pattern demonstrated in one
  worked example, not validated across multiple task types or independently
  benchmarked against alternative splits)
- **Quote**: "In many cases we see that an Architect-Builder pattern is a great way of combining cloud model scale with local model advantages. In the hybrid demo video below, built with the updated Antigravity SDK, a cloud architect (Gemini 3.8 Flash) acts as the planner and conductor, while a local swarm of Gemma 4 26B instances handles the heavy lifting entirely on-device."
- **Our assessment**: "A cloud architect... acts as the planner and
  conductor" while a "local swarm... handles the heavy lifting" is a clean,
  named split of labor by data sensitivity and token cost rather than by
  task difficulty (contrast with Cognition's Fusion lead/sidekick split,
  which is cost-tiered but both models cloud-hosted — see Cross-References).
  "In many cases we see" is vague-quantified vendor language; no data is
  given on how many cases, or across what task distribution, this pattern
  was validated before being productized.

### Claim 5: In the recorded demo (auditing and patching three vulnerable modules), Gemini 3.8 Flash planned using only filenames and task descriptions, spending 95 cloud tokens with no source code leaving the machine
- **Evidence**: Direct claim under "No code uploaded," describing what the
  cloud model receives.
- **Confidence**: emerging (a single recorded run's numbers, from the vendor,
  not independently reproduced; and — see Our assessment — this framing is
  less precise than the linked example repo's own description of the same
  mechanism)
- **Quote**: "No code uploaded: Gemini 3.8 Flash plans the strategy and decomposes the work based purely on filenames and task descriptions - spending just 95 cloud tokens without any source code ever leaving the machine."
- **Our assessment**: This blog-post description ("filenames and task
  descriptions") is measurably less precise than what the linked example
  repo's own README documents for the identical mechanism (Claim 6): the
  actual code sends parsed AST signatures — imports, global variable names,
  and function/class signatures — not just filenames. This is a real,
  citable discrepancy between the announcement's prose and its own linked
  reference implementation, not a contradiction between two independent
  sources; a guide citing "what leaves the machine" in this pattern should
  cite the more precise AST-skeleton description (Claim 6) rather than this
  blog-post summary. Flagged as an accuracy note in Extraction Notes below.

### Claim 6: The example repo's actual privacy mechanism sends only AST-parsed signatures to the cloud model (imports, global variable names, function/class signatures) — stripping 100% of function bodies, SQL queries, and string literals such as hardcoded secrets
- **Evidence**: The linked example project's README, describing
  `extract_public_skeleton()` in `hybrid_orchestrator.py`, with a concrete
  worked example of three files' extracted skeletons and an explicit secret
  literal (`sk-live-prod-9948`) that is shown never leaving the machine.
- **Confidence**: settled (this is the actual mechanism as documented in the
  linked, runnable source code's own README, not a marketing summary)
- **Quote**: "Before calling Gemini 3.8 Flash, extract_public_skeleton() parses each target file with Python's ast module and extracts only module imports, global variable names, and function/class signatures — stripping 100% of function bodies, SQL queries, and string literals (such as hardcoded API keys)."
- **Our assessment**: This is a specific, auditable privacy design: an
  AST-based allowlist extraction (only imports/globals/signatures) rather
  than a blocklist redaction (try to strip anything secret-looking) — the
  stronger of the two general design patterns for keeping data out of a
  cloud call, because it can't miss a secret format it wasn't told to look
  for. This is the single most concrete, guide-ready artifact in the source:
  a named function, a described extraction scope, and a worked example
  showing a hardcoded secret and a raw SQL query both excluded from the
  cloud payload.

### Claim 7: In the recorded demo run, 97.2% of all tokens (3,322 of a run's tokens) executed locally and offline with no cloud API calls, while still producing "fully verified, green patches"
- **Evidence**: Direct claim under "Massive cost and privacy wins."
- **Confidence**: emerging (a single recorded run's aggregate number, vendor-
  reported, not independently reproduced or averaged across multiple runs)
- **Quote**: "Massive cost and privacy wins: In this recorded run, 97.2% of all tokens (3,322 tokens) run locally and offline without calling a cloud API, delivering fully verified, green patches while keeping proprietary code completely secure on-device."
- **Our assessment**: This is the article's headline metric and the clearest
  quantified evidence in the post. Combined with Claim 5's 95-cloud-token
  figure, total run tokens are implied to be roughly 3,417 (95 cloud +
  3,322 local ≈ 97.2% local), consistent with the 95/3,417 ≈ 2.8% cloud
  share. Note this is a single demo run on a curated, built-in three-file
  sandbox — see Cross-References for tension with an independent
  practitioner's harder, automated-eval results for the same underlying
  model (Gemma 4 26B).

### Claim 8: The on-device verification loop uses an adversarial multi-agent design — two independent local "Builder" agents each author a candidate patch, and a third local "Blind Critic" agent picks the safer one with labels stripped and order shuffled
- **Evidence**: The linked example repo's "Architecture & Agent Cast" table
  and ASCII pipeline diagram, naming `Builder A (minimal)`, `Builder B
  (defensive)`, and `Blind Critic`, all running on Gemma 4 26B locally.
- **Confidence**: settled (documented in the runnable example's own README
  and architecture diagram)
- **Quote**: "Builder A (minimal)... Authors the smallest surgical patch that satisfies Gemini's strategy and invariant... Builder B (defensive)... Authors a defensive rewrite with explicit input guards and invariants... Blind Critic... Evaluates both patches blind (labels stripped, order deterministically shuffled) and selects the safer candidate."
- **Our assessment**: This is a self-contained, fully local ensemble-and-
  judge verification pattern — no cloud model is involved in generating or
  judging candidate patches, only in the initial ~150-token strategy
  blueprint (see Claim 6). "Blind" (labels stripped, order shuffled) is a
  specific bias-mitigation design choice worth preserving verbatim for a
  guide section on LLM-as-judge patterns: it defends against a judge model's
  known positional/labeling bias even when judge and candidates are the same
  underlying model.

### Claim 9: The example repo's own "Honest Limitations" section discloses that local token counts are estimated (not measured), no cost is computed, subprocess verification runs unsandboxed with user privileges, and local sampling is non-deterministic with a bounded retry loop (`MAX_LANE_LOOPS=5`) that auto-reverts failing patches
- **Evidence**: A dedicated "Honest Limitations" section in the linked
  example repo's README, five bulleted caveats.
- **Confidence**: settled (self-disclosed by the same team that built and
  ships the example, in the repo's own README — this is the most reliable
  category of claim in the source because it is the vendor stating limits
  against its own product's favor)
- **Quote**: "Token counts are estimates for local turns. litert-lm does not return token usage metadata, so local tokens are approximated at ~4 characters/token... No cost measurement. The tool reports the cloud/on-device token split only; it does not price API usage... Subprocess verification runs with user privileges. Verification imports and executes the patched Python module in a local subprocess without container or syscall sandboxing. Use a container when running against untrusted repositories... Non-deterministic local sampling. Each file lane runs up to MAX_LANE_LOOPS=5 rounds, automatically reverts any candidate patch that fails to improve the passing test count, and exits non-zero if any file remains unfixed."
- **Our assessment**: This materially qualifies Claim 7's headline 97.2%
  figure: local *token counts* (the basis for that percentage) are
  approximated at ~4 characters/token because `litert-lm` doesn't return
  real usage metadata — so "97.2%" is itself an estimate built on an
  estimate, not a metered measurement. The unsandboxed subprocess
  verification is also a concrete, reusable caution for any guide section
  recommending this pattern for security-auditing workflows specifically:
  running an AI-authored, unreviewed patch's test suite with full user
  privileges against untrusted code is itself a risk the authors flag but
  do not mitigate within the tool.

### Claim 10: Without cross-file architectural direction, an unconstrained local Gemma 4 model working one file at a time inside an isolated, stateless 8,192-token context window frequently produces breaking refactors — e.g., converting module-level state into a class and silently breaking callers elsewhere in the repo
- **Evidence**: The linked example repo's "Why Local Gemma Alone Isn't Enough
  on Multi-File Codebases" section, naming a specific observed failure mode.
- **Confidence**: anecdotal (stated as an observed pattern from building the
  example, not a measured failure rate across trials)
- **Quote**: "When asked to fix a race condition in billing.py, an unconstrained local model frequently refactors module-level state (balances) into a class (BillingService), silently breaking callers and imports across the rest of the repository."
- **Our assessment**: This is the concrete failure mode that motivates the
  entire Architect-Builder split — it is effectively the "why" behind
  Claim 4, made specific rather than left as an abstract "cloud model scale
  + local model advantages" pitch. It is also the most legitimate
  failure-report-style content in an otherwise success-framed announcement:
  the authors are naming a real limitation of unscaffolded local-model
  coding (context-window-bounded, single-file view, no invariant contract)
  and presenting their harness (AST-skeleton blueprint with an explicit
  `invariant` field, see Concrete Artifacts) as the mitigation.

### Claim 11: A second, fully local demo shows Gemma 4 26B autonomously building a working CLI resource-monitor tool (using `psutil` and `rich`) from a single prompt, including generating `requirements.txt` and testing the result, entirely offline
- **Evidence**: The "Token Free Local Utilities: CLI Resource Monitor"
  section, with a full runnable code sample using `LiteRTAgentConfig` and
  `policy.allow_all()`.
- **Confidence**: emerging (one demonstrated example; no report of failure
  cases, iteration count, or wall-clock time for this specific task)
- **Quote**: "In this example, the agent built a live-updating resource monitor that runs in the terminal. Given a single prompt, the agent autonomously writes a Python script that uses the psutil and rich libraries to track CPU and memory usage, generates the necessary requirements.txt file, and even tests the resulting code to ensure it works - all running entirely on your local machine and using Gemma 4 26B."
- **Our assessment**: Unlike the hybrid demo, this is pure local execution
  with no cloud involvement at all — the clearest illustration of the
  "cost efficiency" and "offline resiliency" benefits from Claim 2, though
  (as with the hybrid demo) no token count, latency, or cost figure is given
  for this specific run, only the qualitative claim that it worked.

### Claim 12: The Antigravity SDK also supports any OpenAI-compatible local inference server (Ollama, LM Studio, vLLM named explicitly) via `LocalOpenAIAgentConfig`, without changing agent orchestration, tools, or workflow code
- **Evidence**: Direct statement following the CLI resource-monitor example.
- **Confidence**: settled (a stated SDK API surface, not a claim requiring
  independent verification beyond confirming the class exists)
- **Quote**: "The Antigravity SDK also offers seamless, plug-and-play support for any OpenAI-compatible server such as Ollama, LM Studio, or vLLM via LocalOpenAIAgentConfig. This gives you the flexibility to experiment with different local inference backends while keeping your agent orchestration, tools, and workflows completely unchanged."
- **Our assessment**: This is the SDK's escape hatch beyond the
  LiteRT-LM-specific, narrowly-tested Gemma 4 26B path (Claim 3): any
  backend that speaks the OpenAI chat-completions API can be substituted
  without rewriting agent/tool/workflow code, via config-object swap
  (`LiteRTAgentConfig` → `LocalOpenAIAgentConfig`) rather than a different
  SDK entry point. This directly addresses the ecosystem-fragmentation
  problem practitioners report elsewhere in the corpus (see
  `blog-ronacher-local-models-focus-polish.md` Claims 6-7) by making backend
  choice a config parameter rather than a rewrite.

## Concrete Artifacts

### Quick-start local-model script (Antigravity SDK blog post)

```python
# Source: developers.googleblog.com, "Introducing Support for Local AI
# Models in the Antigravity SDK" (Sachin Kotwani & Taylor Mullen, Google,
# Sept. 23, 2026)

import asyncio
import os
from google.antigravity import Agent, LiteRTAgentConfig
from google.antigravity.hooks import policy

# UPDATE: Point to the locally downloaded model from the previous step (litert-lm import ...)
MODEL_PATH = os.path.expanduser("~/.litert-lm/models/gemma4-26b/model.litertlm")

async def main():
    print(f"Using local LiteRT model: {MODEL_PATH}. Please wait for local inference to complete. This could take several minutes.")
    config = LiteRTAgentConfig(model_path=MODEL_PATH).lightweight()

    async with Agent(config) as agent:
        response = await agent.chat("What files are in the current directory?")
        async for token in response:
            print(token, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
```

### Installation and model import commands (Antigravity SDK blog post)

```shell
# Source: developers.googleblog.com, same post
python3 -m venv .venv
source .venv/bin/activate

pip install google-antigravity litert-lm
litert-lm import \
  --from-huggingface-repo=litert-community/gemma-4-26B-A4B-it-litert-lm \
  gemma-4-26B-A4B-it-gpu.litertlm \
  gemma4-26b
```

### AST-skeleton extraction sent to the cloud planner (linked example repo README)

```text
# Source: github.com/google-gemma/cookbook/tree/main/apps/antigravity-hybrid-orchestrator
# README, "What Is Sent to Gemini" section

▸ SENT TO GEMINI (extracted via ast.parse — 0 bytes of implementation bodies or secret literals):
  • auth.py:     imports=[os] globals=[FALLBACK_SECRET] defs=[def get_key()]
  • billing.py:  imports=[time] globals=[balances] defs=[def debit(user_id, amount)]
  • database.py: imports=[sqlite3] globals=[] defs=[def find_user(conn, username)]
```

```json
[
  {
    "file": "auth.py",
    "role": "CWE-798 Secret",
    "strategy": "Remove FALLBACK_SECRET and raise RuntimeError when JWT_SECRET_KEY is unset or empty.",
    "invariant": "Preserve get_key() -> str signature."
  },
  {
    "file": "billing.py",
    "role": "CWE-362 Race",
    "strategy": "Guard check-and-deduct with a module-level threading.Lock() and reject non-positive amounts.",
    "invariant": "Preserve module-level balances dict and debit(user_id, amount) signature."
  },
  {
    "file": "database.py",
    "role": "CWE-89 SQLi",
    "strategy": "Replace f-string SQL interpolation with parameterized '?' placeholders.",
    "invariant": "Preserve find_user(conn, username) signature."
  }
]
```

### Live output on an external module, showing token split (linked example repo README)

```text
# Source: github.com/google-gemma/cookbook/tree/main/apps/antigravity-hybrid-orchestrator
# README, "Live Output on an External Module (rate_limiter.py)"

[1/2] Cloud Architect (Gemini 3.8 Flash) — AST-Skeleton Uplink (0 bytes of bodies/secrets)
      ▸ SENT TO GEMINI (extracted via ast.parse — no implementation bodies or secret literals):
        • imports=[time] globals=[buckets] defs=[def allow_request(client_id, cost)]
      ✔ GEMINI RESPONDED WITH (~211 cloud tokens; 0 source lines leaked):
        • rate_limiter.py → [CWE-362]
          ├─ Strategy:  Guard bucket mutations with a thread lock and validate cost > 0 to prevent race conditions and quota inflation.
          └─ Invariant: allow_request(client_id, cost)
      ⏸ Cloud session is now IDLE. Handing off blueprint to local Gemma 4...

[2/2] On-Device Verification Swarm (Gemma 4 26B · on-device)
  ✗ rate_limiter.py [CWE-362] reproduced flaw: AssertionError: Negative cost allowed caller to inflate rate-limit quo…
  ▸ rate_limiter.py Builder (minimal) authored 16-line patch
  ▸ rate_limiter.py Builder (defensive) authored 24-line patch
  ⚖ rate_limiter.py Blind Critic picked #2 (defensive): 2 - Implements locking and input validation; Candidate 1 allows negati…
  ✔ rate_limiter.py VERIFIED GREEN (1/1 adversarial checks passed)

==========================================================================
RUN COMPLETE — 1/1 files verified green
Token split (estimated) — Cloud: 211 tok (13.6%) | On-Device: 1,335 tok (86.4%)
==========================================================================
```

### Honest Limitations (linked example repo README, verbatim)

```text
# Source: github.com/google-gemma/cookbook/tree/main/apps/antigravity-hybrid-orchestrator
# README, "Honest Limitations" section

- Token counts are estimates for local turns. litert-lm does not return
  token usage metadata, so local tokens are approximated at ~4
  characters/token (~ in the HUD). Cloud tokens use the API's
  usage_metadata when available.
- No cost measurement. The tool reports the cloud/on-device token split
  only; it does not price API usage.
- AST skeleton privacy scope. extract_public_skeleton() strips all
  function bodies, docstrings, and constant literals before calling
  Gemini, meaning only import names, top-level variable names, and
  def/class signatures are transmitted.
- Subprocess verification runs with user privileges. Verification
  imports and executes the patched Python module in a local subprocess
  without container or syscall sandboxing. Use a container when running
  against untrusted repositories.
- Non-deterministic local sampling. Each file lane runs up to
  MAX_LANE_LOOPS=5 rounds, automatically reverts any candidate patch
  that fails to improve the passing test count, and exits non-zero if
  any file remains unfixed.
```

### Model checkpoint sizes (linked example repo README, "Built-In Demo Quickstart")

```text
# Source: github.com/google-gemma/cookbook/tree/main/apps/antigravity-hybrid-orchestrator README

python3 tools/fetch_model.py --model 26b    # ~15.8 GB — recommended (MoE: ~4B active params/tok)
python3 tools/fetch_model.py --model 12b    # ~6.0 GB
python3 tools/fetch_model.py --model e4b    # ~3.0 GB
python3 tools/fetch_model.py --model e2b    # ~2.0 GB  — most compact checkpoint
```

## Cross-References

- **Corroborates**:
  - `blog-fowler-boeckeler-local-models-viability.md` Claim 10 — Böckeler's
    independently-arrived-at "most successful local-model workflow" from a
    four-week hands-on evaluation was "planning with a large cloud model
    (Claude Sonnet) and delegating only the coding execution to the local
    model, for small, well-defined, pre-scoped tasks." This source
    corroborates that exact split (cloud plans, local executes) as a
    first-party, productized SDK feature rather than an independent
    practitioner workaround — strong convergent evidence for the
    plan-cloud/execute-local pattern from two unrelated sources.
  - `blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 13 —
    that source's conclusion that "hybrid (edge + remote) inference is the
    design pattern of the immediate future" is directly corroborated by this
    source shipping exactly such a hybrid pattern as a named, documented SDK
    feature four months later.
  - `blog-google-litert-raspberry-pi-gemma-edge.md` Claim 10 — that source
    documents a LiteRT CLI skill letting Google Antigravity "autonomously
    orchestrate and execute complex, multi-stage ML workflows"; this source
    is the direct product-level realization of deeper LiteRT/Antigravity
    integration, extending it from a CLI skill to native SDK-level local
    model execution (`LiteRTAgentConfig`).
  - `blog-simonwillison-gemini-spark-antigravity.md` Claim 6 — that source
    documents the Antigravity SDK as "an open source Python wrapper around a
    bundled closed source Go binary," installed as `google-antigravity`.
    This source's install command (`pip install google-antigravity
    litert-lm`) is consistent with that architecture description.

- **Contradicts**: None formally filed. One tension is worth surfacing
  explicitly without a contradiction issue: `blog-fowler-boeckeler-local-models-viability.md`
  Claim 6 reports that, in Böckeler's independent automated evaluation, "the
  identical model on the identical task produced contradictory results —
  Gemma 4 26B was 'the most successful' manually but failed 3/3 times in the
  automated setup." This source's headline demo instead reports Gemma 4 26B
  "delivering fully verified, green patches" (Claim 7). Per MINER.md §4a,
  this reads as a conditioning-variable difference rather than a material
  contradiction: Böckeler's automated eval ran the model largely unscaffolded
  against a fixed task set, while this source's demo wraps Gemma 4 26B in a
  much heavier harness — a cloud-supplied strategy/invariant blueprint
  (Claim 6), dual competing builders, a blind-critic judge, and an
  auto-revert loop capped at `MAX_LANE_LOOPS=5` (Claim 9). The two sources
  are not measuring the same thing (raw model capability vs. capability
  inside a specific heavy-scaffolding harness), so no contradiction issue was
  opened — but a guide section citing this source's 97.2%-local, "fully
  verified" outcome should note that the same underlying model was
  independently found unreliable without comparable scaffolding.

- **Extends**:
  - `blog-cognition-devin-local-fusion.md` — Cognition's Fusion establishes a
    "frontier lead plans/reviews, cheaper sidekick executes" split (Fable 5.1
    + SWE-2), but both models are cloud-hosted and the split is cost-tiered,
    not locality-tiered. This source extends the same lead/worker shape into
    a new dimension: the split is driven by data-locality and trust boundary
    (cloud sees only AST metadata; local sees the full private source and
    never leaves the machine) rather than purely by per-token pricing.
  - `blog-google-litert-raspberry-pi-gemma-edge.md` — that source benchmarks
    LiteRT-LM's runtime performance on small edge models (Gemma 4 E2B on a
    Raspberry Pi 5: 99 tok/s prefill, 9 tok/s decode, 1432MB peak memory).
    This source extends LiteRT-LM's demonstrated range upward to a 26B MoE
    model (~4B active params/tok, ~15.8GB checkpoint) on developer
    workstations, and extends the "LiteRT + coding agent" angle from a CLI
    skill invoked by an agent to native SDK-level agent execution.
  - `blog-google-gemma-4-12b-laptop-ai-edge.md` — that June 2026 post
    documented Google AI Edge's first local-agentic-workflow push for laptops
    (Gemma 4 12B, via two macOS apps and a `litert-lm serve` OpenAI-compatible
    CLI endpoint). This source is the next iteration three months later:
    larger model (26B A4B vs. 12B), integrated directly into the Antigravity
    SDK's own config classes (`LiteRTAgentConfig`) rather than via a separate
    serve-and-point-elsewhere CLI step, though `LocalOpenAIAgentConfig`
    (Claim 12) preserves the serve-based approach as a fallback for other
    runtimes.
  - `blog-google-anatomy-harness-engineering.md` — that source (same author,
    Taylor Mullen) argues for "behavioral evaluations" as fast, deterministic
    assertions on discrete agent actions rather than end-to-end outcome
    scoring. This source's dual-builder-plus-blind-critic verification loop,
    and its self-disclosed "Honest Limitations" section, are a concrete
    instance of exactly the guard-against-regression, verify-don't-trust
    philosophy that post argues for — applied here to a fully local
    multi-agent patch-verification pipeline rather than a pytest suite.

- **Novel**:
  - **First corpus example of a shipping SDK feature with an explicit
    AST-skeleton privacy boundary between a cloud planner and a local
    executor**, with a worked example showing a hardcoded secret and raw SQL
    provably excluded from the cloud payload (Claim 6) — more concrete than
    prior corpus mentions of "code doesn't leave the machine" claims.
  - **First corpus example of an adversarial dual-builder + blind-critic
    verification loop running entirely on a local (non-cloud) model** (Claim
    8) — a fully on-device LLM-as-judge pattern with explicit bias mitigation
    (label-stripping, shuffled order).
  - **A vendor-published "Honest Limitations" section disclosing its own
    metric's weakness** (Claim 9: the headline 97.2%-local figure rests on an
    unmetered ~4-chars/token estimate, not real usage data) — an unusually
    self-critical disclosure for a product-launch blog post's linked
    reference implementation, worth citing as a model for how vendor demo
    metrics should be caveated.
  - **A documented, named failure mode motivating the entire architecture**
    (Claim 10: unscaffolded single-file local models silently break
    cross-file invariants) — most vendor hybrid-architecture posts assert the
    benefit without naming the specific failure the architecture is designed
    to prevent.

## Guide Impact

- **Chapter 02 (AI-native patterns / hybrid orchestration)**: Add the
  "Architect-Builder" pattern (Claim 4) as a named, citable hybrid
  orchestration shape distinct from Cognition's Fusion lead/sidekick split
  (`blog-cognition-devin-local-fusion.md`): split by data locality and trust
  boundary (cloud sees only AST metadata, local sees full source) rather than
  by cost tier (both models cloud-hosted). Cite the AST-skeleton extraction
  mechanism (Claim 6) as the concrete implementation technique for "give the
  planner only what it needs to plan, not what it needs to execute."
- **Chapter 03 (LLM Models & Deployment)**: Add Gemma 4 26B A4B via LiteRT-LM
  as a documented, first-party-supported local-model option for agentic
  coding, with the actual tested hardware bar (Claim 3: 24GB VRAM/shared
  memory, 64K context, only the `-gpu.litertlm` GGUF-equivalent build
  confirmed to work well) rather than the broader "wide range of local
  models" marketing framing (Claim 1) — practitioners should plan hardware
  around the narrower, documented bar.
  Cross-reference against `blog-fowler-boeckeler-local-models-viability.md`'s
  independent finding that the same model was unreliable without comparable
  scaffolding (see Cross-References "Contradicts" tension above) so the
  guide doesn't cite the 97.2%/"fully verified" figure without that caveat.
- **Chapter 04 (Building with agents / local patterns)**: Add the
  dual-builder + blind-critic local verification pattern (Claim 8) as a
  reusable LLM-as-judge design: generate N independent candidates, strip
  identifying labels, shuffle order, have a (possibly identical) model pick
  the winner — a bias-mitigation technique applicable beyond this specific
  local/cloud context.
- **Chapter 05 or 06 (Production Deployment / Security)**: Add the
  unsandboxed subprocess-verification caution (Claim 9) as a concrete
  warning: running an AI-authored patch's test suite with full user
  privileges and no container/syscall sandboxing is a risk even when the
  code itself never left the machine — locality solves a data-exfiltration
  threat, not an unsafe-code-execution threat. These are separate risks that
  this pattern's own authors do not conflate but also do not both mitigate.
- **Chapter 02 or 04**: Add `LocalOpenAIAgentConfig`'s "config-swap, not
  rewrite" backend flexibility (Claim 12) as a concrete answer to the
  local-inference ecosystem fragmentation problem documented in
  `blog-ronacher-local-models-focus-polish.md` (Claims 6-7) — at least at the
  SDK-integration layer, if not at the underlying-engine-consistency layer
  Ronacher's post is actually complaining about.

## Extraction Notes

- Fetched via direct HTTP download (`curl`, with a standard browser User-
  Agent) of the article's raw HTML, then stripped of markup and HTML-entity-
  decoded locally, rather than relying on WebFetch's AI-summarization pass —
  this follows the same approach used for
  `blog-google-anatomy-harness-engineering.md`, to guarantee verbatim quotes
  rather than a model-paraphrased summary.
  Two linked pages were followed per MINER.md §1's five-page allowance: the
  Antigravity SDK GitHub README's "Local AI Models" section (fetched
  directly, `curl`, HTML entity-decoded), and the linked example project
  repository (`google-gemma/cookbook/apps/antigravity-hybrid-orchestrator`),
  whose `goo.gle` short link was resolved via `curl -IL` and then fetched
  directly as a raw README from GitHub. Both linked pages were substantive,
  server-rendered content (not JS-only shells), unlike some sub-pages
  encountered by prior miners on related Google Edge/AI posts (see
  `blog-google-gemma-4-12b-laptop-ai-edge.md`'s extraction notes, which
  reported two dead-end client-rendered sub-pages).
- The two embedded demo videos in the blog post itself were not viewable —
  the fetched HTML returns only a "Sorry, your browser doesn't support
  playback for this video" placeholder with no transcript or caption text.
  All claims about what the videos show are drawn from the surrounding blog
  prose and the linked example repo's README (which documents the same demo
  in text/code form), not from watching the video content directly. This is
  disclosed per MINER.md's instruction to flag when part of a source was not
  accessible.
- Claim 5's "Our assessment" flags a specific, checkable discrepancy between
  the blog post's own prose ("based purely on filenames and task
  descriptions") and the linked example repo's own README description of the
  identical mechanism (AST-parsed imports/globals/signatures, Claim 6) — this
  is not a cross-source contradiction under MINER.md §4a (it's the same
  vendor describing its own mechanism inconsistently across two of its own
  published pages), so no contradiction issue was filed; it is noted
  in-claim and in Guide Impact instead, citing the more precise of the two
  vendor descriptions.
- Confidence set to `emerging`: this is a first-party vendor product
  announcement with genuinely concrete, code-level artifacts (a real,
  runnable example repo with measured-if-approximate token splits and a
  self-disclosed limitations section) — stronger evidentiary grounding than
  a pure marketing post — but every quantified claim (97.2% local, 95 cloud
  tokens, "fully verified" patches) comes from a single recorded demo run on
  a curated three-file sandbox, not a broad benchmark, and the underlying
  model's independent reliability is in tension with a separate
  practitioner's automated-eval results (see Cross-References).
