---
source_url: https://developers.googleblog.com/powering-the-agent-development-lifecycle-with-any-framework-from-adk-to-langchain-and-beyond/
source_type: blog-post
title: "Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond"
author: Pier Paolo Ippolito (Product Manager) and Elia Secchi (Solutions Specialist), Google
date_published: 2026-10-21
date_extracted: 2026-10-24
last_checked: 2026-10-24
status: current
confidence_overall: emerging
issue: "#4302"
---

# Powering the Agent Development Lifecycle with any framework, from ADK to LangChain and beyond

> Walkthrough of the Agents CLI Extension System (a Git-hosted `agents-cli-extension.yaml` that overrides or adds CLI commands, SHA-pinned in a lockfile), showing how a platform team can enforce org policy such as an SBOM scan on `deploy` without forking or wrapping the tool.

## Source Context

- **Type**: blog-post (vendor, Google Developers Blog)
- **Author credibility**: Two Google employees (product manager and solutions specialist) for the tool they describe. They know the mechanism, but the post promotes Agents CLI. Commands and output are shown, but not independently verified.
- **Scope**: Covers the extension model (shapes, reference forms, scopes, lockfile), a first-party LangChain template (v1.8.0), and a custom `sbom-deploy` extension. It does not cover a trust or sandbox model for third-party extension code beyond a passing mention of "third-party trust" re-prompting on update. It gives no measurements, adoption data, or failure cases. The system is explicitly experimental.

## Extracted Claims

### Claim 1: Without an extension mechanism, adapting an opinionated agent CLI to an org's policy or framework leaves three bad options: fork, wrap, or rebuild
- **Evidence**: Author argument, no data. Describes the maintenance tax of forks and wrapper bypass.
- **Confidence**: anecdotal
- **Quote**: "The problem is that developers (and their coding assistants) forget about the wrapper and call the underlying tool directly, bypassing the intended abstraction."
- **Our assessment**: The wrapper-bypass failure mode, with coding assistants named as a bypass vector, is the useful insight. It is plausible and matches general harness experience. It is also the vendor's justification for its own feature, so the fork/wrap/rebuild framing is somewhat convenient.

### Claim 2: An extension is a directory in a Git repo with one manifest file; it either overrides built-in commands or adds new ones, and overridden commands receive the user's arguments verbatim
- **Evidence**: Manifest example and `agents-cli --help` / `agents-cli deploy --help` output in the post.
- **Confidence**: emerging
- **Quote**: "An Agents CLI extension is a directory in a Git repository that contains a single file called agents-cli-extension.yaml."
- **Our assessment**: A concrete, small surface. Verbatim arg passthrough keeps the UX identical for humans and agents. Documented by the vendor and not independently tested.

### Claim 3: Distribution is by Git reference with no registry; one repo can hold several extensions selected by a `#<name>` fragment
- **Evidence**: Reference-form examples (`acme/platform-extensions#soc2-deploy`, `local@../my-extension`).
- **Confidence**: emerging
- **Quote**: "There is no central index to publish to, no package format to maintain, and no ownership roster to apply for."
- **Our assessment**: Low friction for internal platform teams. The trade-off, left unstated, is that trust and review rest entirely on whoever controls the Git repo and the pin. This contrasts with the registry model of the Vercel eve extension note.

### Claim 4: Extensions install at project scope (default, committed to the repo) or user scope (`--global`); project wins on conflict, and the system "will not silently merge or override"
- **Evidence**: Description in the post. `agents-cli info` is said to show the source of each active command.
- **Confidence**: emerging
- **Quote**: "Scoping is deliberately explicit: the Extension System will not silently merge or override extensions, and any conflict surfaces to the developer at install time or in the extension list output."
- **Our assessment**: Precedence plus visible conflict reporting is the right design. One tension: a user-scope extension would be overridden by project scope. That is good for project control but means a platform policy installed with `--global` can be displaced by a project-scope extension, so org-wide enforcement is not guaranteed by scope alone. The post does not discuss this, so this is our inference.

### Claim 5: Extensions resolve to an exact commit SHA recorded in a lockfile; `agents-cli install` restores without advancing the pin, and `extension update` advances it and re-prompts for third-party trust
- **Evidence**: Lockfile example in the post, with an analogy to uv and npm.
- **Confidence**: emerging
- **Quote**: "The install command never advances the pin, so an extension cannot change its behavior between two deployments of the same commit."
- **Our assessment**: Standard supply-chain hygiene applied to agent tooling. It is the key control that makes a policy extension auditable. The post does not say what the "third-party trust" prompt checks.

