---
source_url: https://claude.com/blog/claude-enterprise-inference-hooks
source_type: blog-post
title: "Inference hooks: inline data loss prevention for Claude Enterprise"
author: Anthropic
date_published: 2026-08-05
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2520"
---

# Inference hooks: inline data loss prevention for Claude Enterprise

> Official Anthropic announcement (and accompanying platform docs) of Inference hooks, a beta Claude Enterprise feature that routes every governed prompt through a customer-run "AI security server" for a synchronous allow/deny verdict before inference runs, extending the DLP-style inline enforcement previously limited to Claude Code's client-side hooks to every Claude Enterprise surface — and positioned explicitly against the after-the-fact Compliance API.

## Source Context

- **Type**: blog-post (Anthropic official product announcement, claude.com, August 5, 2026), extended by three first-party Claude Platform Docs pages the blog post links to: the [Inference hooks overview](https://platform.claude.com/docs/en/manage-claude/inference-hooks), [Configure Inference hooks](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration), and [Develop an Inference hooks integration](https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint).
- **Author credibility**: Anthropic official communications, no individual byline. First-party, authoritative description of a shipping (beta) feature — request/response schemas, admin UI walkthrough, and signature-verification code samples are the vendor's own technical documentation, not third-party reverse-engineering.
- **Scope**: Covers what Inference hooks does, how the prompt-verdict round trip works, the request (prompt frame) and verdict JSON schemas, signature verification (Standard Webhooks/HMAC-SHA256), operational semantics (timeout, retry, circuit breaker, size limits), admin configuration (enforcement modes, shadow mode, rollout percentage, role exclusions, failure handling), and an explicit comparison to the Compliance API. Does **not** cover: pricing, a GA timeline, non-Claude-Enterprise deployment (Bedrock/Google Cloud and Claude Platform/API-only orgs are explicitly out of scope), or third-party validation of the two named beta partners' integration quality. The feature is explicitly labeled beta with a stated caveat that "field names, request shapes, and headers may change before general availability."

## Extracted Claims

### Claim 1: Inference hooks gives a compliance team a synchronous, inline block/allow checkpoint on every prompt and tool-call response, across all Claude Enterprise surfaces, from a single organization-level configuration
- **Evidence**: Direct product description from the blog post's lead paragraph, corroborated by the docs overview's framing of "governed prompts."
- **Confidence**: settled (first-party description of a shipping, if beta, feature)
- **Quote**: "Inference hooks lets your compliance team inspect and enforce policy on every prompt and tool call response before they reach Claude — across Claude Enterprise surfaces including chat, Claude Code, Claude Cowork, and more. Your DLP server makes the call to block or allow, and Claude enforces that decision in real time, blocking unapproved content before it reaches Claude."
- **Our assessment**: This is the headline capability: a single org-wide switch that puts a customer-controlled checkpoint in front of every Claude Enterprise inference call, rather than requiring per-surface integration work. The "across surfaces" framing is corroborated by the docs overview's Availability section (Claim 11 below), which is explicit about exactly which surfaces are and are not governed.

### Claim 2: Before Inference hooks, Anthropic's only native inline enforcement was Claude Code's client-side hooks, which did not cover other Claude Enterprise surfaces
- **Evidence**: Direct statement in the blog post's second paragraph, framing Inference hooks as closing a specific, named gap.
- **Confidence**: settled (vendor's own characterization of its prior product surface)
- **Quote**: "Until today, native inline enforcement was limited to Claude Code's client-side hooks. Inference hooks closes the gap with a single enforcement layer that covers every Claude Enterprise surface without separate integration work or agent per product."
- **Our assessment**: This is a useful architectural marker: Anthropic is drawing an explicit line between *client-side* enforcement (hooks that run on the user's machine, inside Claude Code) and *server-side* enforcement (Inference hooks, which run on Anthropic's infrastructure before the model sees the prompt, per Claim 3). It corroborates `failure-hooks-enforcement-2k.md`'s Lesson 3 finding that hook-based enforcement is architecturally superior to prose-based rules because it operates outside the model's own decision loop — Inference hooks applies the same "enforcement outside the loop" logic at the organization/server level instead of the individual developer/client level.

### Claim 3: Mechanically, every governed prompt is sent as a signed HTTPS POST to the organization's AI security server before generation begins, and Claude waits for an allow/deny verdict; today the only hook event is the pre-inference "prompt" frame, with response-side (tool-call) enforcement planned as a future event
- **Evidence**: Docs overview "How Inference hooks work" section; corrects the blog post's looser claim (Claim 12 below) that tool-call responses are already checked.
- **Confidence**: settled (first-party protocol description, though scoped as beta)
- **Quote**: "Inference hooks let a Claude Enterprise organization route every governed prompt through an AI security server, an HTTPS service that the organization or its security vendor operates, before inference runs. When a user submits a prompt, Anthropic sends the conversation transcript to your AI security server and waits for an allow or deny verdict; a denied request never reaches the model."
- **Our assessment**: The docs are more precise than the blog post here, and the precision matters: the docs state plainly, "Today the only hook event is prompt, which fires once per governed inference request, before inference begins. Response-side enforcement is planned as a later event." That directly narrows the blog post's claim that "the same check runs on tool calls" (see Claim 12) — as of the beta, tool-call/tool-response inspection is not yet shipped. A reader relying only on the blog post would over-estimate current coverage; the docs' "Current limitations" section is the authoritative statement of what's actually enforced today.

### Claim 4: A verdict is a small JSON object with an `action` field of `allow` or `deny`; a deny carries an optional 500-char `deny_reason` shown to the end user and an optional `reference_id` for the customer's own record-keeping, and malformed non-`action` fields are tolerated rather than rejected
- **Evidence**: Endpoint-integration docs "Return a verdict" section, with worked JSON examples and a constraints table.
- **Confidence**: settled (documented wire schema for a shipping beta API)
- **Quote**: "A deny is never discarded over a formatting problem: an oversize deny_reason is truncated, a malformed reference_id is silently dropped, and the action is still honored."
- **Our assessment**: This is a deliberately fault-tolerant verdict contract — Anthropic prioritizes honoring the customer's allow/deny decision over strict schema validation, but only for the fields describing *why*, not for the `action` field itself, which is validated (see Claim 5). Practically, this means an AI security server can be sloppy about `deny_reason`/`reference_id` formatting without losing enforcement, but cannot get away with returning `action` values other than the two supported ones.

### Claim 5: Anything other than a parseable HTTP 200 verdict body is treated as a webhook failure, not a deny — an error status does not block the request on its own, the organization's failure-handling policy does
- **Evidence**: Endpoint docs, explicit warning against using error codes to signal denial.
- **Confidence**: settled (documented operational contract)
- **Quote**: "Don't signal a deny with an error status. A non-200 response is a failure, not a deny. Any action value other than allow or deny is treated as a webhook failure."
- **Our assessment**: This is a sharp, easy-to-miss integration pitfall for anyone building the AI security server: an over-eager `raise` or a load-balancer 502 does *not* fail closed by default — it falls through to whatever failure-handling mode the org has configured (see Claim 6), which defaults to fail-*open* ("Allow the request"). A naive integration that assumes "error = blocked" will silently leak unapproved content under the default configuration.

### Claim 6: If the AI security server is unreachable, errors, or times out, the organization's own configured failure-handling policy — not a hardcoded default — decides whether the request is blocked (fail closed) or proceeds uninspected (fail open); on first save the platform's own default is fail-open with a 5,000ms timeout
- **Evidence**: Docs overview and Configure Inference hooks page, describing the `Failure handling` `Mode` setting and its factory default.
- **Confidence**: settled (documented admin configuration behavior)
- **Quote**: "If your AI security server is unreachable, returns an error, or doesn't respond within the timeout, your organization's failure handling setting decides the outcome: block the request, or allow it to proceed without inspection."
- **Our assessment**: The configuration docs add the detail the overview omits: "On first save, the defaults are Allow the request and 5,000ms" — i.e., out of the box, a new Inference hooks configuration is fail-open. An organization that flips on Inference hooks expecting it to fail closed by default (a reasonable assumption for a DLP control) must explicitly change this setting. This is a concrete, guide-worthy gotcha for Ch06.

### Claim 7: Organizations can de-risk rollout with three independent levers — shadow mode (observe verdicts on live traffic, block nothing), a percentage-based rollout that inspects only a sampled fraction of requests, and role-based exclusions that exempt whole roles from inspection entirely
- **Evidence**: Blog post "Ways to use inference hooks" section and the Configure Inference hooks page's step-by-step walkthrough of the same three controls.
- **Confidence**: settled (documented, UI-backed configuration options)
- **Quote**: "Enforcement can roll out at your pace, so nobody has to be blocked on day one: shadow mode observes verdicts on live traffic without blocking anything, a rollout percentage inspects a chosen fraction of requests, and exclusions exempt members of chosen roles entirely."
- **Our assessment**: The configuration docs sharpen an important interaction: rollout-percentage sampling happens *per conversation turn*, not per conversation, so "a single conversation can be partially inspected across turns," and — notably — requests outside the sampled percentage proceed uninspected "even when failure handling is set to Block the request." That second point means a low rollout percentage silently overrides a fail-closed failure policy for the un-sampled majority of traffic; teams tuning a phased rollout need to understand that "Block the request" only applies to the sampled slice.

### Claim 8: The AI security server receives the user-visible transcript (text, tool calls and their results, and text extracted from attachments) but never receives system prompts, tool definitions, Anthropic-internal context, Claude's hidden reasoning, or raw file/image bytes
- **Evidence**: Docs overview privacy-scoping statement, and the endpoint docs' more detailed "What the transcript contains" and "Content blocks" sections describing how attachments and tool results are represented.
- **Confidence**: settled (documented data-scoping contract)
- **Quote**: "Your AI security server sees what the user sees: transcript text, tool calls and their results, and text extracted from attachments. It never receives raw file or image bytes, system prompts, or Anthropic-internal context."
- **Our assessment**: This is a meaningful privacy/trust boundary for a feature that, by design, forwards conversation content to a third-party or self-hosted server — and it directly caps what an Inference hooks-based DLP program can catch. Because raw file and image bytes are never sent, "image-only content (for example, a screenshot of a document) is not inspected" (endpoint docs, Current limitations) — a screenshot-based exfiltration attempt would sail past an Inference hooks-based DLP check even with the feature fully enforcing.

### Claim 9: Requests are cryptographically signed per the Standard Webhooks specification (HMAC-SHA256 over `{webhook-id}.{webhook-timestamp}.{raw body bytes}`), and the single most common integration bug is decoding the signing secret with a URL-safe base64 decoder instead of the standard alphabet
- **Evidence**: Endpoint docs "Verify the signature" section, with a full Python reference implementation.
- **Confidence**: settled (documented cryptographic protocol with working code sample)
- **Quote**: "The signing secret is the value after the whsec_ prefix, encoded with the standard base64 alphabet ( + and / ), as is the signature in the header. A URL-safe decoder derives the wrong key bytes whenever the secret contains + or /, which is most of the time."
- **Our assessment**: This is a specific, actionable warning aimed at implementers, and it's the kind of detail that belongs in a "building your own AI security server" checklist — a URL-safe base64 decoder is a common default choice (many `base64` library convenience functions default to it) and will silently produce a wrong verification key rather than throwing an obvious error, since decoding itself succeeds. Also notable operationally: the docs specify Anthropic retries the connection attempt exactly once after a 100ms delay (only on connection failure, never once the server has already responded), and instruct implementers to accept signatures from *both* the old and new secret for about a minute after a rotation, since rotation is an "immediate cutover" with no server-side overlap window otherwise.

### Claim 10: Sustained webhook failures trip an automatic circuit breaker that stops the server from being contacted at all — at that point the org's failure-handling policy applies uniformly to *every* governed request, and recovery requires a human to fix the server and manually re-enable enforcement
- **Evidence**: Both the Configure Inference hooks and endpoint-integration docs describe the same circuit-breaker behavior from the admin and server-builder perspectives respectively.
- **Confidence**: settled (documented failure-mode behavior)
- **Quote**: "Sustained webhook failures attributable to your AI security server trip the circuit breaker, which stops enforcement: your server is no longer contacted, and your Failure handling choice applies to every inspected request. With Block the request selected, users in your organization are blocked until you act."
- **Our assessment**: This is a blast-radius warning: if an org has chosen fail-closed ("Block the request"), a struggling AI security server doesn't just fail a few requests — once the breaker trips, it can block *every* Claude Enterprise user in the organization until an administrator manually fixes the server and re-toggles `Enforce verdicts` to reset the breaker. For a fail-closed configuration, the AI security server becomes a hard operational dependency for all of Claude Enterprise, which the docs implicitly acknowledge by recommending load-testing before a large rollout ("Keep the verdict fast, and load-test your server before rolling it out to a large organization").

### Claim 11: Transcripts are sent untruncated up to a 10 MB request-body ceiling, which exceeds common web-framework defaults (nginx `client_max_body_size` at 1 MB, Express `express.json()` at 100 kB) — and a body a server rejects as too large counts as a webhook failure, meaning an oversized prompt reaches the model uninspected under the (default) fail-open policy
- **Evidence**: Endpoint docs "What the transcript contains" section, explicitly calling out the framework-default mismatch.
- **Confidence**: settled (documented size limit with named framework defaults as evidence)
- **Quote**: "Transcripts are sent untruncated, so a long conversation with large attachments produces a large request body, up to an upper bound of 10 MB. Raise your server's body limit to accept that ceiling. Several common defaults are much smaller, including nginx client_max_body_size at 1 MB and Express express.json() at 100 kB, and a rejected body counts as a webhook failure, so under Allow the request failure handling an oversized prompt would reach the model uninspected."
- **Our assessment**: This is the single most concrete "your DLP will silently fail" gotcha in the whole source. A team that stands up a security server behind a stock nginx or Express reverse proxy without raising the body-size limit will get exactly the failure mode DLP exists to prevent — the largest, most attachment-heavy (and arguably highest-exfiltration-risk) prompts are the ones most likely to exceed a 100 kB–1 MB default and slip through uninspected, precisely because the platform's own default failure policy is fail-open. This deserves a specific callout in any Ch06 guidance recommending Inference hooks.

### Claim 12: The blog post states tool-call responses (including from MCP connectors, skills, and plugins) are checked the same way as prompts — a claim the linked docs narrow, since only the pre-inference "prompt" hook event is shipped today and response-side enforcement is explicitly listed as a future event
- **Evidence**: Direct comparison of the blog post's claim against the docs overview's "Current limitations" and "How Inference hooks work" sections (see also Claim 3).
- **Confidence**: emerging (the docs, which are more precise and more recently maintainable than the blog post, describe current behavior as narrower than the announcement implies)
- **Quote**: "The same check runs on tool calls: when Claude calls a tool — including tools connected through MCP, skills, and plugins — the tool's response is checked before it's sent back to the model." (blog post)
- **Our assessment**: We flag this as an internal tension rather than filing a formal contradiction issue, because it reads as marketing-vs-engineering-docs imprecision on a single beta feature rather than two independently-argued positions — the docs are unambiguous that "Response-side enforcement is planned as a later event" and list it under "Current limitations." Anyone implementing against this feature should treat the docs, not the blog post, as authoritative for what's enforced today: prompts only, not tool-call responses, as of the August 2026 beta.

### Claim 13: Inference hooks and the Compliance API are explicitly positioned as complementary, not overlapping — Inference hooks acts inline before inference (Anthropic calls the customer's server, in real time) while the Compliance API acts after the fact (the customer calls Anthropic's API, to retrieve records post hoc)
- **Evidence**: Docs overview's dedicated "Inference hooks versus the Compliance API" comparison table and framing sentence.
- **Confidence**: settled (first-party product positioning)
- **Quote**: "Use Inference hooks to stop a request before it reaches the model, and the Compliance API to audit what happened afterward."
- **Our assessment**: This directly extends `blog-anthropic-compliance-api.md` and `blog-anthropic-compliance-api-security-partners.md`, which established (and left contested, in now-closed/rejected contradiction issue #858) exactly what conversation content the Compliance API does or doesn't expose. Inference hooks sidesteps that question by offering a *different* mechanism for the same underlying need — real-time transcript capture — that the docs explicitly frame as "a push-based alternative to polling the Compliance API" (Use cases section). It doesn't resolve #858's dispute about the Compliance API's own scope, but it does give regulated-industry teams a first-party path to real-time conversation visibility that doesn't depend on that dispute's resolution at all: an always-allow AI security server that just archives every transcript as it arrives.

### Claim 14: Inference hooks is scoped to Claude Enterprise only — it does not cover Claude Platform (API) organizations, Amazon Bedrock, Google Cloud, or voice mode, and is explicitly beta with a stated risk that field names, request shapes, and headers may still change
- **Evidence**: Docs overview "Availability" and "Current limitations" sections; endpoint docs opening caveat.
- **Confidence**: settled (documented scope and status, both stated plainly by the vendor)
- **Quote**: "Platform organizations (API access through the Claude Platform) are out of scope." … "Inference hooks are not available on Amazon Bedrock or Google Cloud." … "Inference hooks are in beta and available to Claude Enterprise organizations. Field names, request shapes, and headers may change before general availability."
- **Our assessment**: This scope boundary matters for the guide's audience: teams building agents against the Claude Platform API (the deployment model most relevant to Ch02 harness engineering and most Claude Code usage outside of Claude Enterprise seats) get no coverage from Inference hooks at all — the inference-logging/DLP gap for API-based agent workloads that `blog-anthropic-compliance-api.md` Claim 4 first documented remains open for that deployment model. Inference hooks only closes the gap for organizations on Claude Enterprise seats.

## Concrete Artifacts

### Example prompt frame (request body Anthropic sends to the AI security server)
```
Source: Develop an Inference hooks integration docs, "The prompt frame" section
(https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint)

{
  "type": "prompt",
  "request_id": "req_abc123",
  "tenant_id": "11111111-1111-1111-1111-111111111111",
  "actor": {
    "type": "user",
    "id": "user_01AbCdEfGhIjKlMnOpQrStUv",
    "email_address": "[email]"
  },
  "source": { "application": "claude-ai" },
  "session_id": "22222222-2222-2222-2222-222222222222",
  "model": "claude-sonnet-4-5",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "Summarize the attached report." },
        {
          "type": "attachment",
          "file_name": "q2-report.pdf",
          "media_type": "application/pdf",
          "size_bytes": 48213,
          "text": "Q2 revenue grew 14% quarter over quarter..."
        }
      ]
    }
  ],
  "metadata": {}
}
```

### Verdict responses (allow / deny)
```
Source: Develop an Inference hooks integration docs, "Return a verdict" section

Allow:
{ "action": "allow" }

Deny:
{
  "action": "deny",
  "deny_reason": "This prompt appears to contain customer payment card data, which your organization's policy does not allow.",
  "reference_id": "scan_01HXPT4R9V"
}
```

### Minimal "always allow" reference server (Python, from the docs)
```python
# Source: Develop an Inference hooks integration docs,
# "Get a first verdict round trip" (Python tab)
# Run with: python server.py
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class VerdictHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep the connection open between verdicts

    def do_POST(self):
        # Drain the body; transcripts can be megabytes.
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        verdict = b'{"action": "allow"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(verdict)))
        self.end_headers()
        self.wfile.write(verdict)

ThreadingHTTPServer(("", 8000), VerdictHandler).serve_forever()
```

### Signature verification (Python, from the docs)
```python
# Source: Develop an Inference hooks integration docs, "Verify the signature"
import base64
import hashlib
import hmac
import time

TOLERANCE_SECONDS = 300

def verify(secret: str, headers: dict[str, str], body: bytes) -> bool:
    """Return True if the body was signed by Anthropic for this organization.
    Anthropic sends header names in lowercase, but proxies are free to
    re-case them, so normalize the lookup to lowercase.
    """
    lowercased = {name.lower(): value for name, value in headers.items()}
    try:
        message_id = lowercased["webhook-id"]
        timestamp = lowercased["webhook-timestamp"]
        signatures = lowercased["webhook-signature"]
    except KeyError:
        return False  # unsigned request: not from Anthropic
    try:
        signed_at = int(timestamp)
    except ValueError:
        return False
    if abs(time.time() - signed_at) > TOLERANCE_SECONDS:
        return False  # replayed, or the clocks disagree
    try:
        key = base64.b64decode(secret.removeprefix("whsec_"), validate=True)
    except ValueError:
        return False  # misconfigured secret: reject rather than crash
    payload = f"{message_id}.{timestamp}.".encode() + body
    expected = b"v1," + base64.b64encode(hmac.new(key, payload, hashlib.sha256).digest())
    # Compare bytes: compare_digest on str raises on non-ASCII input.
    return any(hmac.compare_digest(expected, candidate.encode()) for candidate in signatures.split())
```

### Inference hooks vs. Compliance API comparison table
```
Source: Inference hooks overview docs, "Inference hooks versus the Compliance API"

                  | Inference hooks                       | Compliance API
------------------|----------------------------------------|--------------------------------------------------
When it acts      | Inline, before inference runs           | After the fact
What it does      | Allows or denies each governed request  | Retrieves activity, chats, files, projects, and
                  | in real time                            | users for audit and export
Direction         | Anthropic calls your AI security server | You call Anthropic's API
```

### Fixed request headers sent to the AI security server
```
Source: Develop an Inference hooks integration docs, "Receive a request"

Content-Type      application/json
User-Agent        anthropic-dlp/1
Accept-Encoding   identity

(plus webhook-id / webhook-timestamp / webhook-signature once a signing
secret exists, and any org-configured custom headers)
```

### Source IP range for allowlisting
```
Source: Develop an Inference hooks integration docs, "Source IP addresses"

160.79.106.0/24 (part of Anthropic's published outbound IP ranges;
allowlisting narrows exposure but is explicitly "not a substitute for
signature verification")
```

## Cross-References

- **Corroborates**: `failure-hooks-enforcement-2k.md` — Lesson 3 of that failure report ("Hook enforcement operates outside the context window and is therefore architecturally superior to prose for hard rules") is corroborated at the organizational level by Claim 2 above: Anthropic's own framing draws the same line between prose/model-mediated compliance and hook-based enforcement that runs outside the model's decision loop, just moved from a single developer's client-side hooks to a server-side, org-wide checkpoint.
- **Corroborates**: `blog-anthropic-cowork-enterprise.md` Claim 3 (OpenTelemetry events from Claude Cowork are SIEM-compatible and correlatable with Compliance API records via a shared user identifier) — both sources describe first-party Anthropic mechanisms for getting enterprise-visibility data out of Claude and into a customer-controlled system, though via different channels (OTel export vs. synchronous inline webhook) and different points in the request lifecycle (after the fact vs. before inference).
- **Extends**: `blog-anthropic-compliance-api.md` and `blog-anthropic-compliance-api-security-partners.md` — Claim 13 above documents the vendor's own explicit inline-vs-after-the-fact positioning between Inference hooks and the Compliance API, and the "real-time transcript archival" use case gives regulated-industry teams a first-party alternative to the disputed Compliance-API-conversation-content question raised in those two notes (contradiction issue #858, filed 2026-05-22, closed as **rejected** — not carried into CONTRADICTIONS.md). This source does not resolve #858; it offers a parallel path (an always-allow AI security server as transcript archiver) that sidesteps the dispute for organizations that adopt it.
- **Contradicts**: None identified against existing source notes. Internally, the blog post's claim that tool-call responses are already inspected (Claim 12) is narrower in the linked docs, which list response-side enforcement as not-yet-shipped; we treat this as blog-vs-docs imprecision on a single beta feature rather than a genuine two-sided contradiction worth filing, per MINER.md §4a's "one side is so weakly supported it doesn't rise to a real claim" guidance — the docs are unambiguously the more current and more authoritative of the two for what's enforced today.
- **Novel**: The verdict JSON schema, Standard Webhooks/HMAC-SHA256 signature scheme and its common URL-safe-base64 failure mode, the circuit-breaker behavior and its all-traffic blast radius, the 10 MB body ceiling vs. common framework defaults, the per-turn (not per-conversation) rollout-percentage sampling, and the explicit Inference-hooks-vs-Compliance-API positioning are all new to the corpus — no prior source note documents a first-party inline, pre-inference DLP checkpoint for Claude Enterprise.

## Guide Impact

- **Chapter 06 (Security and Threat Model)**: Add Inference hooks as a distinct, named enterprise control alongside the Compliance API, using Claim 13's inline-vs-after-the-fact framing to clarify when each applies: Inference hooks to *prevent* a specific prompt from reaching the model, Compliance API to *audit* what already happened. Flag the three concrete operational gotchas from Claims 6, 7, and 11 as an implementation checklist for any team standing up an AI security server: (1) the platform's own default is fail-*open* with a 5,000ms timeout, not fail-closed — verify this matches your risk tolerance before relying on the feature; (2) rollout-percentage sampling is per-turn and overrides a fail-closed policy for un-sampled traffic; (3) raise your server's request-body limit well above common framework defaults (nginx 1 MB, Express 100 kB) or oversized, attachment-heavy prompts — the ones most worth inspecting — will silently bypass inspection under the default failure policy.
- **Chapter 06 (Security and Threat Model)**: Note the coverage gap from Claim 14 explicitly: Inference hooks is Claude Enterprise-only. Teams building agents against the Claude Platform API (the deployment model most of Ch02's harness-engineering guidance assumes) get no first-party inline DLP checkpoint from this feature; the inference-logging gap documented in `blog-anthropic-compliance-api.md` persists unchanged for that population.
- **Chapter 06 (Security and Threat Model)**: If the guide documents Anthropic's Standard-Webhooks-based signature verification pattern anywhere, use Claim 9's base64-alphabet gotcha as a specific, checkable pitfall — it's a subtle failure that passes a happy-path test (decoding succeeds) but silently derives the wrong key.
- **Chapter 05 (Team Adoption)**: The three-lever gradual-rollout pattern (shadow mode → percentage rollout → role exclusions, Claim 7) is a reusable template for introducing any new inline enforcement/guardrail mechanism to an organization without a big-bang cutover; worth citing as a general pattern for rolling out enforcement changes, not just for this specific feature.

## Extraction Notes

- Followed 3 of the blog post's linked sub-pages (Inference hooks overview, Configure Inference hooks, Develop an Inference hooks integration) — all substantive first-party docs, within MINER.md's up-to-5 budget. The blog post itself is short (~350 words); nearly all of the extractable technical detail (schemas, code samples, failure semantics) lives in the linked docs, not the announcement post itself.
- The blog post and the docs disagree in specificity on tool-call/response coverage (Claim 12); resolved by treating the docs as authoritative, per the note under Cross-References → Contradicts, rather than filing a new contradiction issue.
- All quotes were copied character-for-character from HTML-stripped fetches of the live pages (fetched 2026-08-06); table and code-sample formatting was reconstructed from the stripped text but the field names, values, and prose are verbatim.
- `confidence_overall` is set to `emerging` rather than `settled` despite the depth of first-party documentation, because the feature is explicitly beta and the endpoint docs state outright that "field names, request shapes, and headers may change before general availability" — any guide text citing the wire-protocol specifics (Claims 4, 5, 9, 11) should be re-checked against `last_checked` staleness once GA docs ship.
