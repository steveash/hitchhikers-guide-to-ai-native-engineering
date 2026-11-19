---
source_url: https://martinfowler.com/articles/data-contracts.html
source_type: blog-post
title: "Data Contracts"
author: Simon Harrer (Entropy Data; ODCS/ODPS technical steering committee) and Arif Wider (HTW Berlin professor; Thoughtworks fellow consultant)
date_published: 2026-11-18
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4828"
---

# Data Contracts

> A spec-level treatment of the Open Data Contract Standard (ODCS 3.2) as a machine-readable, verifiable, versioned interface for datasets, including an agent-specific `context` block and a CI/CD enforcement pipeline (lint, breaking-change check, test against data) that turns a contract from a "paper tiger" into a control.

## Source Context

- **Type**: blog-post (martinfowler.com article, published 18 November 2026; martinfowler.com is a trusted feed)
- **Author credibility**: Simon Harrer is co-founder/CEO of Entropy Data (a data marketplace vendor) and a member of the ODCS/ODPS technical steering committee at the Bitol project (Linux Foundation); co-author of the retired Data Contract Specification. Arif Wider is a professor at HTW Berlin and Thoughtworks fellow consultant, long-time data mesh author. Both are standard authors/vendors with a stake in ODCS adoption, so the "will be everywhere" argument is advocacy. The article discloses AI assistance for outlining and polishing.
- **Scope**: What a data contract is, ODCS 3.2 sections with YAML snippets, linkage to ontologies/data products/marketplaces, contract-first vs data-first, SemVer and lifecycle, CI/CD automation with Data Contract CLI, and costs/benefits. Prescriptive synthesis: **no measured outcomes, benchmarks, or failure data**. The vendor-adjacent material (Entropy Data, marketplace) is context only.

## Extracted Claims

