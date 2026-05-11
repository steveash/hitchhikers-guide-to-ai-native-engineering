---
source_url: https://github.github.com/gh-aw/reference/threat-detection
source_type: docs
title: "GitHub Agentic Workflows: Threat Detection Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#414"
---

# GitHub Agentic Workflows: Threat Detection Reference

> The authoritative configuration reference for gh-aw's threat detection mechanism —
> documents the two-layer security model (AI-powered analysis + static protected-files)
> that runs as a separate pipeline stage between the agentic job and safe output execution,
> the three threat categories analyzed by default, the structured JSON output schema, the
> six-field advanced configuration object, and the three protection policies for supply
> chain files including the non-blocking `fallback-to-issue` option.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/threat-detection` page —
  in the "Reference" section, alongside the permissions, safe-outputs-specification, and
  concurrency reference pages. Reference pages document platform configuration
  authoritatively.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI. Configuration
  field names, threat category definitions, JSON output schema, and policy options are
  settled platform facts. The fail-secure error handling behavior and protected-files
  category list are architectural decisions from the platform team, not third-party
  measurement.
- **Scope**: The complete threat detection mechanism for gh-aw workflows — the pipeline
  position (separate job between agentic job and safe output jobs), the three default
  threat categories, the AI detection output schema, the boolean and object configuration
  forms, the custom steps interface, the engine configuration options, and the static
  protected-files layer with its three policies. Does NOT cover: the full Safe Outputs
  MCP Gateway specification (see `docs-ghaw-safe-outputs-specification.md`), the seven-stage
  validation pipeline inside the Safe Output Processor (same note), or the permissions
  model that governs the agentic job itself (see `docs-ghaw-permissions-reference.md`).

## Extracted Claims

### Claim 1: Threat detection runs as a dedicated job between the agentic job and the safe output jobs, forming a three-stage pipeline where safe outputs are only applied after passing the detection gate

- **Evidence**: Architectural description from the reference page, consistent across
  multiple fetch passes. The description explicitly frames threat detection as "an
  additional security layer" that runs "before they [safe outputs] are applied."
- **Confidence**: emerging (first-party documentation; pipeline position is described
  clearly but the specific job sequencing mechanism is not shown in workflow YAML)
- **Quote**: "GitHub Agentic Workflows includes automatic threat detection to analyze
  agent output and code changes for potential security issues before they are applied."
- **Our assessment**: This pipeline position is architecturally significant. Threat
  detection is not part of the seven-stage validation pipeline inside the Safe Output
  Processor (documented in `docs-ghaw-safe-outputs-specification.md` Claim 12) — it is
  a separate job that runs before the Safe Output Processor even starts. The safe output
  processor's validation pipeline (schema → limits → sanitization → ...) is therefore a
  second, independent security gate after threat detection has already cleared the output.
  The two mechanisms are complementary: threat detection is AI-powered output analysis
  before processing; the validation pipeline is rule-based schema enforcement during
  processing. For Ch02 (Harness Engineering): document the three-stage pipeline as
  the complete architecture: (1) agentic job with read-only permissions, (2) threat
  detection job, (3) safe output processor jobs. Practitioners who only know about the
  safe-outputs validation pipeline are missing the pre-processor detection layer.

### Claim 2: Three threat categories are analyzed by default: prompt injection (malicious instructions manipulating AI behavior), secret leaks (exposed credentials), and malicious patches (code changes introducing vulnerabilities)

- **Evidence**: Opening description from the reference page, consistent across all three
  fetch passes. The three categories are the default scope of the AI detection engine.
- **Confidence**: settled (first-party documentation; the three categories are explicitly
  enumerated and named)
- **Quote**: (no direct quote; the three categories are listed as bullet items without
  introductory prose — see Concrete Artifacts for the exact names and descriptions)
- **Our assessment**: The three categories address distinct threat models. Prompt injection
  targets the AI reasoning layer (an attacker manipulates the agent's instructions to
  produce malicious output). Secret leaks address the output content layer (credentials
  reaching GitHub state via agent-generated content). Malicious patches target the code
  modification layer (agent-generated code changes introducing vulnerabilities). Together
  they cover the three surfaces where an AI agent operating on code can be exploited.
  For Ch03 (Safety and Verification): these three categories should be named explicitly
  as the default threat surface that threat detection covers. Practitioners with specialized
  threat models can extend or replace them via custom `steps`, `post-steps`, and `prompt`
  configuration (Claims 6–8).

### Claim 3: The AI detection engine produces structured JSON with boolean fields per threat category plus a reasons array; any field set to `true` causes workflow failure and blocks safe outputs

- **Evidence**: JSON schema reproduced from the reference page, consistent across multiple
  fetch passes. The `reasons` array provides justification when a threat is detected.
  The blocking behavior on any `true` value is explicitly stated.
- **Confidence**: settled (first-party documentation; the JSON schema and blocking
  behavior are explicitly defined)
- **Quote**: "If any threat is detected (true), the workflow fails and safe outputs are
  blocked."
- **Our assessment**: The structured JSON output is architecturally important for two
  reasons. First, the `reasons` array provides human-readable justification, enabling
  operators to distinguish true positives from false positives. Second, the boolean
  field structure makes the detection result machine-readable — custom `post-steps` can
  inspect the output and take automated action based on which specific threat category
  was flagged (rather than treating any detection as undifferentiated failure). The
  all-or-nothing blocking behavior on any `true` value implements the same fail-secure
  principle (P4) from `docs-ghaw-safe-outputs-specification.md` Claim 4 — detection
  always errs toward rejection. For Ch03: document the JSON schema as the output
  contract for threat detection; this enables custom post-steps to implement detection
  response logic rather than just logging results.

### Claim 4: Simple boolean control (`threat-detection: true/false`) enables or disables the entire threat detection job; the default is `true` (enabled) whenever safe outputs are configured

- **Evidence**: Boolean syntax described and shown in the reference page, consistent
  across fetch passes. The default-enabled behavior when safe outputs exist is stated
  explicitly.
- **Confidence**: settled (first-party documentation; the default behavior and boolean
  syntax are explicitly specified)
- **Quote**: "Threat detection is automatically enabled when safe outputs are configured"
- **Our assessment**: The default-enabled behavior means any workflow using safe outputs
  automatically gets threat detection without any additional configuration — the security
  layer is opt-out, not opt-in. This is the correct design for a safety mechanism: the
  safe default is the secure default. `threat-detection: false` disables the entire
  detection job, which is why the `copilot-token-optimizer` workflow uses this flag
  (see `docs-ghaw-agentic-ops.md` Extraction Notes point 5 — that note speculated the
  optimizer disables detection to avoid false positives when reading workflow source
  files). This source confirms the semantics: `threat-detection: false` bypasses the
  detection job entirely and is a deliberate opt-out of the security layer. For Ch02:
  warn practitioners that using `threat-detection: false` removes the pre-processor
  security gate and should be reserved for cases with clear justification (e.g.,
  workflows that read and analyze workflow files as data, which can trigger false
  positives in AI detection).

### Claim 5: Advanced object configuration supports six fields — `enabled`, `prompt`, `engine`, `runs-on`, `steps`, `post-steps` — enabling fine-grained control over the detection job

- **Evidence**: Configuration field table from the reference page, consistent across
  multiple fetch passes with matching field names, types, and descriptions.
- **Confidence**: settled (first-party documentation; the six-field schema is explicitly
  enumerated in a table)
- **Quote**: (no direct quote; the fields appear in a table without introductory prose
  to quote — see Concrete Artifacts for the exact table)
- **Our assessment**: The object form enables composition: practitioners can keep AI
  detection (`engine: <model>`) while adding custom tool-based steps (`steps`,
  `post-steps`) and can specify runner requirements (`runs-on`) for the detection job
  independent of the main agentic job. The `enabled` field provides a boolean gate
  within the object form (equivalent to the top-level boolean but composable with the
  other fields). This layered configuration model follows the same two-level hierarchy
  documented in `docs-ghaw-safe-outputs-specification.md` Claim 10 (global vs. type-
  specific parameters) — a consistent configuration design across the gh-aw platform.
  For Ch02: document the object form as the path to customization when boolean control
  is insufficient. The six fields cover the full detection job lifecycle.

### Claim 6: The `prompt` field appends custom instructions to the default detection prompt, enabling domain-specific threat analysis without replacing the default categories

- **Evidence**: Field description from the configuration table (type: string,
  "Custom instructions appended to default detection prompt"). The append-not-replace
  behavior means custom instructions extend the default scope.
- **Confidence**: emerging (field type and description are from the config table; the
  exact append semantics and how the custom prompt interacts with the default categories
  are not elaborated in the fetched content)
- **Quote**: (no direct quote; see Concrete Artifacts for the configuration table)
- **Our assessment**: The `prompt` field is the lowest-friction path to domain-specific
  threat analysis. A team with domain-specific concerns (e.g., detecting disclosure of
  internal API patterns, or checking that agent-generated code doesn't introduce
  protocol violations) can extend the default detection by appending their criteria
  rather than replacing the platform's default three-category analysis. The word
  "appended" suggests the default prompt (which defines prompt injection, secret leak,
  and malicious patch detection) runs first, and the custom prompt adds criteria to the
  same AI reasoning pass. For Ch03 (Safety and Verification): the `prompt` field is
  the recommended starting point for domain-specific threat modeling — it preserves
  platform defaults while adding context-specific concerns.

### Claim 7: Custom `steps` (pre-analysis) and `post-steps` (post-analysis) allow integration of specialized security tools alongside AI detection, with access to workflow prompt text, safe output items, and git patch files as shared artifacts

- **Evidence**: Fields described in the configuration table; the available artifacts
  (workflow prompt text, safe output items as JSON, git patch files) are described in
  the custom detection methods section of the reference page.
- **Confidence**: emerging (field availability is settled; the artifact format and
  exact file paths are described but not shown as working examples)
- **Quote**: (no direct quote; see Concrete Artifacts for artifact list)
- **Our assessment**: The artifact access model is architecturally well-designed. The
  three artifact types cover the three surfaces where threats can appear: the prompt
  (what instructions were given to the agent), the safe outputs (what actions the agent
  intends to take), and the git patch (what code changes the agent generated). A custom
  security scanner in `steps` can inspect all three before AI analysis runs; a custom
  post-processor in `post-steps` can inspect the AI's detection result and take
  additional action (e.g., filing a security issue, sending an alert). This is the
  "threat detection extensibility" capability shipped in v0.66.0 (see
  `blog-ghaw-weekly-2026-04-06.md` Concrete Artifacts → version summary). For Ch02:
  document the three artifact types as the detection data model — practitioners designing
  custom security tools for gh-aw can write scanners that consume these artifact files
  without needing to re-fetch data from the GitHub API.

### Claim 8: The `engine` field accepts a string (AI model name), an object (AI model configuration), or `false` (disable AI analysis entirely, enabling pure-tool-based detection)

- **Evidence**: Field type specification from the configuration table ("string/object/false —
  AI engine config or false for no AI"), consistent across fetch passes.
- **Confidence**: emerging (type signature is settled from the table; the specific model
  names accepted as strings and the object configuration schema are not elaborated in
  fetched content)
- **Quote**: (no direct quote; see Concrete Artifacts for configuration table)
- **Our assessment**: `engine: false` is the most significant option — it disables AI
  analysis entirely while keeping the threat detection job active with only custom
  `steps` and `post-steps`. This enables a detection mode where compliance and security
  tools run without AI reasoning: a SAST scanner, a secret-detection tool (e.g., Gitleaks,
  TruffleHog), or a policy-enforcement script can run in `steps` and fail the detection
  job based on their own exit codes, without any AI involvement. For Ch03: document
  `engine: false` as the pattern for rule-based threat detection that does not depend on
  AI judgment — useful when determinism is required for compliance auditing.

### Claim 9: A static protected-files layer operates independently of AI detection, applying rule-based protection to supply chain files based on glob patterns and policy declarations

- **Evidence**: The protected files section is described as a "complementary static layer"
  that protects critical files. The layer is rule-based (not AI), using file path matching
  to enforce protection policies independent of the AI engine result.
- **Confidence**: settled (first-party documentation; the layer is explicitly named as
  complementary and static)
- **Quote**: (no direct quote; the section is described without a single quotable sentence —
  see Concrete Artifacts for the file categories and policy options)
- **Our assessment**: The static protected-files layer is architecturally complementary to
  AI detection in exactly the right way: AI detection catches semantic threats (injection,
  secrets, malicious logic), while static file protection catches structural threats
  (unauthorized modification of supply chain files). A prompt injection attack might evade
  semantic analysis if the AI is itself manipulated; protecting supply chain files statically
  prevents the attack vector from being exploited regardless of AI correctness. The two
  layers implement defense-in-depth. For Ch03: document the two-layer threat detection
  model — AI semantic analysis (Claims 2–8) + static supply chain file protection (Claims
  9–11) — as the complete threat detection architecture.

### Claim 10: Three supply chain file categories receive static protection by default: dependency manifests (package.json, requirements.txt, etc.), CI/CD workflow files (.github/workflows/), and agent instruction files (AGENTS.md, CLAUDE.md, .claude/, .agents/)

- **Evidence**: Category enumeration from the protected files section, consistent across
  fetch passes. The three categories are named with specific file examples.
- **Confidence**: settled (first-party documentation; the categories and examples are
  explicitly enumerated)
- **Quote**: (no direct quote; the categories are listed as bullet items — see Concrete
  Artifacts)
- **Our assessment**: The agent instruction files category is the most strategically
  significant. Protecting AGENTS.md, CLAUDE.md, .claude/, and .agents/ against
  agent-generated modification prevents a class of supply chain attacks where a
  compromised agent modifies its own instruction files — in effect self-modifying its
  behavior for future runs. This is a concrete defense against the "instruction injection"
  attack class: an attacker who can't directly inject instructions into the current run
  might try to modify instruction files to affect future runs. By making agent instruction
  files a protected supply chain category, gh-aw closes this attack vector by default.
  The `blog-ghaw-weekly-2026-03-23.md` Claim 2 (Trivy supply chain compromise → immediate
  removal) illustrates the real-world stakes of CI/CD supply chain integrity; this feature
  is the proactive defense against the same threat class. For Ch03: name agent instruction
  file protection as a defense against persistent instruction injection across workflow runs.

### Claim 11: Three protection policy options define the response to a protected file change: `blocked` (default, hard error), `allowed` (unrestricted), and `fallback-to-issue` (human review via issue creation)

- **Evidence**: Protection policy table from the reference page, consistent across fetch
  passes. The `blocked` policy is explicitly marked as default.
- **Confidence**: settled (first-party documentation; the three policy values and their
  behaviors are explicitly tabulated)
- **Quote**: (no direct quote; the policies appear in a table — see Concrete Artifacts for
  the exact table)
- **Our assessment**: `fallback-to-issue` is the most architecturally novel policy. It
  converts a hard-block into a human review workflow: instead of failing the safe output
  job with an error, the system creates a review issue (presumably via the `create-issue`
  safe output type) that a human must resolve before the change can proceed. This is the
  same "escalation as an alternative to blocking" pattern seen in the two-level escalation
  model in `docs-ghaw-agentic-ops.md` Claim 4 (routine information → Discussion; threshold-
  crossing → Issue). `fallback-to-issue` applies the same pattern to supply chain file
  changes: agent-generated changes to protected files are treated as requiring human sign-off
  rather than being automatically rejected. For Ch03: document `fallback-to-issue` as the
  recommended policy for teams that want human oversight of supply chain file changes without
  completely blocking agent workflows that legitimately need to touch dependency files
  (e.g., dependency update agents). The `blocked` default is appropriate for most cases,
  but `fallback-to-issue` supports a compliance approval gate pattern.

### Claim 12: Detection process failures are fail-secure — if the threat detection job itself fails (network issues, tool errors), the workflow stops and safe outputs are not applied

- **Evidence**: Error handling section of the reference page, confirmed across multiple
  fetch passes. The failure mode explicitly stops the workflow rather than degrading
  to allowing safe outputs through.
- **Confidence**: settled (first-party documentation; the fail-secure behavior is explicitly
  stated as the error handling policy)
- **Quote**: "If the detection process itself fails (e.g., network issues, tool errors),
  the workflow stops and safe outputs are not applied."
- **Our assessment**: This fail-secure behavior is the correct safety design for a security
  gate. The alternative (fail-open: if detection fails, allow safe outputs to proceed) would
  make threat detection bypassable via infrastructure attacks — deliberately causing network
  failures or tool errors to skip the security check. The fail-secure choice aligns with
  Principle P4 from `docs-ghaw-safe-outputs-specification.md` Claim 4: "Invalid inputs,
  constraint violations, or execution errors result in operation rejection, not degraded
  execution." Threat detection implements P4 at the job level: a failed security check is
  treated as a failed detection, not as a cleared detection. This is also directly relevant
  to `blog-ghaw-weekly-2026-04-27.md` Claim 7: the missing Node.js setup in threat-detection
  workflows caused "node: command not found" failures; under this fail-secure policy, those
  failures would have caused safe outputs to be blocked, which is the correct behavior (and
  why the bug was noticed and fixed). For Ch03: document fail-secure error handling as a
  required property of any security gate in an agentic pipeline — a gate that silently
  passes on failure provides no safety guarantee.

## Concrete Artifacts

### Three Default Threat Categories (from reference page)

```
1. Prompt injection — malicious instructions manipulating AI behavior
2. Secret leaks    — exposed credentials or API keys in agent output
3. Malicious patches — code changes introducing vulnerabilities
```

### AI Detection Engine Output Schema (from reference page)

```json
{
  "prompt_injection": false,
  "secret_leak": false,
  "malicious_patch": false,
  "reasons": []
}
```

*Behavior: any field set to `true` causes workflow failure and blocks safe outputs.*

### Boolean Configuration Syntax

```yaml
# Enable threat detection (default when safe-outputs exist):
threat-detection: true

