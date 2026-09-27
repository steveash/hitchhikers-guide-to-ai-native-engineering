---
source_url: https://simonwillison.net/2026/Sep/20/llm-keys-ui/
source_type: blog-post
title: "Release: llm-keys-ui 0.1"
author: Simon Willison
date_published: 2026-09-20
date_extracted: 2026-09-27
last_checked: 2026-09-27
status: current
confidence_overall: emerging
issue: "#3749"
---

# Release: llm-keys-ui 0.1

> A minimal release announcement for llm-keys-ui — a no-auth, write-only local
> web UI for setting API keys used by Simon Willison's `llm` CLI — built
> specifically so a phone-controlled remote coding agent (Codex Remote) can be
> told to expose a key-entry form on the local network or a Tailscale device
> IP, instead of the human pasting a raw API key into the agent's chat
> interface.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release
  announcement format on `simonwillison.net`; four short paragraphs, one
  command example, and two screenshots with descriptive alt text). Willison's
  GitHub repository (`github.com/simonw/llm-keys-ui`) README was also fetched
  and read in full, per MINER.md §1's instruction to follow substantive linked
  pages — the blog post itself does not describe the tool's security model,
  default network binding, or installation mechanism; all of that lives only
  in the README. The GitHub release notes for tag `0.1` were also checked via
  the GitHub API and contain no additional content beyond "- Initial
  release."
- **Author credibility**: Simon Willison is the creator of the `llm` CLI tool
  and the author of this plugin — first-party release documentation of his
  own software, describing his own workflow. No vendor affiliation; this is a
  personal tool built to solve a problem Willison describes encountering
  himself. Willison has a long track record in this corpus of shipping small,
  single-purpose `llm`/Datasette plugins with explicit, prominently-stated
  security caveats rather than implying guarantees the software doesn't meet
  (cf. `blog-simonwillison-datasette-tailscale.md`).
