---
source_url: https://github.blog/changelog/2026-10-27-github-copilot-supports-server-to-server-authentication
source_type: docs
title: "GitHub Copilot supports server-to-server authentication"
author: GitHub (official changelog and docs)
date_published: 2026-10-27
date_extracted: 2026-10-28
last_checked: 2026-10-28
status: current
confidence_overall: emerging
issue: "#4379"
---

# GitHub Copilot Supports Server-to-Server Authentication

> GitHub's Oct 27, 2026 changelog (public preview) lets a GitHub App installed on an organization authenticate Copilot SDK agents with a short-lived installation token, giving agents an org-owned identity whose spend is billed to the org and attributable per app via `app_client_id` — with caveats (no per-app budgets) that only the linked docs reveal.

## Source Context

- **Type**: docs (GitHub changelog, ~150 words, plus the two linked docs pages: "Server-to-server authentication" in the Copilot SDK how-tos, and "Manage GitHub Apps that use your organization's Copilot")
- **Author credibility**: First-party GitHub product announcement and documentation; authoritative for what the feature does and its stated limits. Says nothing about real-world operation, since the feature is in public preview.
- **Scope**: Credential model, billing attribution, audit and revocation for SDK-built services/agents acting for an organization. Does not cover enterprise/personal-account installs (explicitly unsupported), per-app budgets (not available), or effectiveness data.

## Extracted Claims

### Claim 1: Copilot SDK services and agents can authenticate as an org-installed GitHub App, with no signed-in user
- **Evidence**: Product announcement plus SDK how-to with code samples in six languages.
- **Confidence**: emerging (public preview, "subject to change")
- **Quote**: "Services and agents built with the GitHub Copilot SDK can now make requests on behalf of an organization without relying on a signed-in user’s credentials."
- **Our assessment**: Real, documented capability. It is the Copilot-side instance of the "agent has its own identity" pattern. Preview status means the shape may change.

