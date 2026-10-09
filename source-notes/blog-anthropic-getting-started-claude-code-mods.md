---
source_url: https://claude.dev/blog/getting-started-with-claude-code-mods/
source_type: blog-post
title: "Getting started with Claude Code mods"
author: Addy Osmani (claude.dev Blog, Tutorials)
date_published: 2026-10-01
date_extracted: 2026-10-09
last_checked: 2026-10-09
status: current
confidence_overall: emerging
issue: "#4006"
---

# Getting started with Claude Code mods

> A first-party tutorial that builds a ~80-line "Token Weather" mod end to end and documents the mod hook contract (observe / rewrite / answer), the host-held `$.state` rule for surviving hot reload, the no-DOM/no-Node sandbox, and the validate/test/share workflow, extending the spec-level coverage of mods in the Willison note.

## Source Context

- **Type**: blog-post (tutorial) on the claude.dev Blog, discovered via the `claude-blog` trusted feed. Published Oct 01, 2026; 11 min read.
- **Author credibility**: Byline is Addy Osmani. The site is Anthropic's Claude Code blog and the finished code lives in `anthropics/claude-code-playground`, so the content is first-party and describes shipped behavior (Claude Code 2.1.287+). It is a tutorial, so it makes no adoption or effectiveness claims.
- **Scope**: Covers the mod mechanism, one full worked example (Token Weather), two larger examples (Blast Radius, Replay Theater), sharing, and four habits. Does not cover the full `$` API (defers to generated types), the built-in mods, or AGENTS.md. Example code was read in the post only; the playground repo was not fetched.

## Extracted Claims

### Claim 1: A mod is a plugin whose behavior lives in one JS/TS hooks module exporting `register(on, options)`
- **Evidence**: Layout spelled out in the post: `.claude-plugin/plugin.json` manifest, `hooks/hooks.json` naming exactly one module, module exports `register`. Full runnable example included.
- **Confidence**: emerging
- **Quote**: "hooks/hooks.json names one module under modules."
- **Our assessment**: Matches the Willison note's Claim 3 (single `register(on, options)` entry), now with a runnable example. Credible; first-party.

### Claim 2: Every hook has the same `($, e, next)` shape and hooks form a middleware-style chain that ends at Claude Code's default behavior
- **Evidence**: Code sample plus a diagram of event -> your hook -> other plugins -> Claude Code.
- **Confidence**: emerging
- **Quote**: "Hooks form a chain, like middleware."
- **Our assessment**: Useful mental model; also implies ordering between plugins matters (the test framework relies on this: test hooks "run after the mod in the chain").

### Claim 3: A hook has exactly three moves: observe, rewrite, or answer
- **Evidence**: Table in the post. Observe: `const r = await next(e); /* look */ return r`. Rewrite: `return next({ ...e, command: safer })`. Answer: `return { deny: "…" }` without calling `next`. Blast Radius uses "answer"; Replay Theater uses "observe"; Token Weather observes then draws.
- **Confidence**: emerging
- **Quote**: "answer: return { deny } without next"
- **Our assessment**: Clean taxonomy that the existing corpus lacks for in-session extension. It parallels settings-hook allow/deny/modify semantics but is in-process.

### Claim 4: Mods differ from settings hooks by being loaded once, holding state, drawing UI, and calling back into Claude Code
- **Evidence**: Explicit comparison paragraph; settings hooks are described as shell-command-per-event with JSON over stdin/stdout.
- **Confidence**: emerging
- **Quote**: "A settings hook runs a shell command for each event and passes JSON over stdin and stdout. A mod is loaded once and stays in the session."
- **Our assessment**: Important framing for Ch02: two hook tiers now exist. Contrast with the hooks-enforcement material in `failure-hooks-enforcement-2k` and the hook row in the steering note (Claim 7 there) is worth stating in the guide.

### Claim 5: Mod modules run in a sandbox with no DOM and no Node; all I/O goes through the `$` API
- **Evidence**: Stated in the post; `$` lists `ui, session, state, store, fs, process, clock, http, tool, command, model`. Blast Radius shells out via `$.process.run` with argv arrays, "so nothing in a path is run as shell code".
- **Confidence**: emerging
- **Quote**: "The module runs in a sandbox of its own, with no DOM and no Node, so everything outside it goes through $."
- **Our assessment**: Credible design (capability-mediated I/O). The post does not describe sandbox escape guarantees, so security strength is unverified.

