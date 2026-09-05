---
source_url: https://vercel.com/changelog/give-every-agent-in-herdr-its-own-vercel-sandbox
source_type: blog-post
title: "Give every agent in Herdr its own Vercel Sandbox"
author: Elisabeth Rülke (Vercel), with contributor Amelia Charles
date_published: 2026-08-06
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: emerging
issue: "#3256"
---

# Give every agent in Herdr its own Vercel Sandbox

> Vercel changelog announcing a plugin that runs each terminal coding agent
> (Claude Code, Codex, OpenCode) inside its own persistent Vercel Sandbox,
> orchestrated from Herdr's tmux-style pane manager — with a reviewed-upload
> gate, credential-never-leaves-sandbox design, and git-patch-based apply as
> the safety model. The linked docs additionally reveal that Vercel Sandbox
> supports a second, structurally different isolation model for the same
> problem: multiple agents as separate Linux users inside one shared sandbox,
> using Unix file permissions instead of VM boundaries.

## Source Context

- **Type**: blog-post (Vercel official changelog, `vercel.com/changelog`,
  published August 6, 2026). Per MINER.md §1, two linked docs pages were
  followed in full since the changelog itself is a ~400-word feature
  announcement that compresses mechanics documented in much greater depth
  elsewhere: the Herdr integration reference page
  (`vercel.com/docs/sandbox/ecosystem/herdr`) and the general multi-agent
  isolation concept page (`vercel.com/docs/sandbox/concepts/multi-agent`,
  last updated August 19, 2026, two weeks after the changelog). A third page,
  the KB walkthrough guide ("Run Herdr coding agents in isolated Vercel
  Sandboxes"), was fetched but returned only a summarized restatement of the
  same material already covered by the two primary docs pages, so it was not
  used as a quote source and is not separately cited here.
- **Author credibility**: First-party Vercel product documentation. The
  changelog and both docs pages describe a shipping integration (a
  third-party GitHub plugin, `vercel-labs/herdr-vercel-sandbox-plugin`,
  co-developed or endorsed by Vercel and documented on Vercel's own docs
  site) built on Vercel's own Sandbox product. Authoritative for feature
  existence, configuration mechanics, and security design as stated by the
  vendor; not independently verified, and no named customer or usage
  evidence appears in any of the three pages.
- **Scope**: Covers the Herdr-Vercel Sandbox plugin's installation,
  configuration, upload/apply/delete lifecycle, credential handling, and
  troubleshooting; and, via the multi-agent concept page, the general
  `@vercel/sandbox` SDK mechanism for running several agents inside a single
  sandbox as isolated Linux users. Does NOT cover: pricing for Herdr itself
  (only standard Vercel Sandbox compute/storage rates are mentioned),
  independent security review of either isolation model, comparative
  benchmarks between the one-sandbox-per-agent and one-sandbox-many-users
  approaches, or Herdr's own architecture/pricing as a product (Herdr is
  external to Vercel; only the Vercel-Sandbox-specific plugin is documented
  here).

## Extracted Claims

### Claim 1: Herdr runs each terminal coding agent in its own isolated, persistent Vercel Sandbox, so that nothing the agent runs or edits touches the user's local machine

- **Evidence**: Lead paragraph of the changelog; corroborated by the docs
  page's architecture summary.
- **Confidence**: settled (first-party description of a shipping integration,
  consistent wording across the changelog and the docs page)
- **Quote**: "Terminal coding agents like Claude Code, Codex, and OpenCode can now each run in their own isolated Vercel Sandbox, orchestrated from Herdr, a tmux-style manager that runs them side by side in panes. Nothing an agent runs or edits touches your machine."
- **Our assessment**: This is the one-sandbox-per-agent isolation model, and it
  is architecturally distinct from the same product's other documented
  isolation model (Claim 8 below): here the isolation boundary is a full,
  separate Vercel Sandbox microVM per agent, not a Unix user boundary inside
  one shared sandbox. For a harness engineer running several agents
  concurrently (e.g., one per repo, or one per task), this is the "give each
  agent maximal blast-radius separation" option — a compromised or
  misbehaving agent cannot even see another agent's sandbox exists, at the
  cost of N separate VM boot/cost overheads instead of one.

### Claim 2: Every plugin action returns machine-readable JSON, so that any capability available from a Herdr pane (starting an agent, checking its state, applying its changes) can also be invoked by a script or another agent

- **Evidence**: Explicit design statement in the changelog.
- **Confidence**: settled (first-party description of a shipping design
  property)
