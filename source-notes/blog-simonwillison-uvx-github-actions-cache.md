---
source_url: https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/
source_type: blog-post
title: "Using uvx in GitHub Actions in a cache-friendly way"
author: Simon Willison
date_published: 2026-07-14
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: anecdotal
issue: "#1953"
---

# Using uvx in GitHub Actions in a cache-friendly way

> A TIL from Simon Willison describing a GitHub Actions recipe that pins `uvx`-installed Python tool versions with `UV_EXCLUDE_NEWER` and folds that date into the Actions cache key, so `uvx tool-name` invocations reuse a cached install instead of hitting PyPI on every run.

## Source Context

- **Type**: blog-post (TIL / "today I learned", cross-posted as a short blogmark on simonwillison.net linking to the full recipe on til.simonwillison.net)
- **Author credibility**: Simon Willison is the creator of Datasette and co-creator of Django, and maintains `llm`, `sqlite-utils`, and other widely-used Python CLI tools built on `uv`/`uvx`. He runs these tools in his own GitHub Actions workflows daily, so this is a first-person account of solving his own recurring CI pain point, not secondhand reporting.
- **Scope**: Covers exactly one narrow technique — caching `uvx`-installed tools in GitHub Actions via `UV_EXCLUDE_NEWER` + `astral-sh/setup-uv`. It does not cover caching project dependencies (the `pyproject.toml`/`requirements.txt`-keyed pattern he explicitly contrasts this with), does not cover non-GitHub CI systems, and does not address AI agent behavior at all — this is CI/CD plumbing for Python tooling, not an agent or LLM pattern.

## Extracted Claims

### Claim 1: Running `uvx tool-name` in a GitHub Actions workflow normally re-downloads the tool from PyPI on every run, which Willison wanted to avoid
- **Evidence**: First-person statement of the problem motivating the post.
- **Confidence**: anecdotal
- **Quote**: "I don't want that to result in a network request to PyPI every time the workflow runs. I want the tool to be fetched the first time and then reused from the GitHub Actions cache for subsequent runs."
- **Our assessment**: Plausible and unsurprising — `uvx` by design resolves and fetches on each invocation unless a cache is already warm and the resolution is stable. This is the standard problem statement for any CI tool-caching recipe.

### Claim 2: The standard GitHub Actions caching pattern (hashing `pyproject.toml` or `requirements.txt` as the cache key) doesn't fit ad-hoc `uvx tool-name` invocations
- **Evidence**: Author's account of prior unsuccessful attempts.
- **Confidence**: anecdotal
- **Quote**: "I've tried unsuccessfully to find patterns I like for this in the past, especially given the standard pattern in GitHub Actions of using the hashed contents of a file - often `pyproject.toml` or `requirements.txt` - as a key for the cache."
- **Our assessment**: Reasonable — ad-hoc `uvx tool-name` calls (e.g., `uvx sqlite-utils --version` dropped into an arbitrary step) have no associated dependency-lock file to hash, so the file-hash cache-key pattern genuinely doesn't apply here. This is a real gap the recipe below fills.

