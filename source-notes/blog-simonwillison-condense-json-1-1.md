---
source_url: https://simonwillison.net/2026/Aug/3/condense-json/
source_type: blog-post
title: "condense-json 1.1"
author: Simon Willison
date_published: 2026-08-03
date_extracted: 2026-08-09
last_checked: 2026-08-09
status: current
confidence_overall: emerging
issue: "#2584"
---

# condense-json 1.1

> A ~60-word release-announcement "beat" for `condense-json` 1.1 — two new
> replacement kinds (structural matching and merge-patch references)
> discovered while dogfooding 1.0 into the `llm` project — whose linked
> GitHub PR contains the real substance: a measured 22%→44% storage-savings
> jump on real OpenAI payloads, a diagnosed-and-fixed quadratic performance
> bug, and a property-based test suite that was itself validated by
> mutation testing before being trusted.

## Source Context

- **Type**: blog-post (release announcement, Simon Willison's Weblog,
  "Release" category, ~60 words, published 2026-08-03, tagged `json`).
  Structurally near-identical to the 1.0 post covered in
  `blog-simonwillison-condense-json-1-0.md`: thin on its own, with nearly
  all substantive content reachable only through its linked pages. Per
  MINER.md's instruction to follow substantive linked pages, this note
  draws on all of the post's content-bearing outbound links: the GitHub
  1.1 release notes (`github.com/simonw/condense-json/releases/tag/1.1`),
  GitHub PR simonw/condense-json#8 ("Structural and merge replacements,
  Hypothesis property tests," merged 2026-08-03), and the PR's linked test
  file (`github.com/simonw/condense-json/blob/1.1/tests/test_properties.py`).
  The fifth link (to the third-party Hypothesis library's own docs
  homepage) was not followed — it is generic library documentation, not
  source-specific content. This note also draws on the current README's
  "Structural replacements" and "Merge references" sections
  (`raw.githubusercontent.com/simonw/condense-json/main/README.md`), which
  the sibling 1.0 note referenced as existing but did not quote from (that
  note only quoted the escaping example, which is 1.0-era).
- **Author credibility**: Simon Willison — creator and maintainer of both
  `condense-json` and the `llm` CLI/library that is its motivating
  consumer; first-party source for all claims about both projects.
- **Scope**: Covers exactly what changed between condense-json 1.0 and 1.1:
  structural (dict/list) replacement matching, merge-patch references for
  near-identical objects, the property-based (Hypothesis) test suite added
  to validate both, and the performance/testing engineering that went into
  shipping them, all documented through the PR that implements them. Does
  **not** cover the 1.0-era string/substring-matching mechanism, escaping,
  or error-handling behavior — those are covered in
  `blog-simonwillison-condense-json-1-0.md` Claims 1, 3, 4, 5. Does not
  cover any adoption or measurement of condense-json 1.1 beyond the single
  `llm` integration described in the PR itself.

## Extracted Claims

### Claim 1: The post frames both 1.1 features as things Willison "found" already wanted while integrating 1.0 into `llm`, not features planned in advance of the 1.0 release
- **Evidence**: The blog post's own opening sentence.
- **Confidence**: settled (first-party statement, contemporaneous with the
  work — not inferred after the fact)
- **Quote**: "After shipping condense-json 1.0 I started integrating it
  into LLM, and found there were some desirable new features already:"
