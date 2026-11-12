---
source_url: https://martinfowler.com/articles/tests-as-data.html
source_type: blog-post
title: "Tests as data: ensuring AI-generated code does what we want"
author: Matteo Vaccari (Technical Principal, Thoughtworks Italia)
date_published: 2026-11-11
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: emerging
issue: "#4672"
---

# Tests as data: ensuring AI-generated code does what we want

> Proposes moving the human–AI behavioural contract out of agent-editable test code and into customer-language test data (tables / DSL scenarios) run by a small, AI-generated runner, so unexpected agent edits are easier to spot and block.

## Source Context

- **Type**: blog-post (long-form article on martinfowler.com)
- **Author credibility**: Matteo Vaccari is a Thoughtworks Technical Principal with an Extreme Programming background. The article is explicitly "the point-of-view of one practitioner". The author lists David Farley, Birgitta Böckeler, Ivett Ördög, James Shore, Max Kanat-Alexander and others as draft reviewers, and says AI was used "for brainstorming, research, criticism and proof-reading" with the prose his own.
- **Scope**: Covers why AI-written tests lose trust, the tests-as-data / customer-test / external-DSL technique, its lineage (Fit, Go tabular tests, approval testing, Approved Scenarios), implementation hints (service-layer tests, UI printers/parsers, digital twins, protecting the harness, validating tests via mutation testing and oracles) and limits. It offers **no measured results** for the technique itself. The motivating statistics (Faros, DX, CloudBees) and the 26-developer interviews are reported by the author and were not independently verified here.

## Extracted Claims

### Claim 1: Developers who gave AI high autonomy did not trust their test suites, because the AI refactors tests along with code
- **Evidence**: The author's early-2026 interviews with 26 Thoughtworks developers at an organisation heavily invested in AI coding agents (self-reported by the author; no data table published).
- **Confidence**: anecdotal
- **Quote**: "I don’t trust our tests that much! Because even if I review the tests when they are initially generated, as new features get added, the AI refactors both existing code and existing tests, so I’m no longer confident that the tests are still ensuring the right behaviour"
- **Our assessment**: Names the specific failure mode (silent drift of previously reviewed tests) that justifies a protected test artifact. Sample is one organisation, so treat as a motivating observation, not a prevalence figure.

### Claim 2: Third-party reports show rising defects in AI-assisted delivery, and the author only conjectures that weaker functional tests are a cause
- **Evidence**: Cited vendor reports: Faros AI Engineering Report 2026 (bugs per PR +28.7%, bugs per developer +54%), DX Q1 impact report (50% more defects at some companies), CloudBees State of Code Abundance 2026 (81% of 213 enterprise tech leaders report more production issues; 70% say test-suite maintenance is a bigger burden than writing code). We did not verify these reports.
- **Confidence**: anecdotal
- **Quote**: "I don’t know for certain what the causes are of this widely reported decrease in external quality"
- **Our assessment**: The causal link to test quality is explicitly hedged ("plausible"). Cite the statistics as reported context only, never as evidence the technique works.

### Claim 3: AI-generated tests are often coupled to the implementation and confirm current behaviour, including bugs, rather than specifying correct behaviour
- **Evidence**: Author's experience; mock-heavy tests prove "when we invoke function A, it will invoke function B" rather than "when input is X, output must be Y".
- **Confidence**: emerging
- **Quote**: "most often, the AI will write tests that confirm the current implementation, including any bugs it may contain."
- **Our assessment**: Corroborates the guide's existing mock-heavy-test warning and the tautological-test finding in the Böckeler note. The article lists four problems: volume, readability, implementation coupling, and not proving correctness.

### Claim 4: Prose (Markdown) specs in spec-driven development have four weaknesses: volume/fatigue, maintenance, partial LLM compliance, and ambiguity. Tests are the executable alternative
- **Evidence**: Author's reasoning; coins nothing new but cites "cognitive surrender" (attributed to "someone").
- **Confidence**: emerging
- **Quote**: "In short, prose specs can't be executed; tests can."
- **Our assessment**: Useful counterweight to SDD advice. Also notes agents may give up on parts of a spec "to claim 'done' sooner". Argument is plausible but unmeasured.

