---
source_url: https://github.github.com/gh-aw/reference/cache-memory
source_type: docs
title: "GitHub Agentic Workflows: cache-memory Reference"
author: GitHub Agentic Workflows team (official reference documentation)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#360"
---

# GitHub Agentic Workflows: cache-memory Reference

> The formal reference specification for `cache-memory` — the platform's native cross-run persistence primitive — providing technical constraints (7-day default retention, 10GB repository limit, LRU eviction), the full configuration API (retention-days up to 90, allowed-extensions, multiple named caches, scope, import merge rules), the integrity-aware isolation model for multi-trust-level pipelines, and operational troubleshooting signals including the `missing_data`/`cache_memory_miss` diagnostic.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows reference documentation, "reference" section, "cache-memory" page — the formal API-level reference for this tool, distinct from the guides and patterns pages that document usage examples)
- **Author credibility**: First-party from the GitHub Agentic Workflows platform team (GitHub Next / Microsoft Research). This is the authoritative reference for `cache-memory` configuration — the same team that built the `gh aw` compiler and runtime. Configuration syntax, storage constraints, and integrity semantics are authoritative for the `gh aw` platform; practitioner recommendations (best practices, troubleshooting) are drawn from the same team's production experience with 183+ workflows.
- **Scope**: Covers the full `cache-memory` configuration schema (basic + advanced + multi-cache + import merging), GitHub Actions Cache storage constraints (7-day retention, 10GB limit, LRU eviction), cache key dynamics (compiler key management, restore-key generation, `scope: repo` for cross-workflow sharing), the formal comparison with `repo-memory`, automatic cleanup behavior, the complete troubleshooting table (including the `missing_data`/`cache_memory_miss` diagnostic), integrity-aware caching (git-branch isolation, merge semantics), security model (threat-detection-aware save sequence), and one real-world usage example (Grumpy Code Reviewer). Does NOT cover: the `repo-memory` configuration schema in detail (see `docs-ghaw-agentic-ops.md`), the underlying GitHub Actions cache API, or how to design agent prompts that use cache-memory effectively (see `docs-ghaw-audit-with-agents.md`, `docs-ghaw-dailyops.md`, `docs-ghaw-expert-ops.md`).

## Extracted Claims

### Claim 1: `cache-memory: true` enables persistent file storage at `/tmp/gh-aw/cache-memory/` across workflow runs, with the compiler automatically handling cache directory configuration, restore/save operations, and progressive fallback keys

- **Evidence**: Stated in the Overview and Basic Configuration sections. The page documents that the single `tools: cache-memory: true` flag causes the compiler to automatically configure the cache directory, restore/save operations, and progressive fallback keys — no manual cache step configuration is needed.
- **Confidence**: settled (first-party reference documentation; corroborated by `docs-ghaw-dailyops.md` Claim 6, `docs-ghaw-expert-ops.md` Claim 6, and `docs-ghaw-audit-with-agents.md` Claim 5, all of which document usage of this same mechanism)
- **Quote**: "Cache Memory provides persistent file storage across workflow runs using GitHub Actions cache with 7-day retention. The compiler automatically configures the cache directory, restore/save operations, and progressive fallback keys at `/tmp/gh-aw/cache-memory/` (default) or `/tmp/gh-aw/cache-memory-{id}/` (additional caches)."
- **Our assessment**: This settles what was previously documented across three separate source notes as "emerging." The reference page confirms that `cache-memory: true` is the standard platform primitive for cross-run agent state persistence, and that compiler automation (not manual step configuration) is the intended use pattern. For Ch02 (Harness Engineering): this is the authoritative confirmation of the pattern that `docs-ghaw-dailyops.md`, `docs-ghaw-expert-ops.md`, and `docs-ghaw-audit-with-agents.md` each document from a usage perspective.

### Claim 2: The compiler automatically appends `${{ github.run_id }}` to user-supplied cache keys and generates stable restore-keys by stripping that suffix — practitioners must not include the run ID manually

