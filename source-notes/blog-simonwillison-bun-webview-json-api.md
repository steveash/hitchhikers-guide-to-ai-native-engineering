---
source_url: https://simonwillison.net/2026/Aug/20/bun-webview-json-api/
source_type: blog-post
title: "A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView"
author: Simon Willison
date_published: 2026-08-20
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: emerging
issue: "#3015"
---

# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

> A five-paragraph link-blog "beat" announcing Bun 1.4 and its new
> `Bun.WebView` browser-automation API, pointing to an AI-generated research
> report (built by "Claude Code for web") that implements a zero-dependency,
> ~150-line TypeScript JSON API service — navigate/evaluate-JS/screenshot,
> no Puppeteer or Playwright — and measures how little RAM it needs (as low
> as ~56 MB for JS-only, ~168 MB for full desktop Chromium with screenshots)
> via cgroup memory-limit binary search.

## Source Context

- **Type**: blog-post (a "beat" in Simon Willison's link-blog format — the
  same thin structure documented in `blog-simonwillison-shot-scraper-1-10-release.md`
  and `blog-simonwillison-shot-scraper-1-11-release.md`: a short intro, one
  blockquote, and a pointer to external material). The beat itself is five
  short paragraphs; nearly all of the substantive technical content lives in
  the linked GitHub repository, not the blog post prose.
- **Author credibility**: Simon Willison is a well-established LLM-tooling
  practitioner and the author of `shot-scraper`, the CLI tool this prototype
  explicitly imitates (`shot-scraper javascript`). This is first-party
  research he commissioned and published, not a third-party report. The
  linked repository (`simonw/research`, path `bun-webview-json-api`) is part
  of an explicitly-labeled "research" series; its README is annotated with a
  standard `AI-GENERATED-NOTE` banner (quoted in Claim 4 below) stating all
  text and code in the report was produced by an LLM, not by Willison
  directly. Treat the repository content as an AI-authored artifact
  presented by Willison, not as Willison's own hand-written analysis.
- **Scope**: Covers the Bun 1.4 release announcement (one quoted paragraph
  from Bun's own release notes), the `Bun.WebView` API surface, and one
  prototype's architecture, code, memory/latency measurements, and
  environment-specific gotchas. Does not cover: production deployment
  experience, comparison benchmarks against an actual running
  Puppeteer/Playwright service (the comparison is asserted, not measured
  head-to-head), or any use of this pattern for an LLM-driven agent's own
  tool-calling (the service is JSON-API infrastructure a human or agent
  *client* would call, not itself an agent). Followed the linked GitHub
  repository's `README.md`, `server.ts`, and `notes.md` (3 of the repo's 7
  files, within the "follow up to 5 linked pages" budget) since the blog
  beat's own prose is too thin to extract from alone.

## Extracted Claims

### Claim 1: Bun 1.4 ships `Bun.WebView` as first-class, built-into-the-runtime browser automation, using macOS system WebKit or a driven local Chromium process over the Chrome DevTools Protocol (CDP)
- **Evidence**: Direct product description in the blog post, corroborated by
  the linked repository's own explanation of the same two backends.
- **Confidence**: settled (shipped in a numbered stable release, described
  consistently across both first-party sources)
- **Quote**: "Of these the one that most caught my eye was Bun.WebView, which adds first class support for browser automation to Bun core using either macOS WebKit or control of a local Chromium process via the Chrome DevTools Protocol (CDP)."
- **Our assessment**: This is the core new capability the rest of the source
  is about. Folding browser automation into the JS runtime itself (rather
  than requiring an npm dependency like Puppeteer or Playwright) is a
  meaningful reduction in the dependency surface for any tool — human- or
  agent-facing — that needs to drive a real browser.

### Claim 2: Bun 1.4's own release notes claim +1,517 additional Node.js test-suite passes, 2,900+ issues fixed, 5x lower idle CPU, up to 35% lower memory use, 50% faster Linux startup, and a full runtime rewrite from Zig to Rust
- **Evidence**: Direct blockquote of Bun's official release-notes text, as
  reproduced in the blog post.