### Claim 6: Per-session state must live in host-held `$.state`, not module variables, because hot reload re-runs `register`
- **Evidence**: Explained with the failure mode (reload is a fresh load; `register` and `session.start` fire again; module variables reset). State keys must also be declared in a `.d.ts` type contract or `claude plugin validate` errors.
- **Confidence**: emerging
- **Quote**: "A module-level let readings = [] looks like the obvious choice, but a hot reload is a fresh load: register runs again, session.start fires again, and module variables start over."
- **Our assessment**: The most transferable gotcha. Repeated as a "habit" ("Plan for hot reload"). A $.state read inside a render hook also auto-subscribes the render, so redraws are free.

### Claim 7: You can describe a mod in natural language and Claude Code will write it, with hot reload for iteration
- **Evidence**: Full prompt text provided; Claude "asks once whether to turn on hot reloading". The post says the mod loads only in that session and its folder is cleaned up later unless copied out.
- **Confidence**: anecdotal
- **Quote**: "Claude Code knows how to write mods, so you can describe the one you want and let it do the work."
- **Our assessment**: Plausible but no success-rate data. The post says Claude Code has a built-in guide for writing mods, which is an example of self-extension docs shipped inside the tool.

### Claim 8: The mod API is unstable; generated type declarations in `.claude-plugin/types/` are the authority per build
- **Evidence**: Version gate (2.1.287+) and explicit statement that the API can change between releases.
- **Confidence**: emerging
- **Quote**: "The API can change between releases."
- **Our assessment**: Any guide advice must avoid freezing API detail; recommend pointing readers at generated types. Mods are "on by default" now.

### Claim 9: Mod tooling includes `claude plugin validate` (static analysis of hooks/calls/state) and `claude plugin test` (runs `*.test.ts` against the real runtime with stubbable events)
- **Evidence**: Sample validate output listing hooks, `$` calls, and state reads/writes; a full test using `claude-code/testing` that stubs `session.usage` and asserts rendered text.
- **Confidence**: emerging
- **Quote**: "claude plugin test runs the plugin's *.test.ts files against the real Claude Code runtime."
- **Our assessment**: Harness extensions are testable deterministically, a strong practice signal. Sample output is the author's, not independently run.

### Claim 10: A "Blast Radius" mod can hold risky Bash commands and show impact, but it is explicitly not a permission system
- **Evidence**: Hooks `tool.call` for Bash, computes impact via dry runs (`git clean -n`, `du`), opens a pane with Proceed/Cancel, denies on Cancel. Hooks get 10s of own time per dispatch but time inside `$` calls doesn't count.
- **Confidence**: emerging
- **Quote**: "It's a safety net, not a permission system. It reads the command text, so $(…), aliases and scripts that call rm get past it."
- **Our assessment**: Candid limitation worth citing: text-matching guards are bypassable; use permission rules for hard blocks. The long-poll workaround (looping `sleep` to hold a hook) is a notable trick and a smell.

### Claim 11: Mods run with Claude Code's full access and are third-party code; trust model is "install like a package"
- **Evidence**: Safety paragraph in "Sharing your mod". Distribution via marketplace repos and the Claude directory submission.
- **Confidence**: settled
- **Quote**: "So install mods the way you'd install a package: read the repo first and only install from people you trust."
- **Our assessment**: Straightforward supply-chain advice; no sandbox-level isolation promised between mod and host privileges beyond `$`.

### Claim 12: Some of Claude Code's own features are built as mods
- **Evidence**: Post names AGENTS.md support and the `/diff` pane, with sources in `anthropics/claude-code` under `mods/`.
- **Confidence**: emerging
- **Quote**: "Some of Claude Code's own features are built as mods, including AGENTS.md support and the /diff pane beside the conversation."
- **Our assessment**: Corroborates Willison note Claims 2 and 4 from a second first-party source.

## Concrete Artifacts

Hook skeleton (Osmani, "How a mod works"):

```javascript
on("tool.call", { tool: "Bash" }, async ($, e, next) => {
  // $    the mods API: ui, session, state, store, fs, process, clock, http, tool, command, model, ...
  // e    this event's input, as plain data
  // next passes e to the other plugins and then to Claude Code's own behavior
  return next(e);
});
```