- **Our assessment**: This corroborates, from the source itself, what the
  sibling 1.0 note's Claim 12 could only establish indirectly (by
  comparing GitHub release timestamps and a mid-PR comment). Read
  together, the two notes show the same dogfooding-driven design loop
  described twice: once predicted mid-PR ("So I'm probably going to do a
  condense-json 1.1"), and now confirmed after the fact in the 1.1
  announcement itself.

### Claim 2: Structural replacements let a replacement value be an arbitrary dict or list, matched against any subtree of the input by canonical-JSON-form structural equality — not literal byte identity — with the whole matching subtree replaced by a `{"$": id}` marker
- **Evidence**: README's "Structural replacements for dicts and lists"
  section, with a worked example (an API response echoing back a JSON
  schema in a different key order than the original still matches and
  condenses).
- **Confidence**: settled (documented behavior with a runnable example)
- **Quote**: "These match **structurally**: any subtree of the input that
  is equal to the value - compared in canonical JSON form, so key order
  and formatting never matter - is replaced whole with `{"$":
  replacement_id}`."
- **Our assessment**: This is the generalization that turns condense-json
  from a string-deduplication tool (1.0) into a JSON-subtree-deduplication
  tool. The explicit "key order and formatting never matter" guarantee is
  what makes it usable against real API responses, where a provider is not
  guaranteed to echo a JSON object back with the same key ordering it was
  sent in.

### Claim 3: Structural matching is "outermost-wins" — once a subtree matches, its interior is not scanned for further, nested replacements
- **Evidence**: README's documented matching rules for structural
  replacement.
- **Confidence**: settled (documented behavior)
- **Quote**: "Matching is outermost-wins. Once a subtree matches, its
  interior is not searched further. Inner replacements still match
  anywhere an outer one does not."
- **Our assessment**: A necessary tie-breaking rule once matching can
  operate on nested containers rather than flat strings — without it, a
  large matched subtree and a smaller matched subtree nested inside it
  could both fire, producing ambiguous or redundant condensed output.

### Claim 4: Structural matching requires genuine JSON structural equality — a string that merely *contains* the serialized text of a replacement value is never treated as a match; only actual subtree structure matches
- **Evidence**: README's documented matching rules for structural
  replacement.
- **Confidence**: settled (documented behavior)
- **Quote**: "Matching is strictly structural. A string that happens to
  contain the JSON serialization of a replacement value is never matched -
  a reference in string context must resolve to a string."
- **Our assessment**: This closes an obvious correctness trap: without
  this rule, a log message or free-text field that happened to contain the
  literal serialized JSON of some known object could get silently
  (mis)condensed as if it were that object, corrupting round-trips. The
  rule keeps string-context and structure-context matching cleanly
  separated.

### Claim 5: Merge references let a dict that is "mostly equal" to a known base object (some keys added, changed, or missing) be stored as a small patch against that base — an update map `u` plus a delete list `d` — instead of being stored in full
- **Evidence**: README's "Merge references: a base object plus a patch"
  section, with a worked example (an OpenAI-style response envelope with
  ~6 static keys plus 2 varying ones condenses to a 2-key patch).
- **Confidence**: settled (documented behavior with a runnable example)
- **Quote**: "Dict replacement values also act as **merge bases**. A dict
  in the input that is *mostly* equal to a base - some keys added, changed
  or missing - can be stored as a reference to the base plus a patch,
  using a dict-valued `$` marker"
- **Our assessment**: This is the feature that produces the largest
  practical win in this source (Claim 8) — it targets exactly the shape of
  a verbose, mostly-static API response envelope (see Concrete Artifacts),
  which is common in LLM provider responses but which plain structural
  matching (Claim 2) can only dedupe when the *entire* object recurs
  byte-for-byte, not when it recurs with a few fields varying.

### Claim 6: Whether to emit a merge reference at all is decided by an explicit byte-cost comparison against the plain encoding, not a similarity heuristic — a base unrelated to the input dict simply produces a larger patch than the dict itself and is rejected on cost alone
- **Evidence**: README's "How condensing decides" list.
- **Confidence**: settled (documented design rule, corroborated by the PR
  author's own description: "Condensing needs no similarity heuristic: for
  each base the patch is computed and both encodings are *measured*, and
  the merge form is emitted only when it is smaller — unrelated bases
  price themselves out.")
- **Quote**: "A byte-cost comparison, not a similarity heuristic. For each
  base, the patch is computed and both encodings are measured; the merge
  reference is emitted only when it is smaller than writing the dict out.
  An unrelated base produces a patch bigger than the dict itself, so it
  prices itself out."
- **Our assessment**: This is a deliberately conservative design choice —
  it trades a small amount of computation (compute the patch, measure both
  encodings) for the guarantee that merge-reference matching can never
  make output *larger* than not using it, and never depends on a tunable
  similarity threshold that could misfire on unrelated data.

### Claim 7: Deletion of a base's keys in a merge patch uses an explicit `d` list of key names, rather than the `null`-sentinel convention used by JSON Merge Patch (RFC 7396), because `null` can be a legitimate value inside a real payload
- **Evidence**: README's "How condensing decides" list, explicitly
  contrasting the design against JSON Merge Patch by name.
- **Confidence**: settled (documented design rationale)
- **Quote**: "Deletion is the explicit `d` list, never a `null` sentinel
  (as in JSON Merge Patch), because `null` is a legitimate value in real
  payloads."
- **Our assessment**: A concrete, well-reasoned correctness fix to a
  known failure mode of the more common JSON Merge Patch convention (where
  you cannot distinguish "delete this key" from "set this key to null").
  Worth citing whenever the guide discusses building custom diff/patch
  encodings for LLM payloads that may legitimately contain `null`.

### Claim 8: Applied to real OpenAI Responses API payloads inside `llm`, merge references (not structural replacements) raised typical per-reply storage savings from 22% to 44%, because roughly 15 largely-static top-level envelope keys collapse into a single base reference
- **Evidence**: The PR's own "Claude Fable 5 description" technical
  section, first-party measurement on the same `llm` integration described
  in `blog-simonwillison-condense-json-1-0.md` Claim 6.
- **Confidence**: emerging (single-author, live-call measurement; "a
  typical reply" is not a stated sample size or methodology, and there is
  no independent reproduction)
- **Quote**: "Measured on real OpenAI Responses payloads in llm, merge
  references took a typical reply from 22% to 44% saved, since the ~15
  static top-level envelope keys collapse to one reference."
- **Our assessment**: This roughly doubles the savings rate on the same
  integration relative to what string-only matching alone was already
  achieving (the 1.0 note's Claim 8/10 figures of 86%/40%-of-payload were
  measured on different payload slices — full text responses and echoed
  tool definitions, respectively — so the numbers aren't directly
  comparable, but this claim's point stands on its own: the *envelope*
  fields that string-substitution couldn't touch, because they're small
  scalars and enum-like strings rather than large recurring text blocks,
  are exactly what merge references are built to catch).

### Claim 9: An initial version of the merge-cost computation was accidentally quadratic on deeply nested documents (29ms for a 36KB document); adding a "key-overlap early-out" that skips cost computation for nodes sharing no keys with any base brought that down to 0.6ms, with realistic payloads condensing in under 0.1ms
- **Evidence**: The PR's technical section, describing a diagnosed and
  fixed performance regression with matched before/after timings.
- **Confidence**: settled for the mechanism (documented, merged
  optimization) / emerging for the specific millisecond figures
  (single-author benchmark, not independently reproduced, no stated
  hardware or methodology)
- **Quote**: "Performance was benchmarked and tuned: a key-overlap
  early-out skips the cost computation for nodes sharing no keys with any
  base (without it, deeply nested documents went quadratic - 29ms for a
  36KB doc, now 0.6ms), base canonical forms are computed once per call,
  and input subtree canonicals are memoized."
- **Our assessment**: A ~48x latency reduction from a targeted early-out
  plus memoization is a large win for a small, mechanical fix — but it
  also documents that the *first* implementation of merge-cost comparison
  (Claim 6) was quadratic before this fix, which is a useful cautionary
  data point: adding a "cheap-looking" per-node cost comparison across
  multiple candidate bases can silently become expensive at scale unless
  explicitly guarded, and this was caught by benchmarking rather than by
  the correctness-focused property tests (Claim 10).

### Claim 10: The 1.1 property-based test suite's strategies were validated by mutation testing — three deliberately planted bug classes were confirmed caught by the suite — and that validation process itself surfaced and led to fixing two real weaknesses in the test strategies
- **Evidence**: The PR's technical section, describing the mutation-testing
  process and its concrete findings; independently corroborated by
  fetching the shipped `tests/test_properties.py`, which contains a
  `confusables` strategy (`st.sampled_from([True, False, 0, 1, 0.0,
  1.0, "", "0", "1"])`) and an `assert_equivalent` helper that compares
  both `==` and `json.dumps(..., sort_keys=True)` output — matching what
  the PR text describes.
- **Confidence**: settled (documented in the merged PR description and
  directly verifiable in the merged test file)
- **Quote**: "The strategies were validated by mutation testing - three
  planted bugs (equality-semantics, dropped escaping, raw-instead-of-processed
  patches) are all caught. That process exposed and fixed two real
  weaknesses: a confusables generator now draws True/False/0/1/0.0/1.0
  frequently, and assertions compare canonical JSON alongside ==, because
  True == 1 makes bool/int corruption invisible to == alone."
- **Our assessment**: This is the most guide-relevant claim in this
  source. It documents a two-layer verification discipline that goes
  beyond "write property-based tests and see them pass": (1) Hypothesis
  generates randomized adversarial inputs to check the round-trip
  contract, and (2) mutation testing checks whether that generated test
  suite would actually *notice* if the implementation were broken in
  specific, named ways — and in this case it found that plain `==`
  comparison in Python cannot distinguish `True` from `1` (`True == 1` is
  `True`), meaning a bug that corrupted a boolean into an integer could
  pass a naively-written property test undetected. That is a concrete,
  worked instance of exactly the "green tests that never touch the risky
  code" failure mode the guide already documents (see Guide Impact).

### Claim 11: 1.1 extends the 1.0-era deterministic tie-breaking rule ("first match in mapping order wins ties") to merge-base selection: when multiple candidate bases could produce a valid merge reference for the same dict, the smallest resulting encoding wins, and ties go to the earlier entry in the replacements mapping
- **Evidence**: The PR's "Notes for review" section, explicitly stating the
  rule is a re-application of "the documented rule for other replacement
  kinds" (i.e., the 1.0-era determinism rule covered in
  `blog-simonwillison-condense-json-1-0.md` Claim 4).
- **Confidence**: settled (documented in the merged PR description)
- **Quote**: "First-ID-wins now holds for merge bases too (kept in mapping
  order, equivalent values deduplicated), matching the documented rule for
  other replacement kinds; cost ties also go to the earlier entry."
