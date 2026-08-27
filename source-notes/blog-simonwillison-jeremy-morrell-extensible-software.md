---
source_url: https://simonwillison.net/2026/Aug/19/jeremy-morrell/
source_type: blog-post
title: "A quote from Jeremy Morrell — Extensible Software in the age of LLMs"
author: Jeremy Morrell (quoted by Simon Willison)
date_published: 2026-08-19
date_extracted: 2026-08-27
last_checked: 2026-08-27
status: current
confidence_overall: emerging
issue: "#2990"
---

# A quote from Jeremy Morrell — Extensible Software in the age of LLMs

> Simon Willison's link-blog quote of Cloudflare engineer Jeremy Morrell's essay
> "Extensible Software in the age of LLMs" (followed as a linked page per
> MINER.md §1) — a full architectural thesis arguing that LLMs collapse the
> cost of *authoring* user-facing extensions while modern sandbox primitives
> collapse the cost of *deploying* them safely, letting a "solid, accountable
> core" app extend itself in many directions via an object-capability model
> instead of leaking credentials through proxies, with Salesforce's 19-year-old
> Apex platform as historical precedent and Cloudflare's Dynamic Workers as the
> author's proposed (and disclosed-conflict-of-interest) production reference
> implementation.

## Source Context

- **Type**: blog-post (Simon Willison link-blog quotation entry, published
  19th August 2026, linking to Jeremy Morrell's essay "Extensible Software in
  the age of LLMs" on jeremymorrell.dev, published 18th August 2026). Per
  MINER.md §1, the linked Morrell essay was fetched and read in full — it is
  the substantive source; the Willison page is a three-sentence quotation
  (the essay's own thesis paragraph) plus tags and a one-sentence
  characterization. This mirrors the precedent set by
  `blog-simonwillison-akshat-bubna-quote.md`, where the source_url stays the
  simonwillison.net entry point but the deep extraction follows a linked
  primary source.
- **Author credibility**: Jeremy Morrell works at Cloudflare and explicitly
  discloses this: "Disclosure: I currently work at Cloudflare, where high
  levels of exposure to Kenton Varda’s writing have shaped much of my thinking
  here." Kenton Varda (Cap'n Proto creator, Cloudflare capability-security
  practitioner) is an independently-verified named practitioner already in
  this corpus (`blog-simonwillison-kenton-varda-change-descriptions.md`),
  which raises Morrell's credibility on capability-security specifics — this
  is not a random blogger's take, it channels a documented Cloudflare
  capability-security lineage. The disclosed conflict of interest means the
  essay's conclusion (Cloudflare's Dynamic Workers as the best-fit technology)
  should be read as an informed practitioner's argued recommendation, not a
  neutral technology survey — the essay itself surveys five alternative
  approaches before reaching that conclusion, which partially mitigates this.
- **Scope**: Covers: the case for web-native software extensibility via LLMs,
  four concrete extension-point domains (AI agents, internal corporate
  platforms, support tooling, observability tooling), an enumerated list of
  security/abuse risks from running arbitrary user code, Salesforce Apex as a
  19-year precedent, five technical requirements for a safe extension
  primitive, a critique of credential-proxy patterns in favor of an
  object-capability model, a survey of five isolation technologies
  (interpreters, V8 isolates, microVMs, WASM+WASI, and combinations), and
  Cloudflare Dynamic Workers as the author's proposed production fit. Does
  NOT cover: a working multi-tenant implementation the reader can inspect
  end-to-end (the post links to a separate, non-fetched companion guide,
  "Working with Dynamic Workers," and an embedded interactive demo widget
  that could not be evaluated via static fetch), independent benchmarks of
  Dynamic Workers cold-start latency or cost, or a security audit of the
  object-capability pattern in production.

## Extracted Claims

