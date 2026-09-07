---
source_url: https://openai.com/index/polimill
source_type: blog-post
title: "Polimill builds Japan's next-generation public AI infrastructure"
author: OpenAI (customer case study, featuring Masahiro Wakabayashi, CAIO, Polimill)
date_published: 2026-08-31
date_extracted: 2026-09-07
last_checked: 2026-09-07
status: current
confidence_overall: anecdotal
issue: "#3292"
---

# Polimill builds Japan's next-generation public AI infrastructure

> An OpenAI customer case study describing how Polimill, a Japanese civic-tech
> company, built QommonsAI — a GPT-powered, cross-municipality knowledge
> platform now used by roughly 1,050 municipalities and 550,000 public
> employees across Japan — and used Codex plus OpenAI hands-on support to
> raise its own development speed 3-5x, with a stated ambition to expand into
> a "super agent" public-sector app platform ("Qommons ONE") in fall 2026.

## Source Context

- **Type**: blog-post (OpenAI customer case study, `openai.com/index/polimill`,
  published August 31, 2026; ~800 words). Structured as a narrative case study
  with four named sections ("Building a cross-municipality knowledge base,"
  "Balancing government-grade security with everyday usability," "Codex and
  hands-on support made development 3-5x faster," "Results at a glance,"
  "Beyond efficiency, capturing the tacit knowledge of veteran officials,"
  "Toward a super agent for public-sector work"), two pull quotes, and a
  bulleted "Results at a glance" summary. Not a technical or engineering blog
  post — no code, config, or architecture diagrams appear.
- **Author credibility**: Written and published by OpenAI, not Polimill, as
  promotional customer-success content — OpenAI has a direct commercial
  incentive to present GPT models and Codex favorably. The only named
  individual quoted is Masahiro Wakabayashi, Polimill's Chief AI Officer
  (CAIO). No municipal official, public employee, or independent party is
  named or quoted anywhere in the piece. No methodology is given for the
  "3-5x" development-speed figure, the "1,050 municipalities" / "550,000
  public employees" adoption figures, or the claim that AI-assisted policy
  proposals from less-experienced staff "approached the quality" of veteran
  officials' proposals.
- **Scope**: Covers Polimill's origin (a citizen-engagement platform called
  Surfvote), its pivot to building government-efficiency tooling (QommonsAI,
  released October 2024), the platform's cross-municipality data
  standardization approach, its security/usability posture, its Codex-based
  internal development workflow and OpenAI's "hands-on support," a
  validation finding about AI-assisted policy drafting by less-experienced
  staff, and a forward-looking plan for a "super agent" product (Qommons
  ONE) launching fall 2026. Does NOT cover: the underlying model versions
  used, any technical detail of QommonsAI's search/retrieval architecture
  beyond "metadata" and "high-precision search foundation," independent
  verification of the adoption or development-speed figures, or any
  named municipality, its officials, or citizen-facing outcomes.

## Extracted Claims

### Claim 1: QommonsAI, Polimill's generative-AI platform for public-sector workflows released in October 2024, is now used by about 1,050 municipalities and about 550,000 public employees across Japan
- **Evidence**: Stated adoption figures, repeated in both the article body and the "Results at a glance" bullet list.
- **Confidence**: anecdotal (self-reported, first-party adoption figures with no independent audit, survey methodology, or usage-intensity data — "used by" is undefined: could range from daily active use to nominal account provisioning)
- **Quote**: "About 1,050 municipalities and about 550,000 public employees across Japan now use it."
- **Our assessment**: This is the article's headline scale claim and its most checkable-in-principle figure (municipal governments are public bodies whose contracts could in theory be independently verified), but as published it carries no citation, survey date, or definition of "use." Treat as a vendor-reported adoption ceiling, not a measured active-usage rate — comparable in evidentiary weight to the self-reported enterprise adoption figures already in the corpus (e.g. Samsung's "5 million weekly Codex users," `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 5) rather than to an independently audited number.

### Claim 2: Polimill's motivation for building government-efficiency AI tooling was instrumental to its original civic-participation mission — public-sector teams were too consumed by daily operations to reflect citizen input in policy, so the company built efficiency tools as a precondition for expanding civic participation
- **Evidence**: Origin narrative in the article's opening, describing Polimill's prior product Surfvote and the structural problem it observed.
- **Confidence**: anecdotal (a first-party origin story with no external corroboration)
- **Quote**: "As the company worked with local governments, it saw a structural challenge: public-sector teams were consumed by daily operations and had little time to reflect citizens' voices in policy."
- **Our assessment**: This framing matters for how the rest of the case study should be read — QommonsAI is presented not as a standalone AI-efficiency product but as means to a stated civic-participation end (Surfvote). No data in the article measures whether the efficiency gains described in later claims have actually freed capacity for the stated civic-participation goal; this remains a stated intent, not a demonstrated outcome.

### Claim 3: Polimill collected and standardized assembly minutes from across Japan, added AI-generated metadata, and built a search foundation that works across municipalities and time periods — because each municipality's own workflows and document formats were previously fragmented and required manually reviewing years of minutes to ensure policy consistency
- **Evidence**: Narrative description under "Building a cross-municipality knowledge base."
- **Confidence**: anecdotal (a first-party description of a data-engineering approach, with no detail on the volume of documents processed, metadata schema, or search-accuracy metrics)
- **Quote**: "Polimill collected and standardized assembly minutes from across Japan, then used AI to add metadata and build a high-precision search foundation that works across municipalities and time periods."
- **Our assessment**: This is the article's most concrete technical description, though "high-precision" is asserted without a stated accuracy figure or evaluation method. The described problem — each of ~1,050 municipalities having its own workflows and document formats, requiring manual cross-referencing of years of minutes to check policy consistency — is a plausible, specific instance of the "fragmented legacy data blocks AI adoption" pattern documented more generally (without this specific artifact) in `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 7 (fragmented architectures and inconsistent data governance named among the top blockers between AI prototype and production in government settings).