- **Quote**: "Everything the plugin does is machine-readable. Each action returns its results as JSON, so whatever you can do from a pane, like starting an agent, checking its state, or applying its changes, a script or another agent can do too."
- **Our assessment**: This is a specific, named design choice for
  agent-orchestrating-agents scenarios: the plugin's own control surface is
  scriptable by construction, not merely usable interactively. It means a
  meta-agent (or CI script) could programmatically fan out multiple Herdr/
  Sandbox agent sessions, poll their JSON state, and apply their patches
  without a human operating the tmux-style UI — the same "agent as
  orchestrator of other agents" pattern documented elsewhere in the corpus,
  but here scoped specifically to sandbox lifecycle actions rather than task
  delegation.

### Claim 3: Starting an agent requires two separate invocations of the same action — a dry run that only lists the files it would upload, followed by a second invocation within 10 minutes that actually creates the sandbox and uploads exactly that reviewed file set

- **Evidence**: The docs page's "Start the agent" getting-started step,
  corroborated by the changelog's shorter description of the same two-step
  flow.
- **Confidence**: settled (first-party description of the specific approval
  mechanism, consistent between the changelog and the docs page)
- **Quote**: "Focus a pane inside the linked worktree and run **Start configured agent in a new Sandbox** from Herdr's action menu. The plugin prints the upload manifest for review. Invoke Start again within 10 minutes with the workspace unchanged to approve exactly that file set. The plugin then splits the pane, creates the sandbox, uploads the approved files, and launches the configured agent."
- **Our assessment**: The 10-minute window and the "with the workspace
  unchanged" condition are the operative safety property: this is not a
  generic "confirm to proceed" prompt, it is a manifest-pinning approval —
  if the workspace changes between the dry run and the confirming
  invocation, the approval presumably no longer matches (the docs do not
  state explicit behavior for a changed workspace within the window, only
  that the second invocation approves "exactly that file set"). For a
  practitioner, the actionable takeaway is: review the printed manifest
  before re-invoking Start, and re-run the dry run if more than a few
  minutes pass or the worktree changes, rather than trusting a stale review.

### Claim 4: The plugin never copies the user's Vercel or coding-agent credentials from the local machine; the agent must authenticate fresh inside the sandbox, and that login persists on the sandbox filesystem across stops and reconnects

- **Evidence**: Explicit statement under "How it works," corroborated by the
  getting-started section's note about first-start login.
- **Confidence**: settled (first-party statement of a specific credential
  design)
- **Quote**: "The plugin never copies Vercel or coding-agent credentials from your machine. You authenticate the agent inside its sandbox, where the credential persists across stops and resumes." / "On the agent's first start, it asks you to log in inside the sandbox. That login is stored on the sandbox filesystem and persists across stops and reconnects."
- **Our assessment**: This is a specific instance of the "never transfer a
  standing local credential into a remote execution environment" pattern
  already documented elsewhere in the corpus for other sandbox providers
  (see Cross-References) — here achieved by simply never attempting the
  transfer at all: the human re-authenticates the agent inside the sandbox
  once, and the sandbox's own persistent filesystem (not the plugin) retains
  that credential across the sandbox's stop/resume lifecycle. This is a
  weaker guarantee than a firewall-enforced credential-injection model
  (Cross-References, Claim 8 of `blog-anthropic-claude-managed-agents-selfhosted.md`)
  in one respect: once authenticated, the credential does live inside the
  sandbox's filesystem where the agent's own tool calls run, rather than
  being injected at the network boundary and kept structurally unreachable
  from the agent. The docs do not claim the in-sandbox credential is
  inaccessible to the agent itself.

### Claim 5: Applying an agent's remote changes locally is idempotent and safety-checked — each apply exports only the changes since the last applied snapshot, verifies them with `git apply --check` first, and applies nothing at all if the check fails or if the same changes are reapplied

- **Evidence**: The docs page's "Apply changes locally" getting-started step
  and "How it works" section, both describing the same patch-based mechanism.
- **Confidence**: settled (first-party description of the specific
  conflict-handling behavior)
- **Quote**: "Each apply copies only the work since the last apply, and checks the patch with `git apply --check` first: if it conflicts with local work, nothing is applied. Applying the same changes twice reports that they are already present instead of failing." / "Patch-based apply: Each apply exports only the changes since the last applied snapshot and checks them with `git apply --check` before touching your worktree."
- **Our assessment**: The "nothing is applied" all-or-nothing behavior on
  conflict, combined with idempotent re-application, is a concrete, checkable
  safety property distinct from a generic "we use git patches" claim — it
  means a practitioner can safely retry an apply action without risking a
  partial or duplicated merge. It also means apply and other destructive
  actions "refuse to run while an agent is still active in the mapped pane"
  (docs page, "Apply changes locally" step) — the agent must be explicitly
  exited first, preventing a race between an agent still writing files and a
  human pulling a snapshot mid-write.

### Claim 6: Deleting a sandbox is a distinct, harder-to-trigger action from stopping one — stopping preserves the sandbox's filesystem indefinitely, while deletion requires the human to type the literal word `DELETE` in a confirmation popup within 60 seconds, and reconnecting to a mapped pane never creates a replacement sandbox even if the original is confirmed gone

