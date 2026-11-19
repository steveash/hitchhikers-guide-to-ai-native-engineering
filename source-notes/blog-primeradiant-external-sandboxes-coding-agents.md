---
source_url: https://blog.primeradiant.com/external-sandboxes-for-coding-agents/
source_type: blog-post
title: "External sandboxes for coding agents"
author: Simon Willison (with Prime Radiant)
date_published: 2026-11-16
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4818"
---

# External sandboxes for coding agents

> Prime Radiant and Simon Willison describe the "external sandbox" pattern (agent on the host, executed commands in a separate sandbox over a localhost API), with a default-deny HTTP/HTTPS allow-list proxy, proxy-side credential replacement, and a candid note that Claude Code's Read/Edit tools bypass the sandbox.

## Source Context

- **Type**: blog-post. Primary post on the Prime Radiant blog (2026-11-16, byline Simon Willison, ~12 min read); Willison's link post (https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) is a short summary and adds nothing substantive beyond framing (motivation: safely trying local models).
- **Author credibility**: Willison is a widely cited LLM-tooling commentator; Prime Radiant is the lab behind Superpowers. Claims are about their own prototypes, not independently evaluated.
- **Scope**: Architecture, three prototype servers, per-agent integration (Claude Code, Codex, Pi), network proxy and credential replacement, limitations. No benchmarks, no security audit, no escape testing. Linked repos (prime-radiant-inc/external-sandbox) were not read; only the post was.

## Extracted Claims

### Claim 1: Running the agent outside the sandbox ("external sandbox") is preferable to running the agent inside it
- **Evidence**: Design rationale; authors say they explored both approaches. No measurements.
- **Confidence**: emerging
- **Quote**: "We chose the second. This avoids weird behavior where the agent can modify itself or its direct environment, and keeps the sandbox boundary well defined and easier to audit."
- **Our assessment**: Plausible and consistent with the Cowork design in blog-anthropic-how-contain-claude (Claim 9: agent loop outside the guest). Tradeoff left unstated: the agent process and its own tools (and its credentials for the model API) remain on the host, unprotected.

### Claim 2: A sandbox is protection that does not depend on model judgment, which matters most for smaller/local models
- **Evidence**: Argument; contrasts Claude Code auto mode and Codex auto-review.
- **Confidence**: emerging
- **Quote**: "A sandbox is a protection that doesn't depend on any model's judgment."
- **Our assessment**: Matches the "environmental containment first" stance (how-contain-claude Claims 3-4). The claim that lighter models are "more prone to mistakes and are easier victims of deliberate prompt injection attacks" is asserted without data.

### Claim 3: Manual approval of every action is a poor safety mechanism
- **Evidence**: Assertion/anecdote.
- **Confidence**: anecdotal (here); corroborated elsewhere
- **Quote**: "It's frustratingly slow, and quickly leads to decision fatigue where we instinctively approve everything without taking time to fully understand the question."
- **Our assessment**: Corroborated quantitatively by how-contain-claude Claim 6 (93% of prompts approved).

### Claim 4: Network is default-deny; an optional proxy allows only listed hosts and HTTP methods
- **Evidence**: Config format and behavior described; blocked-request UI screenshot (not reproduced).
- **Confidence**: emerging
- **Quote**: "By default, the three sandbox implementations do not have any external network access."
- **Our assessment**: Sound baseline against the lethal trifecta's exfiltration leg. Note the proxy MITMs TLS via an injected CA (SSL_CERT_FILE, REQUESTS_CA_BUNDLE, NODE_EXTRA_CA_CERTS) and "Code that ignores these settings and tries to connect directly is still blocked." Method-level limits (GET/HEAD only) give read-only access to hosts. See blog-green-sandboxing-rogue-agents Claim 1 for how an allowed registry proxy can still become a covert channel.

### Claim 5: Credential replacement lets sandboxed code make authenticated API calls without the agent or sandbox ever holding the secret
- **Evidence**: Concrete proxy.json (see artifacts): the guest holds a placeholder; the proxy, running on the host with the real env var, swaps the authorization header for matching hosts.
- **Confidence**: emerging
- **Quote**: "This means agents can make authenticated calls to APIs without the API key being made visible to the agent itself."
- **Our assessment**: Strong, concrete mechanism for "capabilities, not credentials". Limits the authors state themselves (next claim); also the agent can still *use* the credential for anything the allowed host/method permits.

### Claim 6: Credential replacement does not protect against an allowed host that echoes the credential back
- **Evidence**: Authors' own caveat.
- **Confidence**: settled (logical consequence)
- **Quote**: "An allowed host could still echo a credential back in its response, so only use credential rules with services you trust, and keep their methods and paths narrow."
- **Our assessment**: Useful honest limit. Guide should state: scope credential rules to host+method+path, trusted hosts only.

### Claim 7: Claude Code's Read and Edit tools are not routed through the sandbox; only Bash is
- **Evidence**: Integration description; Claude Code uses CLAUDE_CODE_SHELL_PREFIX, which wraps only Bash commands.
- **Confidence**: emerging (vendor behavior as of this post; may change)
- **Quote**: "Unlike the other agents, Claude Code's read and edit tools do not run via the sandbox. The mount rules limit what Claude's Bash commands can touch, but Claude can still read and edit files on your Mac directly."
- **Our assessment**: Important scope caveat for any "sandboxed Claude Code" advice built on this pattern. Codex (exec-server, incl. apply_patch) and Pi (extension replacing all tools) route file operations too.