- **Confidence**: settled (first-party vendor release notes, quoted verbatim)
- **Quote**: "Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It adds Bun.Image, Bun.WebView, Bun.markdown, Bun.cron(), Bun.Terminal, bun run --parallel, bun test --parallel, bun audit fix, bun dedupe, and bun prune. And it rewrites Bun from Zig to Rust."
- **Our assessment**: These are vendor-reported aggregate numbers with no
  independent methodology given (what workload for the CPU/memory/startup
  percentages, what test-count baseline). Treat as directional marketing
  claims. The "rewrites Bun from Zig to Rust" line is the same rewrite
  documented in depth by `blog-simonwillison-rewriting-bun-rust.md` and
  `blog-pragmaticengineer-bun-rust-rewrite.md` — see Cross-References.

### Claim 3: A zero-dependency, ~150-line TypeScript file can implement a shot-scraper-style JSON API (navigate, evaluate JS, screenshot PNG/JPEG/WebP) entirely on top of `Bun.WebView`, with no Puppeteer or Playwright dependency
- **Evidence**: The repository's own verdict statement plus the actual
  `server.ts` file, which was fetched and is 139 lines including comments
  and blank lines, implementing exactly the three endpoints described.
- **Confidence**: emerging (one working prototype exists and was fetched and
  read directly; not battle-tested in production, and `Bun.WebView` itself
  is explicitly still marked experimental)
- **Quote**: "Verdict: entirely feasible, with a pleasantly small amount of code. Bun 1.4's built-in `Bun.WebView` gives you navigate / evaluate-JS-returning-JSON / screenshot with no Puppeteer or Playwright dependency, and the whole service — HTTP API included — fits in one ~150-line TypeScript file (server.ts) with zero npm dependencies."
- **Our assessment**: The line-count and "zero dependencies" claims are
  directly checkable against the fetched `server.ts` and hold up — it really
  is a self-contained `Bun.serve` file with no `import` of any third-party
  package. This is a genuine, verifiable reduction in tool surface area
  compared to a Puppeteer- or Playwright-based equivalent, which would pull
  in a multi-hundred-MB browser-driver dependency tree.

### Claim 4: The repository is explicitly disclosed, via a standard banner, as an AI-generated research report — all text and code produced by an LLM
- **Evidence**: A `<!-- AI-GENERATED-NOTE -->` HTML comment block wrapping a
  GitHub `[!NOTE]` admonition at the very top of the repository's README,
  present verbatim in the fetched raw file.
- **Confidence**: settled (directly observed in the fetched README source)
- **Quote**: "This is an AI-generated research report. All text and code in this report was created by an LLM (Large Language Model). For more information on how these reports are created, see the main research repository."
- **Our assessment**: Combined with the blog post's "I had Claude Code for
  web build a prototype" line, this is one of the more explicitly
  disclosed instances of agent authorship in the corpus — disclosed both in
  the human-facing blog prose *and* via a repository-level machine-readable
  banner. This contrasts with `blog-simonwillison-shot-scraper-1-11-release.md`
  Claim 7, where the same author shipped an entire agent-authored release
  with zero disclosure in the human-facing prose, discoverable only via
  commit trailers. See Cross-References.

### Claim 5: The per-request architecture — each API call opens a fresh `Bun.WebView` (a new Chrome tab), does its work, and closes it — gives concurrency-safety "for free" because `evaluate()` only allows one in-flight call per view
- **Evidence**: Architectural description in the README, matching the
  `withView()` helper in `server.ts` which calls `view.navigate()`, awaits
  the caller's function, then always calls `view.close()` in a `finally`
  block.
- **Confidence**: emerging (the mechanism is directly visible in the fetched
  code and is a plausible correctness argument, but the "for free" framing
  is the report's own claim, not independently stress-tested beyond the
  8-concurrent-request benchmark in Claim 9)