### Claim 6: Overrides are announced at runtime and labeled in help output rather than applied silently
- **Evidence**: Terminal output shows a `WARNING:root:agents-cli: applying 6 extension command(s)` line and `[↑ langchain]` / `[↑ sbom-deploy]` suffixes in `--help`.
- **Confidence**: emerging
- **Quote**: "The warning is deliberate: an override quietly changes native behavior, so the loader always announces which commands are being intercepted and by whom."
- **Our assessment**: Good transparency practice, and it matters for agents reading terminal output. It only informs; it does not constrain. Whether the loader can block a user from bypassing it is addressed in Claim 8.

### Claim 7: Manifest validation is strict, and `run:` is a command vector with no shell, so chaining needs a wrapper script
- **Evidence**: Manifest schema description and the rules from the authoring docs, as summarized in the post.
- **Confidence**: emerging
- **Quote**: "The schema uses strict validation, so a typo like reqires: fails install with a did-you-mean suggestion rather than silently dropping the override."
- **Our assessment**: Failing loudly on a typo is important for a policy mechanism, since a silently dropped override would mean a silently skipped compliance gate. Also notable: only specific subcommands (e.g. `eval.generate`) can be overridden, not command groups.

### Claim 8: Recursion is avoided with `AGENTS_CLI_DISABLE_OVERRIDES=1`, which the loader sets for override scripts. The same variable is documented as the bypass for running the built-in command
- **Evidence**: The `sbom_then_deploy.sh` script and the `deploy --help` text.
- **Confidence**: emerging
- **Quote**: "To bypass extension overrides and run the built-in:"
- **Our assessment**: This matters for enforcement: the same environment variable that prevents recursion is also a documented way for any developer or agent to skip the policy override locally. So the extension is a guardrail and not a hard gate. Real enforcement would still need a CI-side or server-side check. The post does not make this caveat, so it is our inference. Because the Quote field must be verbatim and this is a fragment of the help text, see the artifact below for the full lines.

### Claim 9: Org policy (SBOM scan via syft+grype, failing on critical vulnerabilities) can be implemented as a `deploy` override that delegates to the native deploy on success
- **Evidence**: Full manifest and bash wrapper in the post. Only an echo-based demo of the wrapper is shown running, not a real scan.
- **Confidence**: anecdotal
- **Quote**: "grype sbom:/tmp/sbom.cdx.json --fail-on critical"
- **Our assessment**: A clear worked pattern: gate, then `exec` the built-in with `"$@"` forwarded. The post demonstrates the plumbing with an echo stub, not an actual blocked deploy, so the policy behavior itself is unshown.

### Claim 10: A non-ADK framework can reuse the whole framework-agnostic lifecycle by overriding only the framework-coupled commands (6 of ~24)
- **Evidence**: `agents-cli info` listing six overrides; the post states deploy, infra, login and others are unchanged. The grep check for `google-adk` is shown.
- **Confidence**: emerging
- **Quote**: "Within the Agents CLI command surface, six commands assume the ADK runtime: playground, run, and four eval subcommands."
- **Our assessment**: A reasonable decomposition of "framework-coupled vs framework-agnostic" harness pieces. The LangChain details are low priority for the guide.

### Claim 11: Unsupported commands should refuse explicitly with an explanation, which matters when a coding assistant is driving the terminal
- **Evidence**: `eval.dataset` / `eval.optimize` overrides that print a refusal. Example output shown.
- **Confidence**: anecdotal
- **Quote**: "A clear refusal is more useful than a silent failure, especially when a coding assistant is driving the terminal and would otherwise retry a broken command multiple times before giving up."
- **Our assessment**: A small, actionable CLI-for-agents design rule. It is an assertion without measured retry behavior.