### Claim 8: Each agent offers a different hook for redirecting execution, so one protocol serves all three
- **Evidence**: Three integrations: `CLAUDE_CODE_SHELL_PREFIX`; Codex `environments.toml` pointing at a `/codex` WebSocket (exec-server JSON-RPC, experimental, tested against Codex CLI 0.164.0 with a simulated model); Pi extension replacing bash/read/write/edit/grep/find/ls.
- **Confidence**: emerging
- **Quote**: "Different coding agents provide different ways of ensuring all executed commands run in a custom environment."
- **Our assessment**: Shows harness extensibility points are what make external sandboxing feasible. Codex flag `--sandbox danger-full-access` is used so Codex does not layer its own sandbox.

### Claim 9: Fail-closed integration: Pi with built-in tools disabled errors rather than falling back to local execution
- **Evidence**: Documented behavior.
- **Confidence**: emerging
- **Quote**: "If the sandbox cannot be reached, the tools return an error rather than falling back to those defaults."
- **Our assessment**: Same fail-closed principle as docs-github-copilot-app-local-sandboxing Claim 6.

### Claim 10: Three prototype backends implement the same protocol (v86/WASM, Apple Containers, QEMU via Quicksand), with a spec and conformance tool
- **Evidence**: Packages on npm/PyPI; ports 8686/8687/8688. v86 needs only Node 22.19+; container needs Apple silicon + container CLI; Quicksand ships QEMU and Alpine as Python wheels.
- **Confidence**: emerging
- **Quote**: "We've also produced a specification and conformance testing tool for that API, making it easy to build future, compatible sandbox servers on top of other technologies."
- **Our assessment**: No comparative performance or isolation-strength data is given, so the backend tradeoffs triage asked about can only be inferred (WASM emulation = easiest install, likely slowest; VM/containers = stronger/faster but platform-bound). Flag as inference.

### Claim 11: The prototypes are unaudited and have residual risks
- **Evidence**: Authors' stated limitations.
- **Confidence**: settled (self-reported)
- **Quote**: "they have not been audited to a level that you should trust them with sensitive workloads."
- **Our assessment**: Treat as pattern demonstration, not a vetted tool. Also: "A read-write mount still lets the agent damage anything in that folder, so keep it under version control and use read-only mounts where you can." Linux guest means macOS-built node_modules/.venv need reinstall.

## Concrete Artifacts

```json
// proxy.json from the post (credential replacement)
{
  "allow": [
    { "origin": "https://pypi.org", "methods": ["GET", "HEAD"] },
    { "origin": "https://files.pythonhosted.org", "methods": ["GET"] },
    {
      "origin": "https://api.github.com",
      "methods": ["GET"],
      "credential": {
        "header": "authorization",
        "placeholder": "Bearer placeholder-github-token",
        "secretEnv": "GITHUB_TOKEN",
        "prefix": "Bearer "
      }
    }
  ],
  "guestEnv": { "GITHUB_TOKEN": "placeholder-github-token" }
}
```

```bash
# Claude Code against a sandbox (from the post)
CLAUDE_CODE_SHELL=/bin/bash \
CLAUDE_CODE_TMPDIR="$PWD/.external-sandbox-claude-tmp" \
CLAUDE_CODE_SHELL_PREFIX="$PREFIX_DIR/claude-shell-prefix.sh" \
EXTERNAL_SANDBOX_API_URL=http://127.0.0.1:8686 \
claude
```

```toml
# Codex ~/.codex-external-sandbox/environments.toml (from the post)
default = "external-sandbox"
include_local = false
[[environments]]
id = "external-sandbox"
url = "ws://127.0.0.1:8686/codex"
```

Two-command demo: `npx --yes external-sandbox-v86 --preserve-paths --mount-rw "project=$PWD"` then Pi with `-e npm:external-sandbox-pi --no-builtin-tools --sandbox-url http://127.0.0.1:8686`.

## Cross-References

- **Corroborates**: blog-anthropic-how-contain-claude (Claim 3 environmental containment first; Claim 6 approval fatigue; Claim 9 agent loop outside the guest in Cowork); docs-github-copilot-app-local-sandboxing (Claim 6 fail-closed).
- **Contradicts**: None found. (Claim 7 here is a scope caveat on Claude Code's sandboxing, not a disagreement with a corpus claim.)
- **Extends**: blog-simonwillison-smolmachines-untrusted-sandbox (same author's interest; there the sandbox is hardware-isolated VM for untrusted code, here it is a protocol layer with a proxy); blog-green-sandboxing-rogue-agents (Claim 1: allowed egress proxies can become channels; the echo-back caveat here is the same class of risk).
- **Novel**: Proxy-side credential replacement with placeholder in guest; per-method host allow-list; agent-vs-sandbox split with a shared spec/conformance tool; explicit Claude Code Read/Edit scope gap; per-agent redirection hooks (SHELL_PREFIX, exec-server, Pi extension).

## Guide Impact

- **Chapter 06**: Add the external-sandbox pattern next to the existing "capabilities, not credentials" statement, with the placeholder + proxy-injection mechanism and its echo-back limit (Claims 5-6). Add that default-deny egress with method-limited allow-lists is the baseline (Claim 4).
- **Chapter 06 / 02**: State that for Claude Code, a shell-prefix sandbox covers Bash only; Read/Edit still run on the host (Claim 7).
- **Chapter 02**: Note that harness hooks for redirecting execution (shell prefix, exec-server, tool-replacement extensions) determine whether external sandboxing is possible (Claim 8).
- **Chapter 03**: Minor: sandboxed execution as a verification environment; Linux guest means rebuilt dependencies (Claim 11).

## Extraction Notes

- Read the full Prime Radiant post (fetched raw HTML, all sections) and Willison's link post. Quotes copied from the fetched text. Screenshots/diagram not viewable.
- Did not follow the linked repo READMEs, protocol spec or v86 proxy guide; triage suggested preferring them, so details such as path-level policy and the spec are unverified here.
- No contradiction issue filed.