- **Quote**: "Each request opens a fresh WebView (= a Chrome tab), navigates, does its work and closes it. That makes the service concurrency-safe for free: `evaluate()` only allows one in-flight call *per view*, and views are per-request."
- **Our assessment**: This is a clean design choice worth extracting as a
  general pattern independent of Bun specifically: when a per-call resource
  (browser tab, subprocess, connection) has an internal single-flight
  constraint, allocating one fresh instance per request sidesteps the need
  for any explicit locking or queueing in the service layer, at the cost of
  per-request setup/teardown overhead (visible in Claim 9's ~64 ms per
  `/javascript` call, most of which is plausibly tab create/navigate/close).

### Claim 6: Minimum reliable RAM for the prototype ranges from ~56 MB (JS-only, trimmed `headless_shell` flags) to ~168 MB (full desktop Chromium, JS + screenshots), measured via cgroup memory-limit binary search
- **Evidence**: A four-row results table in the README derived from running
  the service inside a cgroup with a hard `memory.limit_in_bytes` (no swap)
  and binary-searching the minimum limit at which a fixed 9-request mixed
  workload (simple JS, heavy-page JS, heavy-page screenshots) reliably
  succeeds; methodology and raw numbers cross-checked against the
  companion `notes.md` file, which restates the same table.
- **Confidence**: emerging (a real, described measurement methodology —
  not just an assertion — but a single run in one sandboxed container, by
  one AI-authored report, not independently reproduced)
- **Quote**: "Minimum RAM for a reliable service is **~104 MB** (Chromium headless shell), **~88 MB** with aggressive Chrome flags, or **~56 MB** if you only need JavaScript execution and no screenshots. A full desktop Chromium binary needs ~168 MB."
- **Our assessment**: The blog post's own headline number ("192MB-256MB
  container... against complex web pages") is *not* this table's literal
  168 MB full-Chromium minimum — it's the README's separate "practical
  guidance" line (Claim 7), which budgets extra headroom above the
  synthetic benchmark floor for real-world heavy pages. This is not a
  contradiction between the two sources, but readers citing "how much RAM
  does browser automation need" from this source should distinguish the
  benchmarked floor (56–168 MB, Claim 6) from the recommended production
  budget (128–256 MB, Claim 7) — the blog post only surfaces the latter.

### Claim 7: Practical guidance from the report is that a 128 MB container comfortably runs a `headless_shell`-based screenshot+JS service for light pages, while full Chrome or heavy real-world pages should budget 192–256 MB
- **Evidence**: README's own stated takeaway following the benchmark table,
  distinct from the raw binary-search minimums in Claim 6.
- **Confidence**: emerging (a recommendation layered on top of Claim 6's
  measured data, from the same single-run, AI-authored source)
- **Quote**: "Practical guidance: **a 128 MB container comfortably runs a headless_shell-based screenshot+JS service for light pages; budget 192–256 MB for full Chrome or heavy real-world pages.** Memory scales with page complexity — a JS-heavy site will need more than these floors."
- **Our assessment**: This is the number the blog post's headline sentence
  actually quotes ("192MB-256MB container... against complex web pages"),
  confirming the blog beat draws from this specific guidance line rather
  than the table's raw minimums. Useful as a concrete sizing data point for
  anyone provisioning a containerized browser-automation microservice, with
  the caveat that it is one AI-generated report's recommendation, not an
  industry-standard figure.

