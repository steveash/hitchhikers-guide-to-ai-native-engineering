---
source_url: https://claude.dev/blog/claude-code-in-the-cloud/
source_type: blog-post
title: "Claude Code in the cloud: a field guide to cloud sessions"
author: Addy Osmani
date_published: 2026-10-06
date_extracted: 2026-10-10
last_checked: 2026-10-10
status: current
confidence_overall: emerging
issue: "#4035"
---

# Claude Code in the cloud: a field guide to cloud sessions

> Vendor tutorial with four worked cloud-session examples that documents the per-task VM isolation model, the proxy-held GitHub credential, the file-boundary rule for parallel sessions, and the "give the session a way to prove its work" pattern.

## Source Context

- **Type**: blog-post (claude.dev, Anthropic-hosted; vendor product tutorial)
- **Author credibility**: Addy Osmani, a well-known engineering writer (see also `blog-addyosmani-code-agent-orchestra.md`). The post is hosted on Anthropic's claude.dev, so product statements are vendor claims.
- **Scope**: Covers Claude Code cloud sessions: isolation, GitHub connection, environment setup, network levels, local-vs-cloud choice, seven workflows. It does not cover cost beyond "included in plan", and it does not compare cloud sessions with other vendors.

## Extracted Claims

### Claim 1: Each cloud task gets a fresh VM and branch, so parallel sessions cannot touch each other's files or ports
- **Evidence**: Worked example of three sessions on one repository (flaky test, docs, logging change) running in parallel, finishing within 87 seconds of the first start.
- **Confidence**: emerging
- **Quote**: "A fresh VM with your repository cloned onto a new branch, so sessions can't touch each other's files or ports."
- **Our assessment**: Plausible and consistent with VM-level isolation arguments elsewhere. It is a vendor description with a small demo and no failure-rate data.

### Claim 2: Isolated parallel sessions can still rediscover or report a bug another session is already fixing
- **Evidence**: In the worked example, the logging session reran the cache test eight times, saw five failures, and traced them to the race the first session was fixing. It proposed the same fix, left the cache alone, and reported the suite as not clean.
- **Confidence**: anecdotal
- **Quote**: "Claude reran the cache test eight times, saw it fail in five of them, and traced the failure to the same race the first session was fixing."
- **Our assessment**: Useful, honest evidence that isolation does not remove coordination cost. The session behaved well (stayed in scope, reported honestly). One example only.

### Claim 3: Parallel work should be split along file boundaries and merged in a deliberate order
- **Evidence**: Advice following the collision example. No measurements.
- **Confidence**: emerging
- **Quote**: "Split parallel tasks along file boundaries, merge the branches in a sensible order, and expect a session to report problems that another session is already fixing."
- **Our assessment**: Sound and matches common worktree-based parallelism advice. Not tested against alternatives.

### Claim 4: Small, separate, single-task sessions are easier to review and cheaper to discard
- **Evidence**: Authority/advice, backed by the three-session example.
- **Confidence**: emerging
- **Quote**: "Small, separate sessions are easier to review and cheaper to throw away."
- **Our assessment**: Reasonable heuristic; aligns with WIP-limit advice in `blog-addyosmani-code-agent-orchestra.md`.

### Claim 5: Give a session a way to check its own work (run tests, start the server, curl endpoints)
- **Evidence**: Two examples. One had the session run `npm test` 40 times in a row with zero failures to verify a flaky-test fix. The other had it start the server and run every curl example while rewriting docs/API.md.
- **Confidence**: emerging
- **Quote**: "A session that can run your tests checks its own work before it hands the work back."
- **Our assessment**: Strong practical pattern (proof by repetition). The 40 runs is one example, not a statistically derived number: 40 clean runs only bounds a flake rate, it does not prove its absence.

### Claim 6: Repeated verification inside one command is cheap against plan limits, but each turn counts
- **Evidence**: Vendor statement about plan accounting. No numbers.
- **Confidence**: anecdotal (vendor claim)
- **Quote**: "Each of Claude's turns still counts toward your plan, but a long test run inside one command costs little."
- **Our assessment**: Vendor claim about pricing. Treat as unverified until checked against Anthropic's usage docs. The practical corollary (batch the loop in one command, not many turns) is sound either way.

### Claim 7: Parallel sessions consume plan limits proportionally faster
- **Evidence**: Vendor statement.
- **Confidence**: anecdotal (vendor claim)
- **Quote**: "Parallel sessions draw on your plan limits in parallel, so five sessions use them about five times as fast as one."
- **Our assessment**: Straightforward and credible; a useful counterweight to the "cloud is free" framing.

### Claim 8: Cloud sessions have no extra compute charge and are included in Pro/Max/Team/Enterprise
- **Evidence**: Vendor pricing statement.
- **Confidence**: anecdotal (vendor claim)
- **Quote**: "Cloud sessions come with your Pro, Max, Team, or Enterprise plan at no additional cost: there's no separate charge for the cloud machine, and sessions draw on the same usage limits as the rest of Claude Code."
- **Our assessment**: Vendor claim that can change; do not put it in the guide as fact without a date and docs citation.

### Claim 9: GitHub credentials never enter the VM; a proxy holds the token and issues a short-lived, branch-scoped credential
- **Evidence**: Architectural description. Not independently verified here.
- **Confidence**: emerging
- **Quote**: "A proxy holds it, and the session gets a short-lived credential that can push only to its own working branch."
- **Our assessment**: Good design (limits blast radius of prompt injection). Compare with the scoped/proxied git remote access at Cursor. Verify against Anthropic's cloud environments docs before citing in Ch06.

