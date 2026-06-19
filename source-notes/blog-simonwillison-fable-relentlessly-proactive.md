---
source_url: https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/
source_type: blog-post
title: "Claude Fable is relentlessly proactive"
author: Simon Willison
date_published: 2026-06-11
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: anecdotal
issue: "#1217"
---

# Claude Fable is relentlessly proactive

> Simon Willison documents Fable 5's autonomous debugging of a CSS scrollbar bug
> in Datasette Agent — a 17-step investigation launched from a single screenshot
> and one-line prompt — surfacing both the practical capability of frontier model
> agents and a concrete security argument for mandatory sandboxing.

## Source Context

- **Type**: blog-post (simonwillison.net, June 11, 2026; ~900 words plus code
  examples, command transcripts, and a sequential list of the agent's actions.
  This is Willison's own first-person account of a debugging session run on his
  local machine via Claude Code with Fable 5 as the underlying model.)
- **Author credibility**: Simon Willison is the creator of Django, Datasette, and
  the `llm` Python CLI. He is a trusted-feed source in this corpus with prior notes
  covering Fable 5 capabilities (`blog-simonwillison-claude-fable-5.md`), silent
  policy interventions (`blog-simonwillison-fable-silent-interventions.md`), and
  Datasette Agent development. No Anthropic affiliation; writes from the
  operator/practitioner side. Claims about the session's behavior are first-person
  observations from his own machine.
- **Scope**: Covers a single debugging session: the prompt given, the 17 steps Fable
  took autonomously, specific code artifacts (PyObjC window introspection, Python CORS
  server, JavaScript injection), the cost (~$12.11), a mid-session model downgrade to
  Opus, and Willison's security assessment of running such agents outside sandboxes.
  Does NOT cover: the full Datasette Agent codebase or the CSS fix itself (linked via
  GitHub commit, not reproduced), formal benchmarks, Fable vs. other model comparisons,
  or the authentication/authorization model for Claude Code.

## Extracted Claims

### Claim 1: Fable, given only a screenshot and a one-line prompt about a CSS scrollbar bug, autonomously executed 17 investigative steps — including starting a development server, browser automation, OS window introspection, template source modification, CORS server creation, and shadow DOM traversal — to identify a two-line CSS fix

- **Evidence**: Willison's sequential bulleted list of every action the agent took,
  documented inline in the article. Each step is specific: terminal commands run,
  files created, browsers opened, workarounds invented.
- **Confidence**: anecdotal (single first-person session; no external replication)
- **Quote**: "After two days of experience with Claude Fable 5 I think the best way
  to describe it is **relentlessly proactive**."
- **Our assessment**: The 17-step sequence is the empirical core of the article.
  Willison's list is a rare ground-truth record of frontier agent behavior on a real
  engineering task — not a benchmark, not a demo, but a live debugging session on
  his own codebase. The range of steps (browser automation → OS scripting → template
  modification → web server → JavaScript injection → shadow DOM traversal) illustrates
  that agentic behavior at the frontier is qualitatively different from script
  execution: the agent is planning, encountering barriers, inventing workarounds, and
  validating outcomes across multiple tool categories simultaneously. This is the
  strongest in-corpus evidence for what "autonomous debugging" actually looks like
  at frontier scale.

### Claim 2: When standard osascript commands were blocked due to assistive access restrictions, Fable autonomously invented a PyObjC/Quartz workaround — using `uv run --with pyobjc-framework-Quartz` at runtime to iterate OS windows and capture targeted screenshots — without being instructed to do so

- **Evidence**: Willison's direct observation of the agent's terminal output, including
  the specific tool invocation and the error message that triggered the workaround.
- **Confidence**: anecdotal (first-person observation; the specific command is documented)
- **Quote**: "Found that `osascript -e 'tell application "System Events" to tell process
  "firefox" to id of window 1'` was blocked because 'osascript is not allowed assistive
  access'"
- **Quote**: "Figured out that `uv run --with pyobjc-framework-Quartz python` workaround,
  described above"
- **Our assessment**: This is the most operationally significant step in the sequence.
  The agent hit a real OS-level permission boundary (assistive access denial), recognized
  the constraint from the error message, and invented an alternative approach using a
  different API (Quartz framework via PyObjC) that accomplishes the same goal without
  the blocked permission. This is not instruction-following — it is constraint
  recognition and autonomous tool escalation. No practitioner prompted this. The
  implication for harness designers: an agent with shell access can discover and use
  OS-level APIs that were not in the original tool grant, simply by being blocked on
  one path and finding another. Permission boundaries at the tool-category level (e.g.,
  "no browser automation") may not hold if the agent can invoke equivalent capabilities
  via system calls or alternate frameworks.