- **Evidence**: The docs page's "How it works" section (stop vs. delete
  distinction) and its "Troubleshooting" section (explicit Reconnect vs.
  Replace behavior for a missing sandbox).
- **Confidence**: settled (first-party description of a specific, named
  two-tier destructive-action design)
- **Quote**: "Explicit deletion: Stopping a sandbox preserves its filesystem. Deleting a sandbox through the plugin requires you to type `DELETE` in a confirmation popup within 60 seconds." / "**Reconnect agent to this Sandbox** never creates a replacement. If the sandbox is confirmed missing, exit the agent in the mapped pane, invoke **Replace this Sandbox**, review the tracked names in the popup, and type `DELETE` within 60 seconds to start a fresh sandbox for the worktree."
- **Our assessment**: This is the same typed-confirmation pattern for
  irreversible actions documented in the changelog's own summary ("requires a
  human to type `DELETE` to permanently remove a Sandbox"), but the docs page
  adds an operationally important detail the changelog omits entirely: the
  plugin deliberately refuses to auto-recreate a missing sandbox on
  reconnect, forcing an explicit, separately-confirmed "Replace" action
  instead. This closes a specific failure mode — a transient error or stale
  pane mapping silently spinning up a brand-new sandbox (and losing track of
  or duplicating the original) — by making sandbox replacement always a
  deliberate, typed-confirmation action rather than an automatic recovery
  behavior.

### Claim 7: Custom terminal agents without a built-in adapter can be added via a declarative JSON profile with nine required fields; the plugin runs the profile's install/launch/version commands inside the sandbox but never imports or executes profile code on the local machine, and labels such agents as unverified

- **Evidence**: The docs page's "Custom agents" section, including a full
  example profile with all nine fields.
- **Confidence**: settled (first-party specification of the exact
  configuration mechanism and its stated security property)
- **Quote**: "To run a terminal agent that has no built-in adapter, describe it with a declarative profile in `config.json`. Add the profile under `customAgents`, keyed by the agent kind, and set `\"allowCandidateAgents\": true`. All nine profile fields are required" / "The install, launch, and version commands run inside the sandbox, and the plugin labels custom agents as unverified. Profiles are plain JSON; the plugin never imports executable profile code on your machine."
- **Our assessment**: "Profiles are plain JSON... never imports executable
  profile code on your machine" is the specific security property worth
  extracting: it distinguishes a declarative-config extension mechanism
  (data describing which commands to run where) from a plugin-code extension
  mechanism (arbitrary code loaded and executed locally to add a new agent
  type). The install/launch/version commands themselves still execute inside
  the remote sandbox, not locally, keeping the local machine's exposure to a
  misconfigured or malicious custom-agent profile limited to parsing JSON.
  The three verified, built-in agents (Claude Code, Codex, OpenCode) are
  implicitly held to a higher trust bar than any custom profile, which the
  docs explicitly flag as "unverified" regardless of correctness.

### Claim 8: Vercel Sandbox supports a second, structurally different multi-agent isolation model in its general SDK — instead of one sandbox per agent, several agents can run as separate Linux users inside one shared sandbox, each with a private home directory enforced by standard Unix file permissions rather than a VM boundary

- **Evidence**: The `vercel.com/docs/sandbox/concepts/multi-agent` concept
  page (last updated August 19, 2026), fetched as a linked, substantive
  related page per MINER.md §1. This page is general-purpose SDK
  documentation, not specific to Herdr, but is directly relevant to the
  triage's key question about architecting per-agent sandbox isolation.
- **Confidence**: settled (first-party SDK documentation with runnable code
  examples demonstrating the isolation boundary)
- **Quote**: "Run several AI agents in one sandbox, each as its own Linux user with a private home directory and separate file permissions. Isolating agents this way keeps one agent's files and output out of reach of the others, while groups let you open up a shared workspace when agents need to collaborate."
- **Our assessment**: This is the single most guide-relevant finding in this
  source: Vercel Sandbox does not offer only one answer to "how do I isolate
  multiple agents" — it offers two, at different layers, with different
  cost/isolation tradeoffs. Herdr's model (Claim 1) gives each agent a full
  separate microVM: maximal isolation (no shared kernel-adjacent resources
  between agents), but each agent pays a separate sandbox's boot/compute/
  storage cost. The `createUser()`/`createGroup()` model gives each agent
  only a Unix permissions boundary within one shared microVM: agents share
  the sandbox's kernel, network egress configuration, and compute allocation,
  but only pay for one sandbox's overhead regardless of agent count. Neither
  page cross-references the other's approach or offers guidance on when to
  pick one over the other — that comparison is this note's synthesis, not a
  vendor-stated recommendation.