- **Evidence**: Documented explicitly in the "Important:" callout in the Advanced Configuration Options section. This explains the mechanism by which each run saves to a unique key while still being able to restore from the previous run's cache: the restore-key prefix matches all prior saves from the same workflow.
- **Confidence**: settled (first-party reference documentation; the behavior is described as automatic compiler behavior)
- **Quote**: "The compiler automatically appends `${{ github.run_id }}` to user-supplied keys and generates stable restore-keys from the prefix. Do not include the run ID manually."
- **Our assessment**: This is the first explanation in the corpus of *how* the cache key dynamics work under the hood. Prior notes document what cache-memory does; this explains why it works across runs: each run gets a unique save key (suffix includes `run_id`), and the restore key is the prefix without the `run_id`, so each run falls back to the most recent prior run's cache. The "do not include the run ID manually" warning is a concrete pitfall for practitioners building custom key configurations. For Ch02: include this explanation when documenting advanced cache-memory key configuration.

### Claim 3: The `retention-days` configuration option (1–90 days) extends cache access beyond the default 7-day GitHub Actions cache retention period

- **Evidence**: Documented in the Advanced Configuration Options section as a named field with comment "1-90 days, extends access beyond cache expiration." The separate Behavior Specifications section states the baseline constraint: "7-day retention period" as the default GitHub Actions Cache behavior.
- **Confidence**: settled (first-party reference documentation)
- **Quote**: `retention-days: 30  # 1-90 days, extends access beyond cache expiration`
- **Our assessment**: This fills a gap in the corpus. `docs-ghaw-audit-with-agents.md` Claim 5 documents a 30-day rolling baseline maintained in cache-memory (with rolling averages kept as file content), but never addresses whether the underlying cache itself persists for 30 days. The `retention-days` option allows the cache entry to persist up to 90 days — meaning the 30-day rolling baseline in audit workflows is achievable only if `retention-days: 30` is also configured, not just through file-content management. For Ch02: document that `retention-days` must be set to match or exceed the workflow's intended data retention window; the 7-day default would silently invalidate longer-horizon data.

### Claim 4: The `allowed-extensions` field restricts storable file types to a whitelist, with disallowed files triggering validation failures rather than silent ignoring

- **Evidence**: Documented in the "File Type Restrictions" subsection under Advanced Configuration Options. Default behavior (empty array) is to allow all file types; when specified, only listed extensions can be written.
- **Confidence**: settled (first-party reference documentation)
- **Quote**: "The `allowed-extensions` field restricts storable file types. By default, all file types are allowed (empty array). When specified, only files with listed extensions can be written. Disallowed files trigger validation failures."
- **Our assessment**: This is a security configuration option with no analog in any existing source note. The failure mode (validation failure, not silent ignore) makes it enforceable as a security control: if an agent attempts to cache a `.env` file, the workflow fails rather than silently caching sensitive data. For Ch02/Ch03 (Safety): recommend configuring `allowed-extensions` when using cache-memory in workflows that process potentially sensitive file types; the whitelist approach is a defense-in-depth measure complementing the "don't store sensitive data" best practice.

### Claim 5: Multiple named caches can be configured via an array with `id:` fields, mounting at `/tmp/gh-aw/cache-memory-{id}/` rather than the default path

- **Evidence**: "Multiple Cache Configurations" section provides a complete YAML example with three named caches (`default`, `session`, `logs`) each with distinct `id:`, `key:`, and `retention-days:` values. The mounting behavior is explicitly documented.
- **Confidence**: settled (first-party reference documentation; YAML example is specific)
- **Quote**: "Multiple caches mount at `/tmp/gh-aw/cache-memory/` (default) or `/tmp/gh-aw/cache-memory-{id}/`. The `id` determines the folder name; `key` defaults to a workflow-scoped prefix derived from the sanitized workflow name."
- **Our assessment**: This is novel to the corpus. Prior notes document only single `cache-memory: true` or `cache-memory: key: <name>` configurations. The multi-cache pattern with named `id:` fields enables workflows to maintain logically separate state stores (e.g., one for session state, one for logs, one for trend data) in isolated paths, without risk of file naming collisions. For Ch02: the multi-cache pattern is the recommended design for workflows that need to maintain multiple categories of persistent state.

