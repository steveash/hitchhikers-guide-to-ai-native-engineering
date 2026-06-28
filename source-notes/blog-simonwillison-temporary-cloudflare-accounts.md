---
source_url: https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/
source_type: blog-post
title: "Temporary Cloudflare Accounts for AI agents"
author: Simon Willison
date_published: 2026-06-21
date_extracted: 2026-06-28
last_checked: 2026-06-28
status: current
confidence_overall: emerging
issue: "#1337"
---

# Temporary Cloudflare Accounts for AI agents

> Simon Willison's commentary on Cloudflare's new `--temporary` flag for `npx wrangler deploy`, which enables a 60-minute ephemeral Cloudflare Workers deployment without account creation — with a claim link for optional permanent conversion — validated by Willison running GPT-5.5 xhigh (via Codex Desktop) to build a working HTTP redirect resolver tool as a live test.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, June 21, 2026; short commentary linking to a Cloudflare product announcement at blog.cloudflare.com/temporary-accounts/. Willison's post adds his own observation about the feature's general usefulness beyond AI agents and provides first-person validation with a real-world test deployment.)
- **Author credibility**: Simon Willison is a 25-year practitioner, creator of Django and Datasette, and a prolific, hands-on AI tooling commentator with no vendor affiliation. His posts in this corpus are consistently first-person, concrete, and grounded in actual work rather than marketing claims. He tested the `--temporary` flag directly — not just a summary of the Cloudflare press release.
- **Scope**: Covers the `npx wrangler deploy --temporary` feature: its mechanics (60-minute deployment window, auto-generated subdomain, claim link for permanent conversion), Willison's practical validation using GPT-5.5 xhigh in Codex Desktop to build a redirect resolver, and his editorial observation that the AI-agent marketing framing undersells the feature's general utility. Also references the Cloudflare announcement's rationale (agent deployment friction, tight write→deploy→verify loop, Stripe/WorkOS partnerships). Does NOT cover: Wrangler version requirements, pricing, rate limits, supported Worker types, or configuration options beyond the `--temporary` flag.

## Extracted Claims

### Claim 1: `npx wrangler deploy --temporary` deploys a Cloudflare Worker to a live public URL without requiring a Cloudflare account, and the deployment stays live for 60 minutes

- **Evidence**: Willison's direct test plus the Cloudflare announcement he links to. The subdomain URL he recorded — `cloudflare-redirect-resolver.educated-celery.workers.dev` — is the live product of this command run by GPT-5.5 xhigh.
- **Confidence**: settled (feature is documented by Cloudflare, validated by a working external test by a credible practitioner)
- **Quote**: (no direct verbatim quote from the CLI behavior itself; see Concrete Artifacts for the command and the Cloudflare announcement quote on the 60-minute window in Claim 2)
- **Our assessment**: This is a zero-friction deployment primitive. The typical friction for a first Workers deployment is: create account, log in, run `wrangler login`, then deploy. The `--temporary` flag removes all of these steps. For agent workflows, this means any environment that has Node.js and internet access can deploy a Worker without pre-provisioned credentials. The 60-minute window provides a meaningful live testing period for iterative development. Critically, the agent need not hold any Cloudflare credentials — the temporary token is provisioned by Cloudflare at deploy time and discarded with the ephemeral account.

### Claim 2: Cloudflare motivated the feature with three specific agent deployment constraints: no human in the loop for background sessions, need for a tight write→deploy→verify loop, and expectation that deployment "just works" without signup