### Claim 9: The user-isolation model demonstrably blocks cross-agent file access at the OS permission level — one user's `cat` of another user's private file fails with a non-zero, permission-denied exit code — and the SDK validates user/group names against a strict pattern specifically to prevent command injection via a crafted name

- **Evidence**: Two separate code examples on the multi-agent concept page:
  one demonstrating a blocked cross-user read, one demonstrating name
  validation.
- **Confidence**: settled (first-party SDK documentation with executable code
  examples and explicit stated exit-code behavior)
- **Quote**: "Each user's home directory is isolated from other users. One agent, running as its own user, cannot read, list, or write another agent's home directory" (followed by a code example where `bob`'s `cat` of `/home/alice/secret.txt` returns "non-zero, permission denied"). "User and group names must match `/^[a-z_][a-z0-9_-]*$/` and be at most 32 characters. This constraint applies to every user and group method. Invalid names throw an error immediately, which prevents command injection through a crafted name" (followed by three examples: `sandbox.asUser('Alice')`, `sandbox.asUser('user name')`, and `sandbox.asUser('$(whoami)')`, each stated to throw).
- **Our assessment**: The `$(whoami)` example is a direct, named acknowledgment
  by the vendor that a naive implementation of per-agent usernames (e.g.,
  deriving a username string from agent-controlled or task-derived input
  without validation) could otherwise be a command-injection vector — the
  regex constraint is explicitly framed as a security control, not just an
  input-format requirement. This is a concrete, reusable pattern for any
  harness that lets an agent or an upstream system supply an identifier used
  later in a shell context: validate against an allowlist pattern before use,
  and treat "no shell metacharacters" as a security property to test for, not
  just a formatting nicety.

### Claim 10: The shared-collaboration mechanism for the one-sandbox-many-users model is a setgid group directory at `/shared/<groupname>`, where files any member creates automatically inherit group ownership, and removing a user from the group revokes access to new commands immediately but does not affect an already-running process by that user until it exits

- **Evidence**: The multi-agent concept page's "Share files between agents
  with groups" section, including the worked three-agent (researcher/coder/
  reviewer) example.
- **Confidence**: settled (first-party SDK documentation with explicit stated
  semantics for the revocation edge case)
- **Quote**: "The shared directory uses the setgid bit, so files created inside it inherit the group automatically." / "Removing a user affects new commands only. A process already running as that user keeps the group until it exits, so terminate and restart any long-lived processes if you need the revocation to take effect immediately."
- **Our assessment**: The revocation caveat is the load-bearing operational
  detail here, and it is the kind of self-disclosed limitation MINER.md flags
  as high-value: "remove this agent's access to the shared workspace" is not
  instantaneous for any long-lived agent process already running under that
  identity — a practitioner building an incident-response or access-
  revocation flow on top of this primitive must explicitly kill and restart
  the agent's process, not just call `removeUserFromGroup()` and assume
  immediate effect. This is structurally the same "revocation has a
  provider-dependent or state-dependent window, not an instant guarantee"
  pattern already documented for a different vendor and a different
  credential type in `blog-vercel-enterprise-apps-and-agents.md` Claim 7
  (Vercel Connect's revocation caveat for providers without a revocation
  API) — see Cross-References.

### Claim 11: Automatic snapshots for a persistent sandbox consume Snapshot Storage, billed separately from compute, so a stopped (non-executing) Herdr-managed sandbox continues to accrue storage cost until deleted

- **Evidence**: A standalone billing statement in the docs page's "How it
  works" section, placed immediately after the stop/delete distinction
  (Claim 6).
- **Confidence**: settled (first-party billing mechanism statement, though no
  specific price is given on this page)
- **Quote**: "Each automatic snapshot for a persistent sandbox consumes Snapshot Storage, which is billed separately from compute."
- **Our assessment**: This page does not give a per-unit price for Snapshot
  Storage (unlike GitHub's equivalent cloud-sandbox storage meter, which
  publishes an explicit per-GiB-month price — see Cross-References), but it
  establishes the same cost-governance shape already documented for a
  competing product: stopping an agent's sandbox is not equivalent to zero
  ongoing cost. A team running many Herdr-managed agents that stop sessions
  without deleting them (e.g., "pause a task for later" as a habitual
  pattern) accrues storage cost proportional to the number of live-but-
  stopped sandboxes and how long they persist, independent of any active
  compute usage — a concrete argument for a sandbox cleanup/deletion policy
  as a real cost lever, not just an active-usage limit.

### Claim 12: Running the full Herdr-Vercel Sandbox integration has concrete version and plan-tier prerequisites — Herdr 0.7.5+, Vercel CLI 56.2.0+, and (for sessions needing more than 45 minutes) a Pro or Enterprise Vercel plan, since a one-hour timeout in the example config requires a paid plan

- **Evidence**: The docs page's "Prerequisites" section and an inline note
  about the example configuration's timeout value.