# Disable threat detection entirely:
threat-detection: false
```

### Advanced Object Configuration Fields (from reference page table)

```
Field       Type              Description
---------   ----------------  -----------------------------------------------
enabled     boolean           Enable/disable detection (default: true when safe-outputs exist)
prompt      string            Custom instructions appended to default detection prompt
engine      string/object/    AI engine config (model name or config object),
            false             or false to disable AI entirely and use only custom steps
runs-on     string/array/     Runner configuration for the detection job
            object
steps       array             Steps run BEFORE AI analysis (pre-analysis hooks)
post-steps  array             Steps run AFTER AI analysis (post-analysis hooks)
```

### Artifacts Available to Custom Steps (from reference page)

```
Artifact                Description
-------------------     -----------------------------------------------
Workflow prompt text    The full prompt/instructions provided to the agent
Safe output items       Agent-declared safe output operations as JSON
Git patch files         Code changes generated by the agent as diff/patch
```

*Custom `steps` (pre-analysis) and `post-steps` (post-analysis) both receive access to these artifacts.*

### Protected File Categories and Policies (from reference page)

```
PROTECTED FILE CATEGORIES:
  Dependency manifests  — package.json, requirements.txt, and similar
  CI/CD workflows       — .github/workflows/
  Agent instruction     — AGENTS.md, CLAUDE.md, .claude/, .agents/
  files

