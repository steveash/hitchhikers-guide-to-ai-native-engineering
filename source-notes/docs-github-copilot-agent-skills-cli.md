---
source_url: https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli
source_type: docs
title: "Manage agent skills with GitHub CLI"
author: GitHub (official changelog)
date_published: 2026-04-16
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#189"
---

# Manage agent skills with GitHub CLI

> GitHub's official announcement of `gh skill` — a package manager for AI agent capabilities
> that introduces supply-chain integrity primitives (content-addressed SHAs, immutable releases,
> frontmatter provenance) to the emerging cross-agent skills ecosystem, along with a concrete
> security warning that unverified skills may contain prompt injections.

## Source Context

- **Type**: docs (GitHub official product changelog, April 16, 2026)
- **Author credibility**: GitHub engineering team announcing a production feature (GitHub CLI
  v2.90.0+). Authoritative for CLI syntax, supply chain mechanisms, and the list of supported
  agent hosts. The security warning ("may contain prompt injections, hidden instructions, or
  malicious scripts") is a first-party admission from the platform provider, not third-party
  commentary — high signal. The source does not cover skill authoring in depth or provide
  empirical data on adoption outcomes.
- **Scope**: The `gh skill` command surface (`install`, `search`, `update`, `publish`, `preview`),
  the Agent Skills open specification at agentskills.io, supported agent hosts, supply chain
  integrity mechanisms, and the explicit security advisory. Does NOT cover: how to author SKILL.md
  files from scratch, skill effectiveness data, cost implications of skill-loaded agent sessions,
  how the spec is governed or versioned, or how skill resolution works when multiple hosts have
  conflicting requirements.

## Extracted Claims

### Claim 1: `gh skill` introduces a package manager paradigm for AI agent capabilities — a new operational primitive distinct from CLAUDE.md, AGENTS.md, or custom commands

- **Evidence**: Official GitHub product changelog with specific CLI commands and flags. The
  `install`, `search`, `update`, `publish`, `preview` subcommands map to standard package
  manager verbs (cf. `npm install`, `pip install`, `brew install`). Requires GitHub CLI v2.90.0+.
- **Confidence**: settled (product fact — these commands exist and are documented)
- **Quote**: "Agent skills are portable sets of instructions, scripts, and resources that teach
  AI agents how to perform specific tasks."
- **Our assessment**: This is the most significant operational signal: skills are now a
  first-class managed artifact, not a file you manually copy between repos. The package manager
  model introduces version semantics, dependency tracking, and distribution infrastructure that
  did not exist for agent context files before this announcement. Practitioners who maintain
  shared context files across multiple repos should evaluate whether the skills distribution
  model simplifies their maintenance burden.

### Claim 2: Content-addressed git tree SHA tracking detects real content changes rather than tag-only moves

- **Evidence**: Official documentation: "Each installed skill records the git tree SHA of its
  source directory. `gh skill update` compares local SHAs against the remote to detect real
  content changes."
- **Confidence**: settled (technical mechanism stated definitively in official docs)
- **Quote**: "Each installed skill records the git tree SHA of its source directory. `gh skill
  update` compares local SHAs against the remote to detect real content changes."
- **Our assessment**: This is the mechanism behind meaningful update detection. Unlike a version
  field (which can be bumped without content changes) or a tag (which can be moved), a git tree
  SHA is content-addressed — it changes if and only if the directory contents change. Practitioners
  using `--pin` to a SHA get a stronger guarantee than pinning to a semantic version tag: a SHA
  cannot be quietly replaced with different content.

### Claim 3: Immutable releases prevent post-publication alteration of skills — even admins cannot change published content

- **Evidence**: Official documentation: "Git tags ensure 'release content cannot be altered
  after publication, even by admins.'" Tag-based protection is the enforcement mechanism.
- **Confidence**: settled (product guarantee stated in official changelog)
- **Quote**: "Git tags ensure release content cannot be altered after publication, even by admins."
- **Our assessment**: This is the supply chain integrity guarantee that makes version-pinned
  installs trustworthy. Without immutability, a publisher could silently update a v1.2.0 tag to
  point to different content. The admin-level immutability claim is stronger than typical access
  controls and closer to what npm's package tarball hashing provides. However, this only protects
  against post-publication modification — it does not protect against a malicious publisher
  who injects prompt injections before publishing, which is exactly what the security warning
  (Claim 6) acknowledges.

### Claim 4: Frontmatter provenance (repository, ref, tree SHA) travels with the skill file across projects, enabling traceability

- **Evidence**: Official documentation: "Provenance data (repository, ref, tree SHA) writes
  directly into SKILL.md frontmatter, enabling portability across projects."
- **Confidence**: settled (technical mechanism stated in official changelog)
- **Quote**: "Portable provenance: Metadata stored in SKILL.md frontmatter travels with the
  skill."
- **Our assessment**: This is the "where did this skill come from?" answer at the file level.
  A SKILL.md file installed via `gh skill` carries its own origin in frontmatter — you do not
  need to consult a lockfile to know what version and source a skill came from. For security
  audits, this means each skill file is self-documenting about its provenance. For practitioners
  sharing skills between projects, this also means the provenance survives copy-paste or manual
  distribution. Cross-reference: Sentry's `agents.toml` pattern (`pin = false`) deliberately
  omits this level of tracking in favor of dynamic updates — a deliberate tradeoff this spec
  enables teams to make either way.

### Claim 5: The Agent Skills open specification (agentskills.io) enables a single skill file to work across GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI, and Antigravity

- **Evidence**: Official GitHub announcement listing all supported agent hosts. The specification
  is described as "open" and hosted at agentskills.io. The `--agent` flag selects the target
  host.
- **Confidence**: emerging (official claim about cross-host compatibility; spec governance and
  actual interoperability across all six hosts not independently verified)
- **Quote**: "They follow the open Agent Skills specification at agentskills.io and work across
  multiple platforms including GitHub Copilot, Claude Code, Cursor, Codex, and Gemini CLI."
- **Our assessment**: This is the first documented evidence in our corpus of a converging
  portable-skills layer that spans competing agent hosts. Claude Code, Cursor, Codex, and Gemini
  CLI have previously been treated as independent ecosystems requiring separate configuration
  files. If agentskills.io delivers on cross-host portability, a team using multiple agent hosts
  can maintain a single canonical skill repository and install the same skills everywhere.
  The "Antigravity" agent host listed is not publicly documented — may be an internal or
  preview agent, possibly the Copilot Cloud Agent renamed. Track agentskills.io governance to
  assess how actively maintained the spec is.

### Claim 6: GitHub explicitly warns that skills are unverified and may contain prompt injections, hidden instructions, or malicious scripts

- **Evidence**: Official security advisory in the changelog: "Skills are installed at your own
  discretion. They are not verified by GitHub and may contain prompt injections, hidden
  instructions, or malicious scripts."
- **Confidence**: settled (first-party warning from the platform provider)
- **Quote**: "Skills are installed at your own discretion. They are not verified by GitHub and
  may contain prompt injections, hidden instructions, or malicious scripts."
- **Our assessment**: This is a highly significant admission. GitHub is describing a prompt
  injection vector that is architecturally embedded in the skills ecosystem — any skill from any
  source can inject arbitrary instructions into the agent's system context. The supply chain
  integrity mechanisms (immutable releases, SHA pinning) protect against *post-publication*
  tampering but provide zero protection against a malicious publisher who injects prompt
  injections *before* publishing. For Ch03 (Safety and Verification): this is the new frontier
  of context injection attacks, operating at the skills layer rather than user input. Teams that
  auto-install or auto-update skills without review have an explicit prompt injection surface.
  The recommended mitigation is `gh skill preview` before installation (Claim 8).

### Claim 7: `--pin` locks a skill to a specific version tag or commit SHA, preventing silent updates

- **Evidence**: CLI syntax documented in changelog: `gh skill install github/awesome-copilot
  documentation-writer --pin v1.2.0` and by commit SHA `@abc123def`.
- **Confidence**: settled (CLI syntax documented in official changelog)
- **Quote**: N/A (command syntax given directly)
- **Our assessment**: Pin-by-SHA is the stronger guarantee over pin-by-tag: SHAs are
  content-addressed and cannot be moved; tags can be deleted and recreated (though the immutable
  releases mechanism should prevent this for published tags). Teams that prioritize security
  should prefer SHA pinning for production use. Teams that want automatic minor/patch updates
  should use semantic version pinning. Teams with no pin get whatever the current HEAD of the
  source directory is — the highest convenience, highest risk posture. This parallels the
  `dependabot` + lockfile choice in traditional dependency management.

### Claim 8: `gh skill preview` is the prescribed trust-verification step before installation — inspect content before it can affect your agent's behavior

- **Evidence**: Official recommendation: "Users should inspect content using `gh skill preview`
  before installation."
- **Confidence**: settled (official recommendation in changelog)
- **Quote**: "Users should inspect content using `gh skill preview` before installation."
- **Our assessment**: This is the human-in-the-loop gate that GitHub provides in lieu of
  verification. Since skills are unverified (Claim 6), `gh skill preview` is the only named
  defense against prompt injection at the install step. For Ch03: establish `gh skill preview`
  + human review as the required gate before any skill install in a team or enterprise context.
  The absence of a scanning tool (e.g., an automated prompt injection detector) here is notable —
  humans are the intended verification mechanism, which does not scale to large skill libraries
  or automated installation pipelines.

### Claim 9: `gh skill publish --fix` auto-validates against the spec and can automatically remediate publishing violations

- **Evidence**: CLI syntax from changelog: `gh skill publish --fix`. The publish command is
  described as checking tag protection, secret scanning, and code scanning.
- **Confidence**: settled (CLI syntax documented)
- **Quote**: N/A (command syntax given directly; validation gates named)
- **Our assessment**: The publisher-side validation adds a trust layer for published skills:
  publishers must pass tag protection, secret scanning, and code scanning checks before a skill
  can be published. This does not prevent prompt injections (which are not secrets or code in
  the traditional sense) but it does prevent accidental credential leaks in skill files and
  requires tag protection to be enabled (supporting the immutability guarantee). The `--fix`
  flag suggests common validation errors can be auto-corrected — lowering the barrier for first-
  time publishers. Practitioners building shared skill libraries should run `gh skill publish`
  as part of their CI pipeline to catch spec violations early.

### Claim 10: The `--agent` flag enables targeted installation for specific agent hosts — the same skill can be installed differently across Claude Code, Cursor, Codex, etc.

- **Evidence**: CLI syntax: `gh skill install github/awesome-copilot documentation-writer
  --agent claude-code --scope user`. Multiple agent values shown: `claude-code`, `cursor`,
  `codex`, `gemini`, `antigravity`.
- **Confidence**: settled (CLI flag documented in official changelog)
- **Quote**: N/A (command syntax given directly)
- **Our assessment**: The `--agent` flag implies that skill installation is not purely
  file-copy — there is host-specific adaptation at install time. The same source skill may be
  installed into different locations or with different formatting depending on the target agent.
  For teams using multiple agent hosts (e.g., Sentry's `agents.toml` supports both Claude and
  Cursor), this flag enables selective installation without maintaining separate skill inventories.
  The `--scope user` flag (vs. the implied project scope) means skills can be installed globally
  for a user rather than per-project — a distinction relevant to Ch01 (individual daily workflow)
  vs. Ch02 (project harness configuration).

## Concrete Artifacts

### Complete `gh skill` CLI Surface

```bash
# Installation variants
gh skill install github/awesome-copilot                           # interactive discovery
gh skill install github/awesome-copilot documentation-writer     # specific skill
gh skill install github/awesome-copilot documentation-writer@v1.2.0   # version pin (tag)
gh skill install github/awesome-copilot documentation-writer@abc123def # version pin (SHA)
gh skill install github/awesome-copilot documentation-writer \
  --agent claude-code \
  --scope user                                                    # agent + scope targeting
gh skill install github/awesome-copilot documentation-writer \
  --pin v1.2.0                                                    # explicit pin flag

# Discovery
gh skill search mcp-apps

# Updates
gh skill update               # interactive check for updates
gh skill update git-commit    # specific skill update
gh skill update --all         # all skills, no prompt

# Publishing
gh skill publish              # validate against spec + checks
gh skill publish --fix        # validate and auto-fix common issues

# Inspection (recommended before install)
gh skill preview OWNER/REPO SKILL
```

### Supported Agent Hosts (via --agent flag)

```
--agent copilot     # GitHub Copilot (default)
--agent claude-code # Anthropic Claude Code
--agent cursor      # Cursor
--agent codex       # OpenAI Codex
--agent gemini      # Google Gemini CLI
--agent antigravity # Antigravity (undocumented)
```

### Supply Chain Integrity Mechanisms

```
1. Content-addressed detection:
   Each installed skill records git tree SHA of source directory.
   gh skill update compares local SHA against remote — reports only
   on real content changes, not tag-only pointer moves.

2. Immutable releases:
   Git tags with protection prevent post-publication alteration.
   "Release content cannot be altered after publication, even by admins."

3. Version pinning:
   --pin v1.2.0     (tag-based; mutable if tag is unprotected)
   @abc123def       (SHA-based; content-addressed, cannot be moved)

4. Portable provenance:
   SKILL.md frontmatter contains: repository, ref, tree SHA.
   Travels with the file across projects. Self-documenting origin.
```

### Publishing Validation Gates

```
gh skill publish checks:
  ✓ Agent Skills spec compliance (agentskills.io)
  ✓ Tag protection enabled (supports immutability guarantee)
  ✓ Secret scanning (no credential leaks in skill files)
  ✓ Code scanning
  --fix: auto-remediate common spec violations
```

### Security Advisory (verbatim)

```
"Skills are installed at your own discretion. They are not verified
by GitHub and may contain prompt injections, hidden instructions,
or malicious scripts."

Prescribed mitigation: gh skill preview OWNER/REPO SKILL
(inspect content before installation)
```

## Cross-References

- **Corroborates**:
  - **practitioner-getsentry-sentry.md** (Pattern 5 — External Skills Registry): Sentry's
    `agents.toml` pulls skills from `getsentry/skills` and `getsentry/warden` with `pin = false`
    and `gitignore = true`. That note documents authoring and consuming skills; this source
    documents the emerging package-manager layer for distributing them. The `gh skill` model is
    the ecosystem-level standardization of what Sentry implemented manually via `agents.toml`.
    Notable tension: Sentry uses `pin = false` (dynamic updates), while the `gh skill` supply
    chain model recommends pinning for security. Teams must choose between Sentry's maintenance-
    convenience model and the security-oriented pinning model this source promotes.
  - **blog-cursor-security-agents.md**: Cursor's security agent deployment describes supply chain
    concerns at the agent execution level. This source extends those concerns to the skill
    distribution layer — prompt injection is now a vector at install time, not just at runtime.

- **Contradicts**: None identified. The `pin = false` choice in Sentry's `agents.toml` is a
  deliberate convenience tradeoff, not a contradiction of the security guidance here — both
  recognize the tradeoff and Sentry made an informed choice. No contradiction issue filed.

- **Extends**:
  - **practitioner-getsentry-sentry.md**: Adds the ecosystem-level view of skills management.
    Sentry's note shows one team's approach; this source documents the standard that is emerging
    around that approach.
  - **paper-gloaguen-agentsmd-effectiveness.md**: Covers AGENTS.md effectiveness for coding
    agents. This source introduces a related but distinct artifact (SKILL.md vs AGENTS.md) and a
    distribution concern (supply chain integrity) that the AGENTS.md literature does not address.
    Practitioners should treat AGENTS.md and SKILL.md as complementary: AGENTS.md configures
    the project context; SKILL.md distributes reusable capabilities across projects and agent hosts.
  - **blog-ccunpacked-claude-code-architecture.md** (Claim 3): The ccunpacked taxonomy places
    skills in Claude Code's `skills/` directory (20 files in the codebase). This source confirms
    that Claude Code is an official target for the agentskills.io distribution model, giving that
    `skills/` directory a standardized upstream distribution mechanism.

- **Novel**:
  - **Package manager paradigm for agent capabilities**: No other source in our corpus documents
    a managed distribution layer for agent skills with version semantics, content-addressed
    update detection, and immutable releases. Prior sources describe authoring and consuming
    skills manually (Sentry, ccunpacked); this introduces the distribution infrastructure.
  - **Prompt injection as a supply chain attack surface**: The explicit GitHub warning that
    skills "may contain prompt injections" frames skill distribution as a new context injection
    attack vector. Prior corpus sources discuss prompt injection as a runtime concern (user input,
    tool output, file content); this is the first source to document it at the install/distribution
    layer.
  - **Cross-agent specification (agentskills.io)**: First evidence in our corpus of a converging
    open specification that enables the same skill file to work across GitHub Copilot, Claude
    Code, Cursor, Codex, and Gemini CLI. Previous sources treat agent configuration as per-tool.
  - **SHA-based content-addressing for skills**: The git tree SHA tracking mechanism is a
    production implementation of content-addressed dependency management applied to agent context
    files. No prior source in our corpus uses this concept.

## Guide Impact

- **Chapter 02 (Harness Engineering — Skills)**:
  - Add a "Skills Distribution" section covering the `gh skill` package manager model. The key
    question for practitioners: should you author skills inline (in `.agents/skills/`),
    distribute them via a shared repository (`getsentry/skills` pattern), or publish them to the
    agentskills.io ecosystem? The answer depends on whether skills are team-private, org-shared,
    or community-shared.
  - Add the `--pin` recommendation: teams that share skills across multiple repos or agent hosts
    should pin to a SHA or version tag in CI/CD contexts. Document the SHA-over-tag preference
    for security-sensitive environments.
  - Reference Sentry's `pin = false` as the opposite end of the tradeoff: high update convenience,
    no stability guarantees.

- **Chapter 03 (Safety and Verification)**:
  - Add a "Skills Supply Chain" subsection documenting the prompt injection attack surface at the
    skill install layer. The new threat model: attackers who compromise a skill repository can
    inject arbitrary instructions into the agent's system context on next `gh skill update`.
  - Prescribe `gh skill preview` + human content review as the required gate before any skill
    install, especially in CI/automated contexts. Note that GitHub's own security warning
    explicitly acknowledges this risk — cite verbatim.
  - Note the gap: `gh skill publish` validation checks tag protection, secrets, and code scanning,
    but has no mechanism to detect prompt injection payloads. The human review gate is currently
    the only defense.

- **Chapter 01 (Daily Workflows)**:
  - Add `gh skill install --scope user` as the individual-developer skill management pattern:
    install commonly-used skills globally (not per-project) for consistent personal tooling
    across projects. Distinct from the per-project harness configuration in Ch02.

- **Chapter 05 (Team Adoption)**:
  - The cross-agent compatibility (agentskills.io) is a team-level governance consideration:
    teams using multiple agent hosts can now maintain a single skill library instead of
    separate configurations per tool. Document this as an emerging capability (spec is new as of
    April 2026; real-world interoperability should be validated before committing to the pattern).

## Extraction Notes

1. **Source is a changelog (~400 words)**: All substantive content was exhausted in 10 claims
   above. Two WebFetch calls were made: the first extracted core commands; the second verified
   completeness and captured verbatim quotes. Results were consistent.
2. **agentskills.io not fetched**: The open specification at agentskills.io was not fetched
   in this extraction. The spec governs SKILL.md format, required frontmatter fields, and
   cross-host compatibility rules. A separate source note for agentskills.io would be high-value,
   particularly for teams that want to author skills rather than just consume them.
3. **"Antigravity" agent host**: Not publicly documented. Appears in the `--agent` flag values.
   May be the Copilot Cloud Agent (CCA) rebranded, an internal preview, or a third-party host.
   Should be tracked for clarification.
4. **No effectiveness data**: This changelog makes no claims about whether skill-loaded agents
   perform better or worse on tasks. For that dimension, see paper-gloaguen-agentsmd-effectiveness
   (which studies AGENTS.md, the closest equivalent) — the cost-increase findings there likely
   transfer to skill-heavy configurations.
5. **GitHub CLI v2.90.0 minimum**: Teams using older GitHub CLI versions will need to upgrade
   before `gh skill` commands are available. Note this as a prerequisite in any guide section
   that references the CLI syntax.
