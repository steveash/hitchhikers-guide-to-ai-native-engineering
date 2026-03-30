# Manual Validation Guide

Before automating the pipeline, validate that the agent definitions produce
deep, useful output by running them manually against hand-picked sources.

## Phase 1: Validate Repo Scout Depth

### Setup
Pick 3-5 repos from the starter list (see below). For each one:

### Run the Repo Scout manually
1. Open a Claude Code session
2. Point it at `agents/REPO-SCOUT.md` as context
3. Give it one repo at a time:

```
Act as the Repo Scout agent defined in agents/REPO-SCOUT.md.
Analyze this repo: https://github.com/{owner}/{repo}

Read the CLAUDE.md, .claude/ directory, any AGENTS.md, and relevant
CI configuration. Produce a practitioner profile following the template
in source-notes/.template-practitioner.md.
```

### Evaluate the output
For each profile, check:

- [ ] **Did it find all AI config files?** Manually verify by browsing the repo.
- [ ] **Are patterns specific?** "Uses progressive disclosure" is vague.
      "Root CLAUDE.md is 23 lines, delegates Go-specific rules to
      packages/api/CLAUDE.md" is specific.
- [ ] **Are examples verbatim?** Config snippets should be copy-pasted from
      the repo, not paraphrased.
- [ ] **Is the analysis non-obvious?** Does the profile tell you something
      you wouldn't get from a 30-second glance at the repo?
- [ ] **Are cross-references attempted?** Even with few existing profiles,
      the agent should note novel patterns.
- [ ] **Is guide impact specific?** "Relevant to Ch02" fails.
      "Ch02 has no monorepo guidance; this repo demonstrates nested
      CLAUDE.md with shared test conventions" passes.

### Iterate
If profiles are shallow, adjust the Repo Scout agent definition:
- Add more specific extraction prompts
- Increase emphasis on verbatim examples
- Add negative examples ("do NOT produce output like this")

## Phase 2: Validate Miner Depth

### Setup
Pick 3-5 text sources. Good candidates:
- A substantive blog post about AI coding workflows
- A lengthy HN discussion thread with specific technical claims
- An official docs page with concrete guidance
- A "this didn't work" Reddit post with details

### Run the Miner manually
Same approach — point Claude at `agents/MINER.md` and give it one source.

### Evaluate the output
- [ ] **Claim count**: A substantive blog post should yield 5-15 specific claims.
      If you got 2-3, the Miner skimmed.
- [ ] **Evidence quality**: Are claims backed by quotes, code, or metrics?
      Or just "the author says..."?
- [ ] **Failure report depth** (if applicable): Did it extract the specific
      failure symptoms, not just "it didn't work"?
- [ ] **Cross-references**: Even early, the Miner should note when a claim
      is novel vs. something Anthropic's docs already say.

## Phase 3: Validate Assayer Rigor

### Setup
Take one good source note and one deliberately shallow one. Run the
Assayer against both.

### The Assayer should:
- **Approve** the good note (with minor nits at most)
- **Reject** the shallow note with specific, actionable feedback
- Not just say "needs more depth" — say exactly what's missing

If the Assayer approves the shallow note, its definition needs tightening.

## Phase 4: Validate Smith Synthesis

### Setup
Once you have 5-10 validated source notes, run the Smith to produce
a draft of one guide chapter.

### Evaluate
- [ ] **Every recommendation cites a source note**
- [ ] **Every recommendation has a concrete example**
- [ ] **Confidence tags are present and justified**
- [ ] **The chapter says something the source notes alone don't** — it synthesizes
- [ ] **It's prescriptive**: "Do X" not "Consider X"
- [ ] **Contradictions are surfaced**, not suppressed

## Starter Repos for Phase 1

These repos are known to have interesting AI agent configurations.
Validate the pipeline against these before turning on automation.

Curated for diversity: language, project size, domain, config sophistication.

### Tier 1: Major Production Codebases

1. **getsentry/sentry** — Python/React, 43k stars. Error tracking platform.
   THE gold standard: CLAUDE.md + AGENTS.md + agents.toml + .claude/ with
   custom commands (gh-pr, gh-review, setup-dev), plans, skills, settings.
   Shows how a large org integrates Claude into a complex Django monolith.
   https://github.com/getsentry/sentry

