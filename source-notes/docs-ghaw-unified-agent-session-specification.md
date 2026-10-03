---
source_url: https://github.github.com/gh-aw/specs/unified-agent-session-specification
source_type: docs
title: "GitHub Agentic Workflows: Unified Agent Session Specification (v1.2.0, Draft)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: 2026-10-02
date_extracted: 2026-10-03
last_checked: 2026-10-03
status: current
confidence_overall: emerging
issue: "#3881"
---

# GitHub Agentic Workflows: Unified Agent Session Specification (v1.2.0, Draft)

> A W3C-style draft spec defining a loss-preserving, engine-neutral session trace (ordered `type`/`data` events) for six agent engines, plus a conclusion-job merger that folds agent, MCP gateway, firewall, safe-output, grader and eval evidence into one provenance-tagged `aw_session.jsonl` — the most detailed "what must a trustworthy agent trace preserve" contract in the corpus.

## Source Context

- **Type**: docs (formal specification in the `specs/` section, RFC 2119 MUST/SHOULD language, requirement IDs T-UAS-001 to T-UAS-066, explicitly "Draft").
- **Author credibility**: First-party (GitHub Next / Microsoft Research, same team as gh-aw). The spec states it is "not an official W3C standard", and that its test suites are "not a blanket declaration of conformance". Claims about how gh-aw's own parsers behave are authoritative; claims about generality across the industry are not.
- **Scope**: Trace model, seven core event types, parsing/normalization rules, token accounting, per-engine mappings (Claude, Copilot, Codex, Gemini, Pi, custom), renderer/bootstrap behavior, the unified conclusion artifact, compliance test matrices, CI fixture provenance, security considerations. Does NOT cover engine execution, frontmatter, model behavior, transport protocols, or cross-language storage APIs (§1.1). Note: the page header says Version 1.2.0 but the Change Log's newest entry is 1.1.0 — the 1.2.0 delta is not documented on the page.

## Extracted Claims

### Claim 1: A single engine-neutral trace — an ordered array of `{type, data}` events — is the canonical session model, with no session wrapper and no per-event spec version
- **Evidence**: T-UAS-003 and the data-flow diagram in §1.2; the Abstract names six engines (Claude, Copilot, Codex, Gemini, Pi, custom) mapped onto the Copilot-compatible event shape; Appendix A gives a complete example.
- **Confidence**: emerging (first-party draft with accompanying implementation and tests; no external adoption evidence)
- **Quote**: "A normalizer MUST NOT introduce a top-level session wrapper or add a specification version property to event records."
- **Our assessment**: A practical answer to "how do we compare Claude Code and Codex transcripts?": adopt one event vocabulary (`session.init`, `user.message`, `assistant.message`, `assistant.reasoning`, `tool.execution_start`, `tool.execution_complete`, `session.result`) and map each engine onto it. The choice of the Copilot event shape as the canonical form is pragmatic rather than neutral.

### Claim 2: Absence is not zero — normalizers must never fabricate IDs, timestamps, costs, token counts, or outcomes
- **Evidence**: T-UAS-005, T-UAS-034, T-UAS-047; the §10 gap matrix lists the pre-spec bugs this rule fixes (renderer-derived turns, defaulted zero duration in Pi, synthetic debug tool successes, random/time-based IDs).
- **Confidence**: settled (the principle is straightforward; the gap matrix shows it was derived from real defects)
- **Quote**: "It MUST NOT fabricate source identifiers, timestamps, model names, tool outcomes, duration, cost, token counts, or turn counts to fill missing fields."
- **Our assessment**: Strong, directly reusable observability principle: "unknown" and "0" are different values. Particularly relevant for cost dashboards, where defaulting missing cost to 0 silently under-reports spend. Gemini example: `stats.tool_calls` must not be used as `numTurns`.

### Claim 3: Dangling tool calls and orphan completions must be preserved as such; a start alone is never success
- **Evidence**: T-UAS-014, T-UAS-023, T-UAS-024, T-UAS-044; the spec also requires exact-ID pairing before any fallback and forbids pairing ambiguous concurrent same-name calls. §10 records that pre-spec formatters "count missing results as success".
- **Confidence**: settled
- **Quote**: "A dangling call or ambiguous completion MUST NOT receive a success checkmark or count toward successful-tool statistics."
- **Our assessment**: Directly useful for anyone writing log viewers or agent-run dashboards: three-state tool outcome (success / failure / unknown-pending), not two. Also relevant to crashed or timed-out runs where the last tool never returned.