### Claim 8: Using Chromium's `headless_shell` build instead of full desktop Chromium is the single biggest memory lever, because it skips the GPU process, most utility processes, and UI baggage
- **Evidence**: README's stated comparison, corroborated by `notes.md`'s
  process-level PSS accounting (Bun ~27 MB; full-Chromium process tree
  ~260 MB across 10 processes including zygotes, GPU, network service,
  storage, and renderers, vs. `headless_shell` spawning "far fewer
  helpers").
- **Confidence**: emerging (a specific, checkable measurement from one run;
  directionally consistent with widely-known Chromium architecture, but the
  exact MB figures are this report's own)
- **Quote**: "Playwright's `headless_shell` build is the big win: it skips the GPU process, most utility processes and UI baggage of full Chrome (~103 MB peak vs ~176 MB for the identical workload)."
- **Our assessment**: Notably, this prototype sources its `headless_shell`
  binary from a Playwright install rather than a bare Chromium download —
  worth flagging for anyone trying to reproduce this without also pulling
  in Playwright's browser-download tooling, which somewhat undercuts the
  "zero dependency" framing at the infrastructure (not npm-package) level.

### Claim 9: Per-request latency on the test container was ~64 ms for `/javascript` and ~308 ms for a heavy-page `/screenshot`; 8 concurrent requests of either kind completed well within a couple of seconds
- **Evidence**: README's stated timing, describing the test container as
  "16 GB, shared CPUs."
- **Confidence**: anecdotal (single container, single run, no statistical
  spread reported — e.g. no p50/p95 breakdown, just single point figures)
- **Quote**: "On this container (16 GB, shared CPUs), per request including tab create/navigate/close: ~64 ms for `/javascript`, ~308 ms for a heavy-page `/screenshot`. 8 concurrent JS requests completed in 193 ms total and 8 concurrent heavy screenshots in 1.7 s — the shared-Chrome/tab-per-request model parallelizes well."
- **Our assessment**: These numbers support Claim 5's "concurrency for
  free" architecture claim in practice — 8 concurrent heavy screenshots
  (1.7s total) taking barely more than 5x a single heavy screenshot (308ms)
  suggests the shared-Chrome-process/one-tab-per-request model does
  parallelize rather than serialize under load, at least at this
  concurrency level and container size.

### Claim 10: Root execution requires an explicit `--no-sandbox` Chrome flag, or Chrome exits immediately with "Chrome process closed the pipe"
- **Evidence**: Listed as a "caveat found along the way" in the README, with
  matching detail in `notes.md`'s log ("needed `--no-sandbox` in argv or
  Chrome dies instantly").
- **Confidence**: anecdotal (specific to this container's root-user setup,
  though consistent with widely-documented Chrome-in-Docker behavior)
- **Quote**: "**Root needs `--no-sandbox`** or Chrome dies instantly (\"Chrome process closed the pipe\")."
- **Our assessment**: This matches a long-standing, widely known constraint
  of running Chrome/Chromium as root in containers generally (not specific
  to Bun or `Bun.WebView`); useful as a concrete, sourced error-message
  string for anyone debugging the same failure with `Bun.WebView`
  specifically, since that exact error string is otherwise undocumented in
  Bun's own release notes.

### Claim 11: This sandbox's TLS-intercepting egress proxy could not parse Chrome's TLS 1.3 ClientHello (carrying a ~1.7 KB post-quantum X25519MLKEM768 key share), causing `ERR_CONNECTION_RESET`, fixed by forcing `--ssl-version-max=tls1.2`
- **Evidence**: Detailed root-cause narrative in both README (summary) and
  `notes.md` (full netlog-debugging log), including the specific Chromium
  build version (141.0.7390.37) and the failed `--disable-features=UseMLKEM/PostQuantumKyber/X25519MLKEM768/...`
  workaround attempt before the working fix was found.
- **Confidence**: anecdotal (a single sandboxed development environment's
  networking quirk; both the README and `notes.md` explicitly flag it as
  environment-specific)
- **Quote**: "**TLS-intercepting proxies**: this sandbox's egress proxy couldn't parse Chrome's TLS 1.3 ClientHello (post-quantum X25519MLKEM768 key share, ~1.7 KB). Fixed for full Chrome with `--ssl-version-max=tls1.2` (cert verification stays on); `headless_shell` doesn't wire up that switch, so its benchmarks used localhost pages. Also had to add the proxy CA to the NSS db (`certutil -d sql:$HOME/.pki/nssdb -A -t \"C,,\" ...`). None of this applies outside sandboxed environments."
- **Our assessment**: Genuinely useful as a concrete debugging trail for
  anyone hitting `ERR_CONNECTION_RESET` from Chrome behind a corporate or
  agent-sandbox TLS-intercepting proxy — the root cause (post-quantum
  ClientHello extension confusing an MITM proxy) is a specific, non-obvious
  failure mode as TLS 1.3 post-quantum key exchange becomes more common in
  Chromium. The report itself is explicit that this caveat does not apply
  to normal (non-sandboxed, non-MITM'd) deployments.

### Claim 12: `evaluate()` accepts only a JavaScript expression (not statements — a bare `throw` is a syntax error) and rejects with the page-side error, matching the exact contract of Willison's own `shot-scraper javascript` command
- **Evidence**: Stated directly in the README's caveats list, explicitly
  framed by the report as matching an existing tool's contract.
- **Confidence**: settled for the description of the behavior as
  implemented and documented; the comparison target (`shot-scraper
  javascript`'s contract) is asserted, not independently re-verified
  against `shot-scraper`'s own source in this extraction
- **Quote**: "`evaluate()` takes an **expression** (statements like a bare `throw` are a syntax error) and rejects with the page-side error — same contract as `shot-scraper javascript`."
- **Our assessment**: This is a deliberate design choice to mirror an
  existing, already-adopted tool's semantics rather than inventing a new
  contract — sensible for a prototype explicitly "inspired by my
  shot-scraper javascript CLI tool" (per the blog post). It means anyone
  already writing JS snippets for `shot-scraper javascript` could reuse them
  against this JSON API with no translation.

## Concrete Artifacts

### `server.ts` — the complete route table (verbatim, `simonw/research/bun-webview-json-api/server.ts`, fetched via raw GitHub content)
```typescript
const server = Bun.serve({
  port: PORT,
  idleTimeout: 120,
  routes: {
    "/": () =>
      Response.json({
        service: "bun-webview-json-api",
        endpoints: {
          "POST /javascript": "{url, javascript, wait_ms?, width?, height?}",
          "POST /screenshot":
            "{url, width?, height?, format?, quality?, javascript?, wait_ms?, b64?}",
          "GET /healthz": "liveness",
        },
      }),

    "/healthz": async () => {
      const view = makeView(320, 240);
      try {
        await view.navigate("about:blank");
        const two = await view.evaluate("1 + 1");
        return Response.json({ ok: two === 2 });
      } finally {
        view.close();
      }
    },

    "/javascript": {
      POST: async (req) => {
        let body: JsBody;
        try {
          body = await req.json();
        } catch {
          return err(400, "invalid JSON body");
        }
        if (!body.url) return err(400, "missing url");
        if (!body.javascript) return err(400, "missing javascript");
        try {
          const result = await withView(body, (view) => view.evaluate(body.javascript!));
          // evaluate() awaits promises and JSON-serializes, like shot-scraper
          return Response.json({ ok: true, result });
        } catch (e: any) {
          return err(502, e?.message ?? String(e));
        }
      },
    },
    // ... /screenshot follows the same withView() pattern, returning image
    // bytes or {ok, content_type, b64} when body.b64 is set
  },
});
```

### `withView()` — the per-request tab lifecycle helper (verbatim, `server.ts`)
```typescript
async function withView<T>(
  body: JsBody,
  fn: (view: InstanceType<typeof Bun.WebView>) => Promise<T>,
): Promise<T> {
  const view = makeView(body.width ?? 1280, body.height ?? 800);
  try {
    await view.navigate(body.url);
    if (body.wait_ms) await Bun.sleep(body.wait_ms);
    return await fn(view);
  } finally {
    view.close();
  }
}
```

### Working example against a real site through the sandbox's egress proxy (verbatim, README)
```
$ curl -X POST localhost:8044/javascript -d '{"url":"https://datasette.io/",
    "javascript":"new Promise(done => done({title: document.title,
                   h2: document.querySelector(\"h2\")?.textContent}))"}'
{"ok":true,"result":{"title":"Datasette: An open source multi-tool for
 exploring and publishing data","h2":"Exploratory data analysis"}}
```

### Full resource-usage table (verbatim, README, cross-checked against `notes.md`)
```
| Configuration | Minimum reliable limit | First failing limit |
|---|---|---|
| Full desktop Chromium, JS + screenshots | 168 MB | 160 MB |
| Chromium headless_shell, JS + screenshots | 104 MB | 96 MB |
| headless_shell + trim flags, JS + screenshots | 88 MB | 80 MB |
| headless_shell + trim flags, JS only | 56 MB | 48 MB |

trim flags: --no-zygote --renderer-process-limit=1 --js-flags=--max-old-space-size=32 --disable-dev-shm-usage
```

### Run command (verbatim, README and `server.ts` header comment)
```
BUN_CHROME_PATH=/path/to/chromium CHROME_EXTRA_ARGS="--no-sandbox" bun server.ts
```

## Cross-References

- **Corroborates**: `blog-simonwillison-servo-crate-exploration.md` Claim 1
  ("Claude Code can cold-start on a brand-new, sparsely-documented crate and
  deliver a working tool in one task") and Claim 5 (the "give it a crate and
  a loose goal" task-framing pattern) — this source is a second, independent
  instance of the same pattern: an agent ("Claude Code for web") given a
  brand-new, still-experimental runtime API (`Bun.WebView`, shipped the same
  day) and a loose goal ("build a prototype... inspired by shot-scraper"),
  which delivered a working, measured artifact.
- **Corroborates**: `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 10
  (the Rust rewrite delivered "concrete, measured stability, memory, size,
  and performance improvements" over the prior Zig version) — this source's
  Claim 2 blockquote (idle CPU down 5x, memory down up to 35%, 50% faster
  Linux startup) is the vendor's own follow-on performance framing for the
  same rewrite, published about six weeks after that note's source.
- **Extends**: `blog-simonwillison-rewriting-bun-rust.md` (the rewrite
  itself, completed via ~50 dynamic workflows per
  `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 6) and
  `blog-simonwillison-claude-code-bun-in-rust.md` (documenting that Claude
  Code itself started running on the Rust-ported Bun before any public
  release) — this source is the first-stable-release payoff of that earlier
  rewrite effort: `Bun.WebView` is one of the new features Bun 1.4 ships
  as a "first stable version since the infamous Rust rewrite" (this post's
  own words, Claim 1's context).
- **Extends**: `blog-simonwillison-shot-scraper-1-10-release.md` and
  `blog-simonwillison-shot-scraper-1-11-release.md` (both documenting the
  `shot-scraper` CLI tool this prototype explicitly imitates) with a new,
  previously-uncaptured design detail: Claim 12 above is the first note in
  the corpus to record that `shot-scraper javascript`'s contract is
  expression-only evaluation with page-side-error rejection — a semantic
  detail neither shot-scraper release note documents directly, only visible
  here because a second implementation deliberately copied it.
- **Compare** (not a contradiction): `blog-anthropic-computer-use-skills-files-api.md`
  Claim 4 describes Anthropic's browser use tool as reading "the structure
  of the page and acts on a specific field or button rather than a position
  on screen." This source's tool takes the opposite approach for two of its
  three endpoints: `/screenshot` returns raw pixels, and `/javascript`
  requires the caller to already know what DOM query or JS expression to
  run — there is no structure-reading or element-targeting built in. These
  are not competing solutions to the same problem: Anthropic's browser use
  tool is a first-class *agent action space* (the model chooses what to
  click), while this prototype is developer infrastructure a human or an
  agent's own code would call with an already-decided script or screenshot
  request. Worth noting in the guide as two different points on the
  "how does code get eyes/hands on a web page" spectrum, not as disagreeing
  claims.
- **Novel**: Claim 4 (explicit dual disclosure of AI authorship — both blog
  prose and a repository-level `AI-GENERATED-NOTE` banner) is a new
  disclosure pattern for the corpus, and sits at the opposite end of the
  spectrum from `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7's
  finding that the same author shipped an entire agent-authored release with
  zero disclosure in the human-facing beat post. Also novel: Claim 6/7's
  RAM-tiering data (56 MB JS-only up to 168 MB full-Chromium-with-screenshots,
  measured via cgroup binary search) is the first concrete, methodology-described
  memory-sizing data point in the corpus for browser-automation-as-a-service
  infrastructure specifically (as opposed to LLM-inference memory sizing,
  which the corpus covers extensively elsewhere).

## Guide Impact

- **Chapter 03 (Tool Use) / Chapter 08 (Dev tooling & infrastructure)**: If
  the guide discusses building custom browser-automation tools for agents to
  call (as opposed to using Anthropic's own computer-use/browser-use
  products), add this source as a concrete existence proof that a
  zero-npm-dependency JSON API wrapping browser automation is achievable in
  ~150 lines on Bun 1.4, with Claim 6/7's memory-tiering table as a sizing
  reference for anyone provisioning a container for such a service.
  Flag explicitly that `Bun.WebView` is still marked experimental and this
  is a single unreproduced prototype (confidence: emerging), not a
  recommended production pattern yet.
- **Chapter 03 / Chapter 05 (Agents and tool use)**: If the guide compares
  approaches to giving an agent (or an agent-adjacent service) access to a
  browser, use the "Compare" cross-reference above to distinguish
  screenshot/JS-eval-based automation (this source; also Anthropic's
  original computer-use approach per `blog-anthropic-computer-use-best-practices.md`)
  from structure-reading, element-targeting automation
  (`blog-anthropic-computer-use-skills-files-api.md` Claim 4's browser use
  tool) — these solve different problems and neither supersedes the other.
- **Chapter 02/09 (Agent-authored work / disclosure norms)**: If the guide
  cites practitioner disclosure patterns for agent-authored artifacts, add
  Claim 4 as a positive example of dual (prose + repository-banner)
  disclosure, contrasting with the zero-disclosure pattern documented in
  `blog-simonwillison-shot-scraper-1-11-release.md` Claim 7 from the same
  author roughly five weeks earlier — evidence that even one prolific,
  generally transparent author's disclosure practice varies by artifact
  type (a "research" repo gets an explicit AI-generated banner; a tool
  release's commits do not).

## Extraction Notes

- The blog beat's own prose (fetched via raw HTML with `curl`, not the
  summarizing WebFetch tool, per the precedent in
  `blog-simonwillison-shot-scraper-1-11-release.md`'s Extraction Notes) is
  only five short paragraphs plus one blockquote — genuinely thin on its
  own. Nearly all of the extracted claims and all of the concrete artifacts
  come from following the linked GitHub repository
  (`simonw/research/tree/main/bun-webview-json-api`), specifically its
  `README.md`, `server.ts`, and `notes.md` files, fetched directly via
  `raw.githubusercontent.com`. Did not fetch `bench.sh`, `testpages.ts`, or
  the two screenshot image files (`datasette.png`, `example.jpg`) linked
  from the same repo — the memory/performance numbers they'd support are
  already fully captured via the README/`notes.md` results tables, and the
  images are visual artifacts with no additional claims to extract.
- Cross-checked every numeric claim (memory limits, latency figures) between
  `README.md` and `notes.md`, which restate the same benchmark table in
  slightly different prose — no numeric discrepancies were found between
  the two files themselves; the only distinction worth flagging (Claim 6 vs
  Claim 7) is between the benchmark table's literal binary-search minimums
  and the README's separately-labeled "practical guidance" recommendation,
  which is what the blog post's headline number actually quotes.
- No contradictions were found against existing corpus source notes; the
  "Compare" entry in Cross-References is a difference in *design purpose*
  (developer infrastructure vs. agent action space), not a factual
  disagreement, so no contradiction issue was filed per MINER.md §4a's
  "when NOT to file" guidance (conditioning variable, not contradiction).
