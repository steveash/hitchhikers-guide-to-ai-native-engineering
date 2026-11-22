---
source_url: https://developers.googleblog.com/how-to-securely-connect-internal-cloud-run-mcp-servers-to-gemini-enterprise/
source_type: blog-post
title: "How to securely connect internal Cloud Run MCP servers to Gemini Enterprise"
author: Neeraj Agrawal (Forward Deployed Engineer, Google Cloud)
date_published: 2026-11-20
date_extracted: 2026-11-22
last_checked: 2026-11-22
status: current
confidence_overall: emerging
issue: "#4899"
---

# How to securely connect internal Cloud Run MCP servers to Gemini Enterprise

> A vendor how-to for an enterprise MCP posture: internal-only Cloud Run ingress reached via a PSC Network Attachment, FQDN-scoped private DNS, and a dual-credential model (platform service identity checked by IAM, end-user OAuth token checked by the MCP app) on every tool call.

## Source Context

- **Type**: blog-post (vendor engineering how-to; companion GitHub repo with setup scripts and a Python MCP server, not reviewed; link target not given in the fetched text)
- **Author credibility**: Google Cloud Forward Deployed Engineer describing Google's own products. First-hand product knowledge; no independent validation, no measurements, no customer results.
- **Scope**: Gemini Enterprise (Google-managed tenant) calling a StreamableHTTP MCP server on Cloud Run through Egress Agent Gateway, PSC, Cloud DNS and Cloud Run IAM. Does not cover non-Google platforms, authorization beyond token validation, tool-level policy, or prompt-injection risk. The 404/502 failure symptoms are vendor-reported, with no reproduction.

## Extracted Claims

### Claim 1: Enterprise MCP servers hit three production problems: no public exposure, two independent identity checks, and DNS collisions in Shared VPCs
- **Evidence**: Architectural framing in the intro; no data.
- **Confidence**: emerging
- **Quote**: "Production deployments require two independent identity checks on every tool call."
- **Our assessment**: A useful checklist for the "prototype to enterprise" transition. The three items are product-specific but the first two (network isolation plus separate service and user identity) generalize to any hosted MCP server.

### Claim 2: With internal ingress enabled on Cloud Run, default public calls from Gemini Enterprise fail with HTTP 404
- **Evidence**: Stated failure symptom; no logs or reproduction shown.
- **Confidence**: anecdotal (vendor-reported)
- **Quote**: "When internal ingress is enabled on Cloud Run, default public calls from Gemini Enterprise are rejected at Google's edge with HTTP 404."
- **Our assessment**: Plausible. The practical lesson is that a 404 (not 403) is the symptom of an ingress-policy rejection, which makes it easy to misdiagnose as a wrong URL.

### Claim 3: Reaching a serverless internal service takes two network bridges: a PSC Network Attachment into your VPC, then a private path to Google's serverless frontend
- **Evidence**: Architecture description and Figure 1 (diagram not extractable as text). Option A uses Private Google Access `199.36.153.8/30`; Option B uses a global PSC endpoint for Google APIs at `240.0.0.10`.
- **Confidence**: emerging
- **Quote**: "Bridge 1 (Into your VPC via PSC Network Attachment): A regional Egress Agent Gateway in Agent-to-Anywhere mode connects to a PSC Network Attachment in your regional subnet (us-central1 or europe-west1)."
- **Our assessment**: A concrete recipe, not a principle. Option B is the interesting one, because it works where the default internet route has been deleted (locked-down VPCs).

### Claim 4: Option B works in locked-down VPCs because Google injects a dedicated /32 route
- **Evidence**: Stated mechanism; no demonstration.
- **Confidence**: anecdotal
- **Quote**: "Google Cloud automatically injects a dedicated /32 internal route into your VPC, so private Cloud Run routing works even in locked-down VPCs where the 0.0.0.0/0 default internet route is deleted."
- **Our assessment**: Credible given the product docs linked, but not verified here.

### Claim 5: Without private DNS, `*.run.app` resolves publicly and the call fails with HTTP 502
- **Evidence**: Stated failure mode with explanation (the PSC attachment has no path to the public internet).
- **Confidence**: anecdotal (vendor-reported)
- **Quote**: "Without Private Cloud DNS, public DNS resolves .run.app domains to public internet IPs, which time out (HTTP 502) because a PSC Network Attachment does not route out to the public internet."
- **Our assessment**: A second misleading symptom: a 502 here is a DNS problem rather than an application fault. Together with Claim 2, it forms a small troubleshooting table.

### Claim 6: Scope the private DNS zone to the single service FQDN rather than a wildcard `*.run.app` zone, so other Cloud Run services in a Shared VPC keep resolving
- **Evidence**: Reasoning from Cloud DNS longest-suffix matching; no measurement.
- **Confidence**: emerging
- **Quote**: "Because Cloud DNS uses longest-suffix matching, every other Cloud Run service in your Shared VPC continues resolving normally."
- **Our assessment**: Sound least-blast-radius reasoning and the most transferable network lesson: a convenience wildcard in shared infrastructure becomes a cross-team outage risk. The cost is one zone per MCP service.

### Claim 7: Each tool call carries two distinct credentials in two headers: a Google-signed OIDC token for the platform's service agent (`X-Serverless-Authorization`) and the user's OAuth token (`Authorization: Bearer`)
- **Evidence**: Header-by-header description plus middleware code.
- **Confidence**: emerging
- **Quote**: "Contains a Google-signed OIDC ID token for your project's Gemini Enterprise service agent. Cloud Run IAM verifies this token against the Cloud Run Invoker role at the serverless edge and strips the header before the request reaches your container."
- **Our assessment**: A clean separation of "which platform is calling" (checked by infrastructure) from "which human is acting" (checked by app code). Because the first header is stripped, the MCP app never sees service identity, so per-user logic must rely on the second token alone.