### Claim 4: Accounting is evidence of activity, not of success — turns/tokens/result presence must not be read as task completion
- **Evidence**: T-UAS-048; §9.4 notes the failed Smoke Copilot workflow "failed in downstream safe outputs, not in its recorded agent session"; Codex `turn.completed` does not imply task completion (§4.6 `status` row).
- **Confidence**: settled
- **Quote**: "A failed workflow does not by itself establish a failed agent session (T-UAS-048)."
- **Our assessment**: Counters a common shortcut (treat "agent ran N turns" or "job red/green" as outcome). Pairs with outcome-level measurement (acceptance/waste rate) rather than session-level proxies.

### Claim 5: Token accounting must distinguish per-turn contributions from cumulative snapshots by source schema, never by a "largest wins" heuristic, and must not double-count cache tokens
- **Evidence**: T-UAS-031, T-UAS-032, T-UAS-033, Appendix C worked examples (two Codex turns sum to 30/8/cache-read 6; a terminal snapshot with the same totals is not added again; `{input_tokens: 0, inputTokens: 99}` reads as 0). Gemini stats are cumulative snapshots with `cached` included in `input_tokens` (recorded as `usage.input_tokens_include_cache: true`); Codex/Pi are per-turn. Overflow above `Number.MAX_SAFE_INTEGER` is rejected and recorded in `usage.overflowed_tokens`.
- **Confidence**: emerging (concrete and tested against sampled CI runs, but engine formats change)
- **Quote**: "An adapter MUST distinguish per-turn contributions from cumulative or terminal snapshots using the supported source schema, not a heuristic such as “largest number wins.”"
- **Our assessment**: Valuable concrete warning for cost tooling: the same field name (usage) means different things across engines. Corroborates the Effective Tokens spec's concern that raw token counts are not comparable, from the parsing side rather than the weighting side.

### Claim 6: The conclusion job merges all evidence into one compact, timestamp-ordered `aw_session.jsonl` with a leading format-version header and per-event provenance
- **Evidence**: T-UAS-054, T-UAS-055, T-UAS-056, T-UAS-057, T-UAS-064. Header line is `{"type":"session.format","data":{"version":1},"provenance":{...}}`; every event carries `component`, `phase`, `path`, `index`; timed events sort by `provenance.timestampMs` using the source schema's units (Squid audit = Unix seconds; native agent and token-tracker = milliseconds); untimed events go after all timed events; no substituting file mtime or neighbour time.
- **Confidence**: emerging
- **Quote**: "Wall-clock ordering does not establish causality or correct cross-process clock skew."
- **Our assessment**: A concrete design for multi-component run forensics (agent + MCP gateway + network firewall + safe outputs in one timeline). The honest caveat about clock skew and the "untimed tail" rule are notable; most ad hoc timeline merges silently invent ordering. Version header + "report missing/unsupported version" is a good pattern for any log artifact meant to outlive its producer.