### Claim 1: LLMs radically lower the cost of *authoring* software extensions while modern sandbox primitives lower the cost of *deploying* them safely, enabling apps to be built as a "solid, accountable core" that users safely extend by having LLMs fill in the missing pieces
- **Evidence**: The essay's stated central hypothesis, positioned as the thesis paragraph and reproduced verbatim as the Willison quote.
- **Confidence**: emerging (explicitly framed by the author as "my hypothesis," not a settled industry consensus; supported later in the essay by a historical precedent (Salesforce) and a named production platform (Cloudflare Dynamic Workers), but the overall claim — that this is a *new* opportunity now available — is forward-looking)
- **Quote**: "My hypothesis is that there is a new opportunity for Extensible Software on the web. LLMs radically lower the cost of authoring extensions, and modern sandbox primitives lower the deployment cost and provide good security boundaries. We can build our app as a solid, accountable core, and allow users to safely extend it in many directions by having LLMs fill in the missing pieces. We can give our users super powers."
- **Our assessment**: This is a clean two-factor model (authoring cost via LLMs, deployment/security cost via sandboxes) that is genuinely distinct from the corpus's existing plugin-extensibility coverage (Datasette Agent) and infrastructure-sandboxing coverage (Claude Managed Agents, How We Contain Claude) — those sources each cover one half of the equation; Morrell explicitly frames the *conjunction* of both as what makes the opportunity new. Worth noting for the guide: this is a claim about a cost-structure shift, not a claim that either technology (LLM code generation, sandbox primitives) is individually novel.