- **Confidence**: settled (first-party specification of exact version numbers
  and a plan-tier gate)
- **Quote**: "Before you begin, make sure you have: macOS or Linux; Herdr 0.7.5 or newer; Node.js 20 or newer; A Git repository for your project; Vercel CLI 56.2.0 or newer, logged in to the account that should own the sandbox" / "The example config sets a one-hour `timeout`, which requires a Pro or Enterprise plan. On Hobby, set `timeout` to `45m` or less. See runtime limits."
- **Our assessment**: The 45-minute Hobby-plan ceiling is a concrete planning
  constraint for any team evaluating this integration on a free/Hobby account
  before committing to a paid plan — a coding-agent session that legitimately
  needs more than 45 minutes of sandbox runtime (a long test suite, a large
  build, an extended multi-step task) will hit a plan-tier wall rather than a
  technical one on Hobby, distinct from any per-agent isolation
  consideration discussed elsewhere in this note.

## Concrete Artifacts

### Installation and startup commands (verbatim, from the changelog and docs page)

```
# Install the plugin
herdr plugin install vercel-labs/herdr-vercel-sandbox-plugin

# Link the target repo to a Vercel project (required before starting agents)
vercel login
vercel link

# Find the Herdr-managed plugin config directory
herdr plugin config-dir vercel.sandbox

Source: https://vercel.com/changelog/give-every-agent-in-herdr-its-own-vercel-sandbox
and https://vercel.com/docs/sandbox/ecosystem/herdr
```

### Plugin configuration file (verbatim example, from the docs page)

```json filename="config.json"
{
  "agentKind": "claude-code",
  "agentArgs": {
    "claude-code": []
  },
  "runtime": "node24",
  "timeout": "1h",
  "uploadExcludes": ["private-fixtures/**"],
  "sensitiveFileOverrides": []
}
```
Source: https://vercel.com/docs/sandbox/ecosystem/herdr — "Configuration" section.
Verified agent kinds at time of writing: Claude Code (2.1.220), Codex (0.146.0), OpenCode (1.18.9).

### Custom (unverified) agent profile — all nine required fields (verbatim, from the docs page)

```json filename="config.json"
{
  "agentKind": "my-agent",
  "allowCandidateAgents": true,
  "customAgents": {
    "my-agent": {
      "title": "My Agent",
      "installationCommand": "npm install --prefix /vercel/sandbox/.herdr-tools my-agent@1.2.3",
      "launchCommand": "/vercel/sandbox/.herdr-tools/node_modules/.bin/my-agent",
      "versionCommand": "/vercel/sandbox/.herdr-tools/node_modules/.bin/my-agent --version",
      "expectedVersion": "1.2.3",
      "authenticationMode": "device-code",
      "herdrDetectionIdentifier": "generic",
      "interactiveTTY": true,
      "resumeSupported": true
    }
  }
}
```
Source: https://vercel.com/docs/sandbox/ecosystem/herdr — "Custom agents" section.

### Optional keybindings (verbatim example, from the docs page)

```toml
[[keys.command]]
key = "prefix+shift+s"
type = "plugin_action"
command = "vercel.sandbox.start-agent"
description = "start the configured agent in a new Vercel Sandbox"

[[keys.command]]
key = "prefix+shift+a"
type = "plugin_action"
command = "vercel.sandbox.apply-changes"
description = "apply Sandbox changes locally"
```
Source: https://vercel.com/docs/sandbox/ecosystem/herdr — "Optional keybindings" section.
Bindings go in `~/.config/herdr/config.toml`, applied via `herdr config check` and `herdr server reload-config`.

### Multi-user isolation SDK example — full researcher/coder/reviewer workflow (verbatim, from the multi-agent concept page)

```ts filename="index.ts"
import { Sandbox } from '@vercel/sandbox';

const sandbox = await Sandbox.create();

// Each agent gets its own isolated workspace
const researcher = await sandbox.createUser('researcher');
const coder = await sandbox.createUser('coder');
const reviewer = await sandbox.createUser('reviewer');

// A shared workspace for collaboration
await sandbox.createGroup('project');
await sandbox.addUserToGroup('researcher', 'project');
await sandbox.addUserToGroup('coder', 'project');
await sandbox.addUserToGroup('reviewer', 'project');

// The researcher writes findings to the shared directory
await researcher.runCommand({
  cmd: 'bash',
  args: ['-c', 'echo "API spec v2" > /shared/project/spec.txt'],
});

// The coder reads the spec, then writes code in their own home
const spec = await coder.runCommand({
  cmd: 'cat',
  args: ['/shared/project/spec.txt'],
});
await coder.writeFiles([
  { path: 'app.js', content: Buffer.from(`// ${await spec.stdout()}`) },
]);