### Claim 10: Even at network level None, data can leave the VM via the Anthropic API
- **Evidence**: Caveat stated in the security section.
- **Confidence**: emerging
- **Quote**: "Even at None, Claude Code still sends requests to the Anthropic API, so data can leave the VM that way, and the session can still push to its own branch."
- **Our assessment**: Important honest limit: "no network" is not "no egress". Matters for the threat model in Ch06. Also noted: "All outbound traffic passes through a proxy that logs hostnames."

### Claim 11: Untrusted code (unknown PRs, install scripts) is safer in a disposable cloud VM than on a laptop
- **Evidence**: Argument by comparison of what is reachable from each environment.
- **Confidence**: emerging
- **Quote**: "In a cloud session it runs in a disposable VM with none of those, a session-scoped GitHub credential, and a network you can narrow."
- **Our assessment**: Sensible. The residual risk is repo content and anything the session can push to its own branch.

### Claim 12: Personal `~/.claude` config does not travel; team-needed config must live in the repository
- **Evidence**: Product behavior description.
- **Confidence**: emerging
- **Quote**: "User-level config doesn't travel, so move what the team needs into the repository"
- **Our assessment**: Reinforces repo-level harness (CLAUDE.md, skills, commands, hooks) as the portable layer. Useful for Ch02.

### Claim 13: Environment setup is cached; setup scripts must exit 0 and finish in about five minutes, and dependency installs belong in a SessionStart hook
- **Evidence**: Product documentation-style guidance. Setup overhead in the examples: "Recreating the repository took roughly a third to just over half of each run."
- **Confidence**: emerging
- **Quote**: "It must exit 0 or the session won't start, and it should finish within about five minutes so the environment gets cached."
- **Our assessment**: Concrete operational constraints, plus a measured setup tax that matters for short tasks.

### Claim 14: Idle VMs are reclaimed, so work must be committed regularly
- **Evidence**: Product behavior.
- **Confidence**: emerging
- **Quote**: "Reopen the session and you get a fresh VM with the conversation restored, so commit work you care about."
- **Our assessment**: A real failure mode: conversation state survives but uncommitted files do not. Compare to the unpushed-work-loss limitation in `blog-anthropic-claude-code-self-hosted-environments.md` Claim 12.

### Claim 15: Stay local when the task needs something only your machine has
- **Evidence**: Decision guidance.
- **Confidence**: emerging
- **Quote**: "Stay local when the task needs something only your machine has."
- **Our assessment**: Simple rule. Listed local cases: local data database, VPN-only service, GPU, phone simulator, desk hardware.

## Concrete Artifacts

```shell
# Commands shown in claude.dev/blog/claude-code-in-the-cloud (Addy Osmani, 2026-10-06)
claude --cloud "Fix the flaky test in auth.spec.ts"
claude --permission-mode plan
claude --teleport <session-id>
claude -p "rebase on main and push" --cloud <session-id>
```

```shell
# Self-check prompt from the article
claude --cloud "docs/API.md is out of date with src/server.js. Rewrite it so every endpoint, parameter, default and response shape matches the code. Start the server and run each curl example to check it."
```

Measurements reported in the article: three parallel sessions done "87 seconds after the first one started"; `npm test` run 40 times with zero failures; cache test rerun 8 times, failing 5; setup overhead of roughly a third to just over half of each run.

Seven workflows listed: parallel backlog; repeated proof; plan locally then build then finish; phone check-ins; CI/review automation; routines (research preview); untrusted code. Network levels: None, Trusted, Custom, Full.

## Cross-References

- **Corroborates**: `blog-cognition-what-we-learned-building-cloud-agents.md` Claim 3 (VM-level isolation over shared-kernel containers). `blog-cursor-cloud-agent-environment-operations.md` Claim 3 (egress restrictions and proxied/scoped git remote access). `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits of 3-5 agents) and Claim 5 (verification is the bottleneck).
- **Contradicts**: none found. The "Even at None" egress caveat does not contradict the others; it only qualifies them.
- **Extends**: `blog-anthropic-claude-code-self-hosted-environments.md` (Claim 6 on data going to Anthropic for inference, Claim 12 on lost unpushed work): this post covers the Anthropic-hosted side of the same model. `blog-anthropic-claude-code-routines.md` Claim 7 (plan-based quotas): same shared usage pool.
- **Novel**: The parallel-session collision example (shared bug rediscovered across isolated sessions) and the file-boundary rule; the explicit statement that `None` network still permits the Anthropic API; the measured setup overhead share; the GitHub sign-in vs App vs `/web-setup` distinction.

## Guide Impact

- **Chapter 01**: Add cloud sessions to the parallel-work section: one task per session, split by file boundaries, commit often, and the local-vs-cloud rule (Claims 3, 4, 14, 15).
- **Chapter 02**: Note that only repo-level config travels to cloud sessions, so CLAUDE.md, skills, and SessionStart hooks are the portable harness (Claims 12, 13).
- **Chapter 03**: Add the "self-check" pattern with repeated runs, with the caveat that N clean runs bound but do not eliminate flakiness (Claim 5).
- **Chapter 05**: Mention plan-limit consumption scaling with parallelism (Claim 7); pricing claims remain vendor-sourced.
- **Chapter 06**: Add the proxy-held credential model (Claim 9) and the "None still reaches the Anthropic API" caveat (Claim 10), after verifying against Anthropic docs.

## Extraction Notes

- The page was read through a fetch tool that summarizes pages, so quotes were obtained by asking for exact sentences in three passes. Each quote is short and contiguous. The Assayer should spot-check them against the live URL.
- The post links to code.claude.com docs; these were not followed, so the security and pricing claims are unverified against docs.
- The triage comment asked that pricing and plan-inclusion claims be marked as vendor claims; they are (Claims 6-8).