- **Our assessment**: A small but telling design-consistency signal —
  rather than inventing a new tie-breaking convention for the new
  merge-base feature, the author explicitly re-applied the existing
  determinism rule established in the 1.0 release. This matters for the
  same reason the 1.0-era rule mattered (per that note's Claim 4): any
  system diffing, hashing, or caching condensed output needs the encoding
  to be a stable function of the input, and a second inconsistent
  tie-breaking rule for a second replacement kind would have reintroduced
  non-determinism through a side door.

### Claim 12: The merged PR's own body is structured as two visibly distinct, explicitly labeled authorship layers — a short human-authored summary from Willison at the top, followed by a collapsed `<details>` section titled "Claude Fable 5 description" containing the full technical writeup, itself closing with a "🤖 Generated with Claude Code" attribution line
- **Evidence**: Direct inspection of PR simonw/condense-json#8's raw body
  via the GitHub API (reproduced in full in Concrete Artifacts below).
- **Confidence**: settled (directly observable structure of the merged,
  public PR body)
- **Quote**: (no direct single-sentence quote captures the structural
  claim; see the PR body reproduced verbatim in Concrete Artifacts, which
  shows the human summary, the `<details><summary>Claude Fable 5
  description</summary>` wrapper, and the closing "🤖 Generated with
  [Claude Code](https://claude.com/claude-code)" line in place)
- **Our assessment**: This is a concrete, dated example of a specific
  PR-authorship-transparency convention: rather than presenting the
  AI-agent-authored technical detail as if it were the human maintainer's
  own prose (or omitting attribution entirely), the PR body marks exactly
  which section was written by the coding agent, and folds it into a
  collapsed disclosure block so it doesn't dominate the PR's default view.
  All of the specific technical claims extracted in this note (Claims
  6, 8, 9, 10, 11, 13) come from inside that agent-authored, collapsed
  section — worth flagging explicitly, since it means this note's
  technical claims are sourced from the coding agent's own self-report of
  its work, not from Willison's independent verification of it (though the
  test counts in Claim 13 and the shipped test file fetched for Claim 10
  are independently checkable, and were checked, by this note).

### Claim 13: Before merge, the PR reports a full green build: 71 tests passing, a clean `mypy` run, Black-formatted code, and README documentation with executable examples for both new features
- **Evidence**: The PR's "Notes for review" section.
- **Confidence**: settled (documented in the merged PR description)
- **Quote**: "`uv run pytest`: 71 passed. `uv run mypy condense_json
  tests`: clean. Black formatted. README documents both new behaviors with
  executable examples."
- **Our assessment**: A minimal but concrete "definition of done"
  checklist for a solo-maintainer library release: types check, tests
  pass, formatting is enforced, and docs exist with runnable examples —
  useful as a citable baseline for what "ready to merge" looks like for
  small, single-author open-source Python libraries in this corpus.

## Concrete Artifacts

```
# condense-json README: structural replacement example (1.1+, current main)
# Source: https://raw.githubusercontent.com/simonw/condense-json/main/README.md

from condense_json import condense_json, uncondense_json

schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}},
    "required": ["name"],
}
response = {
    "output": {"name": "Cleo"},
    "format": {
        # Same schema, different key order - still matches
        "schema": {
            "required": ["name"],
            "type": "object",
            "properties": {"name": {"type": "string"}},
        }
    },
}
condensed = condense_json(response, {"s": schema})
# {'output': {'name': 'Cleo'}, 'format': {'schema': {'$': 's'}}}
assert uncondense_json(condensed, {"s": schema}) == response
```

```
# condense-json README: merge reference example (1.1+, current main)
# Source: https://raw.githubusercontent.com/simonw/condense-json/main/README.md