// The reviewer can read the shared spec but not the coder's private files
const blocked = await reviewer.runCommand({
  cmd: 'cat',
  args: ['/home/coder/app.js'],
});
console.log(blocked.exitCode); // non-zero, isolation enforced
```
Source: https://vercel.com/docs/sandbox/concepts/multi-agent — "A complete multi-agent workflow" section.

### Username/group-name validation against injection (verbatim, from the multi-agent concept page)

```ts filename="index.ts"
sandbox.asUser('Alice'); // throws, uppercase not allowed
sandbox.asUser('user name'); // throws, spaces not allowed
sandbox.asUser('$(whoami)'); // throws, special characters not allowed
```
Source: https://vercel.com/docs/sandbox/concepts/multi-agent — "Valid user and group names" section.
Pattern enforced: `/^[a-z_][a-z0-9_-]*$/`, max 32 characters.

## Cross-References

### Cross-reference verification notes
`blog-anthropic-claude-managed-agents-selfhosted.md`, `blog-vercel-enterprise-apps-and-agents.md`,
`docs-ghaw-sandbox-reference.md`, `docs-github-copilot-teams-shared-agentic-work.md`, and
`blog-cursor-cloud-agent-dev-environments.md` were re-read in full during this extraction
(MINER.md §4b), and every claim number cited below was located and confirmed against
that note's own numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 8 ("Vercel
    sandboxes inject credentials at the network boundary so they never enter
    the sandbox"): that note documents Vercel Sandbox's credential-injection
    pattern for the general Claude Managed Agents self-hosted integration.
    This source's Claim 4 (Herdr never copies local credentials; the agent
    authenticates fresh inside the sandbox) is a related but distinct
    guarantee for the *same underlying product* — the two sources describe
    two different credential-handling mechanisms for two different
    integrations built on Vercel Sandbox: a network-boundary firewall
    injection (Managed Agents / MCP tunnels context) versus a
    never-transferred, re-authenticate-inside-the-sandbox model (Herdr
    context). Worth flagging for the guide as a case where the same
    sandbox provider offers two different credential-security postures
    depending on the integration layer, not one uniform guarantee.
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 7 (Vercel Connect's
    self-disclosed revocation caveat: for providers without a revocation
    API, a "revoked" token stays valid until it naturally expires): this
    source's Claim 10 (removing a user from a shared group revokes access
    for new commands only; an already-running process keeps access until it
    exits) is the same category of self-disclosed, state-dependent
    revocation-latency caveat, for a structurally different mechanism (OS
    group membership vs. an external OAuth token). Two independent Vercel
    docs pages, for two different products, both flag "revocation is not
    instantaneous for already-in-flight access" as an explicit limitation
    practitioners must design around.
  - `docs-ghaw-sandbox-reference.md` Claim 5 (gh-aw's AWF hides the Docker
    socket specifically to prevent agent-issued container-escape/privilege
    escalation): this source's Claim 9 (Vercel's SDK validates every
    user/group name against a strict pattern specifically to block shell
    command injection via a crafted username, with `$(whoami)` given as the
    explicit adversarial example) is the same category of a vendor naming a
    specific attack vector and its specific countermeasure, for a different
    part of the sandbox's attack surface (identifier injection vs. container
    escape).

- **Extends**:
  - `blog-anthropic-claude-managed-agents-selfhosted.md`: that note documents
    Vercel Sandbox as one of four pluggable sandbox providers for Claude
    Managed Agents (alongside Daytona, Cloudflare, and Modal), each
    described from the Anthropic integration's point of view. This source
    documents two isolation architectures native to Vercel Sandbox itself,
    independent of any Anthropic integration — the one-sandbox-per-agent
    model (Herdr) and the one-sandbox-many-users model (`createUser`/
    `createGroup`) — neither of which that note describes, since it covers
    Vercel Sandbox only as a single execution target for one Claude agent at
    a time, not as a platform for isolating multiple agents from each other.
  - `docs-github-copilot-teams-shared-agentic-work.md` Claim 9 (GitHub
    Copilot's cloud sandbox is built on Azure Container Apps Sandboxes, with
    GitHub providing "identity, policy, and billing" as a control-plane layer
    on top of a different cloud vendor's infrastructure) and Claim 11
    (Copilot's three-meter, priced billing model — compute, memory, and
    storage for stopped sessions): this source's Claim 11 (Vercel Sandbox
    also bills snapshot storage for stopped sessions separately from
    compute) extends the same "storage cost persists after compute stops"
    billing shape to a second, independent vendor's cloud-sandbox product —
    though this source gives no per-unit price, unlike GitHub's published
    per-GiB-month rate. This is corroborating evidence that "stopped sandbox
    still costs storage money" is an emerging industry-standard billing
    pattern for persistent agent sandboxes, not one vendor's idiosyncratic
    choice.
  - `blog-cursor-cloud-agent-dev-environments.md` Claim 12 (Cursor's
    equivalent per-environment control: "Teams can restrict outbound network
    access to a specific allowlist for one environment while leaving a
    different environment more permissive. Additionally, secrets configured
    for one environment aren't accessible from any other."): this source's
    Claim 8 (`createUser`/`createGroup` isolate agents by Unix permissions
    within one sandbox) is a finer-grained, cheaper alternative to Cursor's
    per-environment (i.e., effectively per-sandbox) secret and network
    isolation — Vercel's model additionally offers isolation *within* a
    single execution environment, a granularity Cursor's documented model
    does not describe.

- **Contradicts**: No contradiction issue filed. One point is flagged as a
  documentation gap rather than a contradiction: neither the Herdr docs page
  nor the multi-agent concept page references the other's isolation model,
  and neither offers guidance on when a team should choose one-sandbox-
  per-agent (Claim 1) over one-sandbox-many-users (Claim 8) — this is an
  absence of vendor guidance, not a conflicting claim about what either
  model does. The synthesis in Claim 8's "Our assessment" (isolation
  strength vs. per-agent cost overhead) is this note's own comparison, not a
  vendor position, and is presented as such.

- **Novel** (what this note adds that no prior source covers):
  - **Two structurally different per-agent isolation models offered by the
    same sandbox product** (Claims 1, 8): no prior corpus source documents a
    sandbox vendor offering both a full-VM-per-agent model and a
    Unix-user-per-agent-within-one-VM model, let alone the cost/isolation
    tradeoff between them.
  - **Manifest-pinned, time-boxed upload approval** (Claim 3): the specific
    "dry run now, confirm within 10 minutes with the workspace unchanged"
    two-invocation approval pattern for what gets uploaded to a remote agent
    sandbox is new to the corpus.
  - **Declarative-JSON-only custom agent extension with an explicit
    no-local-code-execution guarantee** (Claim 7): no prior corpus source
    documents an agent-harness extension mechanism that is explicitly
    restricted to non-executable JSON profiles specifically to keep
    arbitrary code off the local machine, while still running the
    profile's own commands remotely.
  - **Reconnect-never-replaces / explicit-typed-replace failure-recovery
    design** (Claim 6): the specific refusal to auto-recreate a missing
    sandbox on reconnect, requiring a separately typed-confirmation
    "Replace" action instead, is a named resilience/safety pattern not
    documented for any other sandbox product in the corpus.
  - **Command-injection-by-crafted-username as a named, tested attack
    vector with a regex countermeasure** (Claim 9): no prior corpus source
    documents input validation on an agent-identity string specifically
    framed as a command-injection defense, with an explicit adversarial
    code example (`$(whoami)`).
  - **Setgid shared-directory group collaboration with a stated,
    process-lifetime-bound revocation caveat** (Claim 10): the specific
    mechanism (setgid bit for automatic group inheritance) and its
    revocation-latency caveat are new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the two Vercel Sandbox isolation
  models (Claims 1, 8) as a concrete "pick your isolation granularity"
  decision point for any team designing a multi-agent harness: one sandbox
  per agent (Herdr's model — maximal isolation, N× sandbox overhead) versus
  one sandbox with per-agent Unix users and group-scoped shared directories
  (the SDK's `createUser`/`createGroup`/`/shared/<group>` model — cheaper,
  weaker isolation boundary, built-in collaboration primitive). This is a
  more concrete framing than the guide's existing sandbox-provider coverage
  (which treats "which sandbox provider" as the main decision) — here the
  decision is *how many sandboxes per how many agents*, orthogonal to
  provider choice.

- **Chapter 02 (Harness Engineering)**: Add the manifest-pinned, time-boxed
  upload approval pattern (Claim 3: dry run, then a second confirming
  invocation within 10 minutes against an unchanged workspace) as a named
  pattern for "what gets uploaded to a remote agent execution environment,"
  alongside the reviewed-upload-manifest pattern already documented for
  GitHub Copilot Teams (`docs-github-copilot-teams-shared-agentic-work.md`)
  and Cursor's environment configuration validation
  (`blog-cursor-cloud-agent-dev-environments.md`).

- **Chapter 03 (Safety and Verification)**: Add the two-tier destructive-
  action design (Claim 6: stop preserves state indefinitely; delete requires
  typing `DELETE` within 60 seconds; reconnect never silently recreates a
  missing sandbox) as a named pattern for designing irreversible-action
  confirmation gates in agent harnesses. Add the username/group-name
  injection countermeasure (Claim 9, regex validation with the `$(whoami)`
  adversarial example) as a concrete, minimal-cost defensive pattern for any
  harness that derives shell-context identifiers from agent- or
  task-supplied input.

- **Chapter 03 (Safety and Verification) / Chapter 06 (Security Threat
  Model)**: Add the credential-handling contrast between this source's Claim
  4 (Herdr: never transferred, but lives in the sandbox filesystem once
  authenticated) and the network-boundary-injection model already documented
  for the same underlying product (`blog-anthropic-claude-managed-agents-selfhosted.md`
  Claim 8) as a worked example that "built on the same sandbox provider"
  does not imply "identical credential security guarantees" — the specific
  integration layer changes the guarantee, and practitioners evaluating a
  sandbox-based agent tool should ask which credential model applies to
  their specific integration, not assume the provider's strongest documented
  guarantee applies uniformly.

- **Chapter 04 (Cost Engineering at Scale)**: Add the stopped-sandbox
  snapshot-storage billing detail (Claim 11) alongside the already-documented
  GitHub Copilot cloud-sandbox equivalent
  (`docs-github-copilot-teams-shared-agentic-work.md` Claim 11) as
  corroborating evidence that "stopped, non-executing agent sessions still
  accrue storage cost" is a pattern to check for across sandbox vendors, not
  a single vendor's quirk — sandbox cleanup/deletion policy is a real,
  cross-vendor cost lever.

- **Chapter 05 (Team Adoption)**: Add the Pro/Enterprise-plan timeout gate
  (Claim 12: 45-minute ceiling on Hobby, one-hour-plus requires a paid plan)
  as a rollout-planning detail for teams evaluating this integration —
  agent tasks that legitimately run long will hit a billing-tier wall before
  a technical one on a free account.

## Extraction Notes

1. **Access method and verbatim-quote confidence.** The changelog and both
   docs pages were fetched twice each with prompts explicitly demanding
   verbatim, non-summarized reproduction (per MINER.md §2a's caution about
   WebFetch's summarizing pass). All three pages returned structurally
   consistent, near-identical text across repeated fetches, including
   frontmatter-style metadata blocks and exact code examples — behavior
   consistent with the underlying fetch returning the page's actual
   markdown/plain-text source rather than a paraphrased summary. Every
   `Quote` field in this note is copied from that returned text. One initial
   fetch of the changelog page (before the verbatim-reproduction prompt was
   used) returned a compressed prose summary with paraphrased wording; that
   first-pass output was discarded entirely and is not the source of any
   quote in this note.
2. **Two substantive linked pages followed, one KB guide fetched but not
   used as a quote source, per MINER.md §1.** The Herdr integration
   reference (`/docs/sandbox/ecosystem/herdr`) and the general multi-agent
   concept page (`/docs/sandbox/concepts/multi-agent`) were both fetched in
   full and are the source of every claim and artifact in this note. A third
   linked page, the KB walkthrough guide ("Run Herdr coding agents in
   isolated Vercel Sandboxes"), was also fetched; its returned content was a
   compressed restatement of material already covered by the two primary
   pages (with one bracketed quote whose exact wording could not be
   cross-verified against the other two pages' text), so it was not used as
   a source for any Quote or Concrete Artifact in this note, and is not
   cited above. Other linked pages (the plugin's GitHub README, the general
   Sandbox pricing page, the general "Understanding Sandboxes" concept page)
   were not followed, as they either duplicate detail already captured or
   are outside this issue's scope (Herdr-specific and multi-agent-isolation
   mechanics, not general Sandbox pricing or microVM internals).
3. **No customer or adoption evidence.** None of the three fetched pages
   names a customer, gives a usage metric, or cites independent security
   review. All claims are first-party vendor documentation of a shipping
   plugin and a general SDK feature. Overall confidence is rated "emerging"
   rather than "settled" for this reason, despite individual claims being
   rated "settled" (unambiguous, internally consistent first-party
   descriptions of specific, shipping mechanisms with concrete version
   numbers, exit codes, and regex patterns).
4. **No contradictions filed.** Reviewed `blog-anthropic-claude-managed-agents-selfhosted.md`,
   `blog-vercel-enterprise-apps-and-agents.md`, `docs-ghaw-sandbox-reference.md`,
   `docs-github-copilot-teams-shared-agentic-work.md`, and
   `blog-cursor-cloud-agent-dev-environments.md` in full. No existing corpus
   note makes a claim that materially opposes anything in this source at the
   MINER.md §4a filing threshold. The one internal tension noted (Herdr's
   credential model vs. the network-boundary-injection model documented for
   the same product elsewhere in the corpus) is flagged in Cross-References
   as a "different guarantee for a different integration layer," not a
   factual disagreement about the same mechanism — no contradiction issue
   filed.
5. **Prospector's two triage comments.** The issue carries two triage
   comments from the Prospector, apparently from two separate triage passes
   (the first rating novelty "medium" and citing issues #2737/#2452 as
   overlapping notes that do not exist in the current `source-notes/`
   directory; the second rating novelty "high" and citing three notes that
   do exist and are used above). This note follows the second, more
   specific and verifiable triage comment.
