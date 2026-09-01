---
source_url: https://simonwillison.net/2026/Aug/24/llm-anthropic/
source_type: blog-post
title: "llm-anthropic 0.27"
author: Simon Willison
date_published: 2026-08-24
date_extracted: 2026-09-01
last_checked: 2026-09-01
status: current
confidence_overall: emerging
issue: "#3137"
---

# llm-anthropic 0.27

> A ~60-word first-party release announcement documenting a compatibility-only
> update to the `llm-anthropic` plugin (anthropic Python SDK v1.0.0's
> httpx→httpx2 migration), whose real evidentiary value is the linked,
> independently-verifiable artifact trail: a single prompt to Fable 5 in
> Claude Code, a merged GitHub PR completed in under 7 minutes, and a diff
> that maps precisely onto Anthropic's own migration guide.

## Source Context

- **Type**: blog-post (first-party release announcement; "beat" entry of
  ~60 words plus a blockquoted prompt, published at
  `simonwillison.net/2026/Aug/24/llm-anthropic/`). The post links out to
  three artifacts that this note also extracted: Anthropic's `MIGRATION.md`
  guide (`github.com/anthropics/anthropic-sdk-python/blob/v1.0.0/MIGRATION.md`),
  the resulting merged pull request (`github.com/simonw/llm-anthropic/pull/84`),
  and (unfetched — a private, non-public Claude Code session transcript URL)
  `claude.ai/code/session_01G3SA94Qx13c42KV1YiNejF`, referenced only as a
  transparency artifact.
- **Author credibility**: Simon Willison is the creator and maintainer of the
  `llm` Python CLI/library and the `llm-anthropic` plugin. This is first-party
  release documentation from the person who authored the change (the PR is
  opened and merged by his own GitHub account, `simonw`). No vendor
  affiliation with Anthropic.
