---
source_url: https://latent.space/p/offline-coding/
source_type: blog-post
title: "Coding From the Himalayas With an Offline AI Agent"
author: Rittika Jindal
date_published: 2026-10-27
date_extracted: 2026-11-09
last_checked: 2026-11-09
status: current
confidence_overall: anecdotal
issue: "#4607"
---

# Coding From the Himalayas With an Offline AI Agent

> A practitioner walkthrough of a fully offline coding agent (OpenCode + Ollama + Qwen3.5 9B) with concrete config, Ollama env flags and a "prepare online, verify with network off" procedure, but demonstrated on only one toy bug fix.

## Source Context

- **Type**: blog-post (Latent Space guest tutorial / experience report; ~9 min read; published Oct 27, 2026; companion GitHub repo holds the full `opencode.json`, examples and tests, not read here)
- **Author credibility**: Rittika Jindal, Principal Engineer at Thomson Reuters, who says coding agents "are already a big part of my everyday workflow". Single practitioner; motivation is unreliable network/power in the Himalayan foothills. No controlled study.
- **Scope**: Covers the setup, the network-off verification checks, one offline bug-fix run, and practical lessons. Does NOT cover: large repos, unfamiliar frameworks, the CSV-report and log-analyzer exercises (author says not yet run offline), measured local speed/latency, or the Qwen3.5 9B quality on this setup beyond one task.

## Extracted Claims

### Claim 1: A coding agent can read, edit and test code on a laptop with the network off, when model, dependencies and test tools are all local
- **Evidence**: One recorded run: a one-line fix to a toy expense calculator (3 of 5 unit tests failing before; all 5 passing after) done with Wi-Fi off, with the author re-running tests herself afterwards.
- **Confidence**: anecdotal (n=1, toy task)
- **Quote**: "These tasks can run offline when the model, project dependencies and test tools are available locally."
- **Our assessment**: Credible as an existence proof, and the dependency caveat is the useful part. The article gives no evidence on realistic repos; the author concedes this herself (Claim 10).

### Claim 2: Pinning both model roles to a localhost provider in project config, with web tools blocked and permission prompts on, is the harness-level mechanism for the offline setup
- **Evidence**: Description of `opencode.json`; full file lives in the companion repo and is not reproduced in the article.
- **Confidence**: anecdotal
- **Quote**: "In our file, model and small_model both select Qwen3.5 9B, and baseURL points to Ollama at http://127.0.0.1:11434/v1. Only the local provider is enabled. It also asks before editing files or running shell commands, and blocks the web tools."
- **Our assessment**: Useful: the `small_model` (helper) role must also be pinned locally, otherwise some requests could leave the machine. Config is described, not shown, so we cannot confirm key names beyond `model`, `small_model` and `baseURL`.