### Claim 2: Most web software is static because developers have limited time and attention and build for the largest user segment, leaving a long tail of unmet needs that differs for every user
- **Evidence**: Author's framing argument, illustrated with a linked third-party chart (a Google Maps long-tail-of-user-needs diagram credited to @tophtucker) and a linked essay ("Even if the developers were incredibly motivated to shove in every feature, user interfaces can only become so complex before they become unusable").
- **Confidence**: emerging (a widely-observed pattern in product design — feature bloat vs. long-tail needs — illustrated with one external chart, not the author's own data)
- **Quote**: "Most of the web software we interact with today is static. The developers have a limited amount of time and attention, and focus on building the features that serve the largest group of users. The top of the demand curve is well-served by existing software, but there is a long-tail of unmet needs that’s different for every user."
- **Our assessment**: This is the motivating problem statement for the whole essay, not itself a novel claim — the "long tail of unmet needs" framing is a standard product-design observation. Its value for the guide is as context for *why* extensibility matters as a design goal, not as an evidenced result on its own.

### Claim 3: LLMs have made it possible for non-developers to "speak code into existence" — Pi is offered as an example of "LLM-native software": a battle-tested core that is endlessly extensible just by asking, with users able to share their customizations
- **Evidence**: Author's characterization of Pi (pi.dev) as a working example, plus a linked meme illustrating the interaction pattern ("Add my custom feature" → "Adds feature").
- **Confidence**: anecdotal (single example product cited; no independent verification of Pi's extension mechanism or usage data)
- **Quote**: "In the past year your users have suddenly acquired the ability to speak code into existence. Most existing software can’t leverage this. Pi leans into it."
- **Our assessment**: "LLM-native software" is a useful naming for a pattern the guide should track: software designed from the ground up around the assumption that users can generate small pieces of custom logic via natural language. This is architecturally distinct from a chatbot bolted onto existing software — the claim is that the *extension surface itself* (stable hooks for tools, commands, events, UI) is the product design choice that makes this work, illustrated later for deepseek and opencode (see Concrete Artifacts).

### Claim 4: Existing examples of pluggable, self-extending software are almost all local software (AI agent harnesses, IDEs, video game mods, Blender add-ons, CAD extensions) with a high barrier to entry — despite the web being "the most successful software distribution system in the world," it lacks comparable extensibility
- **Evidence**: Author's direct observation contrasting local-software extensibility precedent against the web's comparative extensibility gap.
- **Confidence**: emerging (a defensible historical observation about software distribution patterns, not empirically measured, but consistent with well-known examples the author names)
- **Quote**: "However most of our existing examples of pluggable software are local software: AI agents, developer IDEs, mods for video games, Blender add-ons, CAD extensions. These tend to be professional tools with a high barrier to entry." / "The web is the most successful software distribution system in the world. It shouldn’t be left behind."
- **Our assessment**: This framing is the "why the web specifically, why now" argument — it positions the LLM+sandbox combination as closing a distribution-vs-extensibility gap that has existed since local software first got extension ecosystems. This is a useful framing device for the guide but is an argued position, not a benchmarked claim.

### Claim 5: Current AI-agent extension models create a governance gap — Pi extensions run with the same permissions as Pi itself unless the user sandboxes it themselves, and organizations experimenting with letting employees "vibe code" their own internal tooling hit unresolved problems around data access scoping, credential leakage, and auditability at scale
- **Evidence**: Author's direct assessment of the current state of AI-agent extensibility (naming pi, deepseek, opencode as examples experimenting in the space) plus an enumerated list of open governance questions for internal corporate platforms.
- **Confidence**: emerging (a specific, checkable technical claim about Pi's permission model stated as fact by the author, combined with a reasoned — not case-study-backed — list of governance risks for internal platforms)
- **Quote**: "Unless you sandbox Pi yourself, Pi extensions run with the same permissions as Pi itself." / "Once you have hundreds or thousands of these apps, how do you maintain them? How do they get access to the data that they need? How do they get access to only the data that they need? How can we audit what this software is doing? If we’re relying on access tokens, what are their scopes? Who rotates them? How do we make sure that we’re not logging out customer information to a third-party? How do we make sure we’re not violating GDPR?"
- **Our assessment**: This is the sharpest concrete risk claim in the essay for a security-conscious guide chapter — it names a specific, current gap (ambient-permission extensions in a shipping agent product) rather than a hypothetical. It sets up the rest of the essay's argument that sandboxing + capability scoping (Claims 8–10) is the fix for exactly this gap. Compare against `blog-anthropic-how-contain-claude.md`, whose containment architecture is presented as an existence proof that this gap is solvable at scale by a first-party agent vendor.

### Claim 6: Executing arbitrary user code creates a specific, enumerable set of abuse and security risks — service-availability risk, credential/data exfiltration, denial-of-service (both by and against the user), Spectre-class speculative-execution attacks, and free-compute cryptomining abuse
- **Evidence**: Author's enumerated "incomplete list" of security challenges, presented as baseline requirements any extensibility platform must address.
- **Confidence**: settled (a well-established, uncontroversial list of security engineering concerns for multi-tenant code execution; each item names a well-documented attack class)
- **Quote**: "Executing arbitrary code is rife with security and abuse challenges. An incomplete list: Errors or infinite loops in the user’s code should never take down your service / With access to keys, customer extensions can forward them to a third party / Likewise if you expose sensitive data, make sure it can’t be exfiltrated / Make sure this system can’t be abused to do a Denial of Service attack / Make sure the user can’t accidentally Denial of Service you / Protect against Spectre attacks / If people can use free compute to mine crypto on your dime, they will / and many more…"
- **Our assessment**: This is a useful checklist artifact for a guide security-threat-model chapter — it's specific enough to serve as a starting audit list for any team evaluating an extension/plugin execution model, distinct from generic "be careful with user code" advice.

### Claim 7: Salesforce has run safe, large-scale multi-tenant user code execution since 2007 (predating AWS S3/EC2, launched 2006) via its Apex language, and is more accurately described as a "massive multi-tenant programmable platform" than as a CRM
- **Evidence**: Author's historical claim, with a linked citation (eweek.com article on the Salesforce Summer '07 Apex Code release) and a comparative date reference to AWS's 2006 launch (linked to Wikipedia's AWS timeline).
- **Confidence**: settled (a checkable historical fact with a cited source; the "more accurate to describe... as a platform" framing is the author's interpretive claim, which is reasonable given Salesforce's documented Apex/multi-tenant architecture)
- **Quote**: "Yes, that Salesforce. And they’ve been doing it since 2007. (As a point of reference, AWS S3 and EC2 were launched in 2006.)" / "However it’s more accurate to describe Salesforce as a massive multi-tenant programmable platform."
- **Our assessment**: This is the essay's strongest piece of evidence that safe extensibility-via-user-code is not a hypothetical — it is a load-bearing existence proof spanning nearly two decades at enterprise scale, which meaningfully strengthens Claim 1's "new opportunity" framing (the *opportunity* is new because LLMs+sandboxes make it cheap, not because the underlying pattern is unproven). Useful historical anchor for a guide chapter arguing that extensibility-via-sandboxed-user-code is a mature, not speculative, architecture.

### Claim 8: A safe code-execution primitive for user extensions needs five properties — near-zero idle cost with tiny-fraction-of-a-penny execution cost, cold starts measured in single-digit milliseconds, fine-grained control over resource limits (CPU, memory, network, log volume), a solid fault- and security-isolation boundary between tenants, and a controlled (non-ambient) way for code to take actions
- **Evidence**: Author's own enumerated technical requirements, each given its own subsection with reasoning (e.g., an illustrated "infinite print loop" failure scenario for the resource-limits requirement).
- **Confidence**: emerging (a reasoned technical requirements list from a practitioner, not independently validated against production incident data, though individually each requirement matches well-known distributed-systems and sandboxing concerns)
- **Quote**: "It needs to cost ~$0 when it’s not being executed, and each execution ideally needs to be tiny-fractions-of-a-penny cheap." / "Ideally a cold start is measured in single-digit milliseconds." / "To protect your system you need to be able to enforce limits on basically everything: CPU, memory, number and size of network requests, response size, log volume and rate, and much more." / "No matter what the user does: crashes, runs an infinite loop, allocates memory as fast as possible, it should have no effect on any other user."
- **Our assessment**: This requirements list functions as a practical evaluation rubric for any team choosing an extension-execution technology — the guide could adopt it near-verbatim as a checklist. It is consistent with (and less detailed than) the concrete gVisor flag recipe (`--network=none --cap-drop=ALL --memory=64m --cpus=0.1`) documented in `blog-google-adk-zero-trust-agents.md` Claim 7, which independently arrives at the same isolation/resource-limit requirements for LLM-generated code specifically.

### Claim 9: The common credential-proxy pattern (giving untrusted code an opaque token that a proxy swaps for the real API key, then filters requests against an allowlist) is strictly better than raw credential exposure but becomes fragile — the filtering logic must anticipate every possible misuse and stay in sync as the backing API evolves, and testing it thoroughly is hard
- **Evidence**: Author's worked example — a ~15-line TypeScript `proxyFetch` function that validates a grant, checks the destination origin/path, and forwards only an explicit header allowlist before injecting the real credential — presented as illustrative of the complexity this pattern requires even for a single operation on a single endpoint.
- **Confidence**: emerging (a reasoned architectural critique illustrated with a concrete code example, not a report of a specific proxy-pattern failure incident)
- **Quote**: "You can try to enforce that in a proxy, but now you are tasked with filtering out all requests that don’t match some narrow set of criteria, and keeping that up-to-date as the backing API evolves. Our proxy code quickly becomes very complicated. It’s difficult to anticipate everything a user might do here. Testing this logic and making sure it’s bulletproof is challenging." / "And this is the filtering logic for just one operation on just one endpoint. In general, starting with a lot of power and then trying to restrict it precisely is a hard problem."
- **Our assessment**: This is a specific, well-argued critique of a pattern the guide's harness-engineering material likely already documents in some form (proxying credentials to scope tool access). The insight — that proxy-based scoping is a *subtractive* security model (start with full power, try to filter it down) rather than an *additive* one — is the setup for Claim 10's alternative.

### Claim 10: A narrow object-capability model — handing untrusted extension code a reference to a specific pre-scoped function (a "capability") rather than a raw credential or proxied token — removes ambient I/O entirely, so the code can only take actions via the exact references it was passed, is easier to reason about than proxy filtering, never exposes the underlying credential to untrusted code, and is more token-efficient for an LLM to generate against than a full OpenAPI spec
- **Evidence**: Author's worked TypeScript example contrasting trusted host code (`const getApprovedEmail = () => fetchEmailById(123, auth)`) passed as a capability into untrusted extension code, plus a comparison to IFTTT's action-specific API design (`twitter.post_new_tweet()` rather than a raw Twitter API key) and a link to the Wikipedia object-capability-model article.
- **Confidence**: emerging (the object-capability model itself is an established, decades-old security-engineering pattern — the Wikipedia citation reflects this — but the specific claim that it is *the* right shape for LLM-authored extensions, and the token-efficiency claim for LLM code generation specifically, are the author's own argued position, not independently benchmarked)
- **Quote**: "If we remove ambient I/O, the code can only take actions via the references it has been passed. This pattern is much easier to reason about. We don’t have to muck around with complicated proxy logic. The API credential is never exposed to the untrusted code at all. And without some other outbound capability, there’s no way to leak data." / "As a bonus, generating logic from a TypeScript definition of capabilities is much easier and token-efficient for an LLM than handing it a pile of OpenAPI JSON definitions." / "If you are familiar with IFTTT, it doesn’t give you a Twitter API key, it gives you twitter.post_new_tweet(). You don’t get a full email client, you get email.send_me_email."
- **Our assessment**: This is the single most guide-actionable architectural claim in the essay — a concrete, code-level pattern for scoping what LLM-generated extension code can do, distinct from (and complementary to) the sandbox-isolation claims elsewhere in the corpus. The token-efficiency-for-LLM-codegen claim is genuinely novel to this corpus: no existing source note frames "expose a narrow capability surface" as also being the *cheaper-to-generate-against* choice for an LLM specifically, versus a full API spec.

### Claim 11: Five isolation-technology families can serve as the sandboxing primitive for extensible software — off-the-shelf embeddable interpreters (Lua, QuickJS), V8 isolates (Cloudflare Dynamic Workers, isolated-vm, Rivet secure-exec), microVMs (Firecracker, libkrun, AWS Lambda MicroVMs, Deno sandbox), and WASM+WASI — and these are not mutually exclusive (e.g., WASM can run inside a V8 isolate or a microVM)
- **Evidence**: Author's technology survey with named production examples for each category, explicitly noting composability between categories.
- **Confidence**: settled (a factual, checkable survey of existing named technologies and their current production users/maintainers, not a claim requiring independent validation)
- **Quote**: "You can also run WebAssembly within a V8 isolate or microVM. None of these options are mutually exclusive." / "Jumping straight to V8 saves you the time. Google has dumped enormous amounts of money and developer time into hardening the V8 JavaScript engine. Cloudflare uses v8 isolates as its isolation boundary for Workers, but it’s not the only option in this space."
- **Our assessment**: This survey is useful as a reference map for the guide's harness-engineering material when discussing sandbox technology choices — it is current as of August 2026 and names specific maintained projects (not just categories), which makes it verifiable and citable. WASM+WASI is specifically flagged as attractive from a security perspective because it "starts out with a blank slate" with no built-in I/O modules — this is a distinct rationale from the V8-isolate rationale (battle-tested hardening) and the microVM rationale (POSIX + full-OS capability), useful for a guide comparison table.

### Claim 12: Cloudflare's Dynamic Workers are, as of 2026, the closest thing to a production-ready out-of-the-box framework for building extensible web apps that the author has found, because they combine V8-isolate-based execution with runtime-integrated OpenTelemetry tracing, per-user multi-tenant storage (Durable Object facets, R2 buckets), durable/long-running workflow execution, built-in source control, and hosted LLM access with token budgets — features a team would otherwise have to build themselves on other isolation primitives
- **Evidence**: Author's direct assessment (disclosed Cloudflare employee) with linked citations for each named feature (Workers tracing beta announcement, Durable Object facets blog post, Workers for Platforms docs, Dynamic Workflows blog post, Cloudflare Artifacts product page, Workers AI product page).
- **Confidence**: anecdotal (a Cloudflare employee's assessment of his own employer's product as best-fit, explicitly disclosed as a conflict of interest by the author himself; each individual feature claim is independently checkable via the linked first-party Cloudflare documentation, but the comparative "closest to production-ready" judgment against alternatives is the author's own, not independently benchmarked)
- **Quote**: "Beyond meeting the criteria I proposed above, they are the closest thing to a production-ready out-of-the-box framework for building extensible web apps that I’ve been able to find in 2026. (But I bet there will be more soon)"
- **Our assessment**: Given the disclosed conflict of interest, this claim should be cited in the guide as "one credible but conflicted practitioner's product recommendation, argued from an explicit requirements list" rather than as a neutral technology endorsement. The requirements list itself (Claim 8) and the object-capability argument (Claim 10) stand independently of whether Dynamic Workers specifically is the right implementation choice for a given team.

### Claim 13: Building a self-extensible platform is genuinely hard — hard to design, hard to run, hard to debug, and requires substantial upfront API design and long-term support commitment — but the author judges it worthwhile because of the surprising creativity it unlocks from users
- **Evidence**: Author's closing personal reflection, drawing on "almost a decade" of platform-engineering experience (unspecified companies/roles).
- **Confidence**: anecdotal (a practitioner's summary opinion, not a specific case study or measured outcome)
- **Quote**: "I’ve worked at platforms for almost a decade. I don’t mean to make “turn your app into a platform” sound easy. Platforms are hard: hard to design, hard to run, hard to debug." / "But they are also really fun, both as a user and a creator. You can be truly surprised by the creativity of your users as they do things that you never considered or would have even thought possible." / "Platforms are hard, but it’s worth it."
- **Our assessment**: A useful, appropriately-hedged closing caveat for the guide — it should accompany any recommendation to adopt the extensibility patterns in Claims 8–10, so the guide doesn't present "add an LLM-authored extension surface" as a low-effort win. This is consistent with the corpus's general pattern that infrastructure-heavy patterns (see `blog-anthropic-claude-managed-agents.md`'s build-vs-buy framing) carry real engineering cost regardless of how cheap LLM-authored extensions themselves become.

## Concrete Artifacts

### Security/abuse checklist for arbitrary user-code execution (verbatim, from jeremymorrell.dev)
```
- Errors or infinite loops in the user’s code should never take down your service
- With access to keys, customer extensions can forward them to a third party
- Likewise if you expose sensitive data, make sure it can’t be exfiltrated
- Make sure this system can’t be abused to do a Denial of Service attack
- Make sure the user can’t accidentally Denial of Service you
- Protect against Spectre attacks
- If people can use free compute to mine crypto on your dime, they will
- and many more…
```

### Object-capability pattern for untrusted extension code (verbatim TypeScript, from jeremymorrell.dev)
```typescript
// Trusted host code
const getApprovedEmail = () => fetchEmailById(123, auth);

// Untrusted extension code
export default async function doSomethingWithAnEmail(
  { getApprovedEmail }: Capabilities,
) {
  const email = await getApprovedEmail();
  // do something with the email
}
```
Contrast with the credential-proxy pattern the author presents as the fragile
alternative — a ~15-line `proxyFetch` function that must parse an opaque
token, validate a "grant," check the destination origin and path against an
allowlist, and forward only an explicit header allowlist before injecting the
real `Authorization` header. (Full snippet in the source article; omitted
here as it demonstrates fragility rather than a pattern to adopt.)

### Salesforce Apex vs. Cloudflare Workers HTTP endpoint comparison (verbatim code-tab pairing, from jeremymorrell.dev)
```apex
@RestResource(urlMapping='/customer-health')
global with sharing class CustomerHealthApi {
    @HttpGet
    global static Account getCustomer() {
        String accountId =
            RestContext.request.params.get('accountId');

        return [
            SELECT Id, Name, Health_Score__c, Renewal_Date__c
            FROM Account
            WHERE Id = :accountId
            WITH USER_MODE
            LIMIT 1
        ];
    }
}
```
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const accountId = new URL(request.url).searchParams.get("accountId");
    const account = await env.ACCOUNTS.prepare(`
      SELECT id, name, health_score, renewal_date
      FROM accounts
      WHERE id = ?
      LIMIT 1
    `)
      .bind(accountId)
      .first();
    return Response.json(account);
  },
} satisfies ExportedHandler<Env>;
```
Author's point: modern serverless platforms are, structurally, a "precursor"
to what Salesforce built from scratch in 2007 — routing, auth, tenant
isolation, and execution handled by the platform with no webserver to deploy.

### Five technical requirements for a safe extension primitive (headings, from jeremymorrell.dev "A new primitive" section)
```
1. Economical to run       — ~$0 idle cost; tiny-fractions-of-a-penny per execution
2. Fast cold starts        — single-digit milliseconds ideally
3. Control over limits     — CPU, memory, network requests, response size, log volume/rate
4. Solid isolation boundary — fault isolation AND security isolation (incl. Spectre-class attacks)
5. Allow actions safely    — controlled capability-scoped I/O, not ambient credentials
```

### Isolation technology survey (named production examples, from jeremymorrell.dev)
```
Interpreter:   Lua, QuickJS, or roll-your-own (Salesforce's original Apex approach)
V8 Isolates:   Cloudflare Dynamic Workers, celld, Node isolated-vm, Rivet secure-exec
MicroVMs:      Firecracker, libkrun, AWS Lambda MicroVMs, @deno/sandbox, smolvm,
               Tensorlake, Daytona
WASM + WASI:   blank-slate execution, host defines capabilities via WASI;
               composable with V8 isolates or microVMs (not mutually exclusive)
```

### Cloudflare Dynamic Workers feature list — capabilities the author says you'd otherwise build yourself (paraphrased list, from jeremymorrell.dev)
```
Observability:          runtime-integrated OpenTelemetry tracing + tail workers
Multi-tenant storage:   per-user SQLite via Durable Object facets, or per-user R2 buckets
Durable execution:      Dynamic Workflows — actions over minutes/days with retries/backoff
Source control:         built into the product (Cloudflare Artifacts)
Hosted LLMs:            Workers AI, exposed to user extensions with token budgets/rate limits
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` (containment architecture for
    shipping agentic products; that note's Claim 1 three-category risk
    taxonomy and general "environmental controls over model-layer defenses"
    thesis): Morrell's Claim 5 governance gap ("Pi extensions run with the
    same permissions as Pi itself" unless sandboxed) is exactly the failure
    mode Anthropic's containment architecture is designed to close for its
    own products — this source documents the same gap existing, unaddressed,
    in a different vendor's product, which strengthens the case that
    environmental sandboxing (not prompt-level trust) is the correct default
    for any system letting LLMs generate or run extension code.
  - `blog-google-adk-zero-trust-agents.md` Claim 6, Claim 7, and Claim 10
    (Docker/kernel-sharing risk, gVisor wrapping for LLM-generated code with
    a specific `--network=none --cap-drop=ALL --memory=64m --cpus=0.1`
    flag recipe, and the "each layer covers what the others cannot"
    defense-in-depth framing): independently arrives at the same isolation
    and resource-limit requirements as Morrell's Claim 8 technical
    requirements list, for the specific case of LLM-*generated* code rather
    than user-*authored* extensions — a second (Google vs. this Cloudflare-
    affiliated author), independently-reasoned convergence on the same
    sandboxing bar.
  - `blog-anthropic-claude-managed-agents.md` Claim 1 and Claim 7 (building a
    production agent requires months of sandboxing/checkpointing/credential-
    management infrastructure before users see anything; scoped permissions
    and identity management as a governance layer): corroborates Morrell's
    framing that safe extensibility infrastructure is the hard, expensive
    part — Managed Agents is a vendor productizing infrastructure-as-a-service
    for exactly the primitive-requirements gap Morrell's Claim 8 describes,
    though for agent *runtime* infrastructure rather than user-*extension*
    infrastructure specifically. Both sources independently conclude that the
    infrastructure, not the LLM code generation, is the bottleneck.
  - `blog-simonwillison-datasette-agent.md` Claim 1 and Claim 5 (Datasette
    Agent as "an open source plugin for Datasette that provides an extensible
    AI assistant"; extensibility via plugins as the core architectural
    feature, demonstrated by three working launch plugins): a working,
    shipped instance of Morrell's Claim 3 "LLM-native software" pattern — a
    battle-tested core with an installable extension surface — though
    Datasette Agent's plugins are traditional Python packages installed by
    the *operator*, not LLM-authored, sandboxed *end-user* extensions
    generated at request time. This is a meaningful architectural distinction
    the guide should preserve: Datasette Agent extends the pattern of
    "pluggable core," but does not yet demonstrate Morrell's specific claim
    about safely running arbitrary end-user-authored, LLM-generated code.

- **Extends**:
  - `blog-simonwillison-kenton-varda-change-descriptions.md` (Kenton Varda as
    a recurring named practitioner in this corpus, previously documented via
    a tweet critiquing AI-written change descriptions and, per that note's
    Cross-References, a separate tweet critiquing Anthropic's per-agent
    identity/ACL permissioning model as not scaling): this source is a third,
    independent point of contact with Varda's capability-security thinking —
    this time filtered through a colleague (Morrell) who explicitly credits
    Varda's influence, applied specifically to the extension-authoring
    problem rather than change-description quality or agent-identity ACLs.
    Together the three sources trace a consistent Cloudflare capability-
    security lineage across three distinct topics.

- **Contradicts**: None identified. This source's core proposals (sandbox
  isolation as the security boundary, capability-scoping over ambient
  credentials) are consistent with every existing corpus source on agent/
  extension sandboxing found during this extraction (`blog-anthropic-how-
  contain-claude.md`, `blog-google-adk-zero-trust-agents.md`,
  `blog-anthropic-claude-managed-agents.md`). No contradiction issue filed.

- **Novel**:
  - **The two-factor cost-structure framing** (LLMs lower authoring cost;
    sandboxes lower deployment cost) as the explicit reason web extensibility
    is newly viable — no existing corpus source frames the opportunity this
    way; prior sources treat sandboxing and LLM code generation as separate
    topics.
  - **The credential-proxy-vs-object-capability contrast**, illustrated with
    working code for both, including the specific claim that a
    capability-based interface is *more token-efficient for an LLM to
    generate against* than a full OpenAPI spec — this LLM-codegen-efficiency
    angle on capability design is new to the corpus.
  - **Salesforce Apex as a 19-year historical precedent** for safe multi-
    tenant user-code execution, predating modern cloud (AWS 2006, Salesforce
    Apex 2007) — no existing source note uses this comparison.
  - **The five-property technical requirements list** for a safe extension
    primitive (economical, fast cold start, controllable limits, solid
    isolation, capability-scoped actions) as a reusable evaluation rubric —
    more general-purpose than the corpus's existing sandboxing coverage,
    which documents specific vendor implementations rather than a
    requirements checklist.
  - **A named survey of five composable isolation-technology families** with
    current (2026) production examples for each — a reference map not
    previously assembled in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a subsection on "extension
  surfaces" distinct from the existing tool/plugin coverage — specifically,
  the distinction between (a) operator-installed plugins (Datasette Agent's
  model, `blog-simonwillison-datasette-agent.md`) and (b) end-user-authored,
  LLM-generated, sandboxed extensions (Morrell's proposed model, not yet
  documented with a production case study in this corpus). Cite Claim 1's
  two-factor cost framing and Claim 8's five-property requirements checklist
  as a rubric for evaluating extension-execution technology choices.

- **Chapter 02 (Harness Engineering)**: Document the object-capability
  pattern (Claim 10) as an alternative to credential-proxy scoping (Claim 9)
  for any harness that needs to give agent- or extension-code bounded access
  to external systems. This is directly actionable: pass narrow,
  pre-scoped function references into untrusted code rather than tokens or
  proxied credentials. Cite the IFTTT `twitter.post_new_tweet()` analogy as
  a memorable illustration, and the token-efficiency-for-LLM-codegen claim
  as an additional argument beyond pure security.

- **Chapter 06 (Security Threat Model)**: Add the enumerated
  arbitrary-code-execution risk checklist (Claim 6, Concrete Artifacts) as a
  starting audit list for any team building or evaluating a sandboxed
  extension/plugin execution model — service availability, credential/data
  exfiltration, DoS in both directions, Spectre-class attacks, cryptomining
  abuse. Cross-reference against the gVisor flag recipe in
  `blog-google-adk-zero-trust-agents.md` for a concrete implementation
  matching several of these requirements.

- **Chapter 06 (Security Threat Model)**: Cite Claim 5's specific finding
  (Pi extensions run with Pi's own permissions unless the user sandboxes
  them) as a concrete example of the ambient-permission failure mode the
  chapter should warn against — paired with `blog-anthropic-how-contain-
  claude.md`'s containment architecture as an example of a vendor closing
  this exact gap for its own products.

## Extraction Notes

- **Two pages fetched and read in full**: the Willison quote page
  (simonwillison.net, three sentences plus tags) and the linked Morrell essay
  (jeremymorrell.dev, the full ~5,000-word article including all section
  headings, code examples, and footnotes). Per MINER.md §1's "follow up to 5
  linked pages" guidance, this counts as one followed page; the essay itself
  links to dozens of further sources (Kenton Varda talks, Salesforce Apex
  docs, Cloudflare product docs, WASI spec, etc.) which were read at the
  citation level (to verify Claim 7's Salesforce dates and Claim 12's feature
  claims against their anchor text) but not independently fetched as full
  pages — those citations are the author's own, and are reported here as his
  claims, not independently re-verified against Cloudflare's own product
  documentation.
- **Not fetched**: the companion post "Working with Dynamic Workers" (linked
  from the "Demo Time" section) and the embedded interactive
  `dynamic-workers-demo` widget, which requires a live browser session and
  could not be evaluated via static HTML fetch. Neither was needed for the
  claims extracted here, which come from the essay's argumentative body, not
  the demo.
- **Verbatim quote verification**: All quotes were copied from the raw HTML
  of both pages (fetched directly, not via the summarizing WebFetch tool, to
  guarantee character-for-character accuracy) rather than reconstructed from
  a summary. The core thesis quote was independently verified as identical
  on both the Willison page and the Morrell essay (Morrell's essay includes
  one additional trailing sentence — "We can give our users super powers." —
  that Willison's blockquote also reproduces in full).
- **Disclosed conflict of interest**: the author's own disclosure ("I
  currently work at Cloudflare...") is treated as material to confidence
  ratings throughout this note, particularly Claim 12 (Dynamic Workers as
  best-fit technology), which is rated `anecdotal` specifically because of
  this disclosed affiliation, despite the individual feature claims being
  independently checkable against first-party Cloudflare docs.
- **No contradiction issue filed**: this source's proposals are consistent
  with, and in some cases independently convergent with, existing corpus
  sandboxing coverage. See Cross-References → Contradicts.