### Claim 5: When AI writes the code, developers become its customers, so customer tests (black-box, in the customer's language) should be the primary human–AI contract and unit tests are secondary
- **Evidence**: Argument from the XP tradition (customer/acceptance tests vs developer tests); no empirical test.
- **Confidence**: emerging
- **Quote**: "That's why I think that customer tests are the primary kind of tests that we should rely on; especially when production code is AI-generated."
- **Our assessment**: The central thesis. The reframing is the novel part. It does not say unit tests are useless: "Unit tests (developer tests) can still be useful, but we don’t treat them as the primary source of truth where specifying behaviour is concerned."

### Claim 6: Tests-as-data (input, expected output/side effects, and setup captured in YAML/CSV/tables or a DSL) makes tests shorter, refactor-resistant, and makes AI changes to them easier to spot
- **Evidence**: Worked Java HTTP greeting example reduced to a 3-field YAML/CSV table; access-control table of 10 rows; BASIC interpreter, allowlist and todo-app DSL examples (see Concrete Artifacts). No metrics.
- **Confidence**: emerging
- **Quote**: "when the tests are written in text files, it's easier to spot when AI is changing them."
- **Our assessment**: Plausible mechanism. Tables work only for stateless rows with scalar inputs; the author warns against encoding stateful action sequences in tables and points to structured scenarios for those.

### Claim 7: Moving the contract into data lets teams protect it mechanically (read-only files, CI file-change checks, harness hooks), because the runner is much smaller than the test code it replaces
- **Evidence**: A matrix of which artifacts should change per task type (new feature: prod code + test data; refactor: prod code only; coverage: test data only; DSL improvement: test data + runner). Author notes hooks give "fast feedback" but are "not bullet-proof".
- **Confidence**: emerging
- **Quote**: "The hooks facility of coding harnesses can provide the model fast feedback when it attempts to change something that it shouldn't, but is not bullet-proof."
- **Our assessment**: Directly actionable harness-engineering pattern: task-type-conditioned write permissions. Honestly caveated: the test runner and DSL implementation are still code the agent can alter ("room for AI to play surprises on us").

### Claim 8: An external DSL (with a parser) makes assertions mandatory and so prevents agents from faking coverage with weak or missing assertions (Ördög's "Constrained Tests")
- **Evidence**: Attributed to Ivett Ördög's Approved Scenarios / Approved Logs / Constrained Tests patterns; contrasts with internal DSLs where an agent could "write tests with no assertions, or weak assertions".
- **Confidence**: emerging
- **Quote**: "Approved Scenarios and Logs make cheating less likely, by making the assertion part of the test mandatory in the DSL syntax, and this requires that the DSL is implemented with a parser, i.e. an external DSL."
- **Our assessment**: A concrete anti-reward-hacking design choice (assertion-in-grammar). Second-hand from Ördög; her talk is not reviewed here. Gherkin is criticised as too free-form and prone to step-definition proliferation.