from condense_json import condense_json, uncondense_json

env = {
    "object": "response",
    "status": "completed",
    "service_tier": "default",
    "truncation": "disabled",
    "store": False,
    "tools": [],
}
response = dict(env, id="resp_123", usage={"total_tokens": 27})
condensed = condense_json(response, {"env": env})
# {'$': {'m': 'env', 'u': {'id': 'resp_123', 'usage': {'total_tokens': 27}}}}
assert uncondense_json(condensed, {"env": env}) == response
```

```
# condense-json PR #8 body, verbatim (merged 2026-08-03T04:52:42Z)
# Source: https://github.com/simonw/condense-json/pull/8 (fetched via GitHub API)
# Title: "Structural and merge replacements, Hypothesis property tests"

Three features that extend replacements beyond substring matching, built for
llm's condensed response payload storage (https://github.com/simonw/llm/pull/1586).

Three key changes:
- Replacements of {"a": {"object": ["nested", "list"]}}` now work - previously
  the value had to be a string, now it can be any JSON structure.
- For objects in that replacement list, the resulting condensed structure can
  specify merge operations - take that object, add or change these keys,
  delete these other keys.
- Hypothesis testing to help ensure round-trips across complex examples.

<details><summary>Claude Fable 5 description</summary>

## Structural replacements

A replacement value may now be a dict or a list. Container values match
structurally - any subtree equal to the value in canonical JSON form is
replaced whole with the existing {"$": id} marker, so key order and
serialization bytes never matter. Matching is outermost-wins and strictly
structural (a string containing the JSON serialization of a value never
matches). Resolution substitutes independent deep copies; round trips are
structurally equal rather than byte-identical, since the original key order
of a matched subtree is not recorded.

## Merge references

Dict replacements double as merge bases: a dict that is mostly equal to a
base - a static envelope with a few varying fields, like API response
metadata - is stored as a dict-valued marker:

{"$": {"m": "base_id", "u": {"added or changed": "keys"}, "d": ["absent keys"]}}

Condensing needs no similarity heuristic: for each base the patch is
computed and both encodings are measured, and the merge form is emitted
only when it is smaller - unrelated bases price themselves out. Deletion
is the explicit d list rather than a JSON Merge Patch-style null sentinel,
because null is a legitimate payload value. The dict-valued marker is
still a single-key $ dict, so the existing $raw escaping already protects
input that looks like a merge reference. Measured on real OpenAI Responses
payloads in llm, merge references took a typical reply from 22% to 44%
saved, since the ~15 static top-level envelope keys collapse to one
reference.

Performance was benchmarked and tuned: a key-overlap early-out skips the
cost computation for nodes sharing no keys with any base (without it,
deeply nested documents went quadratic - 29ms for a 36KB doc, now 0.6ms),
base canonical forms are computed once per call, and input subtree
canonicals are memoized. A realistic payload condenses in under 0.1ms;
adding bases to a large string-replacement workload costs nothing
measurable.

## Property-based tests

Six Hypothesis properties: the round-trip contract under arbitrary,
document-derived, and merge-targeted replacements; output always
JSON-serializable; repeated application lossless; and uncondense_json on
arbitrary input either resolves or raises UncondenseError, never anything
else. The strategies were validated by mutation testing - three planted
bugs (equality-semantics, dropped escaping, raw-instead-of-processed
patches) are all caught. That process exposed and fixed two real
weaknesses: a confusables generator now draws True/False/0/1/0.0/1.0
frequently, and assertions compare canonical JSON alongside ==, because
True == 1 makes bool/int corruption invisible to == alone.
HYPOTHESIS_PROFILE=thorough runs 2,000 examples per property.

## Notes for review

- First-ID-wins now holds for merge bases too (kept in mapping order,
  equivalent values deduplicated), matching the documented rule for other
  replacement kinds; cost ties also go to the earlier entry.
- Patches are flat by design: a nested value that differs at all travels
  whole in u (condensed recursively on the way). Nested bases provide
  depth when wanted.
- uv run pytest: 71 passed. uv run mypy condense_json tests: clean. Black
  formatted. README documents both new behaviors with executable examples.

🤖 Generated with Claude Code (https://claude.com/claude-code)

</details>
```