2. **supabase/supabase-js** — TypeScript, 4.4k stars. Official JS SDK (Nx monorepo).
   CLAUDE.md is a masterclass in monorepo guidance: describes Nx workspace
   architecture across 6 consolidated packages, links to CONTRIBUTING/TESTING/RELEASE.
   https://github.com/supabase/supabase-js

3. **liam-hq/liam** — TypeScript, 4.7k stars. Auto-generates ER diagrams.
   Full stack: CLAUDE.md + AGENTS.md + .claude/ with agents/, commands/, settings.
   Monorepo-aware instructions (pnpm filter, per-package dev/test/format).
   https://github.com/liam-hq/liam

### Tier 2: Interesting Mid-Size Projects

4. **NikolayS/postgres_dba** — PLpgSQL, 1.2k stars. Pure-SQL Postgres DBA toolkit.
   Concise, opinionated CLAUDE.md: lowercase SQL keywords, `<>` not `!=`,
   CI across PG 13-18, mandatory REV review. Proves even pure-SQL repos benefit.
   https://github.com/NikolayS/postgres_dba

5. **dadlerj/tin** — Go, 64 stars. Thread-based version control for conversational
   coding. CLAUDE.md + AGENTS.md + .claude/commands + settings. Instructs agents
   to use tin's own CLI rather than manipulating storage directly.
   https://github.com/dadlerj/tin

6. **udecode/better-convex** — TypeScript, 390 stars. Modern full-stack starter.
   Most elaborate .claude/ found: commands/, settings, skills/, scripts/,
   archived-sessions/, .claude-plugin. Shows the "skills-first" config pattern.
   https://github.com/udecode/better-convex

### Tier 3: Small Teams and Niche Domains

7. **nicholasjclark/mvgam** — R, 180 stars. Bayesian ecological forecasting.
   Rare R ecosystem adoption. CLAUDE.md + .claude/commands + settings.local.json.
   https://github.com/nicholasjclark/mvgam

8. **FrankRay78/NetPace** — C#, 10 stars. Network speed tester CLI.
   Most opinionated CLAUDE.md found: "TDD is non-negotiable" stated twice,
   full RED-GREEN-REFACTOR ASCII diagram. Solo dev using Claude as quality enforcer.
   https://github.com/FrankRay78/NetPace

9. **mikelane/pytest-test-categories** — Python, 8 stars. Pytest plugin.
   CLAUDE.md mandates: create GitHub issue before any work, all changes through
   PRs, never commit to main. Uses Claude config to enforce contribution discipline.
   https://github.com/mikelane/pytest-test-categories

10. **ClementWalter/stark-v** — Rust, 14 stars. RISC-V zkVM (zero-knowledge proofs).
    CLAUDE.md + .claude/ with cache/ and commands/. Cutting-edge crypto/blockchain.
    https://github.com/ClementWalter/stark-v

### Bonus: Organizational Patterns (study these for cross-repo insights)

- **grafana/** (docker-otel-lgtm, grafana-opentelemetry-java, oats, otel-checker) —
  Org-wide rollout across 4+ repos with consistent CLAUDE.md patterns.
  CLAUDE.md delegates to AGENTS.md (clean delegation pattern).
- **WalletConnect/skills** — Centralized Claude config repo with install.sh,
  sync.sh (bidirectional), validate.sh. Solves multi-repo config standardization.
- **trailofbits/claude-code-config** — Trail of Bits (security auditors) published
  their opinionated defaults: sandboxing, permissions, hooks, function-length limits.
  Not app code, but production-tested across real security audits. 1.7k stars.

## Iteration Cadence

| Phase | Time estimate | Goal |
|-------|--------------|------|
| Phase 1 | 2-3 repos/session | Profiles are deep, specific, useful |
| Phase 2 | 3-5 sources/session | Claims are specific, evidence-graded |
| Phase 3 | 2-3 reviews/session | Assayer catches real quality issues |
| Phase 4 | 1 chapter draft | Synthesis adds value beyond source notes |

Don't automate until all four phases produce output you'd actually want to read.
