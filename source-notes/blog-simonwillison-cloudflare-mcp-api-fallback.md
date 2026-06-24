---
source_url: https://simonwillison.net/2026/Jun/16/captcha-on-at-least-one-ampersand/
source_type: blog-post
title: "TIL: Cloudflare CAPTCHA on at least one ampersand"
author: Simon Willison
date_published: 2026-06-16
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: anecdotal
issue: "#1285"
---

# TIL: Cloudflare CAPTCHA on at least one ampersand

> Short practitioner TIL demonstrating two Claude Code patterns: (1) project-scoped MCP
> configuration via `.mcp.json` + `enabledMcpjsonServers` in `.claude/settings.local.json`,
> and (2) the MCP → direct API fallback workflow when an MCP server lacks the required
> capabilities — with Claude Code handling the full API exploration loop (zone discovery,
> rule listing, PATCH update) via curl/jq.

## Source Context

- **Type**: blog-post / TIL — Simon Willison's "Today I Learned" format. The
  simonwillison.net post is a short summary link; the full technical content lives at
  `https://til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand`.
  Both pages were read in full; all quotes and artifacts are drawn from the TIL page.
- **Author credibility**: Simon Willison — creator of Django, prolific AI tooling
  commentator, 25-year practitioner with no vendor affiliation. His TIL posts are
  first-person practice notes: specific, reproducible, and grounded in real task
  outcomes. This post documents an actual workflow Willison ran to solve a concrete
  infrastructure problem on his own site.
- **Scope**: Covers two things: (1) a Cloudflare WAF rule for narrowing CAPTCHA scope
  on faceted search (not guide-relevant per triage), and (2) the Claude Code workflow
  that produced it — including a project-scoped Cloudflare MCP setup, discovery that
  the MCP lacked the needed WAF-rule tools, and a Claude Code–driven pivot to direct
  API calls. Does NOT cover: production deployment patterns, multi-agent coordination,
  or general MCP design principles.

## Extracted Claims

### Claim 1: A dedicated project folder with `.mcp.json` + `enabledMcpjsonServers` in `.claude/settings.local.json` scopes an MCP server to only that project context

- **Evidence**: Willison describes the exact setup he used, including what Claude Code
  produced when he pasted the MCP JSON and asked it to "set this up to only work in
  this project folder."
- **Confidence**: settled (the configuration mechanism is reproducible; Willison's
  description matches Claude Code's documented project settings behavior)
- **Quote**: "(I actually set it up by pasting the MCP JSON into Claude Code and saying
  'set this up to only work in this project folder', but the above is effectively what
  it did.)"
- **Our assessment**: This is the first concrete practitioner demonstration in the corpus
  of project-scoped MCP configuration. The pattern — dedicated project folder, `.mcp.json`
  defining the server, `.claude/settings.local.json` with `enabledMcpjsonServers` listing
  only the servers active for that project — limits MCP token overhead to sessions
  started in that specific folder. It is the practical implementation of `blog-bswen-mcp-token-cost.md`
  Claim 4 ("Limit to 3-6 essential servers — Be ruthless about necessity"): rather than
  adding the Cloudflare MCP globally, Willison isolated it so it only incurs cost in the
  relevant context. The configuration is also a natural extension of Claude Code's project
  isolation model — the same folder contains the `.mcp.json` (what servers are available),
  `.claude/settings.local.json` (which are enabled for this project), and all related work.

### Claim 2: Cloudflare's MCP server (at `https://mcp.cloudflare.com/mcp`) does not implement tools to view and modify WAF Custom Rules

- **Evidence**: Willison completed the full setup and OAuth flow, then discovered the
  limitation through attempted use.
- **Confidence**: anecdotal (single practitioner's observation at a point in time; the
  MCP server may be updated; Willison qualifies with "as far as I can tell")
- **Quote**: "which didn't work, because as far as I can tell Cloudflare's MCP doesn't
  yet implement tools to view and modify the rules in question."