### Claim 3: Setting `UV_EXCLUDE_NEWER` to a fixed date and using it in the Actions cache key makes `uvx` invocations reproducible and cacheable, with upgrades triggered by bumping the date
- **Evidence**: Author's own recipe, presented as the solution he now uses.
- **Confidence**: anecdotal
- **Quote**: "The trick is setting a `UV_EXCLUDE_NEWER: \"2026-07-12\"` environment variable at the start of the workflow and then using that as part of the GitHub Actions cache key."
- **Our assessment**: Sound mechanism. `UV_EXCLUDE_NEWER` (documented by Astral as equivalent to `uv`'s `--exclude-newer` flag) pins dependency resolution to "as of date X," which is exactly the kind of stable, hashable value a cache key needs — simpler than trying to hash a resolved dependency set. The tradeoff (you must remember to bump the date to get new tool releases) is inherent to the technique, not a flaw in the recipe.

### Claim 4: The env var mechanism behind the recipe is `UV_EXCLUDE_NEWER`, documented by Astral as equivalent to the `uv --exclude-newer DATE` flag
- **Evidence**: Direct link to Astral's `uv` environment-variable reference documentation.
- **Confidence**: settled
- **Quote**: "The key turned out to be the [UV_EXCLUDE_NEWER](https://docs.astral.sh/uv/reference/environment/#uv_exclude_newer) environment variable. This works the same as `uvx --exclude-newer DATE`, allowing you to tell `uv` to install the most recent package as-of a specific date."
- **Our assessment**: This is documented, first-party `uv` behavior (not a Willison invention), so it's settled as a mechanism. What's novel here is only the specific application — using it as a cache-key ingredient for ad-hoc tool invocations.

### Claim 5: The concrete recipe uses `astral-sh/setup-uv` with `enable-cache: true`, `cache-dependency-glob: ""`, and `cache-suffix` set to the `UV_EXCLUDE_NEWER` value, plus `prune-cache: false`
- **Evidence**: Full YAML workflow example (see Concrete Artifacts below).
- **Confidence**: anecdotal
- **Quote**: "`cache-dependency-glob: \"\"` disables the feature where it looks for `pyproject.toml` or similar to use as a cache key" / "`cache-suffix: \"tools-${{ env.UV_EXCLUDE_NEWER }}\"` is the bit that uses our single `UV_EXCLUDE_NEWER` value for the cache key"
- **Our assessment**: This is the load-bearing part of the recipe and is concrete enough to copy directly into a workflow. `cache-dependency-glob: ""` is the key insight for making `setup-uv`'s caching apply to ad-hoc `uvx` calls rather than project-lockfile installs, since by default the action keys its cache off dependency files that don't exist for one-off tool invocations.

### Claim 6: A separate step sets `UV_OFFLINE=1` after a cache hit, so that adding a new tool to the workflow without bumping the date produces a hard failure rather than a silent PyPI fetch
- **Evidence**: Second YAML snippet plus explanation of intent.
- **Confidence**: anecdotal
- **Quote**: "Setting that `UV_OFFLINE=1` environment variable causes `uvx tool-name` to fail if the tool has not been previously installed. We only run that if we got a cache hit from the GitHub Actions cache."
- **Our assessment**: This is the most transferable idea in the post beyond the basic cache key trick: it converts "silent cache miss falls back to network" into "loud failure that tells you to update the pinned date." That fail-fast property is generally desirable in CI reproducibility recipes and isn't specific to `uv`.

### Claim 7: Willison's own preference (favoring persisted wheel caches) runs directly against `uv`'s own documented CI guidance, which recommends *not* caching pre-built wheels in CI
- **Evidence**: Direct quote of Astral's `uv` caching-in-CI documentation, followed by the author's explicit disagreement.
- **Confidence**: anecdotal
- **Quote**: "However, in continuous integration environments, persisting pre-built wheels may be undesirable. With uv, it turns out that it's often faster to *omit* pre-built wheels from the cache (and instead re-download them from the registry on each run)."
- **Our assessment**: This is the most notable tension in the piece: the author is knowingly going against the tool vendor's own stated best practice for CI caching, trading a small amount of possible build-time regression for the reliability property of never hitting PyPI mid-workflow. Worth flagging in the guide if we ever cite general "trust the tool's official CI guidance" advice — Willison's post is a first-person counterexample of a practitioner overriding vendor guidance for a specific goal (avoiding PyPI as a runtime dependency), not a case of the vendor guidance being wrong in general.

### Claim 8: There is an open upstream issue asking `astral-sh/setup-uv` to make caching (rather than wheel-pruning) the default behavior
- **Evidence**: Direct link to a GitHub issue against `astral-sh/setup-uv`.
- **Confidence**: emerging
- **Quote**: "Here's an existing [issue](https://github.com/astral-sh/setup-uv/issues/745) against the `astral-sh/setup-uv` repository requesting that they switch the default to cache rather than purge wheels from PyPI."
- **Our assessment**: Signals this is a known, still-unresolved friction point in the `uv` ecosystem's CI tooling defaults as of publication (2026-07-14), not just something Willison personally ran into. We did not independently verify the issue's current state; treat as pointing to ecosystem context rather than a settled fact about `setup-uv`'s current defaults.

## Concrete Artifacts

Full workflow recipe (source: `til.simonwillison.net/github-actions/uvx-github-actions-cache`, linked from the blogmark):

```yaml
name: Run tools

on:
  workflow_dispatch:

env:
  # Bump this date to allow newer package releases and a fresh cache:
  UV_EXCLUDE_NEWER: "2026-07-12"

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Install uv and restore cache
        id: setup-uv
        uses: astral-sh/setup-uv@11f9893b081a58869d3b5fccaea48c9e9e46f990 # v8.3.2
        with:
          enable-cache: true
          cache-dependency-glob: ""
          cache-suffix: "tools-${{ env.UV_EXCLUDE_NEWER }}"
          prune-cache: false

      - name: Require cache-only uv on cache hits
        if: steps.setup-uv.outputs.cache-hit == 'true'
        run: echo "UV_OFFLINE=1" >> "$GITHUB_ENV"

      - name: Run sqlite-utils
        run: uvx sqlite-utils --version

      - name: Run datasette
        run: uvx --pre datasette --version

      - name: Run LLM
        run: uvx llm --version
```

Cache-hit enforcement step (isolated, as highlighted separately in the source):

```yaml
      - name: Require cache-only uv on cache hits
        if: steps.setup-uv.outputs.cache-hit == 'true'
        run: echo "UV_OFFLINE=1" >> "$GITHUB_ENV"
```

## Cross-References

- **Corroborates**: `source-notes/blog-simonwillison-agentsview-custom-model-price.md` (Claim 8: AgentsView is invoked via `uvx agentsview usage daily` / `uvx agentsview serve` — no-install `uvx` invocation), `source-notes/blog-simonwillison-sqlite-utils-40rc2.md` (Claim 10: the agent is instructed to run `uvx agentsview --help` to self-discover the tool's invocation), `source-notes/blog-simonwillison-datasette-agent.md` (Claim 8: local model deployment via `uvx` with the `llm-lmstudio` backend), and `source-notes/blog-simonwillison-shot-scraper-video.md` (author quote recommending `uvx shot-scraper video --help`) — all corroborate that Willison's own tooling ecosystem (`sqlite-utils`, `datasette`, `llm`, `agentsview`, `shot-scraper`) is consistently distributed and invoked via no-install `uvx tool-name` calls. This note is the first in our corpus to address the *CI-caching* side of that same `uvx` usage pattern rather than the interactive/local-invocation side.
- **Contradicts**: None found in our corpus. Note that the source itself contains an internal tension (Claim 7): the author's recipe runs against `uv`'s own documented CI-caching guidance. This is not a contradiction between two of our source notes, so no contradiction issue was filed per MINER.md §4a — it is a single source disagreeing with a third-party vendor doc it links to, not with our existing corpus.
- **Extends**: No existing source note specifically addresses GitHub Actions cache-key design for Python tooling; this is the first in our corpus on that topic.
- **Novel**: The `UV_EXCLUDE_NEWER`-as-cache-key technique, the `cache-dependency-glob: ""` trick for decoupling `setup-uv`'s cache from project lockfiles, and the `UV_OFFLINE=1`-on-cache-hit fail-fast pattern are all novel to our corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: This is a candidate for a small "CI/CD hygiene for agent-adjacent tooling" callout if the guide ever documents how to keep GitHub Actions workflows that invoke `uvx`-distributed CLI tools (several of which — `llm`, `agentsview`, `shot-scraper` — already appear in our corpus as part of AI-native tool stacks) fast and PyPI-independent. Recommend only a narrow, optional callout, not a dedicated section — see Extraction Notes.
- **Chapter 02 (Harness Engineering)**: Marginal relevance at best. The guide's harness-engineering content is about agent harness design (context, tools, permissions), not CI pipeline caching. Do not cite this source as harness-engineering guidance; it is CI/CD plumbing for tools an agent's environment might happen to use.
- No change recommended to existing claims in either chapter — this source doesn't contradict or supersede anything already cited.

## Extraction Notes

- Read both the short blogmark entry on `simonwillison.net` and the full linked TIL page on `til.simonwillison.net/github-actions/uvx-github-actions-cache` (one linked page, well within the 5-page follow budget); the full recipe and both YAML snippets live on the TIL page, not the blogmark.
- This issue carries three separate Prospector triage comments with conflicting novelty ratings (low / high / medium) and conflicting chapter references (some naming chapters — "Ch03 Tooling & Automation", "Ch05 Developer Workflows" — that don't correspond to any file under `guide/`, which currently has only `00-principles.md` through `06-security-threat-model.md`). This looks like the triage step ran more than once against the same issue. I did not treat any one triage comment as authoritative; I read the source directly and mapped Guide Impact to the chapters that actually exist in `guide/`.
- The source is a short, single-technique TIL, not a general pattern report — hence only 8 claims rather than the 5–15 aimed for on a longer source. All 8 are distinct, specific claims from the actual text (problem statement, prior failed approach, the core recipe, the underlying env var, the exact `setup-uv` config, the fail-fast enforcement step, the explicit disagreement with `uv`'s own CI guidance, and the open upstream issue) — there isn't more distinct claim material to extract without padding with restatements.
- Confidence is graded `anecdotal` overall: this is one practitioner's untested-at-scale recipe (no benchmark numbers, no adoption data, published the same day it was extracted), even though the underlying `UV_EXCLUDE_NEWER` mechanism it relies on is itself settled, documented `uv` behavior.
- I did not independently verify the current state of `astral-sh/setup-uv` issue #745 beyond confirming the URL resolves to that repo/issue number as linked in the source; treat Claim 8 as reporting the source's characterization of that issue, not our own verification of its current status.