```
# condense-json 1.1 property-based test strategies (excerpt), shipped in tests/test_properties.py
# Source: https://github.com/simonw/condense-json/blob/1.1/tests/test_properties.py

def assert_equivalent(a, b) -> None:
    """Equality that Python == cannot fake.

    == alone would let a bool/int swap slip through (True == 1), so
    also compare canonical JSON forms, where they serialize differently.
    """
    assert a == b
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)

# Keys biased toward the marker vocabulary so escaping and merge-shaped
# data get exercised far more often than random text would manage
keys = st.one_of(
    st.sampled_from(["$", "$r", "$raw", "m", "u", "d", "a", "b", "key"]),
    st.text(max_size=8),
)

# Values that Python == conflates but canonical JSON distinguishes -
# drawn often, so equality-semantics bugs cannot hide in rarity
confusables = st.sampled_from([True, False, 0, 1, 0.0, 1.0, "", "0", "1"])
```

```
# condense-json 1.1 release notes, verbatim
# Source: https://github.com/simonw/condense-json/releases/tag/1.1 (fetched via GitHub API)
# Published: 2026-08-03T04:56:26Z

- Replacements object can now include values other than strings. These will
  be identified and used as structural replacements by condense_json() and
  uncondense_json(). #8
- Objects can be used as the basis for merge operations. condense_json()
  will identify if there are objects that are a close match and will store
  instructions for keys to update or delete. uncondense_json() can then
  apply these merges. #8
- Now includes additional round-trip tests using hypothesis.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-condense-json-1-0.md` (Cross-References →
    Corroborates section, and Guide Impact → "measurement discipline"
    point): that note already establishes that this corpus treats
    condense-json's storage-savings percentages as single-source,
    workload-specific measurements rather than universal constants. This
    note's Claim 8 (22%→44% via merge references) and Claim 9 (29ms→0.6ms
    performance fix) are two further instances of that same pattern —
    single-author, live-call measurements on a single integration, not
    independently reproduced benchmarks — now specific to the 1.1
    merge-reference feature rather than the 1.0 string-substitution
    feature.