### Claim 6: Importing shared workflows with `cache-memory` configurations follows explicit merge rules: Single→Single (local overrides), Single→Multiple (local converts to array), Multiple→Multiple (merge by `id`, local wins)

- **Evidence**: The "Merging from Shared Workflows" section documents all three merge cases with explicit rules. A code example shows `imports: shared/mcp/server-memory.md` combined with `tools: cache-memory: true`.
- **Confidence**: settled (first-party reference documentation; three merge rules stated explicitly)
- **Quote**: "Merge rules apply: **Single→Single** (local overrides), **Single→Multiple** (local converts to array), **Multiple→Multiple** (merge by `id`, local wins)."
- **Our assessment**: Merge semantics are essential for teams using shared workflow templates. Without these rules, importing a shared workflow that uses cache-memory would silently conflict with a local cache-memory configuration. The "local wins" principle throughout is consistent with the general import semantics in other gh-aw configuration contexts. For Ch02: document these merge rules whenever shared workflow templates that include cache-memory are discussed.

### Claim 7: The underlying GitHub Actions cache has a 7-day retention period, a 10GB per-repository limit, and LRU eviction — all applicable to `cache-memory` storage

- **Evidence**: Documented under "Behavior Specifications → GitHub Actions Cache Constraints" with three specific values. No exceptions or overrides for agentic workflows are noted.
- **Confidence**: settled (first-party reference documentation; these are well-known GitHub Actions constraints formally confirmed in the context of cache-memory)
- **Quote**: "7-day retention period, 10GB limit per repository, LRU (Least Recently Used) eviction policy"
- **Our assessment**: These are the hard operational limits for cache-memory storage. The 10GB limit is shared across all caches in the repository — a team with many cache-memory workflows must budget total cache usage. LRU eviction means that actively-used caches survive; a workflow that runs monthly might have its cache evicted before the next run despite being within the 7-day window if other workflows produce more cache traffic. For Ch02: include these constraints in cache-memory documentation so harness engineers can plan storage budgets and set appropriate `retention-days` values.

### Claim 8: Setting `scope: repo` on a cache key generates an additional restore key without the workflow ID, enabling cross-workflow cache sharing

- **Evidence**: Documented under "Cache Key Dynamics": "For `scope: repo`, an additional restore key without the workflow ID permits cross-workflow cache sharing." The default scope is workflow-specific.
- **Confidence**: settled (first-party reference documentation)
- **Quote**: "For `scope: repo`, an additional restore key without the workflow ID permits cross-workflow cache sharing."
- **Our assessment**: This fills an architectural gap between `cache-memory` (normally per-workflow) and `repo-memory` (always cross-workflow, git-backed). The `scope: repo` option makes `cache-memory` usable as a shared state layer without the git-branch infrastructure of `repo-memory`. For teams that want cross-workflow sharing with cache-memory's "fast" performance profile but don't need `repo-memory`'s version control and unlimited retention, `scope: repo` is the intermediate option. For Ch02/Ch04: document this alongside the `cache-memory` vs `repo-memory` comparison as a third point in the sharing-vs-durability spectrum.

### Claim 9: The automatic cleanup via the maintenance workflow groups caches by key prefix, keeps the latest entry per group, and supports manual triggering via the `clean_cache_memories` operation