### Claim 7: Merging must not sum overlapping observations and must scope tool pairing and accounting by source
- **Evidence**: T-UAS-058 (persisted canonical agent stream takes precedence over raw logs; don't count equivalent representations twice), T-UAS-062, T-UAS-066 (coincident tool IDs in different source files must not pair across sources; gateway/firewall/grader/eval observations must not be added to agent usage).
- **Confidence**: emerging
- **Quote**: "A merger MUST NOT sum overlapping agent, firewall, or accounting observations to produce another session total."
- **Our assessment**: Good guard against double-billing in multi-layer telemetry (e.g., the agent's own token report and a proxy's token tracker both describe the same API calls). Native IDs are never made global (T-UAS-055), which is a trade-off: simpler provenance, but consumers must always key by (path, ID).

### Claim 8: Full-fidelity internal traces are separated from a redacting, bounded publication layer; user prompts are retained but never shown in default summaries
- **Evidence**: T-UAS-045, T-UAS-049, T-UAS-050, T-UAS-060; §8.4 gives a 1000 KiB budget (below GitHub Actions' 1024 KiB step-summary limit); redaction applies to decoded string values (including native IDs) before preview truncation so a clipped credential prefix can't leak; a failed runtime-mask redaction "MUST remove the affected source" rather than leave it eligible for upload; fences are lengthened and HTML escaped against hostile payloads.
- **Confidence**: emerging
- **Quote**: "It is execution evidence with the workflow artifact’s access and retention policy, not a default summary or a public log preview."
- **Our assessment**: Names the tension clearly — lossless evidence vs. safe publication — and resolves it with two artifacts and a fail-closed rule. The spec admits "omission of user messages alone is not sufficient sanitization" since tool output and reasoning can be sensitive too.

### Claim 9: Tolerant parsing — malformed, truncated, or unknown records must not discard valid adjacent records, and unknown event types must survive
- **Evidence**: T-UAS-006, T-UAS-016, T-UAS-017; Appendix D recovery table; the custom-engine adapter detects format by actual signatures, not by "parseable JSON" or non-empty markdown (T-UAS-041).
- **Confidence**: settled (standard robustness practice, here made normative)
- **Quote**: "A parser or loss-preserving reader MUST retain unknown native dot-namespaced event types and their data, top-level fields, and order."
- **Our assessment**: An open vocabulary plus order preservation lets vendors add events without breaking consumers. Streaming deltas get exact-concatenation rules (T-UAS-020/021) and Gemini snapshot-reconciliation logic is elaborate — evidence that real engine streams are messy.

### Claim 10: Compliance is testable — requirement IDs, classes (P/R/B/M/F), fixture matrices, and determinism/idempotence/no-mutation assertions, with CI-sampled real sessions sanitized into fixtures
- **Evidence**: §2.2 classes; §9.1–9.3 matrices; T-UAS-025/026/052 (determinism, no input mutation, frozen fixtures); §9.4 table of sampled runs per engine; Gemini run 36078916290's original trace has 208 observations (33 assistant fragments, 86 tool starts, 86 tool completions — 85 successful, one failed); synthetic cases are labeled synthetic.
- **Confidence**: emerging
- **Quote**: "A report MUST identify failures and unavailable coverage; current implementation tests alone are not a conformance declaration."
- **Our assessment**: A model for how to test an observability pipeline: real-session fixtures with prompts/content sanitized, explicit labeling of synthetic cases, and assertions on structure rather than rendered markdown. Honest about limits (five sampled Gemini runs "contained no supported agent observations").

### Claim 11: Provider/session errors are kept separate from tool failures and from assistant answers
- **Evidence**: T-UAS-015, T-UAS-035; Appendix A shows a failed tool completion alongside `"errors": []` in `session.result`; Pi empty-content provider errors become session errors; two Gemini spending-cap sessions contain only init, user prompt, and terminal provider error with zero tokens/duration.
- **Confidence**: settled
- **Quote**: "The tool failure remains on native-call-c; the source’s empty session-error array is not populated automatically from it."
- **Our assessment**: Useful taxonomy for failure triage: tool failure (agent can recover), provider error (infrastructure/quota), permission denial (policy) are different signals and should be queried separately.

## Concrete Artifacts

```json
// Source: §3.5 T-UAS-064 — mandatory first record of aw_session.jsonl
{"type":"session.format","data":{"version":1},"provenance":{"component":"collector","phase":"conclusion","path":"usage/aw_session.jsonl","index":0}}
```

```json
// Source: §12.3 Appendix C — legacy-telemetry projection from a canonical session.result
{"type":"result","num_turns":2,"usage":{"input_tokens":30,"output_tokens":8}}
```

```json
// Source: §12.2 Appendix B — dangling start plus orphan completion (valid partial trace)
[
  { "type": "tool.execution_start", "data": { "toolCallId": "native-pending", "toolName": "bash", "command": "inspect" } },
  { "type": "tool.execution_complete", "timestamp": "2026-10-02T00:00:03Z",
    "data": { "toolCallId": "native-orphan", "toolName": "bash", "success": false, "output": "", "error": { "message": "Permission denied." } } }
]
```

Other artifacts (see source): Core event field tables (§4.1–4.6), full canonical example (§12.1, all core types with false/0/null outputs), per-engine signature→event mapping tables (§7), essential-payload-per-component table for the unified artifact (§3.5), runtime event vocabulary (`mcp.rpc.request`, `firewall.http_access`, `safe_output.request`, `grader.result`, `session.collection`, ...; §4.7), compliance matrix (§9.2).

```
// Source: §1.2 data-flow diagram (condensed)
engine log / native event stream -> tolerant parser -> ordered canonical events
   -> summary renderer -> legacy display projection
   -> session.result selection -> legacy telemetry projection
// Source: §1.2 — bootstrap persists redacted agent-session.jsonl; conclusion merges
// agent + detection + safe-output + experiment + eval evidence into usage/aw_session.jsonl
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-effective-tokens-specification.md` Claim 9 (completeness; incomplete visibility must be flagged rather than silently dropped) — this spec's T-UAS-050/063 (explicit coverage warnings, absent-component reporting) is the trace-level analogue.
  - `docs-ghaw-safe-outputs-specification.md` Claim 8 (SP5 provenance on created resources) — T-UAS-055 applies provenance to every trace event; safe-output requests vs. executed results are kept distinct (§4.7).
  - `docs-ghaw-open-telemetry-attributes.md` Claim 10 (trace data mirrored to local JSONL uploaded in the `agent` artifact) — `aw_session.jsonl` is a second, richer artifact in the same family, in `usage/`.
- **Contradicts**: None found. (Checked the overlapping gh-aw notes; no opposing claims.)
- **Extends**:
  - `docs-ghaw-copilot-sdk-driver-specification.md` Claim 8 (L3 logging requires full lifecycle event serialization) and the driver's "audit-friendly" design goal — this spec defines what the serialized lifecycle events must look like and how they are merged. It also lists the driver spec as a related reference (§11.2).
  - `docs-ghaw-audit-reference.md` (`gh aw audit` / `logs` consume run artifacts) — the spec notes "Go CLI readers are not automatically changed to consume the richer artifact" (§10.1), so audit does not yet read `aw_session.jsonl`.
- **Novel**: (a) Normative engine-neutral session event vocabulary with per-engine mapping tables; (b) three-state tool outcome and orphan/dangling semantics; (c) snapshot-vs-per-turn token reconciliation by schema; (d) timestamp-unit-aware, untimed-tail timeline merge with clock-skew disclaimer; (e) "failed workflow ≠ failed session" and "activity ≠ success" rules; (f) the privacy split between lossless artifact and redacted summary, including fail-closed removal on redaction failure.

## Guide Impact

- **Chapter 04 (Observability & Tracing)**: Add a "trace fidelity rules" section citing this spec: never default missing metrics to zero (T-UAS-005), use three-state tool outcomes, keep tool failures / provider errors / permission denials separate, and distinguish per-turn vs. snapshot usage. Cite Appendix C as a worked example.
- **Chapter 04 / Ch07 (Debugging)**: Recommend a single merged, provenance-tagged run timeline across agent, tool gateway, and network proxy (T-UAS-054–057), with an explicit note that wall-clock ordering ≠ causality.
- **Chapter 05 (Orchestration & Scaling / cost)**: Warn that "turns > 0" or token totals are activity evidence, not success (T-UAS-048), and that summing overlapping telemetry layers double-counts (T-UAS-062).
- **Chapter 03 / security**: Add the lossless-artifact vs. redacted-summary pattern (T-UAS-045, T-UAS-049, T-UAS-060) as guidance for storing agent transcripts, including "retention policy applies; prompts and tool output may be sensitive".
- No existing chapter recommendation is contradicted; this is additive evidence from a single vendor and should be graded emerging.

## Extraction Notes

- Read the whole page (§1–13 plus all appendices) from the fetched HTML converted to text; did not follow sub-pages (the page's referenced code files live in the gh-aw repo, not in the docs site).
- Page header says v1.2.0 while the Change Log tops out at 1.1.0 and §10.1 refers to "version 1.1.0"; the delta is undocumented. Status is Draft, published 2026-10-02 — one day before extraction, so the text may change.
- Claim quotes are verbatim from the page; no sentences were spliced. Cross-reference claim numbers were verified against the cited notes' numbered headings.
- Implementation is JavaScript (`actions/setup/js/*.cjs`); the spec disclaims any cross-language storage API.