- **Contradicts**: None identified. No existing source note makes a claim
  about structural/merge-based JSON deduplication, property-based test
  validation via mutation testing, or PR-body authorship attribution
  conventions that this source disagrees with.

- **Extends**:
  - `blog-simonwillison-condense-json-1-0.md` Claim 1 (the library's core
    string/substring-matching mechanism): this note's Claims 2-7 document
    the two new, structurally distinct matching modes (whole-subtree
    structural matching, and base-plus-patch merge references) that 1.1
    adds alongside it, without changing or replacing the 1.0 mechanism.
  - `blog-simonwillison-condense-json-1-0.md` Claim 4 (1.0's deterministic
    longest-match-wins overlap resolution for string replacements): this
    note's Claim 11 documents the same author explicitly re-applying that
    determinism principle (first-match-in-mapping-order-wins on ties) to
    the new merge-base selection logic in 1.1, rather than inventing an
    inconsistent second rule.
  - `blog-simonwillison-condense-json-1-0.md` Claim 12 (the same-day
    1.0-to-1.1 dogfooding-driven feature addition, established there via
    GitHub timestamps and a mid-PR comment): this note's Claim 1 confirms
    the same fact directly from the 1.1 announcement post's own framing
    sentence, rather than by inference.
  - `blog-simonwillison-condense-json-1-0.md` Claim 6 (the `llm` PR's use
    of condense-json to restore raw-provider-payload storage without
    duplicating data already held elsewhere): this note's Claim 8 shows
    the *second* round of optimization applied to that same integration,
    targeting the response envelope specifically rather than repeated
    text/tool-definition strings.