### Claim 9: AI makes DSL parsers and bespoke test runners cheap, which removes the historical objection to Fit/Cucumber-style customer tests
- **Evidence**: Historical account (Fit, Specification by Example, James Shore's disillusionment that customers would not write the tables). Author argues two things have changed: developers are now the customers, and runner machinery is cheap to generate.
- **Confidence**: emerging
- **Quote**: "Writing and maintaining the machinery that runs the customer tests is something that coding agents can do quickly and cheaply."
- **Our assessment**: Reasonable economic argument; untested at scale. The runner still needs human validation (the Approved Scenarios process has the developer check the runner "against production code").

### Claim 10: Customer tests need not be end-to-end: invoke the service layer, or test an important component directly with its own DSL, and use side channels / internal resources to seed state
- **Evidence**: Insurance claim-to-lawyer matching rules tested at service level; IP-allowlist component with a custom YAML DSL; todo-app with HTML-to-text "printers" and state "parsers"; side-channel executable never shipped to production.
- **Confidence**: emerging
- **Quote**: "Remember that the most important thing about a customer test is that it supports alignment between customers and developers."
- **Our assessment**: Practical guidance for keeping agent feedback loops fast. Printer/parser design (readable, diffable text) is the reusable idea.

### Claim 11: Agents benefit from fast, local, end-to-end feedback; coding agents can generate local simulators ("digital twins") of external services instead of hand-built Wiremock/Mountebank mocks, and the same test data can run against multiple runners
- **Evidence**: Cites Justin McCarthy (digital twins) and Clare Liguori (mock services). Anecdotes about test payment-gateway credit limits and market-hours-only exchange sandboxes.
- **Confidence**: emerging
- **Quote**: "An emerging approach to this solution is to get coding agents to generate local simulators of the external services."
- **Our assessment**: Author labels this "emerging". Test-data portability (in-process runner for speed, out-of-process for realism) is a distinctive benefit of data over code.

### Claim 12: Because AI-written tests still pose a review burden, validate them: mutation testing (check tests detect faults and fail informatively) plus oracles (official docs, brute-force reference implementation, real system) for the correctness of expected values
- **Evidence**: Author's COBOL interpreter work: IBM manuals supplied as oracle; all customer tests required to pass on a real IBM i system as on his laptop. Notes mutation testing "does not protect us against the risk that the tests themselves are specifying something that is not correct".
- **Confidence**: emerging
- **Quote**: "Mutation testing proves that the tests are effective in detecting faults, but it does not protect us against the risk that the tests themselves are specifying something that is not correct."
- **Our assessment**: Good separation of two verification questions (can the tests catch faults? are the tests right?). The COBOL anecdote is single-author evidence. Also recommends property-based testing and agent-driven simulation (games, browser users).

### Claim 13: The technique is for production systems, not prototypes, and is insufficient alone; human exploratory testing is still recommended
- **Evidence**: The article's own "Limits of applicability" section.
- **Confidence**: emerging
- **Quote**: "Prototypes, proofs-of-concepts, experiments can all be generated quickly without too much concern for tests"
- **Our assessment**: The guide should keep the scope: external DSLs add machinery that is only worth it if humans will review at least a sample of the tests; sometimes letting the model write tests freely is cheaper if other validation exists. Also warns that "large steps" make it harder for humans to keep an understanding of system internals.

### Claim 14: Larger-step test-first with agents: tell the agent what you want and how to validate it rather than prescribing process
- **Evidence**: Author's observation, no data; cites that canon TDD is hard to get from agents who write lots of code before tests.
- **Confidence**: anecdotal
- **Quote**: "we could see this as a way to do test-first, with larger steps."
- **Our assessment**: Consistent with Böckeler's finding that process prescriptions (TDD) did not help agents. Both are single-author, unmeasured.

### Claim 15: Max Kanat-Alexander (reported by the author) prefers agents to write tests as code so static-analysis rules can constrain them, a counterpoint to tests-as-data
- **Evidence**: Anecdote about a Bugzilla query-language test (20 operators, 50 fields) that "could not have been written other than as a data structure"; same person normally prefers tests as code.
- **Confidence**: anecdotal
- **Quote**: "However, Max added that he normally prefers to get agents to write tests as code, so that he can impose rules on the tests through static analysis tools."
- **Our assessment**: Shows two protection strategies exist: data files + file protection vs. code + static analysis. Not a full contradiction since both aim to constrain the agent. Not filed as a contradiction issue.

## Concrete Artifacts

Attributed to the source article (Vaccari, 2026-11-11).

Minimal tests-as-data YAML (replaces ~20 lines of Java HTTP boilerplate):

```yaml
suite: greetings
tests:
  - name: "default greeting"
    request:
      resource: "/hello"
      name: null
    greeting: "Hello, world!"
  - name: "personalised greeting"
    request:
      resource: "/hello"
      name: "Joe"
    greeting: "Hello, Joe!"
```

Task-type vs expected-change matrix for protecting files (reconstructed from the article's table):

```
When                         Prod code?  Test data?  Test runner?
Implementing new function    Yes         Yes         No
Refactoring production code  Yes         No          No
Improving test coverage      No          Yes         No
Improving test DSL           No          Yes         Yes
```

Todo-app external-DSL scenario with state "printers" and "parsers":

```
## Unchecking a completed todo reactivates it
GIVEN model:
    [x] buy milk
    [ ] walk the dog
WHEN user:
    click toggle of "buy milk"
THEN page:
    > ""
    [ ] buy milk
    [ ] walk the dog
    -- **2** items left
THEN model:
    [ ] buy milk
    [ ] walk the dog
```

Approved Scenarios bootstrap process (as described by the author):
1. Decide on a DSL format, likely in collaboration with the AI, and write a first test.
2. Have a coding agent generate the DSL parser and test runner.
3. The developer checks that the runner works correctly, by checking it against production code.
4. The coding agent adds scenarios, using the first test as a template.

Enforcement options named: make un-expected files read-only "in a way that the agent cannot bypass", CI check of which files changed per task type, and harness hooks (fast feedback, not bullet-proof).

## Cross-References

- **Corroborates**: `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 5 (test-first did not prevent tautological tests) and Claim 12 (monitor outcomes and give automated feedback rather than over-specify process). Both support Vaccari's view that agents need "how to validate" rather than process instructions. `blog-anthropic-ai-native-sdlc-playbook.md` (around line 319: the agent "must not be able to weaken the check" on code) is consistent with the protected-harness idea; that note has no numbered claim for it, so cite by section/context rather than claim number. `blog-addyosmani-agentic-code-quality.md` Claim 2 (constraints/quality gates including mutation testing) aligns with the validation section.
- **Contradicts**: None found requiring a contradiction issue. Böckeler's Claim 11 recommends "Approved Scenarios" as a TDD alternative, so the two are compatible. Kanat-Alexander's preference for tests-as-code (Claim 15) is a context-conditioned alternative, not a direct opposition.
- **Extends**: `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 11 (names "Approved Scenarios" as one of three alternatives but does not explain it). This note supplies the mechanism: external DSL, mandatory assertions, generated runner, bootstrap process.
- **Novel**: Customer tests as the primary AI contract; tests-as-data as a tamper-visibility mechanism; the task-type vs changed-artifact protection matrix; external DSL with mandatory assertions as an anti-cheating device (Constrained Tests); running the same test data through multiple AI-generated runners (in-process, out-of-process, real legacy system).

## Guide Impact

- **Chapter 03 (Verification)**: Add a subsection on "protected test contracts": keep behavioural specs as human-readable test data (tables/external DSL with mandatory assertions) interpreted by a small runner, and pair with mutation testing (existing section) plus oracles for validating expected values. Present as emerging, single-practitioner, no measured results.
- **Chapter 02 (Harness Engineering)**: Add the task-type vs changed-file matrix as a concrete hook/CI policy example (refactors must not touch test data; coverage work must not touch production code or the runner), with the author's caveat that hooks are not bullet-proof and the runner itself remains an attack surface.
- **Chapter 04 (Context Engineering)**: Minor: customer-language test data doubles as a compact executable spec that can replace long Markdown specs in agent context (Claim 4, Claim 9).
- **Scope caveat**: State the article's limits (production systems only; skip for prototypes; external DSL overhead only justified if humans review a sample of tests; not sufficient without exploratory testing).

## Extraction Notes

- Read the full article (all sections, sidebars, code and table artifacts). Did not open the linked videos (Ördög, Falco/Kesseler, McCarthy, Liguori) or the third-party reports, so statistics and second-hand attributions are marked as reported by the author.
- Quotes were copied from the fetched page text with line-wrap whitespace normalised to single spaces.
- Claim numbers cited from other notes were checked against those notes' numbered headings (TDD note Claims 5, 11, 12; Addy Osmani code-quality Claim 2).