### Claim 1: Agents lack a human's hesitation about untrusted data, so a data contract must supply the metadata they would otherwise have to guess
- **Evidence**: Argument by analogy (the "Alex" data-engineer persona replaced by an agent); leans on Sadalage/Chandrasekaran for the premise. No data.
- **Confidence**: anecdotal (reasoned assertion, no measurement)
- **Quote**: "A human who distrusts data hesitates, or asks the people who own it. An agent does neither"
- **Our assessment**: Restates the premise of `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 1 rather than adding evidence (the triage flagged this). The useful addition is the enumerated list of what a contract answers: discoverability, schema/semantics, quality/SLA (how far to trust), terms of use (what is allowed).

### Claim 2: A data contract is defined by six properties: machine-readable, verifiable, versioned, provider-driven, consumer-oriented, source of truth for metadata
- **Evidence**: Definitional list in "What's in a Data Contract".
- **Confidence**: emerging
- **Quote**: "A quality rule such as “less than 1% empty names” is not an aspiration but an assertion that tooling can evaluate and either pass or fail."
- **Our assessment**: A crisp checklist for any agent-facing metadata artifact: if a "contract" is prose or unverifiable, it is documentation, not a control. Applicable beyond data (cf. AGENTS.md-style guidance, which is typically neither verifiable nor versioned).

### Claim 3: A contract that nobody checks is a "paper tiger"; value comes from automation, and the source lists nine concrete automations
- **Evidence**: Bulleted list in "Automate All The Things" (docs generation, marketplace publish, PR-time tests, daily prod tests, DDL generation, masking/access-policy derivation from `pii:true` tags, tolerant-reader SQL generation, breaking-change diff in PRs, quarantine validation) plus a tool (Data Contract CLI, "over 1 million downloads per month", Radar "Trial").
- **Confidence**: emerging (concrete tooling exists; effectiveness not measured)
- **Quote**: "A data contract that nobody checks is a paper tiger: its promises are worth no more than a wiki page, and the first time a consumer finds one broken, their trust is gone."
- **Our assessment**: Strongly parallels the guide's verification theme (a declared rule only matters when enforced mechanically). Download figures are self-reported by an author with a stake.

### Claim 4: Contracts belong in CI/CD with a staged pipeline (lint, breaking, ci/test, publish) plus a nightly scheduled test against production
- **Evidence**: Named CLI commands and Figure 6 description.
- **Confidence**: emerging
- **Quote**: "datacontract lint validates the contract, datacontract breaking catches breaking changes against the previous version, and datacontract ci tests the data against the contract in each environment."
- **Our assessment**: A concrete template for gating data-facing agent work: PR-time gate on contract + data, then continuous production monitoring that notifies owners and downstream consumers. Distinguishes pre-merge from runtime verification.

### Claim 5: Testing datasets differs from testing code: you cannot choose the inputs, so assumptions about data must be tested continuously as characteristics (row count, null rate, freshness)
- **Evidence**: Sidebar "Testing Datasets vs Testing Code"; contract checks absorb what Great Expectations-style tools did, and those tools read the checks from the contract.
- **Confidence**: emerging
- **Quote**: "When testing code, we choose the inputs and check the outputs. When consuming data, we can't choose the inputs"
- **Our assessment**: Useful framing for verification of agent systems reading external/untrusted inputs: the check surface is the input's properties, not just outputs.

### Claim 6: The ODCS 3.2 `context` ("AI context") block (instructions, constraints, verifiedStatements) is dataset-level guidance written for agents
- **Evidence**: YAML example (see Concrete Artifacts); ODCS 3.2 added it in 2026 per the origin sidebar.
- **Confidence**: emerging (a published standard feature; no evidence yet on agent adherence)
- **Quote**: "The instructions act like a system prompt for the dataset, for example telling an agent that premiums are stored in cents."
- **Our assessment**: Differs from CLAUDE.md/system-prompt context in being attached to the data asset itself, versioned with its schema, and consumed by any agent that discovers the dataset. Note `constraints` are advisory text; the article does not say they are enforced (enforcement lives in roles/access agreements). `verifiedStatements` (question + provider-checked SQL) is a notable pattern: reusable vetted answers instead of fresh generation.

### Claim 7: Verified statements let an agent reuse a provider-checked query instead of guessing one
- **Evidence**: YAML example pairing "How many active customers do we have?" with SQL.
- **Confidence**: anecdotal (single illustrative example)
- **Quote**: "so an agent can reuse a correct answer instead of guessing one."
- **Our assessment**: Akin to few-shot golden queries / a semantic layer; corroborates the text-to-SQL accuracy argument in the Sadalage/Chandrasekaran note (Claim 12) though this article gives no numbers.

### Claim 8: SemVer plus lifecycle status makes breaking changes detectable before consumers or agents are affected; breaking changes ship as a new major version alongside the old one
- **Evidence**: Rules stated: major = remove/rename column; minor = add column; patch = typo/support-channel fix; status draft/active/deprecated/retired; major version in filename but not ID; schema-registry compatibility mapping, with a warning that the registry default (backward compatibility) permits deleting a field.
- **Confidence**: emerging (borrowed from API practice, well established there)
- **Quote**: "One of the main goals of data contracts is to find breaking changes before consumers are affected, and offer graceful evolution processes."
- **Our assessment**: The CI check "fail if there is a breaking change for only a minor or patch version update" is a directly mechanical drift guard. Treating column addition as non-breaking depends on consumers avoiding `SELECT *` (tolerant reader), which the article states explicitly.

### Claim 9: Once published, the contract is the source of truth and data must follow it; a column rename fails the contract test rather than regenerating the contract
- **Evidence**: Data-first vs contract-first section; Data Contract CLI can bootstrap a first draft from DDL/JSON Schema/Avro.
- **Confidence**: emerging
- **Quote**: "The contract test fails instead, and the rename has to be handled as what it is: a breaking change."
- **Our assessment**: Same direction-of-authority principle as spec-driven development: generation is a starting point, then the spec leads. Anyone letting an agent regenerate the spec from drifted output defeats the control.

### Claim 10: Data contracts enable spec-driven pipeline generation, with contract tests as the agent's feedback loop
- **Evidence**: Described in "Generate Your Data Pipeline" with a coding agent, company skills plugin, and a demo run on dataproduct.com (not independently checked).
- **Confidence**: anecdotal (no metrics; "almost the entire data pipeline" is unquantified)
- **Quote**: "During the generation of the data pipeline, the data can be tested against the contract, acting as a feedback loop, steering the agent in the right direction."
- **Our assessment**: Plausible and consistent with test-as-feedback-loop patterns; treat the "almost entire pipeline" claim as marketing-adjacent given the author's vendor role.

### Claim 11: Agents take prose fields "at their word", which makes metadata quality pay back and changes the incentive for documenting data well
- **Evidence**: Argument in "In the Age of Agents, the Incentive Points the Right Way"; no data.
- **Confidence**: anecdotal
- **Quote**: "An agent takes those prose fields at their word and acts on them."
- **Our assessment**: Interesting claim that agent consumption creates a feedback loop (ask, see wrong answer, fix description, ask again) which improves documentation. Plausible and observed informally elsewhere, but unsupported here by measurement. Also a risk: the article's own Cost section notes an agent acts on an outdated contract as confidently as on a correct one.

### Claim 12: Access should be granted via an access agreement (contract + stated purpose + consumer), short-lived for agents, distinct from the provider-published contract
- **Evidence**: Marketplace section, Figure 5; Bitol RFC for an Open Access Agreement Standard (OAAS) is in progress, no standard yet.
- **Confidence**: emerging (concept; standard does not yet exist per the article)
- **Quote**: "for AI agents, the granted access period can be as short as a few minutes."
- **Our assessment**: Maps to just-in-time, purpose-bound credentials (cf. Sadalage/Chandrasekaran Claim 10). Note terms of use and `context.constraints` are text; enforcement is via roles and access approval.

### Claim 13: Do not roll contracts out everywhere; start where it hurts and focus on team-to-team interfaces
- **Evidence**: Cost section; organizational advice (platform templates, consumer workshops, show reliability in the marketplace, clear alert ownership).
- **Confidence**: anecdotal (experience-based advice)
- **Quote**: "That's why you should not introduce data contracts for all the data in your company."
- **Our assessment**: Honest cost acknowledgment and an adoption heuristic that transfers to agent guardrails generally: verification overhead should target high-stakes interfaces.

### Claim 14: An open, vendor-neutral standard protects metadata sovereignty as agents become the primary metadata consumers
- **Evidence**: Argument; ODCS under Linux Foundation; lock-in test "can you export all your contracts as plain files into git and rebuild your catalog elsewhere from them alone?"
- **Confidence**: anecdotal (opinion; authors have a commercial interest in ODCS)
- **Quote**: "whoever controls its format controls access to your enterprise data."
- **Our assessment**: Reasonable portability argument; weigh against author incentives.

## Concrete Artifacts

Quality rule and freshness SLA (ODCS 3.2, from "A Simple Example Data Contract"):

```yaml
schema:
  - name: "customers"
    properties:
      - name: "customer_name"
        quality:
          - type: "sql"
            description: "Expect less than 1% empty name fields"
            query: |
              SELECT AVG(
                CASE
                  WHEN customer_name IS NULL
                    OR TRIM(customer_name) = ''
                  THEN 1
                  ELSE 0
                END
              )
              FROM customers
            mustBeLessThan: 0.01