- **Evidence**: Cloudflare announcement text, as referenced by Willison's post. The three constraints are explicitly named as the design motivation.
- **Confidence**: emerging (Cloudflare's stated design rationale; not independently validated, but aligns with practitioner evidence in the corpus about agent deployment patterns)
- **Quote**: (no verbatim quote confirmed from the Cloudflare blog — blog.cloudflare.com/temporary-accounts/ returned 404 during extraction; these constraints are referenced in paraphrased form by Willison's post and the WebFetch summary of the announcement)
- **Our assessment**: The three constraints articulate why ephemeral deployment is specifically valuable for AI agents: (1) background agents cannot complete an OAuth flow or accept a browser popup — account creation is not a one-time setup cost when agents are provisioned fresh per task; (2) deployment is part of the agent's verify phase — an agent that can write code but cannot deploy and test it cannot close the feedback loop (corroborating `blog-cursor-cloud-agent-dev-environments.md` Claim 1); (3) agent frameworks expect cloud deployment to be a tool call, not an interactive session. The `--temporary` flag is Cloudflare's infrastructure answer to all three constraints.

### Claim 3: The feature markets itself as "for AI agents" but is genuinely useful for any developer who needs zero-friction ephemeral deployment

- **Evidence**: Willison's direct editorial observation about the feature's broader utility, grounded in his own experience using it.
- **Confidence**: anecdotal (single practitioner's assessment; consistent with the feature's design but not corroborated by other practitioners)
- **Quote**: "The announcement says this is 'for AI agents' but (as is pretty common these days) the AI hook isn't really necessary, this is an interesting feature for everyone else as well."
- **Our assessment**: Willison's observation is a recurring pattern across recent AI-platform announcements: features designed around AI use cases frequently reduce to genuinely useful infrastructure primitives. The AI framing creates marketing around what would have been a compelling developer-experience improvement on its own. For practitioners: the `--temporary` deployment pattern is worth evaluating for human-driven rapid prototyping, demos, and try-something-quickly workflows independently of any AI integration — it removes the account-creation barrier that commonly discourages "try a quick idea" deployments.

### Claim 4: A frontier AI agent (GPT-5.5 xhigh in Codex Desktop) successfully completed a full build-deploy-test cycle using the temporary deployment feature, producing a working HTTP redirect resolver

- **Evidence**: Willison's first-person report of a live test. He used GPT-5.5 xhigh in Codex Desktop to build the tool, and the deployment produced a live URL at `cloudflare-redirect-resolver.educated-celery.workers.dev`. A screenshot of the claim interface is included in the post.
- **Confidence**: anecdotal (single experiment with a single agent; demonstrates feasibility but not general reliability across agent types or worker complexity)
- **Quote**: "I had GPT-5.5 xhigh in Codex Desktop build this test application"
- **Our assessment**: This is the most concrete validation in the post: a frontier AI agent, given access to the `npx wrangler deploy --temporary` command, completed the full cycle from code generation to live deployment to claimable account — without human intervention at the deployment step. The redirect resolver is a meaningful worker (it makes external HTTP requests to follow redirect chains), not a trivial "hello world." The test demonstrates that the pattern works at the level of a real task. This is also the rare corpus note where GPT-5.5 (not Claude) is used for the AI test — the result is generalizable to any capable frontier model, not model-specific.

### Claim 5: The auto-generated deployment URL follows a `{project-name}.{generated-name}.workers.dev` pattern, where the generated component is random and cannot be predicted before deployment

- **Evidence**: Willison's observation of the URL produced by his test deployment: `cloudflare-redirect-resolver.educated-celery.workers.dev`.
- **Confidence**: anecdotal (single example; the pattern may vary)
- **Quote**: (no direct verbatim quote capturing the URL pattern; the URL `cloudflare-redirect-resolver.educated-celery.workers.dev` is the concrete evidence)
- **Our assessment**: The two-part subdomain structure has a harness engineering implication: the project name component (e.g., `cloudflare-redirect-resolver`) is the Worker name as set by Wrangler from `wrangler.toml` or the project directory, while the generated name component (e.g., `educated-celery`) is random and assigned at deploy time. An agent harness cannot construct the URL in advance — it must capture the URL from Wrangler's deployment output. Any automated test or verification step that needs to call the deployed endpoint must parse Wrangler's stdout. This is a concrete harness design requirement for pipelines that deploy and then test.

### Claim 6: The claim link persists for approximately 50 hours after deployment, decoupled from the 60-minute deployment window — allowing permanent account conversion even after the live deployment has expired

- **Evidence**: Willison's screenshot shows "This claim link expires in 49:26" — interpreted as 49 hours and 26 minutes remaining (not minutes:seconds). The triage note corroborates "Claim links expire after approximately 50 hours."
- **Confidence**: anecdotal (single data point from a screenshot; Cloudflare may adjust this timing)
- **Quote**: "This claim link expires in 49:26"
- **Our assessment**: The claim link outlasting the deployment window is an important architectural distinction. The deployment itself (the live Worker) expires after 60 minutes. The claim link (which converts the temporary project to a permanent Cloudflare account) persists for approximately 50 hours. This decouples the testing timeline from the ownership decision: an agent can deploy and verify within the 60-minute window; a human can claim when convenient within the 50-hour window — even hours after the deployment itself has gone offline. The pattern is: agent builds and verifies synchronously; human claims asynchronously. This makes the pattern viable in workflows where the deploying agent and the account owner are different actors.

### Claim 7: Claiming the temporary project transfers ownership of the full deployment — not just Workers, but also associated databases and other bindings

- **Evidence**: Cloudflare announcement referenced by Willison. The claim process includes all provisioned resources.
- **Confidence**: emerging (stated by Cloudflare in the announcement; the scope is plausible given Cloudflare's Workers ecosystem — D1, KV, R2 are bindable to Workers)
- **Quote**: (no verbatim quote confirmed from the Cloudflare blog during extraction)
- **Our assessment**: Full-resource transfer is significant for agent-built tools that use data persistence. A redirect resolver (as in Willison's test) needs no bindings, but a more complex agent-built tool might use D1 (SQLite), KV (key-value), or R2 (object storage). The ability to claim these resources alongside the Worker means the claim-link conversion preserves the full state of what the agent deployed — not just the code. This makes the `--temporary` pattern viable for data-bearing prototypes, not just stateless Workers.

### Claim 8: Cloudflare announced partnerships with Stripe and WorkOS alongside this feature, to streamline agent-driven account creation and OAuth provisioning

- **Evidence**: Cloudflare announcement referenced by Willison's post. The partnerships are positioned as complementary infrastructure for agent account management.
- **Confidence**: emerging (announced partnership; early-stage, not yet independently validated by practitioner experience)
- **Quote**: (no verbatim quote confirmed from the Cloudflare announcement during extraction)
- **Our assessment**: The Stripe and WorkOS partnerships extend the pattern beyond ephemeral accounts. The `--temporary` flag covers the "try without commitment" case (no account); Stripe and WorkOS provide paths for agents to create and manage persistent accounts via programmatic flows (no human OAuth flow). Together, these suggest an emerging Cloudflare platform strategy: the temporary flag covers frictionless testing; the payment/auth partnerships cover frictionless production account creation. This is an early signal of cloud platforms rearchitecting their onboarding flows for agent callers rather than human-interactive flows.

## Concrete Artifacts

### Ephemeral Cloudflare Workers Deployment Command

From Simon Willison's post (simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/, June 21, 2026):

```bash
npx wrangler deploy --temporary
```

Behavior:
- Provisions a temporary Cloudflare account (no Cloudflare login required)
- Grants Wrangler a temporary API token scoped to the temporary account
- Deploys the Worker to an auto-generated subdomain
- Deployment stays live for 60 minutes
- Provides a claim link valid for approximately 50 hours after deployment

### Deployment URL Pattern

Example from Willison's GPT-5.5 xhigh test deployment:

```
cloudflare-redirect-resolver.educated-celery.workers.dev
#        ^                        ^                ^
#   Worker name             Generated name    workers.dev
# (from wrangler.toml         (random, assigned
#  or directory name)          at deploy time)
```

The generated name component is assigned by Cloudflare at deploy time and cannot be predicted in advance. Agent harnesses that need the URL for downstream test steps must parse Wrangler's stdout to obtain it.

### Agent Build-Deploy-Test-Claim Lifecycle

```
# Ephemeral Workers deployment lifecycle
# Source: Willison's post (June 21, 2026) + Cloudflare announcement

STEP 1 — WRITE
  Agent generates Worker code (e.g., HTTP redirect resolver)
  No Cloudflare account or credentials required at this step

STEP 2 — DEPLOY
  Command: npx wrangler deploy --temporary
  Output: live URL at {name}.{random}.workers.dev
          claim link (valid ~50 hours)
  Cloudflare provisions: temporary account + temporary API token

STEP 3 — VERIFY (60-minute window)
  Agent or human tests the live URL
  Automated integration tests can run against the live endpoint
  URL captured from Wrangler output in Step 2

STEP 4 — CLAIM OR DISCARD (within ~50 hours)
  Option A: Human clicks claim link → converts to permanent account
            All resources (Workers, bindings, databases) transfer
  Option B: No action → deployment and temporary account auto-deleted
            No cleanup required

Human interaction required only at Step 4 (and only if keeping the deployment).
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-cloud-agent-dev-environments.md` Claim 1: "An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work." The `--temporary` flag directly addresses the "reach [deployed] services" part of this constraint for cloud deployment scenarios: it enables agents to deploy and test live Workers as part of the write→deploy→verify loop without the account-creation blocker. Cloudflare's stated motivation for the feature (Claim 2 above) explicitly targets this same close-the-loop requirement.
  - `blog-cursor-cloud-agent-lessons.md` Claim 1: "The single biggest factor in cloud agent output quality is ensuring it has a full development environment, like a developer has." The temporary deployment feature extends what a "full development environment" means: an environment that can deploy code to a live URL and test it is more capable than one limited to local execution or static analysis. The `--temporary` flag fills the deployment-capability gap without requiring pre-provisioned cloud accounts in every agent environment.

- **Extends**:
  - `blog-simonwillison-cloudflare-mcp-api-fallback.md`: That note documents Willison using Claude Code + the Cloudflare MCP (and direct API fallback) to manage Cloudflare WAF rules on his own account. This note covers a different Cloudflare surface: ephemeral Worker deployment via `wrangler deploy --temporary`. Both are Willison-authored practitioner notes about AI tooling interacting with Cloudflare infrastructure, but at different levels: management of existing resources (MCP/API) vs. ephemeral deployment of new resources (wrangler). Different agents too: Claude Code (prior note) vs. GPT-5.5 in Codex Desktop (this note).
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 6: That note documents Cloudflare as a sandbox provider for Claude Managed Agents, "runs sandboxes at scale using microVMs and lighter weight isolates" with zero-trust secrets injection. The `--temporary` flag is a different Cloudflare Workers use case: user-facing ephemeral public deployment rather than isolated tool execution sandboxes. Both use Cloudflare Workers infrastructure but serve different agent workflow needs: the Managed Agents sandbox executes agent tool calls in isolation; `--temporary` publishes agent-built applications to a live public URL. They represent complementary Cloudflare integration patterns at different layers of the agent stack.

- **Contradicts**: None identified. No existing corpus note makes claims about ephemeral zero-account Workers deployment, the `--temporary` wrangler flag, or the claim-link conversion pattern. No existing note states that Workers deployment requires an existing account (which would be the claim this source refutes).

- **Novel**:
  - **Zero-account ephemeral cloud deployment as a first-class agent infrastructure primitive**: No prior corpus source documents a pattern where an AI agent can deploy code to a live public cloud URL without pre-provisioned account credentials. All prior sources (Cursor cloud agents, Managed Agents sandboxes) assume agent environments carry pre-configured cloud credentials. The `--temporary` flag introduces a credential-free deployment path.
  - **Claim-link pattern for deferred ownership conversion**: The decoupling of deployment lifetime (60 min) from ownership conversion window (~50 hours) is architecturally novel in the corpus. The agent can build and test within the 60-minute window; the human can decide ownership on a human timescale (hours later). No prior source describes this asynchronous "test-now, claim-later" ownership transfer model.
  - **Harness design requirement: URL capture from Wrangler output**: The observation that the generated subdomain cannot be predicted before deployment — and must be parsed from Wrangler's stdout — is a concrete harness engineering constraint not documented elsewhere in the corpus.
  - **Cloud platform rearchitecting onboarding for agent callers**: The Stripe/WorkOS partnerships signal an emerging platform trend: cloud providers explicitly redesigning account creation and provisioning flows for programmatic (agent-driven) access rather than human-interactive flows. Early signal only, but worth tracking.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `npx wrangler deploy --temporary` pattern as a concrete tool for agent harnesses that include a deploy-and-test step. Note the harness engineering implication (Claim 5): the generated URL must be captured from Wrangler's output and passed to subsequent test steps — it cannot be constructed in advance. The Concrete Artifacts section provides the command, URL pattern, and full lifecycle for direct use. Also add that no Cloudflare credentials need to be present in the harness environment for this pattern to work — a significant simplification compared to standard Workers deployment.

- **Chapter 03 (Verification)**: Add ephemeral cloud deployment (Claims 1, 6) as a verification strategy distinct from local testing: deploy the agent's output to a live public URL, test it against real network conditions, and let it expire without cleanup overhead. The 60-minute window is long enough for automated integration tests; the 50-hour claim window allows human review without urgency. This extends the verification toolkit beyond `pytest`/unit tests and local `wrangler dev` into live-deployment verification.

- **Chapter 01 (Daily Workflows)**: Add the claim-link pattern (Claim 6) as a human-in-the-loop checkpoint that fits naturally into daily agent workflows: agent deploys and tests during a session; developer reviews the live deployment and decides whether to claim (convert to permanent) or discard (let expire). The asynchronous ownership conversion (Claim 6) means the developer is not time-pressured during the agent's execution window.

- **Chapter 02 (Harness Engineering) — agent deployment constraints**: Reference Claim 2 as design rationale for why background agents need credential-free deployment primitives: background sessions have no human to complete OAuth flows; the deploy step must be a tool call; the deployment must be immediately testable. The `--temporary` flag is the first corpus-documented primitive that satisfies all three constraints simultaneously.

## Extraction Notes

- The primary source (simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts/) was fetched successfully across multiple WebFetch passes with targeted prompts. Key verbatim quotes were confirmed across passes: Willison's AI-hook observation (Claim 3), the GPT-5.5 attribution (Claim 4), the claim link expiry display (Claim 6).
- The Cloudflare announcement (blog.cloudflare.com/temporary-accounts/ and variations tried) returned 404 across all fetch attempts. Claims derived from the Cloudflare announcement (Claims 2, 7, 8) are marked without verbatim quotes. They rely on WebFetch summaries of Cloudflare content referenced within the Willison post fetch. These claims should be independently verified against the live Cloudflare blog when accessible.
- The claim link timing (49 hours 26 minutes, not 49 minutes 26 seconds) was disambiguated from context: the triage note says "approximately 50 hours," and the feature's design logic (60-minute deployment + separate longer claim window) supports the hours interpretation. "49:26" in the screenshot caption is hours:minutes.
- The issue URL includes `#atom-everything` (Atom feed anchor). The `source_url` uses the canonical page URL without the fragment, consistent with prior Willison source notes (see blog-simonwillison-datasette-apps.md Extraction Notes).
- The Hacker News discussion at news.ycombinator.com/item?id=48608394 was identified but not fetched — it would likely add community reactions rather than new first-party claims about the feature itself.
- Cross-references verified before writing:
  - `blog-cursor-cloud-agent-dev-environments.md` Claim 1 confirmed at lines 26–31: "An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work." (first `### Claim:` heading in document order)
  - `blog-cursor-cloud-agent-lessons.md` Claim 1 confirmed at lines 26–31: "The single biggest factor in cloud agent output quality is ensuring it has a full development environment, like a developer has." (first `### Claim:` heading in document order)
  - `blog-simonwillison-cloudflare-mcp-api-fallback.md` read in full; referenced at the note level, not by claim number, since the relevant relationship is the note's overall topic rather than a specific claim.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 6 confirmed at lines 133–148: "runs sandboxes at scale using microVMs and lighter weight isolates" with zero-trust secrets injection. (sixth `### Claim:` heading in document order)
- No contradictions to file: this feature is new to the corpus. No existing note claims Workers deployment requires an account, or that zero-credential deployment is impossible. No contradiction exists.