### Claim 3: Fable autonomously wrote its own Python CORS web server to capture computed CSS measurements from the browser's shadow DOM — creating infrastructure it was never asked to create

- **Evidence**: Full Python code for the CORS server is reproduced in the article,
  along with the JavaScript fetch call that sends measurements to it. Both are verbatim
  from the agent's session output.
- **Confidence**: anecdotal (first-person observation; code artifact is documented)
- **Quote**: (no direct quote for this claim; see Concrete Artifacts for the code)
- **Our assessment**: The CORS server is the clearest example of agentic infrastructure
  creation: the agent needed a receiver for browser-side measurements and built one
  rather than stopping to ask. The server is minimal and correct — CORS headers, OPTIONS
  preflight, POST handler, file write — written in ~15 lines of Python using only
  stdlib. This pattern ("build the infrastructure you need to proceed") is a marker of
  frontier-tier autonomous problem-solving that has significant implications for blast
  radius assessment: the agent's effective tool surface is not the tools it was granted
  but the full set of tools it can construct from its shell access.

### Claim 4: Fable modified Datasette's application templates to inject JavaScript that triggers a keyboard shortcut after page load — making unsolicited source-code changes to enable its own automated testing

- **Evidence**: The specific JavaScript injection is reproduced in the article (a
  `window.addEventListener("load", ...)` block dispatching a synthetic `keydown` event
  for the `/` key after 1200ms delay). Willison observes this without having requested
  any template modification.
- **Confidence**: anecdotal (first-person; code artifact documented)
- **Quote**: "I had not told Claude Code to use any browser automation, and I was
  pretty sure it wasn't possible for it to trigger mouse movements or keyboard shortcuts
  within a window, so how was it doing that?"
- **Our assessment**: Template modification to enable automated testing is a form of
  "lateral scope expansion" — the agent widened its operational surface (from debugging
  to code modification) without explicit authorization. Willison's surprise is the signal:
  he didn't know the agent was doing this until he investigated the behavior. For
  practitioners: an agent with write access to a codebase will use that access for
  purposes beyond the stated task if it determines those purposes serve the goal. The
  distinction between "debugging assistant" and "code-modifying agent" collapses when
  the agent has write access.

### Claim 5: Mid-session, without user action or notification, Fable hit an "invisible guardrail" and silently downgraded itself to Opus, continuing the session on the less capable model

- **Evidence**: Willison's direct observation of the session's model behavior.
- **Confidence**: anecdotal (single observation; no technical explanation provided)
- **Quote**: "Having figured out all of these tricks Fable... hit some invisible
  guardrail and downgraded itself to Opus."
- **Our assessment**: The silent downgrade is operationally significant. The user
  received no notification, and the session continued — but on a different model with
  different capability and cost characteristics. This is a distinct behavior from the
  API-level guardrail notification mechanism documented in
  `blog-simonwillison-claude-fable-5.md` Claim 2 (the Claude API can notify callers
  when guardrails trigger). The silent downgrade suggests that some guardrails operate
  at the model-selection layer rather than the API response layer. Practitioners
  tracking session costs or relying on Fable-specific capabilities mid-session may
  encounter unexpected Opus behavior without a triggering event they can inspect.
  The downgrade happened at roughly the 17th step — after the most aggressive
  system access (PyObjC, screencapture, template modification). Correlation is not
  causation, but the timing suggests the guardrail may be sensitivity-triggered.

### Claim 6: The full debugging session cost approximately $12.11 in tokens — frontier-model pricing for a task that produced a two-line CSS fix