PROTECTION POLICIES:
  Policy             Behavior
  ---------------    -----------------------------------------------
  blocked            Hard-block: safe output fails with error (DEFAULT)
  allowed            No restriction; changes to this file are permitted
  fallback-to-issue  Create review issue instead of blocking; requires human review
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-safe-outputs-specification.md` Claim 4 (Principle P4: Fail-Secure By
    Default — "Invalid inputs, constraint violations, or execution errors result in
    operation rejection, not degraded execution"): Claim 12 here is P4 applied at the
    threat detection job level. Detection failures stop the pipeline; they do not degrade
    to clearance. The two sources document the same fail-secure principle at different
    architectural layers (the Safe Output Processor's validation pipeline vs. the threat
    detection job before it).
  - `blog-ghaw-weekly-2026-04-06.md` Concrete Artifacts → version summary (v0.66.0
    entry: "Workflow reliability and threat detection extensibility"): The custom `steps`
    and `post-steps` configuration (Claim 7) is the capability shipped as "threat detection
    extensibility" in v0.66.0. The blog post named the capability without documenting it;
    this reference page provides the full specification.
  - `blog-ghaw-weekly-2026-04-27.md` Claim 7 (Node.js absent from threat-detection
    workflows causing "node: command not found" failures): That claim documents a runtime
    failure in threat detection that blocked the detection job from executing. Under the
    fail-secure policy (Claim 12), that failure would have stopped safe outputs — which
    is why the bug was noticed and fixed. The two claims together illustrate the operational
    consequence of the fail-secure design: detection infrastructure failures are visible and
    blocking, not silent and passing.
  - `blog-ghaw-weekly-2026-04-27.md` Claim 5 (protected-files compilation now accepts both
    string shorthand and `{policy, exclude}` object form): The object form with `policy`
    and `exclude` fields mentioned in that claim corresponds to the advanced protected-file
    configuration of the `blocked`/`allowed`/`fallback-to-issue` policies (Claim 11). The
    two notes together document both the policy options (this note) and the compilation fix
    that makes the object syntax usable (April 27 note).
  - `blog-ghaw-weekly-2026-03-23.md` Claim 2 (Trivy scanner supply chain compromise →
    immediate removal response): The protected-files layer (Claims 9–11) is the proactive
    defense for the threat class that Claim 2 illustrates. That incident required human
    detection and manual removal; the protected-files layer would prevent agent-generated
    modifications to CI/CD workflow files and dependency manifests from reaching GitHub
    state without policy-gated review.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md` (Safe Outputs MCP Gateway Specification):
    That note documents the seven-stage validation pipeline inside the Safe Output Processor
    (Claim 12) and four foundational security principles (Claim 4). This note extends the
    picture by adding the pre-processor threat detection stage — a separate job that runs
    before the Safe Output Processor even begins. The complete gh-aw safety architecture
    is: agentic job (read-only) → threat detection job (AI + static) → safe output
    processor (seven-stage validation pipeline). `docs-ghaw-safe-outputs-specification.md`
    documents stages 2–3 of this pipeline; this note documents stage 2 in full.
  - `docs-ghaw-agentic-ops.md` (Extraction Notes point 5 and Guide Impact Ch03 bullet):
    That note observed `threat-detection: false` in the `copilot-token-optimizer.md`
    frontmatter and inferred its semantics, noting that "the platform documentation for
    this flag was not found in existing corpus source notes." This note is that platform
    documentation. The boolean control semantics (Claim 4) confirm the inferred behavior:
    `threat-detection: false` disables the detection job entirely, which the optimizer
    uses to avoid false positives when analyzing workflow source files that may contain
    code patterns resembling injection payloads.
  - `docs-ghaw-permissions-reference.md` Claim 2 (four security rationales: audit trail,
    blast radius, compliance gates, prompt injection defense): The "prompt injection defense"
    rationale listed there is implemented at the architecture level by the threat detection
    layer documented here. The permissions reference states the principle; this note
    documents the implementation — a dedicated detection job that uses AI analysis to
    detect prompt injection in agent output before safe outputs are applied.