### Claim 3: Ollama can be hardened for local-only use with three env flags
- **Evidence**: Verbatim command in the article.
- **Confidence**: anecdotal (author's own working command; not independently verified by us)
- **Quote**: "OLLAMA_HOST=127.0.0.1:11434 OLLAMA_NO_CLOUD=1 OLLAMA_CONTEXT_LENGTH=65536 ollama serve"
- **Our assessment**: Concrete and reproducible. Note `OLLAMA_CONTEXT_LENGTH=65536` is set at server level (the default context is much smaller), matching the 64K finding in the Fowler/Böckeler note.

### Claim 4: "Offline" should be verified, not assumed: confirm the local API answers and an external lookup fails, then keep the network off during the run
- **Evidence**: Two `curl` commands with captured outputs (local API lists `qwen3.5:9b`; external fails with "Could not resolve host").
- **Confidence**: anecdotal
- **Quote**: "These checks establish what happened at the time of capture: the local service responded and the external lookup failed."
- **Our assessment**: A good, cheap procedure. The author is appropriately modest: it is a point-in-time check, and the config alone does not make the run offline ("We still disconnect the network for the offline test").

### Claim 5: Prepare while online and launch the exact setup once before going offline
- **Evidence**: Procedure in "What helps when the internet is unavailable"; the project uses only Python stdlib so tests need no package downloads.
- **Confidence**: anecdotal
- **Quote**: "Launch the exact setup once while online. Use the same command, model and configuration for the offline attempt, so that required runtime components are already available."
- **Our assessment**: Sensible and low-cost. Also says to "Download its dependencies and keep the documentation you will need on disk", the part most likely to bite on real projects with package managers.

### Claim 6: Give the agent the exact test command; a small model otherwise guesses the wrong test runner
- **Evidence**: Observed failure: the agent proposed pytest for a unittest-based project.
- **Confidence**: anecdotal (one observation)
- **Quote**: "It initially proposed pytest, although this project uses Python's built-in unittest."
- **Our assessment**: Matches the general guidance of encoding build/test commands in agent instructions, and is arguably more important for small local models. The fix is a prompt-level one; the author's task prompt does not include the command in the demonstrated run, only in the advice.

### Claim 7: Keep original tests unchanged and verify the result independently of the agent
- **Evidence**: Prompt said "Don't change the tests or install anything"; author exited OpenCode and re-ran `python3 -m unittest -v`; test file unchanged from starter.
- **Confidence**: anecdotal
- **Quote**: "Keep the original tests so that a passing result still checks the intended behavior."
- **Our assessment**: Standard verification discipline, but made explicit as a guard against agents "fixing" tests. Reinforces human-in-the-loop checking with a weak local model.

### Claim 8: A model's download size is not its memory requirement; a 64k context raises memory needs
- **Evidence**: Table of download sizes (Qwen3.5 4B 3.3–4.0 GB; 9B 6.6–7.6 GB; 27B 17–20 GB); a cited third-party budget (Voltti) of 12–16 GB for the 9B build. No measurement on the author's laptop.
- **Confidence**: emerging (consistent with other sources, but the figure is second-hand)
- **Quote**: "Download size isn't a RAM requirement."
- **Our assessment**: Directionally right and corroborated by Fowler/Böckeler. The specific 12–16 GB figure is borrowed and unverified; the author does not report her own RAM usage.

### Claim 9: Model selection rests on vendor-reported benchmarks, not measurements from this setup
- **Evidence**: Table from Qwen's model card: LiveCodeBench v6 / BFCL-V4: Qwen3.5 4B 55.8 / 50.3; 9B 65.6 / 66.1; gpt-oss-20b 74.6 / not reported.
- **Confidence**: anecdotal (vendor-reported; author labels it so)
- **Quote**: "The above table scores reported in Qwen's model card, not measurements from this laptop."
- **Our assessment**: Do not cite these numbers as evidence of offline agent performance. The author's rationale (stronger tool-calling score than the 4B) is a reasonable heuristic only.

### Claim 10: One toy fix does not show the setup handles large repos or unfamiliar frameworks; further exercises are untested
- **Evidence**: Author's explicit limitations; CSV-report and log-analyzer exercises are published but not yet run offline.
- **Confidence**: settled (as a statement of what was and was not tested)
- **Quote**: "This one-line fix doesn't tell me how well the model would handle a large repository or an unfamiliar framework."
- **Our assessment**: Honest and important. Anything beyond "a small local fix works" is unsupported by this source.

### Claim 11: Agent scaffold token usage differs sharply, but those results come from cloud models and do not transfer
- **Evidence**: Cites preprint "The Scaffold Effect in Coding Agents" (50 Terminal-Bench Pro tasks, two cloud models; pass rates Goose 48%/38%, OpenCode 50%/46%, OpenHands-SDK 50%/46%, with overlapping 95% CIs) and about 40× Goose's tokens per solved task for OpenCode. We did not read the preprint.
- **Confidence**: emerging (second-hand citation of a preprint)
- **Quote**: "The authors caution that most differences in pass rate were not statistically clear."
- **Our assessment**: Pass-rate differences are not significant per the author. The token-cost gap is potentially important for local setups where context is scarce, but the source itself says it does not predict local Qwen3.5 9B behavior.

### Claim 12: Small, self-contained tasks are the right starting point when offline; record failed attempts too
- **Evidence**: Author's recommendation based on the one run.
- **Confidence**: anecdotal
- **Quote**: "I'd start with small, self-contained tasks when using this setup during an outage or a journey."
- **Our assessment**: Consistent with Fowler/Böckeler's finding that task choice dominates local-model viability (their Claim 9).

## Concrete Artifacts

Attributed to Jindal, latent.space/p/offline-coding (Oct 27, 2026).

Ollama server (Terminal B):
```
OLLAMA_HOST=127.0.0.1:11434 OLLAMA_NO_CLOUD=1 OLLAMA_CONTEXT_LENGTH=65536 ollama serve
ollama pull qwen3.5:9b
```

Offline verification:
```
curl --noproxy '*' --fail http://127.0.0.1:11434/api/tags
curl --noproxy '*' --connect-timeout 5 --max-time 10 --head https://example.com
```
(second command is expected to fail with "Could not resolve host")

Launching the agent without external plugins (OpenCode 1.19.4):
```
.tools/node_modules/.bin/opencode --pure
```

Task prompt used for the offline fix:
```
Fix the bug in expense_total.py so the existing tests pass. Don't change the tests or install anything. Run the tests and explain your fix.
```

The recorded one-line fix:
```
total = Decimal(amount)   # before
total += Decimal(amount)  # after
```

Diagnostic prompt used online: "Read expense_total.py and run the tests. Explain the bug without editing any files."

Project config described but not shown: `opencode.json` with `model` and `small_model` set to Qwen3.5 9B, `baseURL` `http://127.0.0.1:11434/v1`, only the local provider enabled, ask-before-edit/shell permissions, web tools blocked (full file is in the companion repo).

## Cross-References

- **Corroborates**: `blog-fowler-boeckeler-local-models-viability.md` Claim 8 (default context far too small; 64K a more reliable default, stretching RAM) and Claim 9 (task choice is the biggest factor in local-model viability); `blog-google-antigravity-local-ai-models.md` Claim 3 (recommended 64K context) and Claim 12 (OpenAI-compatible local servers such as Ollama).
- **Contradicts**: None found. Fowler/Böckeler Claim 12 judges local models "still not ready for a simple 'plug and play' experience"; this source's success is on a much easier task, so they differ in scope rather than conflict. No contradiction issue filed.
- **Extends**: `blog-jetbrains-air-acp-local-models.md` Claim 5 (local model via Ollama with an ACP agent such as OpenCode) by adding a concrete config and an offline verification procedure; `blog-ronacher-local-models-focus-polish.md` Claim 1 (local setup requires many configuration decisions) by showing one worked configuration.
- **Novel**: The "prepare online, then verify with network off" procedure; pinning both `model` and `small_model` to the local provider; `OLLAMA_NO_CLOUD=1`; the explicit offline-readiness checklist (dependencies and docs on disk).

## Guide Impact

- **Chapter 01 (daily workflows)**: Add an "offline/degraded-network" subsection: a minimal local setup (OpenCode + Ollama + a ~9B model), the prepare-online checklist, and a clear caveat that the evidence is one toy fix. Pair with Fowler/Böckeler for realistic expectations.
- **Chapter 02 (harness engineering)**: Example of project-level agent config pinning all model roles to a local provider with web tools blocked and approval prompts for edits and shell.
- **Chapter 04 (context engineering)**: Reinforce that local runtimes need context length set explicitly (64K here) and that this costs RAM beyond the download size.
- **Chapter 06 (security)**: Optional note on verifying no-network execution (local API answers, external lookup fails) and `OLLAMA_NO_CLOUD=1`; do not present as a sandbox since the check is point-in-time.

## Extraction Notes

- Fetched the full article HTML with curl and read all sections, including tables and code blocks. The companion GitHub repo (full `opencode.json`, README) was not followed, so the config file contents are unverified.
- The cited preprint (The Scaffold Effect in Coding Agents) and Voltti memory budget were not independently read.
- Triage caveats applied: only one offline run (toy task); benchmark table is vendor-reported; scaffold results are cloud-only.