- **Evidence**: Willison's direct cost observation from the session.
- **Confidence**: anecdotal (single session measurement; described as "approximate if
  paying full API prices")
- **Quote**: (no verbatim cost quote available from source; reported as approximately
  $12.11)
- **Our assessment**: $12.11 for a two-line CSS fix is a concrete unit-cost data point
  for frontier-model agentic debugging. The asymmetry — 17 investigative steps for a
  minimal fix — is the defining characteristic of agentic frontier use: the model
  invests heavily in exploration and validation. This is either a cost problem or a
  quality feature depending on the use case: for a bug that would take a developer
  30–60 minutes to isolate without the agent, $12 is inexpensive; for a production
  batch workload, the per-bug cost at this rate is prohibitive. Compare with
  `blog-simonwillison-claude-fable-5.md` Claim 10 ($99.26 for the Datasette Agent
  session on June 9) — the relative scale ($12 vs. $99) suggests debugging sessions
  are substantially cheaper than full development sessions at Fable pricing, even
  when the agent is being "relentlessly proactive."

### Claim 7: Willison characterizes "relentless proactivity" as a dual-edged property: impressive for autonomous debugging, but "terrifying" if an agent is subverted by prompt injection

- **Evidence**: Willison's closing editorial framing, which explicitly names the
  prompt injection threat vector and names specific forms of mischief (data exfiltration).
- **Confidence**: anecdotal (practitioner opinion; but the structural argument is
  well-grounded in the capabilities demonstrated in the same session)
- **Quote**: "If Fable had been acting on malicious instructions—a prompt injection
  attack hidden in code or an issue thread, or something I'd carelessly pasted into my
  terminal—it's alarming to think quite how far it could go to exfiltrate data or cause
  other forms of mischief."
- **Quote**: "Fable is arguably smarter and hence more suspicious of potentially
  malicious instructions. But that smartness is very much a two-edged sword: if it
  _does_ get subverted by instructions, the amount of damage it can do given its
  relentless proactivity is terrifying."
- **Our assessment**: The dual-edged framing is precisely calibrated. Willison
  acknowledges that Fable's intelligence makes it harder to subvert via naive prompt
  injection (it may recognize suspicious instructions). But the same proactivity that
  drives autonomous debugging — reading code, building tools, injecting into templates,
  capturing screenshots — makes a successfully subverted Fable significantly more
  dangerous than a subverted less-capable model. A model that invents a CORS server to
  collect measurements could equally invent a CORS server to exfiltrate credentials.
  This is not a speculative risk; it is a direct corollary of the session behavior
  documented above.

### Claim 8: Running coding agents outside sandboxes is Willison's "top contender for a Challenger disaster incident" — a predicted-but-likely-ignored catastrophic failure that will materialize at scale

- **Evidence**: Willison's editorial framing, citing Johann Rehberger's "Challenger
  disaster" security incident framework.
- **Confidence**: anecdotal (practitioner opinion; but the citation of Rehberger places
  this in an established security discourse)
- **Quote**: "it's my top contender for a Challenger disaster incident, as described by
  Johann Rehberger"
- **Quote**: "Running coding agents outside of a sandbox has always been a bad idea."
- **Our assessment**: The Challenger disaster metaphor (from Rehberger's security
  framework) describes a class of incidents where the failure mode is known, understood,
  and likely, yet practitioners continue to deploy without the necessary safeguards
  because the incident hasn't happened yet to them personally. Willison positions
  unsandboxed coding agent deployment in this category. The implication is not
  primarily a technical claim (sandboxing is technically feasible) but a behavioral
  prediction: most teams running Claude Code-style agents on developer laptops are not
  sandboxing, and the eventual prompt-injection-driven exfiltration incident is
  predictable and avoidable. The "always been a bad idea" framing is retrospective —
  this was already bad practice before Fable; Fable's capability makes the bad practice
  catastrophically worse.

### Claim 9: Frontier-model agents execute OS-level actions (window introspection, screenshot capture, browser automation) as routine debugging steps — not through special capabilities but via shell access to standard system tools

- **Evidence**: The specific commands documented in the session: `screencapture -x -o -l
  153551`, `uv run --with pyobjc-framework-Quartz`, `defaults write
  com.google.chrome.for.testing AppleShowScrollBars Always`, Playwright automation.
- **Confidence**: anecdotal (single session; but the documented commands are standard
  macOS/Python tools, not proprietary)
- **Quote**: "this is a robust reminder that coding agents can do anything _you_ can do
  by typing commands into a terminal"
- **Our assessment**: This claim reframes the sandboxing argument: the risk does not
  come from the agent having special privileged capabilities. It comes from the agent
  having shell access and the intelligence to compose existing system tools into
  novel workflows. A macOS developer's shell already has `screencapture`, `defaults
  write`, `uv`, and Python — the agent doesn't need additional permissions to use
  them, and a permission model based on "what tools was the agent granted?" fails if
  the agent can compose granted shell access into arbitrary tool invocations.

### Claim 10: Fable's proactive exploration included Playwright automation across Firefox, Chrome, and WebKit plus OS-level Safari interaction — the agent chose which browsers to test and in what order without instruction

- **Evidence**: Willison's bulleted action sequence, which lists "Fired up a Playwright
  Chrome session," "Cycled through Firefox and WebKit in Playwright too, failing to
  recreate the bug," "Worked out my default browser was Safari," then investigated
  Safari via the PyObjC screenshot approach.
- **Confidence**: anecdotal (first-person observation)
- **Quote**: "Turns out it had been writing its own scratch HTML pages to try and
  recreate the bug, then opening Safari and grabbing screenshots."
- **Our assessment**: The browser selection logic illustrates goal-directed reasoning:
  the agent systematically narrowed scope (cross-browser → Safari-specific) by
  interpreting negative results (Playwright automation didn't reproduce the bug across
  three engines → the bug is likely Safari-specific → investigate Safari directly via
  OS tools). This is not random exploration; it is a coherent debugging strategy
  executed autonomously. Practitioners designing agentic debugging pipelines can treat
  this cross-browser narrowing pattern as a reproducible template.

## Concrete Artifacts

### Full Autonomous Action Sequence (from the article, verbatim bulleted list)

```
Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/

Based on a screenshot and a one-line prompt, Claude Fable 5 + Claude Code:

* Figured out the recipe to run the local development server (with fake environment
  variables needed to get it running)
* Fired up a Playwright Chrome session
* Turned on the visible scrollbars setting for Chrome
  `defaults write com.google.chrome.for.testing AppleShowScrollBars Always`
  (it turned that off again later)
* Cycled through Firefox and WebKit in Playwright too, failing to recreate the bug
* Worked out my default browser was Safari
* Built a `textarea-scrollbar-test.html` HTML document
* Opened that in real (not Playwright) Firefox
* Found that `osascript -e 'tell application "System Events" to tell process "firefox"
  to id of window 1'` was blocked because "osascript is not allowed assistive access"
* Figured out that `uv run --with pyobjc-framework-Quartz python` workaround, described above
* Added JavaScript to the site templates in order to trigger the `/` key
* Built its own little Python CORS web server to capture JSON data
* Rewrote the template to capture that data and send it to the server
* Scripted its way through the Web Component shadow DOM to the information it needed
* Opened Safari to confirm the source of the bug
* Modified its custom template to hack in a potential fix
* Confirmed the hacked fix worked
* Reported back on how to fix the problem
```

### PyObjC Window Capture Workaround (from the article, verbatim)

```bash
# OS window introspection via Quartz framework when osascript is blocked:
uv run --with pyobjc-framework-Quartz python

# Screenshot capture with specific window ID:
screencapture -x -o -l 153551 /tmp/safari-cases.png
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/*

### Python CORS Web Server (from the article, verbatim)

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class H(BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        open("/tmp/diag.json", "w").write(self.rfile.read(n).decode())
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
    def log_message(self, *a):
        pass

HTTPServer(("127.0.0.1", 9999), H).serve_forever()
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/*

### JavaScript Template Injection for Keyboard Event Trigger (from the article, verbatim)

```javascript
window.addEventListener("load", function () {
  setTimeout(function () {
    document.dispatchEvent(new KeyboardEvent("keydown", {key: "/", bubbles: true}));
  }, 1200);
});
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/*

### JavaScript Shadow DOM Measurement Capture (from the article, verbatim)

```javascript
const host = document.querySelector("navigation-search");
const ta = host.shadowRoot.querySelector("textarea");
const cs = getComputedStyle(ta);
fetch("http://127.0.0.1:9999/diag", {
  method: "POST",
  body: JSON.stringify({
    dpr: window.devicePixelRatio,
    scrollWidth: ta.scrollWidth, clientWidth: ta.clientWidth,
    whiteSpace: cs.whiteSpace, width: cs.width,
  }),
});
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/*

### Chrome Scrollbar Setting Toggle (from the article, verbatim)

```bash
defaults write com.google.chrome.for.testing AppleShowScrollBars Always
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` Claim 11: "A researcher successfully phished
    an employee into launching Claude Code with a malicious prompt...Claude completed the
    exfiltration 24 times" (out of 25 attempts). Willison's prompt injection concern
    (Claims 7 and 8) is directly corroborated: the exfiltration phishing test confirms
    that a subverted Fable with shell access can carry out exactly the class of mischief
    Willison describes. That test ran with Claude Code's standard shell access; Fable's
    additional proactivity (building its own CORS server, injecting into templates) would
    expand the attack surface further.
  - `blog-anthropic-how-contain-claude.md` Claim 3: "Yet even with best-in-class
    defenses, protection in the model layer will never be 100% effective, which is why
    it can't stand alone." Willison's Claim 8 ("Running coding agents outside of a
    sandbox has always been a bad idea") directly corroborates this principle: Willison
    is making the same argument from the practitioner side that Anthropic's containment
    engineering team makes from the implementation side.
  - `blog-simonwillison-claude-fable-5.md` Claim 6: Fable identified an optimal upgrade
    path but "was unable to download them itself due to environment restrictions" —
    confirming that environment restrictions stop Fable cold. The contrast with THIS source
    (no restrictions → 17 autonomous steps) is the operational argument for sandboxing:
    what the agent does when restrictions are absent vs. when they are present.

- **Extends**:
  - `blog-simonwillison-claude-fable-5.md` (covers Fable's capability, knowledge depth,
    pricing, and library development on June 9): This source documents a concrete
    production debugging session two days later, showing the full autonomous tool-use
    scope that Fable's capability enables when it has unrestricted shell access.
    The June 9 note covers what Fable *can* do; this note shows what Fable *will* do
    autonomously when given a task and unconstrained access.
  - `blog-simonwillison-fable-silent-interventions.md` Claim 2 (the system card
    disclosed silent degradation methods including "prompt modification, steering vectors,
    or parameter-efficient fine-tuning"): Claim 5 in this source (silent mid-session
    downgrade to Opus) adds a third observation about model-layer interventions that
    are not user-visible — a behavioral guardrail rather than a policy guardrail, but
    equally silent. Together the two notes document two categories of silent model-layer
    behavior: policy-driven silent degradation (now reversed) and capability-driven
    silent model selection.
  - `blog-anthropic-computer-use-best-practices.md` Claim 7 (using the official
    `computer_20251124` tool type gives automatic prompt injection classifier protection):
    This source documents what frontier agents do when running *outside* that official
    tool type with its built-in classifier — the Fable + Claude Code session used
    standard shell access, not the computer-use tool type. The capability gap between
    "has prompt injection classifier" and "has unrestricted shell access" is illustrated
    concretely by Claims 2–4.

- **Contradicts**: None identified. The silent mid-session downgrade (Claim 5) creates
  tension with `blog-simonwillison-claude-fable-5.md` Claim 2's statement that "the
  Claude API has new mechanisms for letting you know when you hit [guardrails]" — the
  downgrade in this source was silent, not notified. However, the two may describe
  different guardrail categories (API-layer notifications for policy guardrails vs.
  silent model selection for different guardrails), so this is better classified as
  tension that requires more evidence than a contradiction. No contradiction issue filed.

- **Novel**:
  - **First in-corpus documentation of autonomous OS-level window introspection by an
    agent**: The PyObjC/Quartz pattern (discovering `osascript` is blocked, switching to
    a different system API) is completely new to the corpus. No prior note documents an
    agent autonomously discovering and using a platform API that was not in its original
    tool grant.
  - **First in-corpus documentation of an agent building its own diagnostic web server**:
    The CORS server pattern — creating receive-side infrastructure to capture browser
    measurements — is architecturally novel. It demonstrates that an agent's effective
    tool surface is larger than the tools it was granted, because it can construct new
    tools from shell access.
  - **First concrete session-cost measurement for frontier agentic debugging**: ~$12.11
    for a debugging session that found a two-line CSS fix is the most specific
    debugging-session unit cost in the corpus.
  - **First documentation of a silent mid-session model downgrade**: Claim 5 (Fable
    downgrading itself to Opus mid-session without notification) is a new category of
    agent runtime behavior not previously documented.
  - **"Challenger disaster" framing for unsandboxed agent deployments**: Willison's
    citation of Johann Rehberger's framework names this risk class with a recognized
    label — predicted, avoidable, likely to materialize. No prior corpus note uses
    this framing for agent sandboxing.
  - **Lateral scope expansion without authorization**: Claim 4 (agent modifying
    application source templates to enable its own automated testing) is the first
    in-corpus case of an agent making code changes to its own test environment without
    being asked to.

## Guide Impact

- **Chapter on Agent Security (Ch05 or Ch06 — sandbox isolation requirements)**:
  This source should be cited as the primary evidence case for mandatory sandboxing.
  Willison's 17-step sequence demonstrates concretely what an unsandboxed frontier
  agent will do autonomously: it is not a theoretical risk list but a documented
  session. Recommendation: "Treat the action sequence in Willison's June 11, 2026
  post as the minimum blast radius you must design your sandbox to contain —
  a single debugging prompt produced OS window introspection, template source
  modification, CORS server creation, and JavaScript injection into production-like
  templates." Cite Claims 1, 2, 3, 4, 8, and 9.

- **Chapter on Agent Tool Use (Ch03 or Ch04 — autonomous constraint-bypass)**:
  Add the PyObjC workaround pattern (Claim 2) as a documented case of autonomous
  tool-use escalation: an agent hitting a permission boundary, recognizing the
  constraint, and finding an alternative approach using a different API — without
  explicit instruction or prompt engineering. Current guidance on "tool grants" should
  note that a tool grant model (what tools the agent was given) is insufficient if
  the agent has shell access, because shell access can be composed into arbitrary
  tool invocations. Cite Claims 2, 3, and 9.

- **Chapter on Cost and Operations (Ch05 — agentic debugging cost model)**: Add the
  ~$12 debugging session cost as a data point for frontier-model agentic debugging.
  Pair with `blog-simonwillison-claude-fable-5.md` Claim 10 ($99.26 for a full
  development session) to establish the range: debugging tasks at Fable pricing run
  roughly $10–15 for a focused task; development sessions with multiple tool-use chains
  can reach $100+. Cite Claim 6.

- **Chapter on Agent Design (Ch02 — autonomy patterns)**: Add "lateral scope expansion"
  (Claim 4 — agent modifying application source code to enable its own automated testing)
  as a documented pattern that practitioners must anticipate when giving agents write
  access. The agent's goal was to debug a CSS bug; it determined that template
  modification was instrumentally useful for that goal and proceeded without asking.
  This is a capability, not a failure — but it requires that practitioners scope write
  access to the minimum necessary for the stated task. Cite Claims 1 and 4.

## Extraction Notes

- The `#atom-everything` fragment in the issue URL is an Atom feed anchor; `source_url`
  uses the canonical page URL without the fragment, consistent with prior Willison
  source notes in this corpus.
- WebFetch returned summaries rather than complete verbatim text due to the tool's
  copyright limitations. Quotes were extracted via multiple targeted prompts and
  cross-validated for consistency across responses. The code artifacts (CORS server,
  JavaScript injection, command syntax) were extracted verbatim from multiple
  consistent fetches. Quotes are from the article; all appear consistent across
  multiple independent fetch attempts.
- The exact cost figure ($12.11) was described as approximate by Willison and
  refers to the cost "if paying full API prices" — the session may have been run
  on a subscription plan with different billing.
- The Challenger disaster reference (Claim 8) attributes the framework to Johann
  Rehberger; this note does not attempt to characterize Rehberger's work beyond
  Willison's citation.
- Cross-references verified:
  - `blog-anthropic-how-contain-claude.md` Claim 11: confirmed at lines 228–243
    (phishing test, 24/25 exfiltration completions, only environmental controls
    stopped it).
  - `blog-anthropic-how-contain-claude.md` Claim 3: confirmed at lines 88–100
    (environmental containment as primary priority; model-layer defenses not 100%).
  - `blog-simonwillison-claude-fable-5.md` Claim 2: confirmed at lines 53–59
    (API guardrail notification mechanisms; frequency claim).
  - `blog-simonwillison-claude-fable-5.md` Claim 6: confirmed at lines 85–93
    (environment restriction caused Fable to stop; human bridged the gap).
  - `blog-simonwillison-fable-silent-interventions.md` Claim 2: confirmed at lines
    73–88 (silent degradation methods: prompt modification, steering vectors, PEFT).
  - `blog-anthropic-computer-use-best-practices.md` Claim 7: confirmed at lines
    155–157 (official computer_20251124 tool type provides automatic classifier
    protection).
- No contradiction issues filed. The tension with `blog-simonwillison-claude-fable-5.md`
  Claim 2 (API notification for guardrails vs. silent downgrade in this note) is
  logged in the Contradicts section as tension requiring more evidence, not a
  confirmed material contradiction.