### Claim 8: The user's OAuth token is passed through untouched so the MCP server can enforce per-user permissions
- **Evidence**: Description plus the middleware example, which validates the token and returns 401 on failure when `REQUIRE_OAUTH` is set.
- **Confidence**: emerging
- **Quote**: "Contains the signed-in user's OAuth 2.0 access token untouched, allowing middleware inside your MCP server to verify the caller's identity and enforce per-user permissions."
- **Our assessment**: Good for confused-deputy resistance. Caveats from the code: the `/health` path skips auth, and the example only validates when `REQUIRE_OAUTH` is true. It checks that the token is valid, not what the user is allowed to do. Per-tool authorization is left to the reader. Also, `has_serverless_auth` is computed but never used in the shown code.

### Claim 9: Only the project's Gemini Enterprise service agent should hold the Cloud Run Invoker role
- **Evidence**: Step 1 of the setup.
- **Confidence**: emerging
- **Quote**: "grant the Cloud Run Invoker role to your project's Gemini Enterprise service agent so only your Gemini Enterprise instance can invoke the container."
- **Our assessment**: Standard least-privilege IAM, applied to an agent platform's service identity.

### Claim 10: The whole integration can be set up in five steps and verified in Cloud Logging
- **Evidence**: Step list (lock down Cloud Run, provision VPC/PSC/gateway, FQDN DNS, bind gateway and register server, verify logs). Verification is by observing logs, not a test suite.
- **Confidence**: anecdotal
- **Quote**: "you can verify that tool initialization, discovery, and execution calls route privately through the Egress Agent Gateway to your internal Cloud Run container with both service IAM and user OAuth 2.0 checks passing."
- **Our assessment**: The reference repo is claimed to automate this; we did not run it. Treat the "five steps" as an outline, since step 2 alone contains several IAM and DNS-peering grants.

## Concrete Artifacts

Middleware from the source (verbatim, attributed to the article; indentation as rendered):

```python
class OAuth2ValidationMiddleware(BaseHTTPMiddleware):
  """Validates the end-user OAuth 2.0 Bearer token on incoming MCP requests."""
  async def dispatch(self, request: Request, call_next) -> Response:
    if request.url.path == "/health":
      return await call_next(request)
    has_serverless_auth = "x-serverless-authorization" in request.headers
    auth_header = request.headers.get("authorization", "")
    if auth_header.lower().startswith("bearer "):
      raw_token = auth_header.split(" ", 1)[1].strip()
      verified = await _verify_google_oauth_token(raw_token)
      if verified is None and REQUIRE_OAUTH:
        return JSONResponse(
            {"error": "Invalid or expired OAuth 2.0 Bearer token."},
            status_code=401,
        )
    elif REQUIRE_OAUTH:
      return JSONResponse(
          {"error": "Missing Authorization: Bearer <token> header."},
          status_code=401,
      )
    return await call_next(request)
```

Failure symptoms table (vendor-reported):

| Symptom | Stated cause |
|---|---|
| HTTP 404 from Cloud Run | Internal ingress rejecting a public-path call |
| HTTP 502 from Egress Agent Gateway | `*.run.app` resolved to a public IP; PSC attachment cannot reach the internet |

## Cross-References

- **Corroborates**: `blog-google-gemini-enterprise-custom-ui-auth.md` (same author and date) supports the theme of separating caller identity from per-user identity (Claim 2 there, "Pass the signed-in user's identity (not a shared identity)..."), and the Gemini Enterprise service-agent model. `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 2 (trust boundary so the harness does not handle credentials) is consistent with the user token being validated by the server, not the model.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-google-gemini-enterprise-custom-ui-auth.md` with the network path (PSC, DNS) and the header split that note does not cover. `blog-google-api-gateway-model-routing.md` Claim 12 mentions Agent Gateway egress governance as an asserted pattern; this note gives a concrete Egress Agent Gateway configuration, though for MCP, not model routing. Adjacent to `blog-google-adk-zero-trust-agents.md` (zero-trust; it covers signing and sandboxing rather than Cloud Run IAM or PSC) and `blog-google-mcp-stateless-scaling.md` (MCP hosting on serverless).
- **Novel**: Dual-header (`X-Serverless-Authorization` vs `Authorization`) identity split; FQDN-scoped private DNS argument; PSC Network Attachment plus PGA/global PSC endpoint routing; the 404/502 symptom mapping.

## Guide Impact

- **Chapter 06 (security)**: Add the enterprise MCP posture as a vendor-sourced example: internal-only ingress plus a platform identity check at the edge, plus per-user token validation in the MCP app (Claims 7, 8). Mark it `emerging` and Google-specific.
- **Chapter 06**: Note the "shared wildcard config in shared infrastructure" hazard (Claim 6) as a least-blast-radius example.
- **Chapter 02**: If the guide covers MCP hosting, add the 404/502 symptoms (Claims 2, 5) as troubleshooting hints for private MCP connectivity.
- **Caveat for authors**: The middleware validates tokens only; do not cite it as an example of per-tool authorization.

## Extraction Notes

- Fetched the article HTML with curl and read the full text. The architecture figure and the code were read from the page text; the figure content is not captured beyond its caption.
- The GitHub repo and the five related documentation links were not followed (no URLs resolved from the extracted text).
- The article published 2026-11-20 and gives no measurements, so all claims are vendor-reported.