- **Our assessment**: This is direct empirical evidence supporting `blog-anthropic-mcp-production-agents.md`
  Claim 7, which names Cloudflare as an example of a large-surface API where "an
  intent-grouped toolset likely won't cover it." Even Cloudflare's own first-party MCP
  server doesn't cover the full API surface — a practitioner can complete OAuth and still
  find that their specific operation is absent from the tool set. The "yet" in Willison's
  quote acknowledges this is a coverage gap at a point in time, not a permanent limitation.
  For practitioners: before committing to MCP-based integration with any vendor's server,
  verify that the specific operations you need are implemented.

### Claim 3: When an MCP server lacks the needed capabilities, Claude Code can suggest and execute a pivot to direct API calls

- **Evidence**: Willison's description of the transition: after MCP failed, "Claude did
  suggest using the API instead, but I'd need an API token." Willison then obtained the
  token and Claude handled the rest.
- **Confidence**: anecdotal (single practitioner report; but the pattern — model detecting
  tool gaps and proposing alternatives — is consistent with Claude's documented behavior)
- **Quote**: "Claude did suggest using the API instead, but I'd need an API token."
- **Our assessment**: The MCP → API fallback pattern has two components: (1) the model
  recognizes that its current tools are insufficient for the task and says so explicitly
  rather than hallucinating tool use, and (2) the model proposes an alternative approach
  (direct API) that it can actually execute. This is a model behavior claim: Claude
  Code surfaces tool gaps proactively rather than silently failing. The pattern is
  practically significant: practitioners who hit MCP limitations should know that asking
  Claude to proceed via API is a viable fallback, not a dead end.

### Claim 4: Claude Code handled the full Cloudflare API exploration workflow — zone discovery, rule listing, ID extraction, and PATCH update — without the practitioner reading API documentation

- **Evidence**: Willison describes the workflow as "Claude Code handle the rest" after
  providing the API token. The TIL page then shows "a rough version of what it did" —
  a multi-step curl/jq pipeline that Willison could reproduce and annotate.
- **Confidence**: anecdotal (first-person practitioner report; no independent verification)
- **Quote**: "Then I let Claude Code handle the rest."
- **Our assessment**: This is the primary AI-native engineering value demonstrated in the
  post. The workflow Claude Code executed was non-trivial: get zone ID → list custom WAF
  rules with selected fields → extract ruleset ID and rule ID for the specific rule →
  PATCH with new expression. Each step required knowing the correct endpoint, query
  structure, and field names. Willison obtained the result without reading Cloudflare
  API documentation directly. The TIL post itself is Willison's own reconstruction of
  what Claude Code did — indicating he understood the workflow well enough to document
  it but did not drive it step by step. This is the "Claude Code as API exploration
  partner" pattern: the practitioner provides credentials and goal; Claude navigates
  the API surface.

### Claim 5: HTTP-type MCP servers (remote over HTTPS) require only URL configuration, enabling seamless OAuth flows via the `/mcp` command in Claude Code

- **Evidence**: The `.mcp.json` configuration Willison shows uses `"type": "http"` with
  the Cloudflare MCP URL. He used the `/mcp` command to authenticate via OAuth.
- **Confidence**: settled (the `type: http` MCP configuration is documented; the `/mcp`
  OAuth flow is a Claude Code feature)
- **Quote**: "Then I ran `claude` in the folder and used the `/mcp` command, selected
  the Cloudflare MCP and used the authenticate option to jump through an OAuth flow."
- **Our assessment**: Remote HTTP-type MCP servers (as recommended in `blog-anthropic-mcp-production-agents.md`
  Claim 5) can be set up with a minimal two-field configuration (`type: http`, `url`).
  The OAuth authentication is handled in-session via `/mcp` without requiring manual
  token management. This is the intended usage pattern for third-party cloud MCP servers
  and demonstrates that the setup friction is low — the hard part is discovering whether
  the server implements the tools you need.

## Concrete Artifacts

### Project-Scoped MCP Configuration

Configuration Willison's Claude Code produced when asked to "set this up to only work in this project folder" (from the TIL page at til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand):

```
# Project structure for isolated MCP context
mkdir cloudflare-dev
cd cloudflare-dev

# .mcp.json — defines available MCP servers for this project
{
  "mcpServers": {
    "cloudflare-api": {
      "type": "http",
      "url": "https://mcp.cloudflare.com/mcp"
    }
  }
}

# .claude/settings.local.json — enables only the listed servers from .mcp.json
{
  "enabledMcpjsonServers": [
    "cloudflare-api"
  ]
}
```

### Claude Code's Cloudflare API Exploration Workflow

"a rough version of what it did" — as reconstructed by Willison from the TIL page:

```bash
# Step 1: Get zone ID
export TOKEN="$(cat token.txt)"
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/zones?name=simonwillison.net" \
  | jq '{success, errors, zones: [.result[] | {id, name}]}'

# Step 2: List custom WAF rules
export ZONE="2ce4f4f41f239d041e25f8320ad3c3fd"
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE/rulesets/phases/http_request_firewall_custom/entrypoint" \
  | jq '{success, errors, rules: [.result.rules[]? | {description, action, expression, enabled}]}'

# Step 3: Get ruleset ID and rule ID for the specific rule
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE/rulesets/phases/http_request_firewall_custom/entrypoint" \
  | jq '{ruleset_id: .result.id, rule: (.result.rules[] | select(.description=="/search/ extra protection") | {id, description, action, expression, enabled})}'

# Step 4: PATCH the rule with the new expression
export RS=0682fdbd40cc444cbe1e93d136e2b174
export RULE=8b2766d7802e4e988163531670976cb9

curl -s -X PATCH \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones/$ZONE/rulesets/$RS/rules/$RULE" \
  --data '{
    "action": "managed_challenge",
    "expression": "(http.request.uri.path wildcard r\"/search/*\" and http.request.uri.query contains \"&\")",
    "description": "/search/ extra protection",
    "enabled": true
  }'
```

### Final WAF Rule Expression

From the TIL page (the outcome of the Claude Code session):

```
(http.request.uri.path wildcard r"/search/*" and http.request.uri.query contains "&")
```

This expression activates Cloudflare's Managed Challenge only when the search URL contains at least one `&` (i.e., multiple query parameters — the faceted search crawler pattern), while allowing simple `?q=term` searches to pass without challenge.

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 7: That note states "If your service
    requires hundreds of distinct operations, such as Cloudflare, AWS, or Kubernetes, an
    intent-grouped toolset likely won't cover it." Willison's experience is direct empirical
    evidence: even Cloudflare's own first-party MCP server doesn't cover WAF custom rule
    editing. The Cloudflare MCP example in that note is not hypothetical — it reflects a
    real coverage gap.
  - `blog-anthropic-mcp-production-agents.md` Claim 5: Willison's `.mcp.json` uses
    `"type": "http"` with the remote Cloudflare MCP URL — exactly the remote server pattern
    recommended for production MCP use.
  - `blog-bswen-mcp-token-cost.md` Claim 1: Willison's project-folder isolation (one server,
    project-scoped via `enabledMcpjsonServers`) is a practical implementation of the
    discipline Bswen recommends. By scoping the Cloudflare MCP to only the `cloudflare-dev`
    folder, he avoids loading Cloudflare's tool definitions into every other Claude Code session.