### Claim 2: GitHub frames this as a "workload-owned identity" that decouples agent auth and usage from individual users
- **Evidence**: Changelog framing; no data.
- **Confidence**: emerging
- **Quote**: "This workload-owned identity helps agents and automated services operate reliably at larger scale without tying their authentication or usage to individual users."
- **Our assessment**: The stated benefit is reliability at scale (agents don't break when a person leaves or their token lapses). No measurements; this is design rationale.

### Claim 3: The credential flow is a read-only org permission, app installation, and a short-lived installation token passed to the SDK
- **Evidence**: Changelog; SDK docs give the token request body `{"permissions": {"organization_copilot_requests": "read"}}`, and say to pass the `ghs_` token to the SDK's `gitHubToken` / `github_token` option.
- **Confidence**: emerging
- **Quote**: "Developers can give a GitHub App the read-only Copilot Requests organization permission, install the app on an organization, and pass a short-lived installation access token to the Copilot SDK."
- **Our assessment**: Concrete and least-privilege in shape: one narrow permission, an expiring token, no stored user secret.

### Claim 4: Installation tokens expire after one hour, so the host must re-mint and restart the SDK client/runtime
- **Evidence**: SDK docs "Refresh tokens" section.
- **Confidence**: emerging
- **Quote**: "Installation tokens expire after one hour."
- **Our assessment**: An operational cost of the short-lived design. Long-running agents need a refresh loop. The docs say that for child-process runtimes you restart the client with the new token, not hot-swap it.

### Claim 5: With `useLoggedInUser: false` the SDK ignores environment-variable tokens, so the installation token must be passed explicitly
- **Evidence**: SDK docs note and troubleshooting table; examples in TypeScript, Python, Go, Rust, .NET, Java.
- **Confidence**: emerging
- **Quote**: "`useLoggedInUser: false` turns off automatic credential discovery, including environment variable tokens such as `COPILOT_GITHUB_TOKEN`, so pass the installation token through the SDK’s explicit token option."
- **Our assessment**: A useful credential-hygiene detail: an unattended agent can be configured so it cannot silently fall back to a developer's stored credentials.

### Claim 6: Usage is billed to the installing org and org model policies, budgets and spending controls apply
- **Evidence**: Changelog and both docs pages.
- **Confidence**: emerging
- **Quote**: "Usage is attributed and billed to the organization that owns the installation. The organization’s model policies, budgets, and spending controls apply."
- **Our assessment**: Matches the AW `GITHUB_TOKEN` org-billing shift. The admin docs add important limits (Claims 7 and 8).

### Claim 7: "Read-only" does not mean cost-free, and budgets cannot be set per app
- **Evidence**: Admin docs "Understand access and billing" and "Control app spending."
- **Confidence**: emerging
- **Quote**: "In this context, Read-only does not mean that the app cannot incur costs."
- **Our assessment**: Easy to misread the permission name as safe. Also: "You cannot create a budget for an individual app or installation." Spend from all apps pools into the org budget, so one runaway agent can exhaust spend for humans. This should temper any "per-app cost control" reading of the changelog.

### Claim 8: A budget that only alerts does not stop spend; the "Stop usage when budget limit is reached" setting is required for a hard cap
- **Evidence**: Admin docs.
- **Confidence**: emerging
- **Quote**: "A budget that only sends alerts does not stop spending."
- **Our assessment**: A concrete operational gotcha for admins approving agent apps.

### Claim 9: Per-app attribution exists only in CSV exports via `app_client_id`, joined to the installations API
- **Evidence**: Admin docs "Identify app usage" steps.
- **Confidence**: emerging
- **Quote**: "App attribution is available in CSV exports, not in the AI usage view on GitHub."
- **Our assessment**: Attribution is after-the-fact and manual (match `app_client_id` to `client_id` from the "List app installations for an organization" endpoint to get `app_slug`). The field is empty for user, Actions, other GitHub-owned apps and pre-attribution usage, so it is not a complete cost ledger.

### Claim 10: Revocation is suspending or uninstalling the app, which also cuts its other org access
- **Evidence**: Changelog; admin docs "Block an app's access."
- **Confidence**: emerging
- **Quote**: "To stop requests from one app installation, suspend or uninstall it for your organization."
- **Our assessment**: A clean single kill switch. Side effect: it blocks everything the app does in the org, not only Copilot.

### Claim 11: Scope limits: org installs only, and approval is a trust decision
- **Evidence**: Admin docs.
- **Confidence**: emerging
- **Quote**: "It applies to apps installed on an organization. Personal account and enterprise installations cannot use this authentication method."
- **Our assessment**: Enterprise-level agent services can't use this yet. The docs also say "Only approve apps that you trust to spend your organization’s Copilot usage," so governance rests on human review of app owner, purpose and permissions.

### Claim 12: Inside GitHub Actions, GitHub points to `GITHUB_TOKEN` instead of an app
- **Evidence**: SDK docs: YAML with `copilot-requests: write`.
- **Confidence**: emerging
- **Quote**: "This approach needs no GitHub App or stored authentication secret."
- **Our assessment**: Gives a decision rule: Actions workloads use `GITHUB_TOKEN`; other services and CI use the app. The two paths have separate policies, since the app path does not need the "Allow use of Copilot CLI billed to the organization" policy.

## Concrete Artifacts

```
# Source: SDK docs, "Server-to-server authentication" (Actions path)
permissions:
  contents: read
  copilot-requests: write
```

```
# Source: SDK docs, installation token request body
{
  "permissions": {
    "organization_copilot_requests": "read"
  }
}
```

```
# Source: SDK docs, TypeScript runtime config
const client = new CopilotClient({
  connection: RuntimeConnection.forStdio(),
  gitHubToken: token,
  useLoggedInUser: false,
});
```

Troubleshooting (SDK docs): 401 = expired/invalid token; 403 "not enabled" = org doesn't support app-installation auth; 403 Forbidden from the Copilot API = missing `Copilot Requests` permission; "Wrong account billed" = installation belongs to the wrong org.

## Cross-References

- **Corroborates**: `docs-github-copilot-aw-github-token-auth.md` Claim 3 (org-owned repo `GITHUB_TOKEN` bills the org) and Claims 1–2 (dropping long-lived credentials). `docs-ghaw-auth-projects.md` Claim 4 (GitHub App tokens as the org-wide alternative to per-user PATs). `blog-anthropic-agent-identity-access-model.md` Claim 5 (agent runs under its own service accounts, not on behalf of users) and Claim 12 (revoking an identity ends access in one operation).
- **Contradicts**: None filed. Note that the changelog's "budgets ... apply" could be read as per-app budgeting; the admin docs rule that out (Claim 7 above), which is a clarification, not a cross-source contradiction.
- **Extends**: `docs-github-copilot-cli-sdk-session-credit-limits.md` Claim 8 (session limits complement org-level budgets): the org budget is the only cap on app spend, so per-session limits are the only finer-grained control. `docs-github-copilot-usage-metrics-agent-app-activity.md` (app-attributed activity in metrics) and `docs-github-copilot-repository-level-usage-metrics.md` Claim 8 (GitHub App installation tokens for metrics endpoints): this adds the auth/billing side.
- **Novel**: First note on Copilot usage attribution by app identity (`app_client_id`), the "no per-app budget" limitation, the alert-only-budget gotcha, and the `useLoggedInUser: false` hygiene pattern.

## Guide Impact

- **Chapter 05**: Where it mentions GitHub App installation tokens (~line 469, AW context), add the Copilot SDK path: org-installed app, `Copilot Requests` read-only, billed to the org, attributable only via `app_client_id` in CSV reports. Warn that there is no per-app budget and that budgets must have "Stop usage when budget limit is reached" to hard-cap.
- **Chapter 06**: Add as an example of workload identity for unattended agents: narrow permission, one-hour tokens, explicit-token-only config (`useLoggedInUser: false`), and suspend/uninstall as revocation. Note that "read-only" permissions can still spend money.
- Treat claims as public-preview; do not present as settled recommended practice.

## Extraction Notes

- Read the changelog and followed both linked docs pages (SDK server-to-server page; admin "Manage GitHub Apps" page); most substantive detail and the limits come from the docs pages, not the changelog.
- Quotes copied verbatim from the fetched HTML text (curly apostrophes preserved). The Claim 7 second quote and the Claim 11 second quote are from the admin docs page.
- Feature is public preview; no usage data or independent evaluation exists, hence `emerging`.