### Claim 12: The Extension System is experimental, so teams should pin the CLI version
- **Evidence**: Explicit statement in the post. Introduced in v1.5.0, with the first-party LangChain extension in v1.8.0.
- **Confidence**: settled (as a statement of the vendor's own status)
- **Quote**: "The manifest schema and the command surface may still change in breaking ways before the system is finalized, so teams depending on it should pin their Agents CLI version."
- **Our assessment**: Any guide advice drawn from this must be flagged as version-dependent. The post also states "in about thirty minutes" for the ADK path, which is unmeasured.

## Concrete Artifacts

Manifest (from the post, "Step 1: Defining the Extension Manifest"):

```yaml
# agents-cli-extension.yaml
schema: agents-cli-extension/v1alpha1
name: sbom-deploy
description: Scan the project SBOM, then run the native agents-cli deploy.
requires:
  agents_cli: ">=1.5,<2"
  on_incompatible: warn
commands:
  override:
    deploy:
      run: ["bash", "scripts/sbom_then_deploy.sh"]
      description: SBOM scan via syft+grype, then the built-in deploy.
  add:
    sbom-report:
      run: ["bash", "scripts/sbom_report.sh"]
      description: Produce an SBOM for the current project (no deploy).
```

Wrapper script (from the post, "Step 2"):

```bash
#!/usr/bin/env bash
# scripts/sbom_then_deploy.sh
set -euo pipefail
cd "$(dirname "$0")/.."
echo "[sbom-deploy] generating SBOM..."
syft dir:. -o cyclonedx-json > /tmp/sbom.cdx.json
echo "[sbom-deploy] scanning for criticals..."
grype sbom:/tmp/sbom.cdx.json --fail-on critical
# AGENTS_CLI_DISABLE_OVERRIDES=1 is already set by the loader,
# so this call hits the built-in deploy. No infinite recursion.
echo "[sbom-deploy] SBOM clean; running native deploy..."
exec agents-cli deploy "$@"
```

Lockfile (from the post, "Lockfile Discipline"):

```yaml
# agents-cli-extensions.yaml  (lockfile; commit this to version control)
extensions:
- name: sbom-deploy
  source: acme/platform-extensions#sbom-deploy
  ref: v1.0.0
  sha: a1b2c3d4...
  scope: project
```

Override transparency output (from the post):

```
WARNING:root:agents-cli: applying 6 extension command(s): eval.dataset [langchain/project], eval.generate [langchain/project], eval.optimize [langchain/project], playground [langchain/project], publish.gemini-enterprise [langchain/project], run [langchain/project]
```

Bypass text from `agents-cli deploy --help` (from the post):

```
  To bypass extension overrides and run the built-in:
  AGENTS_CLI_DISABLE_OVERRIDES=1 agents-cli deploy
```

Install forms (from the post): `agents-cli extension add acme/platform-extensions#sbom-deploy --ref v1.0.0`, `agents-cli extension add local@../my-sbom-extension`, `agents-cli extension update sbom-deploy`.

## Cross-References

- **Corroborates**: `blog-vercel-eve-extensions.md`, Claim 2 (updates arrive by updating the package rather than copying code into the consumer) on the general principle of extension-based customization without forking. Mechanisms differ: eve uses a registry and namespaced mounts, Agents CLI uses Git refs and command overrides.
- **Contradicts**: None filed. No existing note was found taking an opposing position on extension-based policy enforcement.
- **Extends**: `blog-google-adk-recipes-three-layers.md` (same Google ADK ecosystem, Claims 7 and 11 on plugins and skills install). This note adds the CLI-level command-override layer. Also complements `blog-google-adk-zero-trust-agents.md` at the tooling level, though that note covers runtime agent trust.
- **Novel**: Command-level override of an agent CLI via a Git-hosted manifest; SHA-pinned lockfile for CLI extensions; explicit "no silent override" and runtime-announcement behavior; the env-var recursion/bypass trick; the design rule that unsupported commands should refuse loudly for agent callers.

## Guide Impact

- **Chapter 02**: Add a harness-extensibility example. Per-project command overrides, with transparent labeling and strict manifest validation, are a way to put policy hooks in the tooling path that coding agents invoke. Note the wrapper-bypass problem (Claim 1) and that env-var bypass (Claim 8) makes this a guardrail, not enforcement.
- **Chapter 05**: Platform teams can distribute org policy (compliance scan, SSO gate) through an internal Git repo of pinned extensions, with the lockfile committed so CI matches reviewed code (Claims 3, 5, 9). Pair with a CI-side check since local overrides can be bypassed.
- **Chapter 06**: Third-party extensions pulled from Git are executable code in the deploy path. The post supplies SHA pinning and an update-time trust prompt but no sandboxing or signing. Cite as a supply-chain control and as an open question. Flag as vendor-reported and experimental.

## Extraction Notes

- Read the full post text (fetched as HTML and converted to text for verbatim quoting). The linked docs pages (Using/Authoring Extensions, First-party frameworks) were not followed, so details such as the trust prompt and rule list are second-hand via the post.
- The post is vendor-authored. The sbom-deploy extension is demonstrated with echo stubs; no real scan or blocked deploy is shown.
- Claim 8's quote is a fragment of the help-text line; the bypass command appears in Concrete Artifacts. The enforcement caveat is our inference.
- Cross-reference claim numbers were checked against the headings in `blog-vercel-eve-extensions.md` and `blog-google-adk-recipes-three-layers.md`.
- No contradictions were filed.