- **Novel**:
  - Mutation testing used specifically to validate that a property-based
    (Hypothesis) test suite's *strategies* are strong enough to catch
    named bug classes, rather than merely running the suite and observing
    that it passes (Claim 10). This technique does not appear anywhere
    else in the corpus (checked via full-text search for "mutation
    testing" and "Hypothesis" across all source notes).
  - The specific, concrete finding that plain Python `==` cannot
    distinguish `True` from `1`, and that this can hide bool/int
    type-confusion bugs from equality-based test assertions unless
    canonical-JSON comparison is added alongside `==` (Claim 10) — a
    reusable, narrow correctness lesson for anyone writing property-based
    tests over JSON-like data in Python.
  - The diagnosed-and-fixed quadratic performance regression in the
    merge-cost comparison, and its fix via a key-overlap early-out plus
    canonical-form memoization (Claim 9) — a concrete example of
    performance engineering (not just correctness engineering) happening
    inside a small, single-author library's release cycle.
  - The explicit, labeled split between human-authored and
    AI-agent-authored ("Claude Fable 5 description") sections within a
    single merged PR body (Claim 12) — a concrete, dated example of one
    specific PR-authorship-transparency convention in practice.

## Guide Impact

- **Chapter 03 (Verification)**: The existing "Green tests that never
  touch the risky code ('Lying Tests')" section (sourced from
  `blog-fowler-malykhin-archaeologist-copilot`) covers how to sanity-check
  an *existing* test suite (does it exercise the risky path, can it
  actually fail). This source adds a distinct, complementary technique for
  *newly written* property-based tests: validate the test strategies
  themselves via mutation testing — deliberately plant named bug classes
  and confirm the suite catches all of them — before trusting a green
  Hypothesis run as a verification signal (Claim 10). Recommend adding
  this as a named technique alongside the existing Lying Tests material,
  with the concrete, citable finding that plain `==` comparison can hide
  bool/int type-confusion bugs in Python and needs a canonical-JSON check
  alongside it to actually catch them.