- **Evidence**: "Automatic Cleanup" section describes grouping by "key prefix (everything before the run ID)" and keeping only the latest entry per group. The manual trigger path is documented as running the "Agentic Maintenance" workflow with the `clean_cache_memories` operation.
- **Confidence**: settled (first-party reference; corroborates `docs-ghaw-ephemerals.md` Claim 6)
- **Quote**: "The agentic maintenance workflow automatically cleans up outdated cache-memory entries on schedule. Caches are grouped by key prefix (everything before the run ID), keeping only the latest entry per group."
- **Our assessment**: This formally confirms `docs-ghaw-ephemerals.md` Claim 6's description of the cleanup mechanism. The "key prefix (everything before the run ID)" grouping strategy is consistent with the compiler appending `run_id` to save keys (Claim 2 here): the prefix is the stable identifier, the `run_id` suffix is the variable component. For Ch07 (Cost Management): scheduled cleanup is required to prevent unbounded storage growth; without it the 10GB repository limit can be reached by long-running deployments with many workflows.

### Claim 10: When an agent calls `missing_data` with reason `"cache_memory_miss"`, the conclusion handler flags a likely cache path misconfiguration — the specific path and key consistency are the first things to verify

- **Evidence**: Troubleshooting table row for "Cache path misconfiguration": the resolution instructs practitioners to check for this specific `missing_data` call and then verify the agent prompt references the correct path.
- **Confidence**: settled (first-party reference documentation; the `missing_data` tool call with this specific reason is named as the diagnostic signal)
- **Quote**: "When agent calls `missing_data` with reason \"cache_memory_miss,\" the conclusion handler flags a likely cache path problem."
- **Our assessment**: This is the first operational diagnostic signal for cache-memory failures in the corpus. The `missing_data` tool call with `"cache_memory_miss"` is a structured agent signal (not just a workflow failure) that the platform's conclusion handler interprets as a likely configuration error. For Ch02: when documenting cache-memory troubleshooting, this is the first signal to check when agents report that expected data is absent — it indicates the agent looked in the right conceptual place but found no cache entry, pointing to either a path reference mismatch or a key inconsistency between the workflow's configuration and the agent's prompt instructions.

### Claim 11: Integrity-aware caching isolates cache state into git branches by integrity level, with ascending-trust read access (each level sees data from its level and all higher-trust levels) and mandatory cache invalidation when the guard policy changes

- **Evidence**: "Integrity-Aware Caching" section documents the full mechanism. The git-branch isolation approach, four integrity tiers, the ascending merge semantics (what each level can read), and policy-change invalidation are all specified. The merge semantics table: `merged` sees merged only; `approved` sees approved + merged; `unapproved` sees unapproved + approved + merged; `none` sees all levels. Activated when `tools.github.min-integrity` is configured.
- **Confidence**: settled (first-party reference documentation; corroborates `blog-ghaw-weekly-2026-03-30.md` Claim 1 which first reported this feature)
- **Quote**: "When workflows use `tools.github.min-integrity`, cache-memory applies integrity-level isolation. Cache keys include the workflow's integrity level and a hash of the guard policy, forcing cache misses when any policy field changes."
- **Our assessment**: This reference page provides the formal specification for what `blog-ghaw-weekly-2026-03-30.md` Claim 1 reported at announcement. Two significant new details not in the weekly blog: (1) the ascending-trust read semantics — `unapproved` runs can read `approved` and `merged` data, but `merged` runs cannot read `unapproved` data; (2) the cache-miss warning for legacy data on first upgrade. The stated rationale: "This prevents lower-integrity agents from poisoning data that higher-integrity runs would later read." For Ch03 (Safety): this is the authoritative specification for integrity-tier isolation in agent state storage — the pattern prevents trust-tier cross-contamination at the storage layer, not just at the policy layer.

### Claim 12: Upgrading to integrity-aware caching causes a cache miss on the first run — existing caches have no integrity provenance and cannot be classified into tiers

