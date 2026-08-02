---
source_url: https://vercel.com/changelog/github-tools-eve
source_type: blog-post
title: "Give your eve agent GitHub tools"
author: Hugo Richard, Ben Sabic (Vercel)
date_published: 2026-07-07
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2419"
---

# Give your eve agent GitHub tools

> Vercel changelog announcing that `@github-tools/sdk/eve` now registers a
> full set of GitHub API tools for `eve` agents from a single file, with
> named presets, safe-by-default write approval that pauses a session
> durably until a human approves, and trimmed high-volume reads — plus,
> via the linked first-party knowledge-base guide and the third-party
> `github-tools.com` reference docs it points to, the credential-minting,
> `@mention` channel, idempotency, and preset/token-scoping mechanics
> behind that headline feature.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  "1 min read" feature announcement — one intro paragraph, a three-file code
  sample, and three bulleted feature callouts). Per MINER.md §1, four linked
  pages were followed because the changelog's own prose is thin relative to
  the feature's surface area: `vercel.com/kb/guide/github-agent-eve` (Vercel's
  own first-party, step-by-step knowledge-base guide for this exact feature,
  fetched and read in full), and three pages on `github-tools.com` (the
  `vercel-labs/github-tools` open-source SDK's own documentation site) that
  the KB guide and changelog link to: `/frameworks/eve` (the eve-specific
  integration reference), `/guide/approval-control` (the write-safety/approval
  reference), and `/api/tools-catalog` (the full tool catalogue, read for
  structure/domain breakdown rather than quoted in depth). A fifth candidate
  link, `eve.dev` itself, is a product marketing/template page and was not
  followed.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to two named individuals (Hugo Richard, Ben Sabic) in both the
  changelog byline and the KB guide's `authors` frontmatter. The KB guide and
  the three `github-tools.com` pages are consistent with each other on every
  mechanic checked (presets, approval semantics, tool counts) and no
  independent third-party benchmark, customer story, or adoption metric
  appears anywhere in the source family — this is vendor documentation of a
  shipping feature, not independent reporting. `github-tools.com` is the
  documentation site for `vercel-labs/github-tools`, a Vercel Labs
  (`github.com/vercel-labs`) open-source SDK, not a fully independent
  third party, but it is a separate npm package (`@github-tools/sdk`) from
  `eve` itself and is credited as such throughout.
- **Scope**: Covers registering GitHub API tools in an `eve` agent via
  `@github-tools/sdk/eve` — the five/six named presets, write-approval
  policies (`always`/`once`/`never`/predicates) and their durability,
  high-volume read trimming, Vercel Connect credential minting (OIDC → no
  stored PAT), the `eve` GitHub channel for `@mention`-driven turns, tool
  idempotency, and the two integration paths (direct SDK import vs. a
  forthcoming mountable `eve` extension). Does **not** cover: pricing,
  a GA/beta status label for the `eve` toolset itself (none found anywhere
  in the four pages read), the full 42-tool-by-tool API reference (only
  domain-level structure was read from `/api/tools-catalog`), or independent
  production usage evidence — every example given (nine-line agent, sample
  prompts) is a vendor-authored illustration, not a documented customer
  deployment.

## Extracted Claims

### Claim 1: `@github-tools/sdk/eve` registers GitHub API tools for an `eve` agent from a single file, and a complete GitHub code-review agent can be built in nine lines of code across three files
- **Evidence**: The changelog's opening sentence and accompanying three-file code sample (`agent/instructions.md`, `agent/agent.ts`, `agent/tools/github.ts`); corroborated by `frameworks/eve`'s framing of the same integration as "all 42 tools registered from a single file."
- **Confidence**: settled (first-party, unambiguous feature description with a runnable code sample)
- **Quote**: "[GitHub Tools](https://github-tools.com/frameworks/eve) now ships an [eve](https://eve.dev) toolset through the new `@github-tools/sdk/eve` subpath. One file in `agent/tools/` can register every GitHub tool, or use a preset such as `maintainer`, so you can build a complete GitHub agent in nine lines of code."
- **Quote (tool count)**: "all 42 tools registered from a single file, with durable human-in-the-loop approval that actually pauses the session until a person approves"
- **Our assessment**: The "nine lines of code" claim is checkable against the changelog's own code sample (see Concrete Artifacts) and holds up — the instructions file, agent definition, and tool registration together are genuinely that short, because `createGithubTools({ preset: "maintainer" })` is doing all the work of exposing 42 typed tools to the model. This is a strong, concrete illustration of "framework does the tool-plumbing" as a design goal, not just a marketing number.

### Claim 2: Every write tool requires human approval unless explicitly opted out; gating is configurable per tool (`always`, `once`, or an input-dependent predicate), and on `eve` the pause is durable — it survives process restarts and redeploys
- **Evidence**: The changelog's "Safe by default" bullet, elaborated by `frameworks/eve`'s "Durable approval, done right" section and `guide/approval-control`'s "eve approval (richer policies)" section.
- **Confidence**: settled (first-party, consistent across three independently-fetched pages)
- **Quote**: "**Safe by default:** Every write tool, such as `mergePullRequest`, requires approval unless you opt out. Gate individual tools with `always`, `once`, or an input-dependent predicate; pauses survive restarts and deploys."
- **Quote (durability contrast)**: "This is eve's headline advantage over the boolean `needsApproval` on the AI SDK and Workflow paths: approval **pauses the session durably** until a human responds, and policies are expressive."
- **Quote (default)**: "Default (no `requireApproval`): all write tools → `always()`. Unlisted write tools keep the `always()` fail-safe default. Read tools never require approval."
- **Our assessment**: The fail-safe default — any write tool *not* explicitly listed in `requireApproval` still defaults to `always()` — is the load-bearing safety property here: a practitioner who forgets to configure a newly-added write tool does not silently get unattended write access, they get the safe (blocking) default. The framing "eve's headline advantage over... the AI SDK and Workflow paths" is itself an explicit, first-party admission that the same SDK's other two integration surfaces (`@github-tools/sdk` for the plain AI SDK, `@github-tools/sdk/workflow` for Vercel's Workflow SDK) only support a boolean `needsApproval` without eve's durable pause — see Claim 10 for the sharper edge of that same gap.