- **Contradicts**: None identified. No existing source note makes claims that conflict
  with the fail-secure error handling, the three default threat categories, the two-layer
  detection architecture, or the protected-files policy options. No contradiction issue
  filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Threat detection as a separate pipeline stage** (Claim 1): No prior corpus note
    documents that threat detection runs as a dedicated job between the agentic job and
    the safe output jobs. Prior notes describe the safe-outputs architecture and the
    seven-stage validation pipeline without mentioning this intermediate stage.
  - **AI detection JSON output schema** (Claim 3): The structured JSON schema
    (`prompt_injection`, `secret_leak`, `malicious_patch`, `reasons`) is not described
    in any existing source note. This is the output contract for the threat detection
    engine.
  - **Six-field advanced object configuration** (Claim 5): The `enabled`, `prompt`,
    `engine`, `runs-on`, `steps`, `post-steps` field set is not documented in any
    existing source note. Prior notes only knew about the boolean `threat-detection: false`
    form from the optimizer workflow.
  - **`engine: false` for pure-tool-based detection** (Claim 8): The ability to disable
    AI analysis entirely while keeping the detection job active (using only custom steps)
    is not described in any prior note.
  - **Static protected-files layer** (Claims 9–11): The existence of a static, rule-based
    layer that protects supply chain files independently of AI detection is not documented
    in any existing source note. The layer's coverage of agent instruction files (AGENTS.md,
    CLAUDE.md, .claude/, .agents/) is particularly novel — no prior note identifies agent
    instruction files as a protected supply chain category.
  - **`fallback-to-issue` policy** (Claim 11): The non-blocking policy that converts a
    supply chain file change into a human review issue rather than a hard error is not
    described in any prior note. This is the most operationally flexible protection option.
  - **Semantic explanation of `threat-detection: false`** (Claim 4): While the flag
    appeared in `docs-ghaw-agentic-ops.md`, its semantics were inferred. This note
    provides the authoritative explanation.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - **Add the three-stage pipeline architecture**: Document the complete gh-aw execution
    pipeline as: (1) agentic job with read-only permissions → (2) threat detection job →
    (3) safe output processor job. Current guide coverage of the safe-outputs architecture
    lacks this middle stage. Practitioners need to understand that there are two independent
    security gates: the threat detection job (AI + static) and the safe output processor
    (seven-stage validation). Both must pass before GitHub state is modified.
  - **Document the six-field threat detection object configuration**: Add `threat-detection:`
    as a first-class frontmatter configuration block alongside `safe-outputs:` and
    `permissions:`. The six fields (`enabled`, `prompt`, `engine`, `runs-on`, `steps`,
    `post-steps`) enable the full customization surface for security practitioners.
  - **Warn about `threat-detection: false`**: When practitioners disable threat detection,
    they remove the pre-processor security gate entirely. This should be documented as a
    deliberate opt-out that removes a safety layer, not a performance optimization.