- **Evidence**: The "Note:" callout at the end of the Integrity-Aware Caching section. This is a migration warning for teams enabling `min-integrity` on existing workflows that already use `cache-memory`.
- **Confidence**: settled (first-party reference documentation; explicitly noted as a migration behavior)
- **Quote**: "Existing caches will experience a cache miss on first run after upgrading to this feature—legacy data has no integrity provenance."
- **Our assessment**: This is a practical migration warning that practitioners enabling `min-integrity` on existing workflows must know. A workflow that relied on cache-memory for 30-day rolling baselines (as in `docs-ghaw-audit-with-agents.md` Claim 5) would lose its baseline state on the first run after enabling `min-integrity`. Teams should plan for a warm-up period after the migration and ensure that workflows can handle a cold-cache start gracefully. For Ch03: include this warning in any `min-integrity` deployment guidance.

### Claim 13: When threat detection is enabled, cache saves occur only after validation succeeds in a five-step sequence: restore → modify → upload artifact → validate → save

- **Evidence**: Security Considerations section, final bullet: "With threat detection enabled, cache saves only after validation succeeds (restore→modify→upload artifact→validate→save)"
- **Confidence**: settled (first-party reference documentation; the step sequence is explicit)
- **Quote**: "With threat detection enabled, cache saves only after validation succeeds (restore→modify→upload artifact→validate→save)"
- **Our assessment**: This is novel to the corpus. The five-step sequence describes how cache saves are gated behind the platform's threat detection validation when that feature is enabled. The intermediate "upload artifact" step (between modify and validate) indicates the platform uploads the candidate cache contents to an artifact store for validation before committing to the cache — meaning threat detection applies to cache content, not just to agent tool calls. For Ch03 (Safety): document this as an additional defense-in-depth layer for high-security deployments; it means that even a compromised agent cannot poison the cache with malicious content when threat detection is active.

### Claim 14: `cache-memory` and `repo-memory` serve formally distinct persistence roles — cache-memory for fast per-workflow temporary state, repo-memory for version-controlled cross-workflow long-term history

- **Evidence**: Formal comparison table in the "Comparison with Repo Memory" section specifying six dimensions: storage backend (GitHub Actions Cache vs. Git Branches), retention period (7 days vs. Unlimited), size limit (10GB/repo vs. Repository limits), version control (No vs. Yes), performance (Fast vs. Slower), best use case (Temporary/sessions vs. Long-term/history).
- **Confidence**: settled (first-party reference documentation; corroborates `docs-ghaw-agentic-ops.md` Claim 7 which described this distinction from usage patterns)
- **Quote**: (table form — see Concrete Artifacts)
- **Our assessment**: This reference page provides the formal authoritative comparison that `docs-ghaw-agentic-ops.md` Claim 7 described qualitatively from usage patterns. The six-dimension comparison gives harness engineers a concrete decision framework. The "Temporary/sessions" vs "Long-term/history" use-case labels are the clearest summary of the choice. For Ch02: this comparison table is the canonical decision guide for the cache-memory vs repo-memory choice — include it or a summary as a reference artifact. The `scope: repo` option (Claim 8) provides an intermediate point on the spectrum.

## Concrete Artifacts

### Basic Configuration

```yaml
# Minimum configuration — stores at /tmp/gh-aw/cache-memory/
---
tools:
  cache-memory: true
---
```
*Source: gh-aw cache-memory reference, "Basic Configuration" section*

### Advanced Configuration Options

```yaml
---
tools:
  cache-memory:
    key: custom-memory-${{ github.repository_owner }}
    retention-days: 30  # 1-90 days, extends access beyond cache expiration
    allowed-extensions: [".json", ".txt", ".md"]  # Restrict file types
---
```
*Source: gh-aw cache-memory reference, "Advanced Configuration Options" section*

Note from source: "The compiler automatically appends `${{ github.run_id }}` to user-supplied keys and generates stable restore-keys from the prefix. Do not include the run ID manually."

### Multiple Cache Configurations