- **Scope**: Covers the initial 0.1 release of llm-keys-ui: the motivating
  problem (configuring API keys on a remote machine controlled via a phone
  app, without pasting them into the agent's chat interface), the core usage
  pattern (`uvx --with llm-keys-ui llm keys-ui --all`, then `llm keys get
  <provider>` to retrieve a key later), and — from the README — the tool's
  network binding options, authentication posture, and write-only design.
  Does NOT cover: any production or team-scale usage of the tool, independent
  security review, how the `llm` ecosystem's existing key storage mechanism
  works under the hood, or any adoption/usage data beyond Willison's own
  account of building and using it once.

## Extracted Claims

### Claim 1: llm-keys-ui exists to solve one specific, narrow problem — Willison did not want to paste API keys directly into a mobile-controlled remote agent's chat session
- **Evidence**: First-person statement of motivation, opening the post.
- **Confidence**: anecdotal (a single author's stated motivation for building a tool for himself)
- **Quote**: "This plugin solves a very specific problem." ... "I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly."
- **Our assessment**: This is a specific, relatable instance of a broader problem already documented in this corpus from the enterprise side — keeping raw credential values out of any interface a human types into or an agent reads from. Willison's framing is narrower than the enterprise sources: his concern is specifically the *human-to-agent chat channel* (typing a key into the ChatGPT app), not the agent's own execution context. That distinction matters — see Claim 3 and the Cross-References tension with `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`.

### Claim 2: The tool is designed to be launched by the agent itself, which then reports back a reachable URL — including local-network or Tailscale device IPs — for a human to open and enter keys into
- **Evidence**: Direct workflow description plus a screenshot (alt text extracted verbatim from the page's HTML) showing the agent's chat response.
- **Confidence**: settled (first-party description of the tool's actual, demonstrated usage pattern, corroborated by the screenshot)
- **Quote**: "With this plugin, I can tell Codex to run: [`uvx --with llm-keys-ui llm keys-ui --all`] Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys."
- **Our assessment**: The notable design choice here is inverting who initiates key setup: rather than the human pre-provisioning a machine with keys before handing it to an agent, the human tells the *agent* to start the key-entry server and report the URL back through the chat interface. The API key value itself never needs to appear in that chat exchange — only a URL does. This is a narrow but genuine improvement over "paste the key into chat": it moves the secret-entry step out-of-band from the primary conversational channel, onto a separate (if unauthenticated — see Claim 5) web form.

### Claim 3: Once a key is stored, the agent (not just the human) retrieves it later at the point of use, as part of a shell command it executes itself
- **Evidence**: Direct statement of the retrieval workflow.
- **Confidence**: settled (first-party description of the tool's intended usage)
- **Quote**: "Then later it can use a command like `llm keys get anthropic` as part of a shell command when it needs to use a key."
- **Our assessment**: This is the claim most worth flagging for the guide. Unlike the vault-based patterns already in this corpus — where a placeholder is injected into the sandbox and the agent explicitly "never sees" the resolved credential (`blog-anthropic-managed-agents-scheduled-vaults.md` Claim 4: "The agent never sees your key because the sandbox only holds a placeholder") — `llm keys get anthropic` is a command the agent runs itself, whose output is the raw key value. Whether that value then flows back into the agent's own context window depends entirely on how the surrounding harness handles shell tool output, something this source does not address at all. The post solves "don't type the key into the chat UI"; it does not claim to solve, and should not be read as solving, "keep the key out of the agent's context." See the Cross-References tension with `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` below.

### Claim 4: The web interface is write-only — once a key is saved, its value cannot be read back through the tool
- **Evidence**: An explicit README statement plus corroborating screenshot alt text (extracted verbatim from the page's HTML, describing the second screenshot).
- **Confidence**: settled (first-party statement of a specific, checkable design property)
- **Quote (README)**: "Existing key values cannot be read using this tool." **Quote (screenshot alt text, from the blog post's HTML)**: "LLM keys web interface listing anthropic, openai, openrouter, and qwen-dummy as stored keys, with a form containing Key name and New value fields and a Save key button. Existing key values are never displayed."
- **Our assessment**: This is a genuine, verifiable mitigation given the tool's other constraints (no authentication — Claim 5): anyone who can reach the web UI while it is running can overwrite a key with a new value, but cannot exfiltrate the existing one through the UI itself. It does not protect against the value being read some other way (e.g., from the underlying storage file, or via `llm keys get` once the reader has shell access), but it does close off "browse to the page and read the keys" as an attack path specifically through the web form.

### Claim 5: The interface implements no authentication at all, and the author explicitly instructs users to shut the server down once keys are set rather than leaving it running
- **Evidence**: Explicit README security-model statement.
- **Confidence**: settled (first-party, unambiguous statement of a security limitation, not a hedge)
- **Quote**: "The interface does not implement authentication. Stop the server once you have set your keys."
- **Our assessment**: This is the load-bearing caveat for the entire tool, and it is stated plainly rather than buried. Combined with Claim 6 (opt-in exposure beyond localhost), the security model is: anyone who can reach the server while it is running and before it is stopped can both read the list of configured key *names* (see the screenshot) and write new key *values* for any of them — there is no login, token, or other gate. The tool's actual safety depends entirely on the operator (or the agent acting on the operator's behalf) starting the server, doing the key-entry task, and then stopping it promptly — a manual, easy-to-skip step with no enforcement mechanism in the tool itself.

### Claim 6: By default the server binds only to localhost; reaching it from another device requires explicitly opting in via a host flag or the `--all` option, which listens on every network interface and prints a URL for each assigned IPv4 address
- **Evidence**: README usage documentation, showing the default and the two ways to widen exposure.
- **Confidence**: settled (first-party documentation of the exact CLI flags and their effect)
- **Quote**: "Start the server on `127.0.0.1:8010`: `llm keys-ui`" ... "Use `-h` or `--host` to listen on a different interface: `llm keys-ui -h 0.0.0.0`" ... "The `--all` option also listens on `0.0.0.0` and prints an HTTP URL for every IPv4 address assigned to the computer... Use this if you want to set keys for a machine accessible via your local network or over Tailscale."
- **Our assessment**: The default-localhost-only, opt-in-wider-exposure design is the right default given Claim 5's lack of authentication — a user who never passes `-h` or `--all` never exposes the no-auth form beyond the machine itself. The `--all` flag's behavior (print a URL per assigned IPv4 address, explicitly calling out Tailscale) is the same "reach a machine over your private/mesh network without configuring public ingress" pattern already documented from Willison's Datasette ecosystem in `blog-simonwillison-datasette-tailscale.md`, applied here to the `llm` ecosystem instead. Neither tool requires the user to already have a Tailscale-specific integration — `llm-keys-ui` just relies on Tailscale (or any private LAN) already making the machine's IP reachable, whereas `datasette-tailscale` runs an actual Tailscale sidecar node. The two are different depths of Tailscale integration solving structurally the same "reach my dev machine privately" problem.

### Claim 7: llm-keys-ui is installed and run as a standard `llm` CLI plugin, and can be run ad hoc via `uvx` without a persistent install
- **Evidence**: README installation instructions and the blog post's own invocation, which uses `uvx --with llm-keys-ui` rather than a prior `llm install` step.
- **Confidence**: settled (first-party documentation of both installation paths)
- **Quote**: "Install this plugin in the same environment as [LLM](https://llm.datasette.io/). `llm install llm-keys-ui`"
- **Our assessment**: The `uvx --with llm-keys-ui llm keys-ui --all` invocation used in the blog post's actual workflow (Claim 2) never runs a persistent `llm install` at all — `uvx --with` fetches and runs the plugin for a single invocation. This matters for the remote-agent use case specifically: the agent doesn't need llm-keys-ui permanently installed on every remote machine it might touch; it can pull and run it on demand for the one task (setting keys), consistent with the "stop the server once you're done" guidance in Claim 5 — the tool is designed to be ephemeral, not a persistent service.

### Claim 8: The tool supports storing keys for multiple named providers side by side in the same store
- **Evidence**: Screenshot alt text (verbatim from the blog post's HTML), showing four provider keys configured simultaneously.
- **Confidence**: settled (demonstrated in the author's own screenshot of the running tool)
- **Quote**: "LLM keys web interface listing anthropic, openai, openrouter, and qwen-dummy as stored keys, with a form containing Key name and New value fields and a Save key button."
- **Our assessment**: This confirms the tool is a general key-value store scoped to the `llm` CLI's existing multi-provider key mechanism (Anthropic, OpenAI, OpenRouter, and a locally-named "qwen-dummy" entry are all present at once) rather than a single-provider point solution — consistent with `llm`'s own long-standing design of supporting many model providers through one CLI.

### Claim 9: The release itself carries no changelog beyond marking it the initial version
- **Evidence**: GitHub Releases API response for tag `0.1`.
- **Confidence**: settled (directly queried from the GitHub API, not paraphrased)
- **Quote**: "- Initial release."
- **Our assessment**: Confirms this is a first release with no prior version history to compare against — there is no evidence yet of the tool evolving in response to any reported problem or security review; everything known about it comes from this one post and its README as they exist today.

## Concrete Artifacts

### Blog post body (verbatim, from `simonwillison.net/2026/Sep/20/llm-keys-ui/`)

```
This plugin solves a very specific problem.

I've started using Codex Remote to run coding agents on various machines
while controlling them from my phone.

Sometimes I use those machines to hack on LLM projects, and occasionally
that means I need to configure an API key.

I don't like pasting API keys into agent sessions, so I wanted a way to get
those keys onto a machine without pasting them into the ChatGPT app
directly.

With this plugin, I can tell Codex to run:

    uvx --with llm-keys-ui llm keys-ui --all

Then have it tell me the URL - including local network or Tailscale device
IPs - for an interface to save additional API keys.

Then later it can use a command like `llm keys get anthropic` as part of a
shell command when it needs to use a key.
```

### Screenshot alt text (verbatim, from the page's HTML `<img alt="...">` attributes)

```
Image 1: "Chat conversation requesting uvx --with llm-keys-ui llm keys-ui
--all, with a response listing four server URLs on port 8010 and confirming
the server is still running."

Image 2: "LLM keys web interface listing anthropic, openai, openrouter, and
qwen-dummy as stored keys, with a form containing Key name and New value
fields and a Save key button. Existing key values are never displayed."
```

### README (verbatim, from `github.com/simonw/llm-keys-ui`, fetched via GitHub API)

```
A local web UI for setting keys used by LLM.

This plugin is particularly useful if you are running a coding agent on a
remote machine and want to set some API keys without pasting them into the
agent context.

## Installation

llm install llm-keys-ui

## Usage

Start the server on 127.0.0.1:8010:

llm keys-ui

The port can be changed with -p or --port:

llm keys-ui -p 8080

Use -h or --host to listen on a different interface:

llm keys-ui -h 0.0.0.0

The --all option also listens on 0.0.0.0 and prints an HTTP URL for every
IPv4 address assigned to the computer:

llm keys-ui --all

Use this if you want to set keys for a machine accessible via your local
network or over Tailscale.

The interface does not implement authentication. Stop the server once you
have set your keys.

Existing key values cannot be read using this tool.
```

### GitHub release body for tag `0.1` (verbatim, via GitHub API)

```
- Initial release.
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-datasette-tailscale.md`,
`blog-simonwillison-sean-lynch-mcp-auth-gateway.md`,
`blog-anthropic-managed-agents-scheduled-vaults.md`,
`blog-openai-1password-codex-case-study.md`, and
`blog-anthropic-zero-trust-ai-agents.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located
and confirmed against that note's own numbered `### Claim N:` headings (or,
for the zero-trust eBook, its Concrete Artifacts section) before writing
this section.

- **Corroborates**:
  - `blog-simonwillison-datasette-tailscale.md` Claim 1 (Tailscale/local-network
    reachability without public internet exposure) and Claim 2 (Datasette
    itself binds only to 127.0.0.1; the Tailscale sidecar handles all external
    connectivity): this source's Claim 6 (the server binds to localhost by
    default; `--all` prints a URL per assigned IPv4 address, explicitly naming
    Tailscale) is a second,
    independently-shipped Willison tool using the same "reach my machine over
    a private network by explicit opt-in flag" design, this time in the `llm`
    ecosystem rather than Datasette's.
  - `blog-simonwillison-datasette-tailscale.md` Claim 6 (Willison's pattern of
    shipping minimal alpha releases with explicit, prominently-stated
    caveats): this source's Claim 5 ("The interface does not implement
    authentication. Stop the server once you have set your keys.") is a
    second instance of the same authorial habit — stating a security
    limitation plainly in the README rather than omitting or softening it.

- **Contradicts**: No formal MINER.md §4a contradiction issue filed. Two
  tensions are worth flagging prominently, both judged to be differences in
  target scenario (a single developer's personal remote-access workflow vs.
  enterprise production credential architecture) rather than a factual
  disagreement about the same claim:
  1. **vs. `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1**
     ("The real valuable capability MCP offers over skills/CLI is isolating
     the auth flow outside of the agent's context window, and potentially
     out of the harness completely.") — this source's Claim 3 describes the
     opposite mechanism for its own use case: the agent itself runs `llm
     keys get anthropic` and gets the raw value back as command output,
     which is the CLI-retrieval pattern Lynch's quote contrasts unfavorably
     with MCP's server-side auth isolation. Willison's post never claims to
     solve context-window isolation — it solves a narrower problem (don't
     type the key into chat) — but a reader could easily conflate the two.
     The guide should keep them distinct: llm-keys-ui improves the
     human-to-agent entry channel; it does nothing for the
     agent-to-model-context channel Lynch is describing.
  2. **vs. `blog-anthropic-zero-trust-ai-agents.md` Concrete Artifacts →
     Phase 6 / Claim 12** ("Static API keys and shared service-account
     passwords are... no longer a legitimate entry point, not even at
     Foundation. Short-lived, narrowly-scoped tokens issued by an identity
     provider are the new baseline.") and `blog-anthropic-managed-agents-scheduled-vaults.md`
     Claim 4 ("The agent never sees your key because the sandbox only holds
     a placeholder.") — llm-keys-ui is explicitly a persistent, static,
     plaintext API key store with no authentication, retrieved directly by
     the agent's own shell commands. Measured against the Zero Trust
     eBook's Foundation-tier bar or the vault+placeholder pattern, it is the
     pattern those sources argue against. This is not filed as a
     contradiction because the two source families address different
     scales and audiences (a solo developer's personal machine vs.
     enterprise agent deployments with a security team) — a genuine
     conditioning variable, not opposing claims about the same situation —
     but the gap is large enough that the guide should not present
     llm-keys-ui's approach as a substitute for vault-based credential
     isolation at any team or production scale.

- **Extends**:
  - `blog-openai-1password-codex-case-study.md` Claim 10 (secret references
    resolved and injected only at the point of action, so plaintext never
    enters the model's context) and `blog-anthropic-managed-agents-scheduled-vaults.md`
    Claim 4 (vault placeholder pattern): both describe the enterprise-scale
    version of the same underlying problem this source's Claim 1 names —
    getting a credential to an agent's execution environment without a
    human (or, in the enterprise case, the model) handling the raw value
    unnecessarily. This source is the lightweight, single-developer end of
    the same problem spectrum, solved with a manual, unauthenticated web
    form instead of a managed vault and proxy.
  - `blog-simonwillison-datasette-tailscale.md` overall: extends Willison's
    demonstrated pattern of private-network-reachable local tools (a
    Datasette instance there, a key-entry form here) into a second,
    independent tool in a different plugin ecosystem, reinforcing that this
    is a recurring personal-infrastructure design habit rather than a
    one-off.

- **Novel**:
  - **First corpus source describing a tool whose sole purpose is
    "let a phone-controlled remote coding agent request its own key-entry
    UI"**: no existing note documents this specific bootstrap-credentials
    workflow for mobile-controlled remote agents (Codex Remote).
  - **Write-only key storage as an explicit, named design property**
    (Claim 4): no prior corpus source documents a credential tool that can
    be written to but not read from as its stated mitigation for running
    without authentication.
  - **A concrete, first-person example of the CLI-retrieval-by-the-agent
    pattern Sean Lynch's quote argues against** (Claim 3): the corpus
    previously had Lynch's abstract argument for auth isolation but no
    named tool whose documented usage is the pattern he contrasts it with.

## Guide Impact

- **Chapter 02 (Harness Engineering) / credential handling**: Present
  llm-keys-ui as a concrete, relatable "minimum viable personal workflow"
  for a narrow problem (don't paste API keys into a phone chat UI), while
  explicitly contrasting it with the vault+placeholder pattern already
  documented from Anthropic Managed Agents (`blog-anthropic-managed-agents-scheduled-vaults.md`
  Claim 4) and 1Password's point-of-action credential resolution
  (`blog-openai-1password-codex-case-study.md` Claim 10). The guide should
  be explicit that this tool solves the human-to-agent entry channel only
  (Claim 1, Claim 2) and makes no claim about, and does not achieve,
  keeping the credential out of the agent's own context (Claim 3) — a
  distinction a reader skimming the blog post alone would likely miss.
- **Chapter 06 (Security)**: Cite Claim 5 and Claim 6 as a worked example of
  a tool whose author states its security ceiling plainly (no
  authentication; stop the server after use) rather than implying a
  guarantee it doesn't meet — a pattern worth holding up alongside
  `blog-simonwillison-datasette-tailscale.md`'s similar "unvalidated
  cryptography" disclosure as a model for how small tools should document
  their own limitations. Pair this with the Zero Trust eBook's Foundation-tier
  bar (`blog-anthropic-zero-trust-ai-agents.md`, Phase 6) to make explicit
  that this tool's static, no-auth key store is appropriate for solo,
  personal use only — not a pattern to scale to a team or production agent
  deployment.
- **Chapter 04 (Context Engineering) / prompt injection and secrets
  exposure**: Use Claim 3 (`llm keys get anthropic` run "as part of a shell
  command" by the agent) as a concrete prompt for a question the guide
  should raise explicitly: when an agent's own shell tool retrieves a
  secret, does the harness let that value flow back into the model's
  context via the tool-output channel? This source does not answer the
  question for its own tool, which is itself the point — practitioners
  adopting a similar pattern should check their own harness's tool-output
  handling rather than assume "the human never typed it" is equivalent to
  "the model never saw it."

## Extraction Notes

- **WebFetch's summarized output was not trusted for quotes.** An initial
  WebFetch pass on the blog post returned a plausible-sounding but
  restructured paraphrase (merging separate sentences and describing the
  screenshots only in general terms). Per MINER.md §2a, this note instead
  fetched the raw page HTML directly via `curl` and read the actual
  `<div class="beat-note blogmark-body">` markup, extracting the blog post
  body and both `<img alt="...">` attributes character-for-character. Every
  `Quote` field attributed to the blog post in this note was verified
  against that raw HTML, not against the WebFetch output.
- **One substantive linked page followed, per MINER.md §1.** The blog post
  itself contains no security-model or installation detail — that
  information exists only in the GitHub repository's README
  (`github.com/simonw/llm-keys-ui`), which was fetched via the GitHub
  Contents API (`/repos/simonw/llm-keys-ui/readme`), base64-decoded, and
  read in full. The GitHub Releases API was also checked for tag `0.1`
  and found to contain only "- Initial release." with no further content.
  No other linked pages (e.g., the Codex Remote documentation link) were
  substantive enough to warrant following per MINER.md's judgment call —
  Codex Remote itself is not the subject of this issue.
- **Source is thin by design.** This is a "beat" — Willison's shortest
  post format — plus a short plugin README. Nine claims were extracted from
  the combination of the two; a shallow read of the blog post alone would
  have yielded only Claims 1–3 and 7–8, missing the security-model claims
  (4, 5, 6) that exist only in the README.
- **Confidence set to `emerging`.** The tool's mechanics (network binding,
  write-only design, no-auth posture, installation path) are settled,
  verifiable, first-party facts. What is not yet established is any
  independent validation of the tool in practice beyond the author's own
  one-time account of building and using it — there is no adoption data,
  no security review, and no report of anyone besides Willison using it.
  This mirrors the calibration used for `blog-simonwillison-datasette-tailscale.md`
  (also a first-release "beat" + README pair from the same author, rated
  `emerging` for the same reason).
- **No contradiction issues filed.** Two tensions were identified and
  evaluated against MINER.md §4a (see Cross-References → Contradicts): the
  CLI-retrieval-by-agent pattern versus Sean Lynch's auth-isolation
  argument, and the static-no-auth-key-store design versus the Zero Trust
  eBook's Foundation-tier bar and the vault+placeholder pattern. Both were
  judged to be differences in target scenario and scale (personal tool vs.
  enterprise production architecture) rather than factual disagreements
  about the same claim. The Assayer or Smith may reach a different
  conclusion on either.