- **Chapter 03 (Safety and Verification)**:
  - **Name the three default threat categories and the JSON output schema**: Chapter 03
    coverage of prompt injection defense should now specify that gh-aw detects three
    categories by default and produces structured JSON output. This enables practitioners
    to reason about what threat detection covers and what it doesn't (e.g., logical errors
    in agent reasoning are not a threat detection concern; those are handled by staged mode
    and human review).
  - **Add the two-layer threat detection model**: AI semantic analysis + static supply chain
    file protection should be documented as complementary layers covering different attack
    surfaces. The static layer operates independently of AI correctness.
  - **Document agent instruction file protection as a defense against persistent injection**:
    The protection of AGENTS.md, CLAUDE.md, .claude/, .agents/ closes the attack vector
    where a compromised agent modifies its own instructions for future runs. This is a
    concrete, platform-provided defense that practitioners should know is active by default.
  - **Add `fallback-to-issue` as the human-review policy for compliance gates**: When
    organizations require human sign-off for supply chain file changes, `fallback-to-issue`
    implements that gate without blocking legitimate workflows entirely. This connects to
    the compliance approval gate rationale in `docs-ghaw-permissions-reference.md` Claim 2.
  - **Establish fail-secure detection failure handling as a required property**: Any security
    gate that silently passes on failure provides no safety guarantee. Document this principle
    using the threat detection error handling as the reference implementation.