```yaml
---
tools:
  cache-memory:
    - id: default
      key: memory-default
    - id: session
      key: memory-session-${{ github.run_id }}
    - id: logs
      retention-days: 7
---
```
*Source: gh-aw cache-memory reference, "Multiple Cache Configurations" section.*
*Mounts: default at `/tmp/gh-aw/cache-memory/`, named caches at `/tmp/gh-aw/cache-memory-{id}/`.*

### Merging from Shared Workflows

```yaml
---
imports:
  - shared/mcp/server-memory.md
tools:
  cache-memory: true
---
```
*Source: gh-aw cache-memory reference, "Merging from Shared Workflows" section.*
*Merge rules: Single→Single (local overrides), Single→Multiple (local converts to array), Multiple→Multiple (merge by `id`, local wins).*

### Cache-Memory vs Repo-Memory Comparison

```
| Feature          | Cache Memory          | Repo Memory           |
|------------------|-----------------------|-----------------------|
| Storage Backend  | GitHub Actions Cache  | Git Branches          |
| Retention Period | 7 days                | Unlimited             |
| Size Limit       | 10GB/repo             | Repository limits     |
| Version Control  | No                    | Yes                   |
| Performance      | Fast                  | Slower                |
| Best Use Case    | Temporary/sessions    | Long-term/history     |
```
*Source: gh-aw cache-memory reference, "Comparison with Repo Memory" section*

### Integrity-Aware Cache Merge Semantics

```
Integrity level | Can read data from
----------------|-----------------------------------------
merged          | merged only
approved        | approved + merged
unapproved      | unapproved + approved + merged
none            | all levels (unapproved + approved + merged)
```
*Source: gh-aw cache-memory reference, "Integrity-Aware Caching" section.*
*Activated when `tools.github.min-integrity` is configured. Cache keys include the integrity level + a hash of the guard policy, forcing cache misses when any policy field changes.*

### Troubleshooting Reference

```
Issue                       | Resolution
----------------------------|-----------
Files not persisting        | Verify cache key consistency; check logs for restore/save messages
File access issues          | Create subdirectories first; verify permissions; use absolute paths
Cache size problems         | Track growth; clear periodically; use time-based keys for auto-expiration
Cache path misconfiguration | When agent calls missing_data with reason "cache_memory_miss,"
                            | the conclusion handler flags a likely cache path problem.
                            | Verify agent prompt references /tmp/gh-aw/cache-memory/ (default)
                            | or /tmp/gh-aw/cache-memory-{id}/ (named caches); ensure key consistency
```
*Source: gh-aw cache-memory reference, "Troubleshooting Guide" section*

### Threat-Detection-Aware Save Sequence