- **Chapter 04 (Context Engineering)**: Extends the storage-side
  deduplication pattern already recommended from
  `blog-simonwillison-condense-json-1-0.md` (dedupe a raw provider
  response against data already normalized elsewhere in a harness's
  storage schema). This source adds the specific follow-on technique that
  produced the larger second-round win on the same production integration:
  once obvious string-level duplication is handled, identify small,
  mostly-static structured objects that recur with only a few varying
  fields (e.g., an API response's envelope metadata) and encode them as a
  base-plus-patch merge reference rather than as more string-replacement
  entries (Claims 5-8). Flag Claim 6's design rule (emit the merge
  reference only when a byte-cost comparison shows it's actually smaller)
  as the general principle: prefer a measured cost comparison over a
  similarity heuristic for any deduplication scheme, since a heuristic
  threshold can misfire on unrelated data in ways a direct cost comparison
  cannot.

## Extraction Notes

- The blog post itself (`simonwillison.net/2026/Aug/3/condense-json/`) is
  very short (~60 words of body text) and was read in full via a direct
  `curl` fetch of the page HTML, stripped to plain text, to source
  verbatim quotes directly rather than through a model-paraphrased
  intermediary (consistent with the approach used in the sibling 1.0 note,
  and for the same reason: WebFetch summarizes rather than preserving
  verbatim text for short pages like this one).
- The post's GitHub links (`github.com/simonw/condense-json/...`) render
  almost entirely as JavaScript-driven navigation chrome when fetched as
  raw HTML via `curl` — the actual PR/release content is not present in
  the static HTML response. This note instead used the GitHub REST API
  (`api.github.com/repos/simonw/condense-json/pulls/8` and
  `.../releases/tags/1.1`) to retrieve the authoritative, verbatim
  Markdown body text for both the PR and the release notes. This is a
  more reliable source than scraping the rendered page and is
  recommended for any future Miner work touching GitHub PR/release pages.
- Per MINER.md's "follow up to 5 linked pages that seem substantive," this
  note followed 3 of the post's 4 content-bearing linked pages (the 1.1
  release tag, PR #8, and the linked `tests/test_properties.py` file),
  plus the current README's "Structural replacements" and "Merge
  references" sections (not itself a link from this specific post, but
  already established as in-scope by the sibling 1.0 note, which
  referenced these sections without quoting them). The link to the
  Hypothesis library's own documentation homepage was not followed, as it
  is third-party library documentation rather than source-specific
  content. The link back to the 1.0 post was not re-followed since it is
  already fully covered by `blog-simonwillison-condense-json-1-0.md`.
- **Cross-reference verification** (per MINER.md §4b): all `Claim N`
  citations to `blog-simonwillison-condense-json-1-0.md` above (Claims 1,
  4, 6, 12) were checked against that file's actual numbered `### Claim`
  headings by reading the full note in this session: Claim 1 ("`
  condense_json` compresses JSON by replacing strings..."), Claim 4
  ("condense-json 1.0 makes overlapping-replacement resolution
  deterministic..."), Claim 6 ("A real deployment (GitHub PR
  simonw/llm#1586...) uses condense-json to restore full
  raw-provider-payload logging..."), and Claim 12 ("The `llm` integration
  work directly motivated same-day extensions to condense-json
  itself..."). All four numbers and their content match what is cited
  above.
- No paywall or access issues on any fetched page (blog post, PR #8,
  release notes, test file, README — all public).
- `confidence_overall` is set to "emerging," matching the sibling 1.0
  note's grading rationale: the documented mechanism, design rules, and
  test-methodology claims (Claims 2-7, 10, 11, 12, 13) are settled,
  verifiable facts, but the practically important storage-savings and
  performance numbers (Claims 8, 9) are single-author, non-reproduced,
  live-call measurements on one integration.
- No contradiction issue was filed. No existing source note makes a claim
  this source disagrees with.