### Claim 3: Five named presets — `code-review`, `issue-triage`, `repo-explorer`, `ci-ops`, and `maintainer` — scope the registered toolset, and can be used alone or merged as an array
- **Evidence**: The changelog's "Presets" bullet; `frameworks/eve`'s "Presets and options" section confirms all five work with `createGithubTools` and that `preset` accepts "Single preset or array to merge."
- **Confidence**: settled (first-party, named and enumerated consistently across two pages)
- **Quote**: "**Presets: **`code-review`, `issue-triage`, `repo-explorer`, `ci-ops`, and `maintainer` scope the toolset, alone or merged."
- **Quote (merge mechanic)**: "preset: ['code-review', 'issue-triage']" (from the `agent/tools/github.ts` example in the linked KB guide, step 4)
- **Our assessment**: Naming presets after agent *roles* (a code reviewer, an issue triager, a CI operator) rather than after GitHub API resource types (issues, PRs, actions) is a deliberate design choice that maps directly onto the "what job is this agent doing" question a practitioner is already asking, rather than requiring them to reverse-engineer which raw GitHub endpoints a code-review agent actually needs. The `maintainer` preset (used in the changelog's own nine-line example) is presumably the broadest/union preset, though the source never states this explicitly — only that it "scopes the toolset."

### Claim 4: High-volume read tools such as `listPullRequestFiles` and `getCommit` trim what the model sees via conservative default output projections, while other consumers (eve's "channels") still receive full, untrimmed payloads
- **Evidence**: The changelog's "Trimmed reads" bullet, elaborated by `frameworks/eve`'s "Presets and options" section describing the underlying mechanism as a `toModelOutput` projection.
- **Confidence**: settled (first-party, consistent across two pages)
- **Quote**: "**Trimmed reads: **High-volume read tools such as `listPullRequestFiles` and `getCommit` trim what the model sees, while channels still get full payloads."
- **Quote (mechanism)**: "High-volume read tools (`listPullRequestFiles`, `getCommit`, `getFileContent`) include conservative default `toModelOutput` projections — full payloads still reach channels; the model sees trimmed diffs/content."
- **Our assessment**: This is a concrete, named instance of a context-budgeting default applied specifically to *tool results*, not tool definitions — a `listPullRequestFiles` call against a large PR could otherwise return an enormous file/diff listing directly into the model's context. The "channels still get full payloads" distinction matters: the trimming is applied only to what the *model* sees when reasoning, not to what a human reviewing the eve GitHub channel's thread reply would see, so no information is silently lost from the human-facing surface — only from the token budget the model itself consumes per turn.

### Claim 5: Vercel Connect mints short-lived, per-request GitHub tokens from a project's OIDC identity, so no personal access token lives in the environment and the developer never registers a GitHub App or handles its private key
- **Evidence**: The KB guide's opening paragraph and "How it works" section, describing the three-part architecture (`eve` runtime + GitHub Tools + Vercel Connect).
- **Confidence**: settled (first-party mechanism description, consistent with the general Vercel Connect model documented elsewhere in the corpus)
- **Quote**: "GitHub agents need three things: a durable runtime, tools that call the GitHub API, and credentials for those calls... [Vercel Connect] mints short-lived GitHub tokens at runtime so no personal access token lives in your environment. Vercel Connect also manages the GitHub App for you, which means you never register an app or handle a private key."
- **Quote (token lifecycle)**: "The token is cached in-process and refreshed automatically as it approaches expiry, so there is no long-lived secret to rotate, leak, or copy between environments."
- **Our assessment**: This is the same short-lived-credential-over-standing-secret pattern documented in `blog-vercel-enterprise-apps-and-agents.md` Claim 4 (Vercel Connect generally), now shown as the specific mechanism wired into a shipping GitHub-tools integration rather than described abstractly — see Cross-References → Extends. The trade-off, per Claim 7 below, is that this automatic refresh only covers the *Connect SDK's* own token cache, not a token already handed off to `createGithubTools`, which is a meaningfully different (and easy-to-miss) guarantee.

### Claim 6: The `eve` GitHub channel lets people `@mention` the agent in issues, pull requests, and review comments, and the agent replies in the thread with the PR diff already loaded into context — but mention-driven turns only work once the agent is deployed, not against a local dev server
- **Evidence**: The KB guide's step 7 ("Add the GitHub channel") and its description of webhook forwarding.
- **Confidence**: settled (first-party mechanism description with an explicit stated limitation)
- **Quote**: "The [eve GitHub channel](https://eve.dev/docs/channels/github) lets people `@mention` the agent in issues, pull requests, and review comments, and the agent replies in the thread with the PR diff already in context."
- **Quote (deployment requirement)**: "Trigger forwarding delivers to deployed URLs only, so mention-driven turns need a deployment. While testing locally, you can use both the terminal UI and the HTTP API."
- **Our assessment**: This is a specific, self-disclosed constraint worth flagging for practitioners building against this feature: local development lets you exercise the tool-calling and approval flow via the terminal UI or HTTP API, but the `@mention`-triggered channel path — arguably the feature's most visible end-user-facing behavior — cannot be tested end-to-end without a deployment, because Vercel Connect only forwards GitHub webhooks to deployed URLs. A team iterating on channel behavior needs a deploy-and-test loop, not a pure local one.

### Claim 7: A GitHub token minted once when `createGithubTools` loads is not automatically re-minted afterward, even though the underlying Connect SDK refreshes its own cached token — so a long-running local dev session can start returning 401 errors and needs a manual restart
- **Evidence**: The KB guide's Troubleshooting section, under "The GitHub token goes stale in a long-running process."
- **Confidence**: settled (first-party, self-disclosed known limitation with a documented workaround and a named roadmap item)
- **Quote**: "GitHub Tools currently accepts the token as a static string, minted when eve loads the tool file. The Connect SDK refreshes cached tokens automatically on each `getToken` call, but a token already handed to `createGithubTools` is not re-minted until the module reloads. Restart the dev server if GitHub calls start returning 401 errors after a long local session. Per-session tokens through eve connections are on the GitHub Tools roadmap."
- **Our assessment**: This is exactly the kind of self-disclosed limitation MINER.md flags as high-value: it is a specific, checkable gap between two components' refresh guarantees (Connect SDK token cache vs. the static string handed to `createGithubTools`) rather than a vague "may have edge cases" caveat. Note this is distinct from the KB guide's earlier claim that "the token is cached in-process and refreshed automatically as it approaches expiry" (Claim 5) — that statement is true of the Connect SDK's *own* cache, but does not carry through to a token that has already been copied into `createGithubTools`'s config at module-load time. The roadmap item ("per-session tokens") implies the current architecture mints one token for the process lifetime rather than per eve session, which is the root cause.

### Claim 8: Two ways exist to add GitHub Tools to an eve agent — direct `@github-tools/sdk/eve` import (documented, working today) and a mountable `@github-tools/eve-extension` — with the extension explicitly stated as the future-recommended path, though it is not yet published to npm
- **Evidence**: `frameworks/eve`'s callout at the top of the page and its dedicated "eve extension" section.
- **Confidence**: settled (first-party statement of current vs. intended-future integration surface, with an explicit publication-status caveat)
- **Quote**: "There are two ways to add the tools to an eve agent: importing `@github-tools/sdk/eve` directly (below), or mounting them as an [eve extension](#eve-extension) via `@github-tools/eve-extension`. Both are supported today — the extension is the direction this integration is moving toward and will become the recommended way to add GitHub tools to an eve agent."
- **Quote (publication status)**: "Not yet published to npm; see [`examples/eve-extension-agent`]... and [`packages/github-tools-eve-extension`]... to build and consume it from the workspace."
- **Our assessment**: A practitioner adopting this today should treat the direct `@github-tools/sdk/eve` import (Claims 1-4) as the stable integration path, since the extension form is explicitly not yet npm-published and must be built from the monorepo workspace to use at all. The extension's namespacing behavior — tools exposed as `<mount-file-name>__<toolName>` (e.g., `github__listPullRequests`) rather than bare tool names — is also a concrete forward-compatibility detail: code written against the extension's namespaced tool names would need updating if a team later migrates between the two integration paths.

### Claim 9: eve replays completed workflow steps but re-runs steps that were interrupted mid-execution, so non-idempotent GitHub write tools (e.g. `addIssueComment`, `createIssue`, `mergePullRequest`) should be gated behind `always()` or `once()` approval specifically to protect against duplicate execution on replay
- **Evidence**: `frameworks/eve`'s "Idempotency" section and its accompanying table distinguishing naturally-idempotent tools from non-idempotent ones.
- **Confidence**: settled (first-party mechanism description with a specific, named tool-by-tool breakdown)
- **Quote**: "eve replays completed steps but re-runs steps interrupted mid-execution... Gate non-idempotent writes behind `always()` or `once()` where replay safety matters."
- **Quote (non-idempotent tools)**: "`addIssueComment`, `createIssue`, `mergePullRequest`, … **Not** idempotent"
- **Our assessment**: This connects two mechanics documented separately elsewhere in the source (durable session replay, and approval gating) into a single concrete safety argument that neither the changelog nor the KB guide states on its own: durability (surviving restarts/interruptions, Claim 2) is a double-edged property for write tools specifically, because an interrupted `createIssue` call could, absent an approval gate, be replayed and create a *second* issue rather than resuming exactly where it left off. `createOrUpdateFile`, `closeIssue`, and `createBranch` are named as "naturally" idempotent (safe to retry because their effect is state-convergent — same content+sha, already-closed, branch-exists-at-same-SHA), which is a meaningfully different safety property from being approval-gated.

### Claim 10: `requireApproval` — including the durable, expressive `always`/`once`/predicate policies — is not enforced by `createDurableGithubAgent` (the SDK's Workflow-based durable-agent helper) as of this writing; durable human-in-the-loop approval requires using `createGithubAgent`, an eve agent, or an application-level guard instead
- **Evidence**: An embedded "copy this into your coding agent" instruction block at the top of `guide/approval-control`, stating the gap explicitly as a note to whoever is configuring write safety.
- **Confidence**: settled (first-party, explicit self-disclosed limitation, though notably placed inside an AI-agent-directed instructional snippet on the page rather than in the page's narrative prose — see Extraction Notes)
- **Quote**: "Note: requireApproval is not enforced by createDurableGithubAgent today — use createGithubAgent, eve agents ([https://github-tools.com/frameworks/eve](https://github-tools.com/frameworks/eve)), or app-level guards for durable paths."
- **Our assessment**: This is a sharp, specific instance of the same "eve's approval story is more complete than the SDK's other integration surfaces" point already visible in Claim 2's "headline advantage" framing — here stated as an outright non-enforcement gap on one specific named helper (`createDurableGithubAgent`), not merely a feature-richness comparison. A team building a durable GitHub agent on the Workflow SDK path who assumes `requireApproval` behaves the same way it does under `@github-tools/sdk/eve` would get no approval enforcement at all on that path today, and would need to either switch to `createGithubAgent`/eve or build their own application-level guard.

### Claim 11: The `maintainer` and `repo-explorer` presets include gist tools that fail (HTTP 403) when used with Vercel Connect–minted tokens, because GitHub grants gist access only to user access tokens and never to the installation tokens Connect mints — so the `code-review` preset, which excludes gist tools, is recommended specifically when pairing with a Connect connector
- **Evidence**: `frameworks/eve`'s "eve extension" section, explaining why its own example uses `code-review` rather than `maintainer`.
- **Confidence**: settled (first-party, specific and mechanistically explained limitation)
- **Quote**: "`code-review` is used here (rather than `maintainer`) because it pairs cleanly with a Connect connector — `maintainer` and `repo-explorer` include gist tools, and GitHub only grants gist access to user access tokens, never the installation tokens Connect mints, so gist calls 403 over Connect."
- **Our assessment**: This is a concrete preset-selection gotcha created by the interaction of two independently-reasonable design choices (Claim 3's role-based presets; Claim 5's installation-token-based Connect credentials) — a practitioner who picks `maintainer` because it sounds like "the complete toolset for a repo maintainer" and pairs it with Vercel Connect (the recommended, no-stored-secret credential path) will get silent-until-called 403s on any gist tool the agent tries to use. The source states the *cause* (GitHub's own token-type restriction on gist access) rather than treating it as an unexplained SDK quirk, which makes it a checkable, GitHub-platform-level constraint rather than a `github-tools` bug.

### Claim 12: `eve` v0.19 and later requires AI SDK `ai` v7 as a peer dependency (incompatible with `ai` v6), and the KB guide's own prerequisites specify Node.js 24 or newer for scaffolding a new eve GitHub agent
- **Evidence**: The KB guide's Prerequisites section and Step 3; `frameworks/eve`'s Install section restates the same `ai` v7 requirement and names it as a common source of peer-dependency conflicts.
- **Confidence**: settled (first-party, consistent version requirement stated across two independently-fetched pages)
- **Quote**: "Node.js 24 or newer" (KB guide, Prerequisites)
- **Quote (peer dependency)**: "Ensure `ai` resolves to **v7** — eve v0.19+ is not compatible with AI SDK v6. You still need `GITHUB_TOKEN` (or pass `token` explicitly)."
- **Quote (troubleshooting)**: "eve v0.19 and later requires `ai` v7, and so does `@github-tools/sdk/eve`. If your lockfile pins `ai` v6, update it and reinstall."
- **Our assessment**: This ties this source directly to `blog-vercel-ai-sdk-7-release.md`, which documents AI SDK 7's own stated minimum as Node.js 22 (that note's Claim 2) — this source's Node 24 prerequisite is `eve`'s own, higher floor on top of that, not a restatement of the AI SDK's minimum. For a team already running an older `eve` version or pinned to `ai` v6 for other reasons, adopting GitHub Tools' eve integration is gated behind an AI SDK major-version upgrade first, which is a non-trivial migration per that note's Claims 2-14 (breaking ESM-only imports, `HarnessAgent`, `toolApproval`, `WorkflowAgent`, and more) — not a drop-in addition.

## Concrete Artifacts

### The nine-line GitHub agent (verbatim, from the changelog)

```
Source: https://vercel.com/changelog/github-tools-eve

// agent/instructions.md
You are a GitHub code review assistant.

// agent/agent.ts
import { defineAgent } from "eve";

export default defineAgent({
  model: "anthropic/claude-sonnet-5",
});

// agent/tools/github.ts
import { createGithubTools } from "@github-tools/sdk/eve";

export default createGithubTools({
  preset: "maintainer",
});
```

### Registering tools with per-tool approval and a predicate (verbatim, from the linked KB guide step 4)

```
Source: https://vercel.com/kb/guide/github-agent-eve

import { getToken } from "@vercel/connect";
import { createGithubTools } from "@github-tools/sdk/eve";

const token = await getToken("github/github-agent", {
  subject: { type: "app" },
});

export default createGithubTools({
  token,
  preset: ["code-review", "issue-triage"],
  requireApproval: {
    mergePullRequest: true,
    createIssue: "once",
    addPullRequestComment: false,
  },
});
```

### `requireApproval` value → behavior mapping (verbatim table, from `github-tools.com/frameworks/eve`)

```
Source: https://github-tools.com/frameworks/eve, "Durable approval, done right"

Value                      Maps to    Behavior
true / 'always'            always()   Require approval on every call
false / 'never'            never()    Skip approval
'once'                     once()     Approve once per session, then auto-allow
predicate                  custom     Input-dependent gate (toolInput, session context)
                           Approval
always()/once()/never()    passthrough  Import helpers from eve/tools/approval
```

### Tool idempotency table (verbatim, from `github-tools.com/frameworks/eve`, "Idempotency")

```
Source: https://github-tools.com/frameworks/eve

createOrUpdateFile   — Natural when content + sha unchanged
closeIssue           — Natural when already closed
createBranch         — Natural when branch exists at same SHA
addIssueComment, createIssue, mergePullRequest, … — Not idempotent
```

### Tool catalogue domain structure (section headings, from `github-tools.com/api/tools-catalog`)

```
Source: https://github-tools.com/api/tools-catalog

Repository tools     (available in all presets)
Pull request tools
Issue tools
Gist tools
Workflow tools
Search and commit tools

"Each tool is implemented with a durable "use step" boundary, so calls
are proper workflow steps (retries, observability, full Node) when you
run inside the Vercel Workflow SDK."
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-enterprise-apps-and-agents.md`, `blog-vercel-ai-sdk-7-release.md`,
`blog-latentspace-vercel-andrew-qu-eve.md`, `blog-vercel-agent-runs-mcp-cli.md`,
and `docs-ghaw-github-tools.md` were re-read (in full, or via their numbered
`### Claim N:` heading list) during this extraction per MINER.md §4b, and
every claim number cited below was located and confirmed against that note's
own numbered claims in document order before writing this section.

- **Corroborates**:
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 4 ("Vercel Connect
    replaces long-lived, broadly-provisioned credentials sitting in
    environment variables with short-lived credentials an agent requests per
    task, which expire when the task completes"): this source's Claim 5 is
    the same mechanism shown wired into a specific, shipping tool
    integration — a GitHub agent that mints its token from an OIDC identity
    via `getToken` rather than reading a stored `GITHUB_TOKEN`. Neither
    source alone shows both the general architecture and a concrete,
    working code path; together they do.
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 8 (Andrew Qu: "If you
    deploy eve to Vercel, you get observability and evaluations out of the
    box... We value partners that provide specialized parts of the agent
    lifecycle"): this source is a concrete instance of that "batteries
    included, partner-extensible" strategy applied to GitHub tooling
    specifically — `eve` ships the runtime and approval model, a
    Vercel-Labs-adjacent SDK (`@github-tools/sdk`) ships the GitHub-specific
    tools, and Vercel Connect supplies credentials, rather than Vercel
    building GitHub API tooling into `eve` itself.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim
  in this source opposes any existing corpus note.

- **Extends**:
  - `blog-vercel-ai-sdk-7-release.md` Claim 2 (AI SDK 7 requires Node.js 22
    as a minimum runtime): this source's Claim 12 adds `eve` v0.19+'s own,
    higher Node 24 prerequisite and its hard `ai` v7 peer-dependency gate —
    a team on `ai` v6 cannot add this GitHub-tools integration without
    first completing the AI SDK 7 migration that note documents in detail
    (its Claims 2-14).
  - `blog-vercel-agent-runs-mcp-cli.md` (eve's Agent Runs observability,
    exposed via Vercel MCP tools and CLI commands with `--json` output):
    that note documents how a coding agent can query *its own* past run
    history; this source's Claim 9 (idempotency-aware approval gating for
    replayed steps) documents a related but distinct durability concern —
    what happens *during* a run when it is interrupted and replayed, as
    opposed to querying a run's history *after* the fact. Both are facets of
    `eve`'s "sessions survive restarts and deploys" durability model
    (this source's Claim 2), examined from different angles.
  - `docs-ghaw-github-tools.md` (GitHub Agentic Workflows' `tools.github`
    reference — an 18-toolset catalogue, three transport modes, and
    authentication options for gh-aw workflows): **this is a different
    system from a different vendor**, despite the name-collision the
    Prospector's triage comment flagged. `docs-ghaw-github-tools.md`
    documents GitHub's own first-party `gh-aw` platform's built-in
    `tools.github` configuration (a YAML `tools:` block inside a GitHub
    Actions workflow, using GitHub's own MCP server or `gh` CLI). This
    source documents a separate, Vercel-ecosystem npm package
    (`@github-tools/sdk`, published by `vercel-labs`) for `eve` agents
    running on Vercel's infrastructure. Both independently converge on a
    named-preset/toolset-grouping design for scoping GitHub API access
    (this source's five presets vs. gh-aw's 18 named toolsets with
    `default`/`all` shorthands) and both gate at least one high-risk
    operation family behind non-default configuration (this source's
    approval-gated writes vs. gh-aw's opt-in-only `dependabot` toolset) —
    worth noting as convergent design across two unrelated GitHub-tooling
    integrations, but the guide must not conflate the two systems' tool
    names, configuration syntax, or credential models.

- **Novel**:
  - **A durable-approval system where write-tool safety is explicitly tied
    to workflow-step idempotency** (Claim 9): no prior corpus source
    connects "this session can be interrupted and replayed" durability to a
    specific, per-tool idempotency classification that determines which
    tools need approval gating *for replay-safety reasons* specifically
    (as opposed to purely for human-oversight reasons).
  - **A stated non-enforcement gap for approval policies on one specific
    named integration surface of the same SDK** (Claim 10): no prior corpus
    source documents a vendor explicitly stating that its own safety
    feature (`requireApproval`) does not function on one of several
    parallel integration paths (`createDurableGithubAgent`) it ships,
    while it does on the others.
  - **A credential-type/preset interaction bug surfaced and explained by the
    vendor** (Claim 11): the gist-tools-403-over-Connect issue is a novel,
    concrete example of role-based tool presets and credential-minting
    architecture interacting in a way that silently breaks specific tools
    within an otherwise-working preset — documented here with its root
    cause (GitHub's own token-type restriction), not merely as a known bug.
  - **A token-freshness gap between an SDK's credential cache and a
    downstream tool-registration call that consumes it once** (Claim 7): no
    prior corpus source documents this specific class of staleness bug —
    where a lower-level SDK (Vercel Connect) correctly refreshes its own
    cached token, but a higher-level integration point captures that token
    once at module-load time and does not observe subsequent refreshes.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this source's approval-policy
  vocabulary (Claim 2's `always`/`once`/predicate, Claim 2's Concrete
  Artifacts table) as a concrete, named example of durable human-in-the-loop
  gating for a coding-agent's external write actions — distinct from the
  simpler boolean `needsApproval` pattern the same SDK offers on its
  non-`eve` integration paths (Claim 10), which is a useful contrast for any
  guide discussion comparing "approval as a boolean toggle" against
  "approval as a session-durable, input-dependent policy."

- **Chapter 02 (Harness Engineering) — tool-result context budgeting**: Add
  Claim 4 (trimmed high-volume reads via `toModelOutput` projections, full
  payloads still reaching non-model consumers) as a second concrete,
  named-tool example of budgeting a tool's *return payload* against the
  model's context window, alongside `blog-vercel-agent-runs-mcp-cli.md`
  Claim 6's `maxFieldLength` truncation parameter — two independent
  instances of the same general pattern from the same vendor ecosystem, at
  two different points (read-tool projection vs. explicit truncation
  parameter).

- **Chapter 03 (Safety and Verification) or wherever self-disclosed
  vendor limitations are tracked**: Add Claims 7, 10, and 11 as three
  concrete, vendor-stated gaps a team must specifically check for before
  relying on this integration in production: (a) long-running dev sessions
  can silently start failing GitHub calls with 401s because the token is
  minted once at module load, not refreshed; (b) `requireApproval` is not
  enforced at all on the `createDurableGithubAgent` Workflow path, only on
  `createGithubAgent`/eve; (c) the `maintainer`/`repo-explorer` presets will
  403 on gist calls specifically when paired with Vercel Connect
  installation tokens. All three are the kind of "this looks like it works
  but has a sharp edge" gap the guide's safety-verification material should
  surface explicitly rather than let a reader discover in production.

- **Chapter 04 (Context Engineering) or wherever credential/identity
  patterns are covered**: Add Claim 5 (OIDC-derived, per-request GitHub
  tokens via Vercel Connect, no stored PAT or GitHub App private key) as a
  second, tool-integration-specific instance of the short-lived-credential
  pattern already documented generally in
  `blog-vercel-enterprise-apps-and-agents.md` Claim 4 — this source shows
  the same pattern with a concrete `getToken(...)` call site inside a real
  tool-registration file.

## Extraction Notes

1. **Raw content fetched via markdown content-negotiation, not WebFetch
   summarization.** All four pages in this source family (the changelog and
   three `github-tools.com`/`vercel.com/kb` pages) support a
   `text/markdown` `Accept` header that returns clean, already-de-HTML'd
   markdown (the changelog page also advertises this via a `<link
   rel="alternate" type="text/markdown">` tag in its raw HTML head, which is
   what prompted checking for content negotiation in the first place). Per
   MINER.md §2a, every `Quote` field in this note was located
   character-for-character in that markdown capture (cross-checked against
   the raw HTML `<p>`/`<li>` text for the changelog's three bulleted
   callouts specifically, since those bullets use bold lead-ins that could
   be reformatted by a markdown converter) before being used here.
2. **Four linked pages followed per MINER.md §1**: `vercel.com/kb/guide/
   github-agent-eve` (first-party Vercel KB guide, read in full — supplied
   Claims 5-7, 12), `github-tools.com/frameworks/eve` (read in full —
   supplied Claims 1, 3, 4, 8, 9, 11, 12), `github-tools.com/guide/
   approval-control` (read in full — supplied Claim 10 and corroborating
   detail for Claim 2), and `github-tools.com/api/tools-catalog` (read for
   its section-heading domain structure only, used in Concrete Artifacts;
   the full per-tool table was not transcribed as it is out of scope for
   this changelog-focused note). `eve.dev` itself was not followed — it is
   the marketing/template landing page for the `eve` framework generally,
   not specific to this GitHub-tools feature.
3. **Claim 10's quote is sourced from an embedded AI-agent instruction
   block, not narrative prose.** `github-tools.com/guide/approval-control`
   opens with a `<prompt>`-tagged block whose stated purpose is to be
   copy-pasted into a coding agent's own context ("Configure @github-tools/sdk
   write safety in this project...") — the `createDurableGithubAgent`
   non-enforcement note quoted in Claim 10 appears inside that block, not in
   the page's regular explanatory text below it. The claim is still treated
   as settled because the same non-enforcement fact is independently
   consistent with `frameworks/eve`'s own framing (Claim 2's "headline
   advantage over... the AI SDK and Workflow paths" language, which implies
   the Workflow path's approval is comparatively weaker) — but this note
   flags the unusual source location explicitly in case the Assayer wants to
   weight it differently than ordinary page prose.
4. **`/api/tools-catalog`'s full per-tool table (42 tools across six
   domains) was not individually transcribed.** The page enumerates every
   tool with its capability description and write/read status in HTML
   tables; this note captured the six domain headings (Concrete Artifacts)
   and the "durable `use step` boundary" framing but did not extract each of
   the ~42 individual tool rows, judging that level of detail out of scope
   for a changelog-anchored source note — a future source note keyed
   directly to `github-tools.com` itself (rather than to this Vercel
   changelog) would be the right place for a full tool-by-tool catalogue
   extraction if that becomes needed.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts. The
   `docs-ghaw-github-tools.md` name collision (same "GitHub tools" phrasing,
   different vendor/system) was checked carefully per MINER.md §4 and
   determined to be a documentation naming coincidence, not a contradiction
   — the two systems' claims do not overlap on any shared factual claim
   (different toolset names, different transport/credential models,
   different host platforms), so no contradiction issue was warranted; see
   Cross-References → Extends for the explicit disambiguation.
6. **Confidence calibration: emerging.** Individual claims are rated
   "settled" because they are unambiguous, first-party statements about a
   named, shipping feature, cross-checked across four independently-fetched
   pages that agree with each other everywhere they overlap. The note's
   overall confidence is "emerging" rather than "settled" because: (a) this
   is a single vendor ecosystem's own documentation (Vercel + the
   Vercel-Labs-published `github-tools` SDK) with no independent
   verification, benchmark, or named production customer anywhere in the
   source family; (b) the feature shipped less than a month before
   extraction (2026-07-07 vs. this note's 2026-08-02 extraction date), with
   at least one integration path (the `eve` extension, Claim 8) explicitly
   not yet published to npm; and (c) several of the most specific,
   guide-relevant claims (7, 10, 11) are self-disclosed limitations of a
   very new feature, which are exactly the kind of detail likely to change
   as the SDK matures — a re-check closer to a stated GA/1.0 milestone
   (none exists yet in this source family) would be warranted before
   treating these as durably settled.