```
With threat detection enabled:
  restore → modify → upload artifact → validate → save

Normal (no threat detection):
  restore → modify → save
```
*Source: gh-aw cache-memory reference, "Security Considerations" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-audit-with-agents.md` Claim 5 ("`cache-memory` provides persistent state across agent runs for rolling trend analysis"): this reference page formally settles the underlying storage mechanism (GitHub Actions Cache, `/tmp/gh-aw/cache-memory/` path) that the audit guide described without specifying. The 30-day rolling baseline pattern described there now has an explicit hardware constraint context (7-day default, `retention-days` required for longer windows).
  - `docs-ghaw-dailyops.md` Claim 6 ("`cache-memory: true` enables persistent state at `/tmp/gh-aw/cache-memory/` across scheduled runs"): the reference page is the authoritative source for this claim; the DailyOps guide's description is accurate and consistent.
  - `docs-ghaw-expert-ops.md` Claim 6 ("`cache-memory: true` enables ExpertOps agents to accumulate domain observations across runs"): same as above — reference page confirms the configuration and path.
  - `docs-ghaw-ephemerals.md` Claim 6 ("Cache-memory cleanup groups cache entries by workflow prefix, keeps the latest run per prefix"): the reference page confirms this with the phrase "key prefix (everything before the run ID)"; consistent with the compiler appending `run_id` as the variable suffix.
  - `blog-ghaw-weekly-2026-03-30.md` Claim 1 ("Cache storage segmented into git branches enforces storage-level integrity isolation"): this reference page provides the formal specification for the feature that the weekly blog announced. The git-branch isolation approach and the four integrity tiers are consistent; this source adds the merge semantics and the migration warning.

- **Extends**:
  - `docs-ghaw-agentic-ops.md` Claim 7 (`repo-memory` vs `cache-memory` distinction): the reference page provides the formal comparison table with specific metrics (7-day vs. unlimited retention, 10GB vs. repository limits, fast vs. slower performance) that `docs-ghaw-agentic-ops.md` described qualitatively from usage patterns. Also adds `scope: repo` as an intermediate sharing option.
  - `blog-ghaw-weekly-2026-03-30.md` Claim 1 (integrity-aware cache-memory): the reference page adds two specifications not in the weekly blog: (a) ascending-trust read semantics (each level sees data from its level and all higher-trust levels, not just its own), (b) the migration warning that existing caches experience a cache miss on first upgrade.
  - `docs-ghaw-audit-with-agents.md` Claim 5 and `docs-ghaw-ephemerals.md` Claim 6 together: those notes establish what cache-memory does and how it's cleaned up; this reference page completes the picture with the full configuration API (retention-days, allowed-extensions, multi-cache, scope, import merge rules) and the constraint envelope (7-day default, 10GB, LRU).

- **Contradicts**: None identified. No existing source note makes claims that conflict with this reference page's specifications. The `retention-days` option (1-90 days) does not contradict the "7-day retention period" described in existing notes — they describe the default and the configurable extension respectively. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Compiler key management with "do not include run ID manually" warning** (Claim 2): The mechanism by which the compiler appends `run_id` and generates restore-keys is not described in any existing note. The practitioner warning is entirely new.
  - **`retention-days` option (1-90 days)** (Claim 3): No existing note documents that cache-memory retention can be extended beyond the 7-day GitHub Actions cache default.
  - **`allowed-extensions` security configuration** (Claim 4): Novel; no prior note documents file-type restriction for cache-memory writes.
  - **Multi-cache array configuration with `id:` fields** (Claim 5): Novel; prior notes show only single `cache-memory: true` or `cache-memory: key: <name>` configurations.
  - **Import merge rules** (Claim 6): Novel; merge semantics for cache-memory in shared workflow templates are not documented elsewhere.
  - **Hard storage constraints: 7-day, 10GB, LRU** (Claim 7): Prior notes assume the constraints but never state them formally. This is the first explicit specification.
  - **`scope: repo` for cross-workflow sharing** (Claim 8): Novel; provides an intermediate option between workflow-local `cache-memory` and cross-workflow `repo-memory`.
  - **`missing_data`/`cache_memory_miss` diagnostic signal** (Claim 10): Novel operational troubleshooting signal not described in any prior note.
  - **Integrity-aware ascending-trust read semantics and migration warning** (Claims 11, 12): The weekly blog announced the git-branch isolation feature; this reference adds the ascending-trust read model and the first-run cache-miss migration warning as formal specifications.
  - **Threat-detection save sequence** (Claim 13): Novel; the five-step restore→modify→upload artifact→validate→save sequence for threat-detected workflows is not in any existing note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - This source is the authoritative reference for the `cache-memory` configuration API. Ch02 should treat it as the definitive specification and cite it alongside the usage examples from `docs-ghaw-dailyops.md`, `docs-ghaw-expert-ops.md`, and `docs-ghaw-audit-with-agents.md`.
  - Add the `retention-days` option (Claim 3) as a required configuration for any workflow maintaining rolling state beyond 7 days. The omission of this option is a likely silent bug in existing workflows that assume 30-day rolling baselines survive across runs.
  - Add the `allowed-extensions` option (Claim 4) as a security best practice for cache-memory in workflows that process potentially sensitive file types.
  - Add the multi-cache configuration pattern (Claim 5) as the recommended design for workflows that need to maintain logically separate state stores.
  - Add the `cache-memory` vs `repo-memory` comparison table (Claim 14) as the canonical decision guide for choosing between the two persistence primitives.
  - Add the `scope: repo` option (Claim 8) as an intermediate sharing option for teams that need cross-workflow state without `repo-memory` infrastructure.
  - Add the compiler key management explanation (Claim 2) with the "do not include the run ID manually" warning to prevent misconfiguration.
  - Add the hard storage constraints (Claim 7: 7-day, 10GB, LRU) so harness engineers can plan storage budgets.

- **Chapter 03 (Safety and Verification)**:
  - Add the `allowed-extensions` security configuration (Claim 4) as a defense-in-depth layer for cache-memory alongside the "don't store sensitive data" best practice.
  - Add the integrity-aware caching specification (Claims 11–12) as the authoritative reference for integrity-tier isolation in agent state storage. Include the migration warning (Claim 12) in any `min-integrity` deployment guidance.
  - Add the threat-detection-aware save sequence (Claim 13) as a security mechanism for high-trust deployments where agents must not poison the cache.

- **Chapter 04 (Agent Coordination)**:
  - The `scope: repo` option (Claim 8) and the `cache-memory` vs `repo-memory` comparison (Claim 14) are the authoritative guide for coordination decisions around shared agent state. Current patterns (`docs-ghaw-agentic-ops.md` Claim 7) recommend `repo-memory` for cross-workflow sharing; Ch04 should note that `scope: repo` on `cache-memory` is a faster but less durable alternative without version control.

- **Chapter 07 (Cost Management)**:
  - Add the 10GB repository limit (Claim 7) and the cleanup mechanism (Claim 9) as required maintenance items for long-running agent deployments. Include the manual `clean_cache_memories` trigger path for on-demand cleanup.

## Extraction Notes

1. **WebFetch uses an AI model to process page content**: All quotes were extracted from the WebFetch-processed output. The tool converts HTML to markdown and uses an AI model for extraction. Quotes presented here appeared in the WebFetch output in the form shown; practitioners verifying specific wording should check the source URL directly.

2. **Reference page is the first formal API-level documentation for `cache-memory`**: Unlike the guides and patterns pages (which document usage examples), this reference page documents the full configuration schema. The "Behavior Specifications" section is particularly significant as the first place in the corpus to state the hard constraints (7-day, 10GB, LRU).

3. **`retention-days` implementation mechanism unclear**: The reference page says `retention-days: 30` "extends access beyond cache expiration" but the mechanism is not described. GitHub Actions caches have a 7-day default retention; whether `retention-days` uses a GitHub artifact alongside the cache (or a different mechanism) is not specified. The configuration option is documented as real, but how it achieves retention beyond 7 days at the infrastructure level is an open question.

4. **`scope: repo` configuration syntax not shown in code examples**: The reference mentions `scope: repo` as a feature in prose but provides no YAML example showing how to configure it. The syntax is inferred to be a field within the advanced `cache-memory` configuration block, but is not confirmed by a code snippet in the extracted content.

5. **No publication date**: The documentation page does not carry an explicit publication date. Content is consistent with gh-aw platform behavior as of the extraction date (May 2026).

6. **No contradictions filed**: Reviewed all existing source notes that reference `cache-memory` — `docs-ghaw-audit-with-agents.md`, `docs-ghaw-dailyops.md`, `docs-ghaw-expert-ops.md`, `docs-ghaw-ephemerals.md`, `docs-ghaw-agentic-ops.md`, `docs-ghaw-github-actions-primer.md`, `docs-ghaw-monitoring-patterns.md`, and `blog-ghaw-weekly-2026-03-30.md`. No claims in this source materially oppose existing source notes at the MINER.md §4a filing threshold.