- **Scope**: Covers the `llm-anthropic` 0.27 release (a compatibility update
  for `anthropic>=1`) and the specific AI-driven workflow used to produce it.
  Also covers, via linked pages fetched per the MINER rubric: (1) the
  `anthropic-sdk-python` v1.0.0 `MIGRATION.md` guide's "httpx2" and "removed
  deprecated request parameters" sections, which explain *why* the PR's code
  change was necessary, and (2) the GitHub PR #84 diff and metadata (files
  changed, additions/deletions, timestamps, PR description). Also fetched the
  `llm-anthropic` 0.27 GitHub release notes (not linked from the blog post
  itself, but the canonical enumeration of everything shipped in the
  release) to check whether 0.27 shipped anything beyond the httpx2
  compatibility fix. Does NOT cover: the full `MIGRATION.md` guide beyond the
  two sections relevant to this PR (e.g., Bedrock region requirements,
  `.with_raw_response` changes — irrelevant to `llm-anthropic`'s usage), the
  OpenAI v3.0.0 release the post references but does not link to, or the
  contents of the linked Claude Code session transcript (URL requires
  authentication; not fetched).

## Extracted Claims

### Claim 1: llm-anthropic 0.27 is framed by its author as a compatibility-only release for the anthropic Python SDK's v1.0.0 httpx→httpx2 migration
- **Evidence**: Opening sentence of the release note, first-party.
- **Confidence**: settled
- **Quote**: "This release of the Anthropic plugin for LLM mainly provides compatibility with the recently released anthropic v1.0.0 Python library, which switches from httpx to httpx2."
- **Our assessment**: Consistent with the GitHub release notes (Concrete Artifacts, below), whose first line item is "Upgraded to `anthropic>=1`. #84" — the httpx2 compatibility fix is presented as the release's lead change, though the release notes show it shipped alongside five unrelated bug fixes and feature additions (Claim 8).

### Claim 2: The author states OpenAI made the equivalent httpx-layer change in their own SDK's v3.0.0 release two weeks before this post
- **Evidence**: Direct statement in the same opening sentence, offered without a supporting link or independent citation.
- **Confidence**: anecdotal (single-source, uncorroborated claim about a different vendor's SDK; this Miner did not independently verify the OpenAI v3.0.0 release)
- **Quote**: "OpenAI made the same change in their v3.0.0 release two weeks ago."
- **Our assessment**: If accurate, this indicates the httpx→httpx2 transition (see Claim 9) is an ecosystem-wide, not Anthropic-specific, dependency shift affecting any Python SDK built on `httpx`. Practitioners maintaining wrappers around both the OpenAI and Anthropic Python SDKs should expect to face the same `httpx2` migration on both dependencies within a similar window. This claim is not independently corroborated elsewhere in our corpus and should be treated as a single-source data point pending confirmation.

### Claim 3: Willison drove the SDK migration by giving Fable 5 in Claude Code a single-sentence prompt naming the target version constraint, a link to Anthropic's migration guide, and a pass/fail success criterion (tests passing) — with no manual code edits described
- **Evidence**: Verbatim blockquoted prompt in the release post, immediately followed by a link to the resulting merged PR. This is the complete instruction as given; the post does not describe any follow-up prompts, corrections, or manual intervention.
- **Confidence**: settled (the prompt text and resulting PR are both directly, verifiably first-party)
- **Quote**: "Upgrade to anthropic>=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing"
- **Our assessment**: This is a minimal, three-part prompt structure worth naming explicitly: (1) a version constraint as the goal, (2) a canonical raw-URL link to the authoritative migration reference rather than relying on the model's training data, (3) an objective, checkable success criterion ("tests passing") rather than a subjective one. The PR diff (Concrete Artifacts, below) shows the resulting change tracks the migration guide's specific "Removed: deprecated request parameters" guidance (Claim 6) almost verbatim in approach — strong evidence the model actually followed the linked document rather than pattern-matching from stale training knowledge of `httpx`/`anthropic` APIs.

### Claim 4: The resulting pull request was opened and merged by the same author on the same day, with wall-clock time from PR creation to merge of approximately 7 minutes
- **Evidence**: GitHub API metadata for PR #84: `created_at: "2026-08-24T14:19:33Z"`, `merged_at: "2026-08-24T14:26:27Z"`. Fetched directly via `gh api repos/simonw/llm-anthropic/pulls/84`, not from the blog post itself (the post links to the PR but does not state timing).
- **Confidence**: settled (directly observed GitHub API data, not a claim made in the source prose)
- **Quote**: (no direct quote; see paraphrase in Our assessment — this claim is derived from GitHub API timestamp fields, not source prose)
- **Our assessment**: A ~7-minute PR lifecycle (open → merge, same author, single commit, no review comments) indicates Willison read and accepted the AI-generated diff essentially as-is, with the review consisting of reading a 2-file, 20-insertion/6-deletion diff rather than an extended iteration cycle. This is a small, low-risk, single-purpose migration — the fast turnaround should not be generalized to larger or higher-stakes migrations (contrast with `blog-anthropic-code-migration-playbook.md`'s six-step process for larger migrations, under Cross-References → Extends).

### Claim 5: The actual code change moved `temperature`, `top_p`, and `top_k` from direct keyword arguments into an `extra_body` dict, because `anthropic>=1` removed these three parameters from the SDK's generated method signatures
- **Evidence**: PR #84 diff (`llm_anthropic.py`), fetched via `gh api repos/simonw/llm-anthropic/pulls/84/files`. The PR's own description states the same mechanism. Independently corroborated by `MIGRATION.md`'s "Removed: deprecated request parameters" table, which names exactly these three parameters as removed from `messages.create()` and states they must be "passed through `extra_body`" — the guide the model was told to read.
- **Confidence**: settled (verified directly against the diff, the PR description, and the independent migration-guide text — three consistent first-party sources)
- **Quote**: "Migrated `temperature`, `top_p`, and `top_k` parameters from direct `kwargs` to `extra_body` dict to comply with anthropic>=1 API changes" (PR #84 description, attributed there as "Fable 5 PR" summary)
- **Our assessment**: This is a case where the fix and the reason for the fix can both be checked independently of the author's framing: `MIGRATION.md`'s "Removed: deprecated request parameters" table (Concrete Artifacts, below) states the *general* rule ("Current models do not use these sampling parameters... pass them through `extra_body`"), and the PR diff shows the model applying that general rule correctly to `llm-anthropic`'s specific call site, including a `kwargs.setdefault("extra_body", {})["thinking"] = ...` edit to avoid clobbering an existing `extra_body` value already set for the `thinking` parameter elsewhere in the same function. The setdefault correction indicates the model tracked a second, unrelated `extra_body` usage already present in the file and adjusted for it, rather than doing a naive parameter rename.

### Claim 6: Anthropic's own migration guide explicitly names Claude Code as the recommended tool for performing this class of upgrade, via a specific slash command
- **Evidence**: Direct instruction in `MIGRATION.md`'s "Upgrading" section, immediately following the `pip install --upgrade "anthropic>=1,<2"` command.
- **Confidence**: settled (directly quoted from Anthropic's own first-party migration documentation)
- **Quote**: "If you use Claude Code, the fastest route through the rest of this guide is to let it do the edits: run `/claude-api upgrade python` in your project and review the diff."
- **Our assessment**: This is a first-party, prescriptive statement from Anthropic (not from Willison) that a specific Claude Code slash command exists and is the recommended path for this exact migration — a stronger and more general claim than Willison's ad hoc single-sentence prompt (Claim 3), which did not use this slash command and instead hand-wrote an equivalent instruction. The guide frames "review the diff" as the human's remaining responsibility, matching the PR-review-not-manual-editing pattern in Claim 4. Practitioners upgrading `anthropic` themselves (not through `llm-anthropic`) have a first-party, packaged alternative to Willison's manual prompt.

### Claim 7: The migration guide recommends running a type checker after the upgrade specifically because it will surface nearly all breaking changes as errors, even for teams that don't normally type-check
- **Evidence**: Direct statement in `MIGRATION.md`'s "Upgrading" section, immediately after the Claude Code slash-command recommendation.
- **Confidence**: settled (first-party documentation)
- **Quote**: "A type checker (`pyright` / `mypy`) will flag almost everything below as an error after upgrading, which makes it a good checklist even if you don't normally run one."
- **Our assessment**: This is a reusable pattern for migration-guide authorship generally, not specific to this SDK: a breaking-change guide that is largely composed of type-signature changes can be paired with a type checker to give both a human and an AI coding agent an automatically-generated, complete checklist of call sites needing attention — reducing reliance on the guide's prose being read exhaustively. This complements Claim 3's prompt structure ("get the tests passing" as the success criterion) — a type checker plus a test suite together give an AI agent two independent, automatable verification signals for a mechanical migration, without the human needing to manually enumerate affected call sites.

### Claim 8: Beyond the httpx2 compatibility fix, llm-anthropic 0.27 also shipped five unrelated bug fixes and feature additions not mentioned in the blog post
- **Evidence**: GitHub release notes for tag `0.27`, fetched via `gh api repos/simonw/llm-anthropic/releases/tags/0.27`. Not linked from or mentioned in the blog post itself, which only discusses the httpx2 compatibility item.
- **Confidence**: settled (directly fetched first-party release notes, independent of the blog post's framing)
- **Quote**: "Fixed a `TypeError` when `temperature=None` was passed explicitly, and fixed a validation bug where setting only `top_p` incorrectly raised \"Only one of temperature and top_p can be set\". #70 - thanks Charlie Tonneslan" (GitHub release notes, tag 0.27)
- **Our assessment**: The blog post's "mainly provides compatibility" framing (Claim 1) is accurate but incomplete as a full changelog — the release also fixes two `temperature`/`top_p` validation bugs (credited to an external contributor, Charlie Tonneslan), adds structured-outputs support for Claude Haiku 4.5, adds mid-conversation system-message support for Opus 4.8 and the Claude 5 family, and preserves `redacted_thinking` blocks across tool continuations. Practitioners relying solely on the blog post (rather than the full release notes) would miss these five changes. This is a general lesson about Willison's release-announcement format: the "beat" post highlights the single most structurally significant change, not a complete changelog — consistent with the same pattern already noted for the 0.25.1 and 0.26 announcements in this corpus (see Cross-References → Extends).

### Claim 9: `httpx2` is described by Anthropic as an API-compatible fork of `httpx` maintained by the Pydantic team, created because the original `httpx` library is no longer actively maintained
- **Evidence**: Direct statement in `MIGRATION.md`'s "The SDK is built on `httpx2`" section.
- **Confidence**: settled (first-party documentation from the SDK vendor; the claim about `httpx`'s maintenance status is presented as fact, not independently verified by this Miner against the `httpx` project itself)
- **Quote**: "The SDK's HTTP layer moved from `httpx`, which is no longer actively maintained, to [`httpx2`](https://github.com/pydantic/httpx2) - an API-compatible fork maintained by the Pydantic team. `httpx2` is a drop-in continuation of `httpx`, with the same classes, same behaviour, and security fixes included."
- **Our assessment**: This is the root cause explaining both this release and, per Claim 2, the near-simultaneous OpenAI SDK change — if `httpx` genuinely lost active maintenance, any Python SDK vendor depending on it faces the same forced migration on a similar timeline, independent of any coordination between Anthropic and OpenAI. This also explains why the migration guide provides an `httpx2.alias_httpx()` escape hatch for applications and tracing/instrumentation libraries that still import `httpx` directly — a detail out of scope for `llm-anthropic`'s own fix (Claim 5) since the plugin does not construct custom HTTP clients or transports.

## Concrete Artifacts

### Full text of the release note (verbatim, simonwillison.net/2026/Aug/24/llm-anthropic/)
```
This release of the Anthropic plugin for LLM mainly provides compatibility
with the recently released anthropic v1.0.0 Python library, which switches
from httpx to httpx2. OpenAI made the same change in their v3.0.0 release
two weeks ago.

Anthropic provide this migration guide for upgrading to 1.0, so I prompted
Fable 5 in Claude Code with:

> Upgrade to anthropic>=1 - read
> https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md
> and get the tests passing

Here's the resulting PR.
```
*Source: simonwillison.net/2026/Aug/24/llm-anthropic/, posted 24th August 2026 at 4:27 pm*

### PR #84 diff — `llm_anthropic.py` (verbatim, github.com/simonw/llm-anthropic/pull/84)
```diff
+        # anthropic>=1 removed temperature/top_p/top_k from the method
+        # signatures; the API still accepts them, so send via extra_body
+        extra_body = {}
         if prompt.options.top_p:
-            kwargs["top_p"] = prompt.options.top_p
+            extra_body["top_p"] = prompt.options.top_p
         else:
-            kwargs["temperature"] = (
+            extra_body["temperature"] = (
                 prompt.options.temperature
                 if prompt.options.temperature is not None
                 else DEFAULT_TEMPERATURE
             )

         if prompt.options.top_k:
-            kwargs["top_k"] = prompt.options.top_k
+            extra_body["top_k"] = prompt.options.top_k
+
+        if extra_body:
+            kwargs["extra_body"] = extra_body
...
         if max_tokens > 64000 and not self.supports_adaptive_thinking:
             betas.append("output-128k-2025-02-19")
             if "thinking" in kwargs:
-                kwargs["extra_body"] = {"thinking": kwargs.pop("thinking")}
+                kwargs.setdefault("extra_body", {})["thinking"] = kwargs.pop("thinking")
```
*Source: `gh api repos/simonw/llm-anthropic/pulls/84/files`, file `llm_anthropic.py`*

### PR #84 diff — `pyproject.toml` (verbatim)
```diff
 dependencies = [
     "llm>=0.32",
-    "anthropic>=0.96.0",
+    "anthropic>=1,<2",
 ]
...
-dev = ["pytest", "pytest-recording", "pytest-asyncio", "cogapp", "inline-snapshot[black]"]
+dev = [
+    "pytest",
+    "pytest-recording",
+    # vcrpy 8.3+ can record/replay httpx2, used by anthropic>=1
+    "vcrpy>=8.3",
+    "pytest-asyncio",
+    "cogapp",
+    "inline-snapshot[black]",
+]
```
*Source: `gh api repos/simonw/llm-anthropic/pulls/84/files`, file `pyproject.toml`*

### PR #84 description (verbatim, github.com/simonw/llm-anthropic/pull/84)
```
> Upgrade to anthropic>=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing

Fable 5 PR:

## Summary
Updates the Anthropic API integration to support anthropic>=1, which removed
temperature, top_p, and top_k from method signatures. These parameters are
now passed via the extra_body parameter instead.

## Key Changes
- Migrated temperature, top_p, and top_k parameters from direct kwargs to
  extra_body dict to comply with anthropic>=1 API changes
- Updated extra_body handling for the thinking parameter to use setdefault()
  to avoid overwriting existing extra_body values
- Updated dependency constraint from anthropic>=0.96.0 to anthropic>=1,<2
- Added vcrpy>=8.3 to dev dependencies to support recording/replaying
  httpx2 requests used by anthropic>=1

## Implementation Details
- Parameters are collected in an extra_body dict and only added to kwargs
  if non-empty
- The thinking parameter handling was refactored to safely merge with any
  existing extra_body dict using setdefault()
- This maintains backward compatibility with the API while adapting to the
  new SDK structure

https://claude.ai/code/session_01G3SA94Qx13c42KV1YiNejF
```
*Source: `gh api repos/simonw/llm-anthropic/pulls/84`, PR body field. PR metadata: title "Support anthropic>=1 by using extra_body for model parameters", author simonw, 1 commit, 2 files changed, +20/-6, created 2026-08-24T14:19:33Z, merged 2026-08-24T14:26:27Z, no review comments.*

### llm-anthropic 0.27 GitHub release notes (verbatim, github.com/simonw/llm-anthropic/releases/tag/0.27, published 2026-08-24T16:27:04Z)
```
- Upgraded to anthropic>=1. #84
- --no-stream now uses the streaming API under the hood, fixing an SDK
  error for models with large default max_tokens: "Streaming is required
  for operations that may take longer than 10 minutes". #85
- Fixed a TypeError when temperature=None was passed explicitly, and
  fixed a validation bug where setting only top_p incorrectly raised
  "Only one of temperature and top_p can be set". #70 - thanks Charlie
  Tonneslan
- -o top_p 0.0 is now sent to the API instead of being treated as unset. #74
  - thanks Charlie Tonneslan
- Schemas now use Claude's structured outputs feature for Claude Haiku 4.5. #61
- Claude Opus 4.8 and the Claude 5 family models now support
  mid-conversation system messages: role: "system" messages passed via
  messages= are sent inline to the API. #73
- Thinking blocks with omitted content and redacted_thinking blocks are
  now preserved in conversation history and replayed in tool
  continuations. #81
```
*Source: `gh api repos/simonw/llm-anthropic/releases/tags/0.27`*

### `MIGRATION.md` — deprecated request parameters table (verbatim excerpt, anthropic-sdk-python v1.0.0)
```
| Method(s) | Removed parameter | Use instead |
|---|---|---|
| messages.create(), messages.stream(), messages.parse() and their
  beta.messages counterparts, beta.messages.tool_runner(), and the
  per-request params of messages.batches.create() | temperature, top_p,
  top_k | Remove them. Current models do not use these sampling
  parameters; for an older model that still does, pass them through
  extra_body (see below). |
```
*Source: raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md, "Removed: deprecated request parameters" section*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-anthropic-0251.md` and `blog-simonwillison-llm032.md`: both prior `llm-anthropic` release notes are structured identically to this one — a short first-party "beat" post with verbatim release-note bullets, model/version-specific changes, and (for 0251) linked-page context the Miner is expected to follow. This note's Claim 8 (blog post omits five of six release-note items) generalizes a pattern implicit but not stated in those earlier notes: Willison's release "beats" highlight the single most narratively interesting change, not a full changelog.
  - `blog-anthropic-code-migration-playbook.md` Claim 1 ("The core insight is that you don't fix the code. You fix the process (loop) that produced the code."): this note's Claim 3 (a single prompt naming a goal, a reference document, and a pass/fail test criterion, with no manual follow-up editing described) is a small-scale, single-file instance of the same discipline — verifying the loop's output (tests passing, diff review) rather than hand-editing the generated code.

- **Contradicts**: None identified. No existing source note makes a claim about `httpx`/`httpx2`, the `anthropic` Python SDK's parameter signatures, or this specific PR that this note's claims conflict with.

- **Extends**:
  - `blog-simonwillison-llm-anthropic-0251.md` and `blog-simonwillison-llm032.md`: continues the `llm-anthropic` plugin's release history in this corpus (0.25.1 → 0.26 → 0.27), tracking Anthropic model support (Opus 4.8, Claude 5 family) and, in this release, the underlying `anthropic` SDK's own major-version compatibility requirements.
  - `blog-anthropic-code-migration-playbook.md`: that note documents Anthropic's generalized six-step methodology for large-scale migrations (Bun's ~1M-line Zig→Rust rewrite, a 165,000-line Python→TypeScript port). This note is a minimal, single-PR, single-file counterexample at the opposite end of the same spectrum — a 26-line, 2-file, ~7-minute mechanical dependency migration driven by one prompt rather than a multi-agent adversarial-review pipeline. Useful for the guide to contrast "migration-at-scale needs a designed verification loop" against "a small, well-scoped, mechanically-checkable migration can be a single prompt plus a test suite."

- **Novel**:
  - First in-corpus documentation of Anthropic shipping a first-party Claude Code slash command (`/claude-api upgrade python`) specifically for automating an SDK major-version migration, stated directly in vendor migration documentation (Claim 6).
  - First in-corpus documentation of the `httpx`→`httpx2` dependency transition affecting Python AI SDKs, including the claim that OpenAI made an equivalent change in the same window (Claims 2 and 9).
  - First in-corpus example where a PR's diff, description, and an independently-fetched upstream migration guide were cross-checked against each other to verify an AI agent's claimed reasoning (Claim 5) rather than relying on the author's summary alone.

## Guide Impact

- **Chapter 02 (AI-driven workflows) or Chapter 04 (Build-time Patterns)**: Add this as a minimal worked example of a scoped dependency-upgrade prompt: name the target constraint, link the canonical migration document, specify an objective pass/fail check ("tests passing"), and treat "review the diff" as the human's remaining role. Contrast with `blog-anthropic-code-migration-playbook.md`'s six-step process for migrations at a scale where a single prompt and test suite are not a sufficient verification loop — this note's PR (2 files, +20/-6, single commit) is well below that threshold; the guide should be explicit about the scale at which "one prompt + tests passing" stops being sufficient verification.
- **Chapter 04 (Build-time Patterns — Plugin Ecosystem / `llm` Tool Integrations)**: Note that `llm-anthropic` now requires `anthropic>=1,<2`, which drops Python 3.9 support (MIGRATION.md states the SDK's minimum supported Python version increased from 3.9 to 3.10) — a transitive constraint practitioners upgrading `llm-anthropic` to 0.27+ should be aware of even though the blog post does not mention it.
- **Chapter 01 or Chapter 04 (documentation/migration-guide authorship patterns)**: If the guide discusses how to write AI-agent-friendly migration or upgrade documentation, cite Claim 7's pattern directly — pairing a breaking-change guide with "run a type checker, it will flag almost everything" gives both a human and an AI coding agent an automatically generated, complete checklist without requiring exhaustive prose enumeration of every affected call site.

## Extraction Notes

- **Followed three linked pages per the MINER rubric**: (1) the Anthropic `MIGRATION.md` migration guide, fetched via `curl` against the raw GitHub URL (the same URL given to Fable 5 in the prompt), used for Claims 5–7, 9 and the deprecated-parameters table artifact; (2) PR #84 on `github.com/simonw/llm-anthropic`, fetched via `gh api` for both metadata (`pulls/84`) and diff (`pulls/84/files`), used for Claims 3–5 and the diff/description artifacts; (3) the `llm-anthropic` 0.27 GitHub release notes (`releases/tags/0.27`), fetched via `gh api`, used for Claim 8 and its artifact. A fourth linked resource — the Claude Code session transcript at `claude.ai/code/session_01G3SA94Qx13c42KV1YiNejF` — was identified but not fetched, since it is a private/authenticated Claude Code session URL rather than a public page; it is referenced in Claim 3's assessment and the PR description artifact as an existing but unverified transparency artifact.
- **Quote fidelity**: The main blog post was fetched via `curl` with HTML tags stripped by `sed`; the blockquoted prompt text was cross-checked against the raw (unstripped) HTML to confirm the `&gt;=1` entity decodes to `>=1` and no other characters were altered. All GitHub API quotes (release notes, PR body, diff) are verbatim JSON string fields from `gh api`, not summarized or paraphrased.
- **Source is thin on its own**: the blog post itself is ~60 words plus a blockquote. All of Claims 4–9 required fetching linked pages; without doing so, this source would support only 2–3 claims (Claims 1–3), well under MINER.md's "5–15 claims, or you probably didn't read deeply enough" guidance. The three linked-page fetches (migration guide, PR, release notes) are what raise this note to 9 claims.
- **No contradiction filed**: nothing in this source conflicts with existing corpus claims; see Cross-References → Contradicts.