slaProperties:
  - property: "freshness"
    value: 24
    unit: "hours"
    element: "customers.last_updated_at"
    description: "Within 24 hours of the last update"
```

AI context block (from "AI Context" section):

```yaml
context:
  instructions: >
    Use this data for analytics on life insurance customers.
    Annual premiums are stored in cents; divide by 100 before
    reporting amounts.
  constraints:
    - constraint: >
        Do not use this data to make decisions about individual
        customers, such as pricing a policy or assessing a claim.
  verifiedStatements:
    - question: "How many active customers do we have?"
      answer: |
        SELECT COUNT(*)
        FROM customers
        WHERE customer_status = 'active'
```

Repository layout (from "Its Natural Habitat is a Git Repository"):

```
customers.odps.yaml
|- datacontracts
   |- customers_pii_snowflake_v1.odcs.yaml
   |- customers_pii_snowflake_v2.odcs.yaml
   |- customers_npii_snowflake_v1.odcs.yaml
|- code
   |- pipeline.sql
.gitlab-ci.yml
```

CI stages (Data Contract CLI, from "Data Contracts Belong in Your CI/CD Pipeline"): `datacontract lint` → `datacontract breaking` → `datacontract ci` → `datacontract publish`; nightly: `datacontract test --server prod` on a cron.

## Cross-References

- **Corroborates**: `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 1 (agents lack human judgment about data trust), Claim 3 (ODCS contracts with quality rules and freshness SLAs), and Claim 4 (contract-validation quarantine; this article lists it as one automation). `blog-thoughtworks-birari-ai-readiness-data-ownership.md` Claim 5 (agents need context via metadata, interfaces and quality checks) and Claim 7 (policy-as-code / computational governance).
- **Contradicts**: None found. No filed contradiction issue.
- **Extends**: `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 3 with the full ODCS 3.2 structure, the AI `context` block, SemVer/lifecycle rules, the CI/CD stage commands, and access agreements. Adds a detail the earlier note does not have: the earlier freshness-anchor advice (last successful load) differs in example only; here the SLA is keyed to `customers.last_updated_at`, a change-time column, which the earlier note's Claim 3 warns can mask a stalled pipeline. This is a tension in examples, not a filed contradiction, since this article does not argue for change-time anchoring.
- **Novel**: The `context.instructions/constraints/verifiedStatements` agent-guidance pattern; breaking-change diff gating by SemVer level in PRs; consumer-driven data contracts (consumers publish expectations in the same format, enabling agent-driven matching); access agreements with minutes-long grants for agents.

## Guide Impact

- **Chapter 03 (verification)**: Add data contracts as an example of a declarative, machine-checkable control: quality rules and SLAs as pass/fail assertions, run at PR time (`lint`/`breaking`/`ci`) and nightly in production. Cite Claims 3, 4, 8 of this note. Keep at "recommended practice" confidence; no measured outcomes.
- **Chapter 04 (context engineering)**: Cite the ODCS `context` block (Claim 6) as an example of dataset-attached, versioned agent context that differs from repo-level CLAUDE.md, and `verifiedStatements` as vetted-answer context. Caveat that constraints are advisory text unless backed by roles/access control.
- **Chapter 03 / spec-driven material**: Claim 9 (contract is source of truth; drift fails the test rather than regenerating the spec) supports the direction-of-authority principle.

## Extraction Notes

- Read the full article (all sections and sidebars, fetched from the source HTML) and compared against the existing Fowler/Sadalage note. Quotes were copied from the fetched text; curly quotes in the source were preserved.
- Linked pages (datacontract.com walkthrough, dataproduct.com demo, Technology Radar) were not followed; claims about them are the article's own.
- The article contains no metrics, benchmarks, or failure reports; all confidence ratings reflect that. Authors have commercial interests (Entropy Data marketplace, ODCS governance).