### Claim 4: Polimill's CAIO states that GPT models' broad capability and public familiarity — via widespread awareness of ChatGPT — are the main reasons the company adopted them, because that familiarity lowers the adoption barrier for public employees encountering a new tool
- **Evidence**: Attributed characterization in the "Balancing government-grade security with everyday usability" section.
- **Confidence**: anecdotal (a single executive's stated adoption rationale, not measured against any alternative-vendor comparison or adoption-rate data)
- **Quote**: "The widespread awareness of ChatGPT matters when public employees need to use a new tool after rollout. Even if they are not familiar with technical terms or other model names, knowing the system is based on widely used ChatGPT technology lowers the initial barrier to adoption."
- **Our assessment**: This is a specific, named adoption-psychology mechanism — brand familiarity as a change-management lever for mass rollout to a non-technical public-sector workforce — distinct from any capability-based justification. It is asserted, not measured (no before/after adoption-speed comparison against a less-known model is given), but it is a novel, citable mechanism for the corpus's coverage of large-scale enterprise/institutional AI rollout.

### Claim 5: QommonsAI includes operational controls letting administrators review feature usage history and restrict which models are available according to organizational policy, framed as necessary for public-sector information management and audit readiness
- **Evidence**: Direct statement in the same section as Claim 4.
- **Confidence**: anecdotal (a stated product-governance capability, with no detail on what usage history is logged, at what granularity, or how model-restriction policies are configured)
- **Quote**: "QommonsAI includes operational controls that let administrators review feature usage history and limit which models are available according to organizational policy."
- **Our assessment**: A concrete, if underspecified, governance-control claim — administrator-level usage auditing and model allowlisting — that is directionally consistent with, but far less detailed than, the "meaningful in practice, not merely formal" human-oversight framework OpenAI itself published a month earlier in `blog-openai-government-national-security-partnerships.md` Claim 9. This source gives no equivalent detail on audit scope, retention, or how "organizational policy" restrictions are actually enforced.

### Claim 6: Polimill adopted Codex across its own software development workflow — from requirements definition to checking consistency with existing GitHub code, implementation, and testing — shifting engineers toward reviewing AI-generated plans and making high-level decisions while AI executes more of the implementation autonomously, which the CAIO says raised development speed to 3-5x previous levels
- **Evidence**: Direct statement and attributed characterization in "Codex and hands-on support made development 3-5x faster."
- **Confidence**: anecdotal (a single vendor-selected customer's self-reported multiplier, no baseline methodology, no named project, and no independent measurement)
- **Quote**: "With AI coding speed and continued background work, development speed rose to 3-5x previous levels."
- **Our assessment**: This is the article's headline productivity figure and sits within the range of other OpenAI customer case studies already in the corpus — narrower and more conservative than Asana's ~1.5-week/2-calendar-week compression of an estimated 5-year project (`blog-openai-asana-codex-case-study.md` Claim 1) or Notion's "2 Weeks → 3 hours" framing (`blog-openai-notion-codex-case-study.md` Claim 1), but structurally the same pattern: a vendor-published multiplier with no disclosed baseline measurement. Treat as directionally consistent with, not independent confirmation of, those other multipliers.

### Claim 7: OpenAI provided Polimill "hands-on support" beyond the base product, including sharing best practices from other advanced global deployments, tailored guidance, and help designing which development steps AI should handle versus where humans should review and retain responsibility
- **Evidence**: Direct statement following the 3-5x development-speed claim.
- **Confidence**: anecdotal (a first-party description of a vendor services relationship, with no detail on the frequency, staffing, or duration of this support)
- **Quote**: "The collaboration includes sharing best practices from advanced global examples, providing information tailored to Polimill, and helping design the development process itself, including which steps AI should handle and where humans should review and take responsibility."
- **Our assessment**: This is a concrete, if vague, description of a vendor-consulting layer beyond the raw API/product — OpenAI acting as an active development-process advisor, not just a model supplier. Notable for practitioners assessing what a frontier-lab "enterprise deployment" relationship can include beyond licensing: process design consulting on the human/AI division of labor, not just technical support.

### Claim 8: In Polimill's internal validation, less-experienced employees using AI plus accumulated administrative information drafted policy proposals that received evaluations "close to" proposals from experienced officials — but proposals from experienced officials still received the highest evaluations, a gap Polimill attributes to tacit, undocumented practical judgment
- **Evidence**: Direct statement and attributed CAIO quote under "Beyond efficiency, capturing the tacit knowledge of veteran officials."
- **Confidence**: anecdotal (an internal, unpublished validation exercise with no stated evaluator identity, evaluation criteria, sample size, or scoring methodology)
- **Quote**: "I think the parts that are not captured in knowledge or data contributed to the quality of the outcome. Put another way, when people with that kind of experience use AI, they can create even better work."
- **Our assessment**: This is the most conceptually interesting claim in the source — a first-party account of AI narrowing but not closing an experience gap, with the residual gap explicitly attributed to *tacit* (uncodified) knowledge rather than to AI capability limits. This directly corroborates, from a real (if unaudited) internal validation exercise rather than a philosophical argument, the "transmissibility"/tacit-knowledge thesis in `blog-thoughtworks-kamelman-unbundling-expertise.md`: that article's Claim 6 argues experts who have "never been asked to make their reasoning explicit" produce a "productivity ceiling," and this source's Wakabayashi quote independently describes exactly that residual — the veteran officials' advantage is specifically the "parts that are not captured in knowledge or data." Where Kamelman's piece is a philosophical/interpretive essay built on a secondhand characterization of an Anthropic study, this source is a (still unaudited) real organizational finding pointing at the same mechanism from a completely different domain (Japanese municipal government vs. Anthropic's Claude Code session data).

### Claim 9: Polimill plans to record how veteran officials instruct AI and revise its outputs, in order to convert previously undocumented tacit judgment into organizational knowledge, framing the goal as amplifying and transferring — not replacing — experienced staff
- **Evidence**: Forward-looking statement following Claim 8, describing Polimill's stated plan.
- **Confidence**: anecdotal (a stated future intention, not a built or deployed capability — no timeline, tooling, or pilot data given)
- **Quote**: "Polimill plans to record how veteran officials instruct AI to research and how they revise outputs, turning judgment that has not previously been documented into organizational knowledge."
- **Our assessment**: This is a specific, if unbuilt, proposed mechanism for operationalizing Claim 8's tacit-knowledge gap: capturing not the officials' outputs but their *interaction pattern with the AI* (instructions given, revisions made) as the artifact to be transferred. This is a more concrete mechanism than most "capture institutional knowledge" aspirations in the corpus, but it remains a stated plan with no described pilot, tooling, or evaluation criteria — should be flagged for revisit if Polimill publishes results.

### Claim 10: In fall 2026, Polimill plans a full rollout of "Qommons ONE," a marketplace where third-party companies provide municipal applications, centered on a "super agent" that combines multiple specialized AI systems and private-sector apps so a user can state a goal and have the system call the necessary tools to produce deliverables
- **Evidence**: Direct statement under "Toward a super agent for public-sector work," describing the planned product and its scheduled launch window.
- **Confidence**: anecdotal (a forward-looking product announcement with a stated but unverified timeline; the article gives no detail on which third-party companies, if any, are already committed, or on the technical architecture of the "super agent")
- **Quote**: "In fall 2026, Polimill plans a full rollout of Qommons ONE, a store where outside companies can provide applications for municipalities. At its center will be a super agent that brings together multiple specialized AI systems and private-sector apps."
- **Our assessment**: This is the article's most speculative claim — an orchestrator-of-orchestrators product (a "super agent" calling multiple specialized AI systems and third-party apps to fulfill a stated goal) that does not yet exist as described. It is directionally consistent with the general industry pattern of agent products expanding from single-task tools toward multi-agent orchestration layers, but as a named, dated (fall 2026) product commitment from a single vendor case study, it should be treated as an announced intention, not a shipped or demonstrated capability, until independently confirmed.

## Concrete Artifacts

### Results-at-a-glance bullet list (verbatim)

```
Source: https://openai.com/index/polimill

- About 1,050 municipalities and about 550,000 public employees across
  Japan are using QommonsAI.
- Polimill built infrastructure that unifies assembly minutes and
  administrative information distributed across Japan and makes them
  searchable across organizations.
- Codex and OpenAI's hands-on support accelerated validation and
  implementation cycles, increasing development speed by 3-5x.
- GPT models' advanced reasoning helped less-experienced employees use AI
  and accumulated administrative information to draft policy proposals
  that approached the quality of proposals from veteran officials.
```

### CAIO quotes — verbatim, attributed to Masahiro Wakabayashi, CAIO, Polimill

```
Source: https://openai.com/index/polimill

"Amid a worsening labor shortage, using AI to make government work more
efficient is essential. But introducing separate tools can create service
gaps between municipalities. That is why we want QommonsAI to become a
common foundation that supports every municipality equally—and grow into
the public OS that supports Japan's government."

"I think the parts that are not captured in knowledge or data contributed
to the quality of the outcome. Put another way, when people with that
kind of experience use AI, they can create even better work."
```

## Cross-References

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` Claim 8 (GroundVue, a startup
    using Codex to make government public meetings searchable across
    ~90,000 government bodies, letting "a small team perform work that
    previously would have required large groups of technologists and
    researchers"): both sources describe Codex/GPT-based tooling applied
    specifically to organizing and searching government/public-sector
    records at scale. GroundVue's case is a private startup indexing
    public government proceedings from outside; Polimill's case is a
    vendor building the equivalent infrastructure from inside government,
    at a larger stated scale (1,050 municipalities vs. GroundVue's ~90,000
    government bodies indexed, which is a different unit — bodies indexed
    vs. municipalities as customers). Both are vendor-selected, unaudited
    case studies but corroborate the same general pattern: AI-assisted
    search/organization tooling applied to fragmented government records
    as a recurring 2026 OpenAI case-study theme.
  - `blog-openai-asana-codex-case-study.md` Claim 6 (Asana: "an engineer
    checked progress twice a day and reviewed every proposed change...
    simpler instructions worked better than a more elaborate setup") and
    `blog-openai-notion-codex-case-study.md` Claim 1 ("2 Weeks → 3 hours"
    headline framing): this source's Claim 6 (3-5x development speed via
    Codex, human review of AI-generated plans) is a third OpenAI customer
    case study reporting a self-reported development-speed multiplier from
    a Codex-centric workflow with human review retained — the specific
    multiplier (3-5x) is more conservative than Asana's or Notion's
    headline ratios, but the underlying pattern (Codex plus a human
    reviewing AI-proposed plans/changes) is the same across all three.
  - `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 6 (experts
    who have "never been asked to make their reasoning explicit... may
    find the tool unexpectedly disappointing," producing "a productivity
    ceiling") and Claim 8 (the knowledge/transmission gap "has never,
    until now, had a direct economic cost attached to it"): this source's
    Claim 8 and Claim 9 (veteran officials' proposals still rated highest
    due to "parts that are not captured in knowledge or data," with
    Polimill now planning to explicitly record and transfer that tacit
    judgment) is a concrete, real-organization instance of the same
    tacit-knowledge/transmissibility gap Kamelman's essay argues for
    philosophically. See also Claim 8's assessment above for the detailed
    parallel.
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 7
    (fragmented architectures, brittle legacy systems, and inconsistent
    data governance named among the top blockers between AI prototype and
    production specifically in government settings): this source's Claim 3
    (each of ~1,050 municipalities having its own workflows and document
    formats, requiring manual cross-referencing of years of minutes) is a
    concrete, named instance of exactly that fragmented-government-data
    blocker, and this source's Claim 3 solution (collect, standardize, and
    add metadata to build a cross-municipality search foundation) is a
    real, if unaudited, example of the kind of data-standardization
    prerequisite that source's Claim 9 argues underlies safe AI adoption.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Polimill, QommonsAI, or Japanese municipal AI infrastructure that
  opposes what this post states. This source's Claim 4 (ChatGPT brand
  familiarity as an adoption driver) and Claim 6 (a modest, human-reviewed
  3-5x speed multiplier) are consistent in kind with, not opposed to,
  other OpenAI customer case studies already in the corpus. No
  contradiction issue filed.

- **Extends**:
  - `blog-openai-government-national-security-partnerships.md` Claim 4
    (OpenAI's Daybreak cyber-defense program established "Trusted Access
    for Cyber" partnerships with nine named allied governments/
    institutions, including Japan, "in the past month" as of July 2026):
    that source documents a direct OpenAI-to-Japanese-government security
    partnership; this source documents a separate, indirect channel —
    OpenAI's models reaching Japanese local government via a third-party
    Japanese company (Polimill) building consumer-facing civic
    infrastructure on top of GPT/Codex, rather than a direct national
    cyber-defense partnership. Together they show at least two distinct
    OpenAI-to-Japan government-adjacent channels active within about a
    month of each other (national-security partnership in July 2026;
    municipal-government software vendor deployment reported August 2026),
    though this source gives no indication the two are related or that
    Polimill's deployment involves any of the Daybreak partnership
    machinery.
  - `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 3 ("Codex
    started as a tool for software development, but it's increasingly
    useful for more kinds of work") and `blog-openai-codex-knowledge-work.md`
    Claim 2 (knowledge workers now represent ~20% of Codex's user base,
    growing 3x faster than developers): this source extends that
    "Codex beyond developers" trend with a specific institutional
    instance — Polimill's own engineering team uses Codex for software
    development (Claim 6), while separately building a *product*
    (QommonsAI) that puts GPT-based knowledge-work tooling in front of
    550,000 non-developer public employees. It is a single company
    occupying both sides of the "Codex for developers" / "GPT for
    knowledge workers" split documented elsewhere in the corpus.

- **Novel**:
  - **QommonsAI and Polimill** are not previously documented anywhere in
    this corpus — this is the first source-note coverage of a
    Japan-specific, municipal-government-focused AI software vendor.
  - **A stated adoption-psychology mechanism specifically tied to consumer
    brand familiarity** ("knowing the system is based on widely used
    ChatGPT technology lowers the initial barrier to adoption," Claim 4)
    — not previously named in the corpus as a distinct lever for
    large-scale institutional/public-sector rollout to a non-technical
    workforce.
  - **A concrete, named plan to convert tacit human-AI interaction
    patterns (how veteran officials instruct and revise AI output) into
    organizational knowledge** (Claim 9) — a more specific proposed
    mechanism than the general "capture institutional knowledge" theme
    elsewhere in the corpus.
  - **"Qommons ONE" and the "super agent" framing** (Claim 10) — a named,
    dated (fall 2026) multi-agent orchestration product for public-sector
    third-party apps, not previously documented in the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add Claim 4 (ChatGPT brand familiarity as
  an explicit, named adoption-psychology lever for rolling AI tools out to
  a large, non-technical institutional workforce) as a citable mechanism
  distinct from the capability-based adoption arguments already in the
  guide — relevant to any section on driving adoption across large,
  non-engineering user populations. Flag it as a single vendor's stated
  rationale, not a measured adoption-rate comparison.
- **Chapter 05 (Team Adoption)**: Add Claims 8 and 9 (the tacit-knowledge
  gap between AI-assisted novices and veteran officials, and Polimill's
  plan to capture officials' AI-interaction patterns rather than just their
  outputs) alongside the existing `blog-thoughtworks-kamelman-unbundling-expertise.md`
  citation as a second, independent (if anecdotal and unaudited) data point
  for the "transmissibility, not raw expertise, is what AI adoption
  rewards" thesis — this time from a real organizational validation
  exercise rather than a philosophical argument built on a secondhand study
  characterization.
- **Chapter 02 (Harness Engineering)**: Add Claim 6 and Claim 7 (Codex
  adopted across requirements-to-testing workflow, with OpenAI providing
  process-design consulting on which steps AI should own vs. where humans
  retain review responsibility) as a fourth OpenAI customer case study
  (alongside Asana, Notion, Samsung already in the corpus) reporting a
  Codex-centric development workflow with human review retained — note
  that this source's 3-5x figure is markedly more conservative than
  Asana's or Notion's headline ratios, worth citing as a lower-end data
  point in that range rather than citing only the more dramatic figures.
- **No chapter should cite Claim 1's adoption figures (1,050 municipalities,
  550,000 employees), Claim 6's "3-5x" development-speed figure, or Claim 10's
  "Qommons ONE" fall 2026 launch as independently verified facts** — all are
  first-party, unaudited, vendor-published claims with no disclosed
  methodology, consistent with every other OpenAI customer case study
  already in this corpus.

## Extraction Notes

1. **Direct fetch blocked (Cloudflare challenge)**: Both `WebFetch` and a
   direct `curl` (with a standard browser user-agent) against
   `https://openai.com/index/polimill` returned an HTTP 403 Cloudflare
   bot-challenge page (confirmed by inspecting the returned HTML, which
   contained Cloudflare challenge-platform script tags rather than article
   content). No Wayback Machine snapshot existed yet for this URL as of
   extraction time (`archive.org/wayback/available` returned an empty
   `archived_snapshots` object) — this is a very recently published
   article (2026-08-31), only one week old at extraction time, which
   likely explains the absence of a crawl. `archive.ph` returned HTTP 429
   (rate-limited) and is refused directly by `WebFetch`. The article was
   ultimately retrieved via the `r.jina.ai` reader-proxy
   (`https://r.jina.ai/https://openai.com/index/polimill`, HTTP 200),
   which returned clean Markdown-converted article text. Unlike the
   inconsistent, apparently-paraphrased `r.jina.ai` output documented as a
   failure mode in `blog-openai-effingham-county-community-infrastructure.md`'s
   Extraction Notes (three fetches of that URL produced three different
   sets of figures), this fetch was only performed once; all `Quote`
   fields above were copied character-for-character from that single
   retrieval, and the retrieved text is internally consistent (headline
   figures in the body match the "Results at a glance" bullet list
   verbatim), which is the same cross-check `blog-openai-effingham-county-community-infrastructure.md`
   used to validate its own Wayback-sourced text. No second independent
   fetch was available to cross-verify this specific retrieval, which is a
   real limitation — a future revisit once a Wayback snapshot exists would
   be worth doing to confirm no paraphrasing occurred, per the caution
   raised in that prior note.
2. **RSS feed cross-checked as a partial verification**: OpenAI's news RSS
   feed (`https://openai.com/news/rss.xml`) was also fetched directly
   (HTTP 200) and contains this article's title and one-sentence
   description ("Polimill uses OpenAI GPT models and Codex to help
   municipalities search and use administrative knowledge while
   accelerating development"), which matches the `r.jina.ai`-retrieved
   body content's substance and confirms the article's existence and
   publication date independent of the `r.jina.ai` retrieval.
3. **No sub-pages followed**: The retrieved article text contained no
   inline links to further substantive pages (e.g., no linked PDF,
   companion site, or "Keep reading" footer was present in the `r.jina.ai`
   Markdown output, unlike several other OpenAI Global Affairs posts in
   this corpus that link to companion sites or PDFs). No sub-pages were
   available to follow.
4. **Cross-reference verification**: Before writing citations above,
   `blog-openai-codex-knowledge-work.md`,
   `blog-openai-asana-codex-case-study.md`,
   `blog-openai-notion-codex-case-study.md`,
   `blog-openai-samsung-chatgpt-codex-deployment.md`,
   `blog-openai-government-national-security-partnerships.md`,
   `blog-thoughtworks-kamelman-unbundling-expertise.md`, and
   `blog-thoughtworks-lewis-gov-structural-modernization.md` were re-read
   directly (MINER.md §4b) and all claim numbers cited above were
   confirmed against those notes' numbered `### Claim N:` headings in
   document order.
5. **No contradiction filed**: Checked this source's content against the
   cross-referenced notes above; no material opposition to any existing
   claim was found — see Cross-References → Contradicts.
6. **Confidence rated `anecdotal` overall**: every claim in this source is a
   first-party, vendor-published figure or characterization with no
   disclosed methodology, no independent audit, and (with the partial
   exception of the RSS-feed cross-check in Extraction Note 2) no second
   independent source confirming the specific figures. This matches the
   `anecdotal` rating already applied to the corpus's other single-company
   OpenAI customer case studies (Asana, Notion) rather than the `emerging`
   rating applied to OpenAI's own policy/principles documents, which name
   more independently checkable specifics (regulatory dockets, named
   government partners).