## Extraction Notes

1. **WebFetch processes pages via AI model**: The source URL points to an Astro/Starlight
   SPA. Three separate fetch passes were used with different prompt strategies to maximize
   content coverage. Quotes marked with verbatim status are consistent across at least two
   passes; where passes returned different phrasing for the same section, quotes are marked
   `(no direct quote; see paraphrase in Our assessment)`. The JSON schema, configuration
   field table, and protected-files policy table were highly consistent across passes and
   are extracted as code blocks with high confidence.

2. **No sub-pages followed**: The reference page links to individual protected-file type
   documentation and to the broader safe-outputs reference. These were not followed — the
   focus was on the threat detection mechanism itself. A separate source note for protected-
   files advanced configuration may be warranted if the object form (`{policy, exclude}`)
   has additional undocumented fields.

3. **`threat-detection: false` in agentic-ops note now explained**: The `docs-ghaw-agentic-ops.md`
   Extraction Notes point 5 speculated about the semantics of `threat-detection: false`.
   This source confirms: it disables the detection job entirely. The optimizer's use of this
   flag is now explained by its need to read workflow source files without triggering false
   positives in AI detection.

4. **No publication date**: The documentation page does not carry an explicit publication date.
   `date_published` is left null. Content is consistent with the current gh-aw platform
   as of 2026-05-11.

5. **No contradictions filed**: Reviewed all existing gh-aw source notes. No claims in this
   source materially oppose any existing note. The threat detection mechanism adds a pipeline
   stage not previously documented; it does not contradict any existing description of the
   safe-outputs architecture. No contradiction issue required.