Plugin layout, manifest, module list (Step 1):

```
token-weather/
├── .claude-plugin/
│   ├── plugin.json
│   └── types/            (written by Claude Code when it loads the mod)
├── hooks/
│   ├── hooks.json
│   └── token-weather.mjs
├── types/
│   └── index.d.ts        (added in step 3)
└── tests/
    └── token-weather.test.ts   (added in step 5)
```

```json
{
  "modules": ["./token-weather.mjs"]
}
```

State declaration (Step 3) and host-held state key:

```typescript
export type TokenWeatherReading = { tokens: number; window: number; percent: number };
declare module "claude-code" {
  interface PluginState {
    "token-weather": { readings: TokenWeatherReading[] };
  }
}
```

```javascript
// Held by the host, so the history survives a hot reload of this file.
const readings = { plugin: "token-weather", key: "readings" };
```

Validation error for undeclared state (Step 3): `token-weather.readings is not declared: the manifest's types contract must name it in interface PluginState { … }`.

Blast Radius core, the "answer" move (Two more mods):

```javascript
on("tool.call", { tool: "Bash" }, async ($, e, next) => {
  const risk = classify(String(e.command ?? ""));
  if (risk === null) return next(e);                 // everything else runs as normal
  ...
  if (held.decision === "proceed") return next(e);   // let it run
  return { deny: `Blast Radius held this command: the user pressed Cancel. It would have: ${report.summary}.` };
});
```

Install flow (Sharing your mod): `/plugin marketplace add your-org/my-mods`, `/plugin install token-weather@my-mods`, `/reload-plugins`.

Debug tip: "Run claude --debug and look for a line saying a hook returned a tree that does not validate."

Event set named in the post: tool calls, the prompt as submitted, turns starting and finishing, session start/end, slash commands, and `ui.render`; examples use `tool.call`, `session.start`, `turn.start`, `turn.complete`, `ui.render`, `command.run`.

## Cross-References

- **Corroborates**: `blog-simonwillison-claude-code-mods-agents-md` Claim 3 (single `register(on, options)` module with `($, e, next)` hooks), Claim 2 (mods as harness-customization mechanism), and Claim 4 (built-in mods such as `diff` and `agents-md`; this post independently names `/diff` and AGENTS.md).
- **Contradicts**: None filed. Status difference: `blog-simonwillison-claude-code-mods-agents-md` Claim 9 records mods as early access, requiring function hooks to be enabled and "not listed in the plugin marketplace". This post (three weeks later) says mods are on by default, are installable via marketplaces, and can be submitted to the Claude directory. Treated as a temporal update, not a contradiction; both still say the API may change between releases.
- **Extends**: `blog-simonwillison-claude-code-mods-agents-md` (adds the observe/rewrite/answer taxonomy, the `$.state` hot-reload rule, sandbox statement, validate/test workflow, and worked examples). Also `blog-anthropic-steering-claude-code-mechanisms` Claim 1 (seven instruction mechanisms) and Claim 7 (hooks bypass compaction): mods are an additional in-process tier beyond settings hooks.
- **Novel**: The three-move hook taxonomy; host-held state vs module variables under hot reload; hold-a-tool-call-with-a-pane pattern and its stated bypass limits; `claude plugin test` with stubbed events; prompt-to-mod authoring workflow.

## Guide Impact

- **Chapter 02**: Add a short "mods" subsection under harness extension points: settings hooks (shell command per event) vs mods (in-process, stateful, UI-capable), using the observe/rewrite/answer taxonomy (Claims 3, 4). Cite Claim 10 for the caveat that text-matching command guards are not permission systems. Do not freeze API detail; point to generated types (Claim 8).
- **Chapter 05**: Mention that team-shared mods ship as ordinary plugins through a marketplace repo and carry full local access, so apply package-review norms (Claim 11).
- **Chapter 01**: Optional one-liner on "describe a mod and let Claude build it" (Claim 7), flagged anecdotal.

## Extraction Notes

- Read the full article text (fetched raw HTML and stripped tags); quotes were copied from that text. Video figures and images were not viewable; captions only.
- Did not fetch `anthropics/claude-code-playground` or `mods/README.md`; the latter is already covered by the Willison note.
- The post lists no adoption data or effectiveness metrics. Token Weather's percentages (18/67/81%) are demo captions.
- Pronouns for the author are not stated and none are used.
