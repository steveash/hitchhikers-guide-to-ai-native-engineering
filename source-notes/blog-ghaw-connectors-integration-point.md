---
source_url: https://github.github.com/gh-aw/blog/2026-11-12-connectors/
source_type: blog-post
title: "Connectors: A Clear Integration Point for Services"
author: Copilot (GitHub Agentic Workflows blog)
date_published: 2026-11-12
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: emerging
issue: "#4694"
---

# Connectors: A Clear Integration Point for Services

> A short vendor overview of gh-aw's experimental connectors: a reviewable YAML service contract that grants nothing until each workflow selects reads and writes, with a conservative rollout recipe.

## Source Context

- **Type**: blog-post (first-party gh-aw blog; submitted as "documentation")
- **Author credibility**: Byline is "Copilot" (AI-authored post on the project's own blog). It speaks for the gh-aw maintainers, but it is design intent from the feature's vendor, with no production data.
- **Scope**: Overview and rationale only. Includes one partial Linear YAML excerpt. The normative rules (phase-scoped credentials, exact-ID grants, redirect rejection, etc.) live in the spec, already extracted in `docs-ghaw-connector-specification.md`. The post has no metrics, incidents or evaluation.

## Extracted Claims

### Claim 1: A connector is a single declarative contract bundling endpoints, credential routes, resource grants, reads and safe outputs, with shared compiler/runtime machinery.
- **Evidence**: Architectural description; no measurements.
- **Confidence**: emerging
- **Quote**: "A connector brings the pieces of an integration together: fixed endpoints, credential routes, resource grants, read capabilities, and safe outputs."
- **Our assessment**: A sound tool-surface design: per-provider specifics are data, while validation, tool exposure and write execution are common code. Whether this holds across very different providers is untested here.

### Claim 2: Adding a supported operation is a declaration change rather than new provider-specific execution code.
- **Evidence**: Assertion only; the example catalog is the implied support.
- **Confidence**: emerging
- **Quote**: "Adding a supported operation is a declaration change, not a reason to build a new provider-specific execution path."
- **Our assessment**: Plausible for bounded REST/GraphQL readers and typed mutations. The spec forbids arbitrary script execution, which is what makes this true, and which also limits expressiveness.

### Claim 3: Because the contract is declarative, integration changes are reviewable as diffs and the contract is versionable.
- **Evidence**: Design argument.
- **Confidence**: emerging
- **Quote**: "A new endpoint, a different secret reference, or an added write operation is visible in a diff."
- **Our assessment**: Real benefit over integrations scattered in scripts and prompts. It only helps if reviewers actually look at the connector diff; the post gives no mechanism to enforce review.

### Claim 4: Without a shared integration point, service answers (location, auth, permitted actions) scatter across scripts, custom tools and prompts, making each service a special case.
- **Evidence**: Motivation statement; no data.
- **Confidence**: anecdotal
- **Quote**: "Without a clear integration point, those answers end up scattered across scripts, custom tools, and prompts."
- **Our assessment**: Matches common experience, but this is the problem statement, not demonstrated evidence.

### Claim 5: Define once, select per workflow: importing a connector enables nothing; reads are selected under `tools` and writes separately under `safe-outputs`, outside the agent's writer-credential boundary.
- **Evidence**: Design statement; mirrors spec Claims 2 and 3 in the existing note.
- **Confidence**: emerging
- **Quote**: "Importing alone enables no provider tools or writes."
- **Our assessment**: Strong least-privilege pattern (capability declared broadly, authority granted narrowly per task). Same claim as the spec; this post adds the framing, not new controls.

### Claim 6: Resource bindings constrain access, and IDs returned by the service do not expand grants.
- **Evidence**: Design statement (normative form is spec Claim 4).
- **Confidence**: emerging
- **Quote**: "Resource bindings constrain access, and IDs returned by the service don’t expand those grants."
- **Our assessment**: Addresses a confused-deputy path in which untrusted read output nominates write targets. Good rule; corroborates the spec only.

### Claim 7: The same declaration can serve different workflows with different selections and approved resources; the Linear triage example selects two readers and one staged comment.
- **Evidence**: One example workflow, described but not shown.
- **Confidence**: anecdotal
- **Quote**: "For example, the Linear triage workflow selects two readers and one staged comment."
- **Our assessment**: Illustrates the split but the post gives neither the workflow nor a second consumer. Closing line "The service contract is reusable. The authority stays specific to the task." is a good compact principle.

### Claim 8: Staging previews a write without delivering it while reads stay live.
- **Evidence**: Statement; the spec adds that staging does not suppress readers or workflow scripts.
- **Confidence**: emerging
- **Quote**: "Staging previews the write without delivering it; reads remain live."
- **Our assessment**: Important caveat for rollout: a staged run still exercises live read credentials and calls provider APIs, so "staged" is not "no side effects or no exposure". See the staged-mode reference note.

### Claim 9: Connectors are experimental and not turnkey: declarations do not provision credentials, install webhook receivers, or turn scope metadata into provider permissions.
- **Evidence**: The post's own stated limits.
- **Confidence**: settled (as a statement of the feature's limits)
- **Quote**: "Declarations don’t provision credentials, install webhook receivers, or turn scope metadata into provider permissions."
- **Our assessment**: Honest limit. Scope metadata is documentation, not enforcement, so the operator must configure provider-side least privilege separately.

### Claim 10: Recommended rollout: connector-capable compiler with matching runtime, a reviewed source revision, manual dispatch, and staged outputs.
- **Evidence**: Prescriptive advice; no justification beyond experimental status.
- **Confidence**: emerging
- **Quote**: "Start with a connector-capable compiler and matching runtime, a reviewed source revision, manual dispatch, and staged outputs."
- **Our assessment**: A concrete four-part gate for adopting a new, unproven agent integration: pin tooling, review the source, keep a human trigger, preview writes. Generalizable beyond gh-aw.

## Concrete Artifacts

Linear connector excerpt (verbatim from the post; the post says it is "not a complete connector"):

```yaml
connectors:
  linear:
    experimental: true
    endpoints:
      api: https://api.linear.app
    credentials:
      reader:
        phase: agent
        header: Authorization
        scheme: raw
        scopes: [read]
        secret: ${{ github.aw.import-inputs.reader-secret }}
    resources:
      issues: ${{ github.aw.import-inputs.issues }}
```

Location: connector YAML lives "in the frontmatter of an importable Markdown file under .github/workflows/connectors/". Services with declarations per the post: Linear, Jira, Azure DevOps, Slack, Teams. Full declarations add typed operation inputs, request mappings, response limits, resource checks and import input definitions.

## Cross-References

- **Corroborates**: `docs-ghaw-connector-specification.md` Claim 2 (importing selects nothing), Claim 3 (writer credentials never reach the agent), Claim 4 (IDs returned by a read never become write authority), Claim 13 (staging suppresses writes but not readers). `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents execute without write permissions) is the underlying separation.
- **Contradicts**: None found.
- **Extends**: `docs-ghaw-staged-mode-reference.md` Claim 7 (staged-first adoption loop) by applying it to connectors; `docs-ghaw-connector-specification.md` by adding the diff-review argument, the Linear excerpt and the rollout gate.
- **Novel**: The four-part rollout gate (Claim 10), the "reviewable as a diff" rationale (Claim 3), and the "reusable contract, task-specific authority" framing. No new controls beyond the spec.

## Guide Impact

- **Chapter 06**: Where the guide cites the connector spec for least-privilege tool surfaces, add this post as an accessible one-paragraph statement of "declare broadly, select narrowly, IDs from reads never grant writes". Note that staged mode keeps reads live (Claim 8).
- **Chapter 02**: Cite as an example of keeping tool contracts declarative and diff-reviewable instead of scattering them across scripts and prompts (Claims 1-3). Treat as design intent, not validated.
- **Chapter 02 / rollout guidance**: Claim 10's gate is a reusable pattern for adopting any experimental agent integration.

## Extraction Notes

- Read the full post (single page, no substantive sub-pages followed; the connector reference and create-connector skill are linked but were not fetched, since the spec is already covered by #4681).
- Quotes copied verbatim from the page text. The post byline is "Copilot".
- Thin source by nature (overview); extracted only claims not duplicating the spec note, per triage guidance. Confidence stays `emerging`: no production evidence.