- **Extends**:
  - `blog-bswen-mcp-token-cost.md` Claim 4 ("Limit to 3-6 essential servers — Be ruthless
    about necessity"): Willison's approach goes further — not just reducing global server
    count, but creating an isolated project context for a single MCP server that would
    otherwise be unnecessary overhead. The project-scoped MCP pattern is the most granular
    form of MCP discipline: scope the server to the folder where it is actually needed.
  - `blog-simonwillison-code-w-claude-2026.md`: That note documents Willison's live blog
    of the Code w/ Claude 2026 event. This TIL is a concrete Claude Code usage example
    from the same author, providing practitioner evidence of the patterns he observed at
    the event (async API exploration, Claude Code as interactive development partner) in
    a real task context.

- **Contradicts**: None identified. No existing note claims Cloudflare's MCP covers WAF
  rule editing; no note claims MCP always supersedes direct API calls.

- **Novel**:
  - **Project-scoped MCP via `enabledMcpjsonServers`**: The specific mechanism —
    `.mcp.json` in a project folder + `.claude/settings.local.json` with
    `enabledMcpjsonServers` to restrict which defined servers are active — is not
    documented in any prior corpus source note. This is the first practitioner
    demonstration of per-project MCP server activation in Claude Code.
  - **MCP → direct API fallback as a documented workflow**: Prior notes discuss MCP
    limitations abstractly (coverage gaps, token cost). This is the first source note
    showing the complete fallback arc: set up MCP → discover capability gap → model
    proposes API alternative → practitioner provides token → Claude executes full API
    workflow.
  - **Claude Code as interactive API explorer**: The workflow Willison describes —
    Claude navigating zone discovery → rule listing → ID extraction → PATCH update
    without the practitioner consulting API docs — is a concrete demonstration of
    Claude Code's utility for unfamiliar API surfaces. No prior corpus source shows
    this specific "API navigation without docs" pattern in detail.

## Guide Impact

- **Chapter on Claude Code Tooling / MCP Integration** (Ch01/Ch05 per triage): Add the
  project-scoped MCP configuration pattern (Claim 1 + Concrete Artifacts) as a
  recommended setup discipline. Currently no corpus source documents the
  `enabledMcpjsonServers` mechanism or the "dedicated project folder" approach. Frame
  it as the most granular form of MCP token discipline: scope the server to the folder
  where it is needed, not globally.

- **Chapter on Claude Code Tooling / MCP Integration**: Add the MCP capability-gap
  discovery workflow (Claims 2–3) as a practitioner note: (1) before using an MCP server
  for a specific operation, verify that operation is implemented; (2) when the MCP gap
  is discovered, the direct API fallback via curl/jq is the natural next step, and Claude
  Code can drive that fallback. Cite Claim 7 from `blog-anthropic-mcp-production-agents.md`
  as the architectural explanation for why coverage gaps occur.

- **Chapter on Integrating with External Systems** (Ch04 per triage): Add Claude Code
  as interactive API explorer (Claim 4) as a concrete pattern for unfamiliar API surfaces.
  The pattern: provide Claude Code an API token and a goal; Claude discovers endpoints,
  extracts IDs, and constructs requests. This works particularly well for REST APIs with
  predictable URL patterns and JSON responses, where jq-based extraction fits naturally.
  The Cloudflare workflow (zone → ruleset → rule → PATCH) is a concrete example.

## Extraction Notes

- The simonwillison.net post (`source_url`) is a short summary with a link to the full
  TIL at `til.simonwillison.net/cloudflare/captcha-on-at-least-one-ampersand`. Both pages
  were read in full via WebFetch. All quotes and artifacts are from the TIL page, which
  contains the complete technical content.
- The TIL was published 2026-06-15T17:21:36-07:00 (Pacific time); the blog post on
  simonwillison.net was published 2026-06-16 UTC — the same content appearing on both
  sites the same day.
- The concrete artifacts (curl commands) are Willison's reconstruction of what Claude
  Code did — "a rough version of what it did." The actual Claude Code session transcript
  is not reproduced; what appears in the TIL is Willison's cleaned-up version. Artifacts
  are labeled accordingly.
- The WAF rule expression and CAPTCHA configuration are included in Concrete Artifacts
  for completeness but are not extracted as standalone claims — the triage explicitly
  notes "The CAPTCHA configuration itself is not guide-relevant."
- Confidence is `anecdotal` overall: this is a short first-person TIL from a single
  practitioner. The MCP configuration mechanism (Claim 1, Claim 5) is setteable
  to `settled` since the mechanism is standard Claude Code behavior; the MCP limitation
  (Claim 2) and API exploration workflow (Claims 3–4) are `anecdotal` since they reflect
  one practitioner's experience at one point in time.
- No sub-pages were followed beyond the two pages noted above. The Cloudflare dashboard
  and API links in the TIL are external; they were not followed.
