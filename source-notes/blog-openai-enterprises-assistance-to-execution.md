---
source_url: https://openai.com/index/how-enterprises-put-ai-to-work
source_type: blog-post
title: "From assistance to execution: How enterprises put AI to work"
author: OpenAI
date_published: 2026-08-12
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: emerging
issue: "#2861"
---

# From assistance to execution: How enterprises put AI to work

> OpenAI's synthesis post announcing two companion enterprise-adoption
> studies — the "Enterprise Signals" data page and an academic working paper
> co-authored with Columbia and Wharton researchers — arguing that a
> widening "frontier gap" between the most agentic enterprise AI adopters
> and typical adopters is driven less by model access than by whether firms
> connect agents to company context/tools, govern them, and turn individual
> workflows into shared organizational practice.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`), unsigned,
  functioning as a synthesis/index page for two linked companion sources
  that this note also extracts from: the "Enterprise Signals" data page
  (`openai.com/signals/enterprise-data/`, updated August 12, 2026) and the
  working paper "How Organizations Use AI: Evidence from ChatGPT" (Chatterji,
  Holtz, Rakholia, Tambe, and Weeratunga; OpenAI, Columbia Business School,
  and the Wharton School; last updated August 11, 2026,
  `cdn.openai.com/pdf/how-organizations-use-chatgpt.pdf`). All three pages
  were fetched and read in full for this note (the blog post is short — one
  page — and links directly to the other two as "two complementary
  studies").
- **Author credibility**: The blog post and Enterprise Signals page are
  house-authored OpenAI vendor content built on first-party, unaudited
  enterprise telemetry (aggregated, de-identified usage data, with an
  explicit disclosure that "we used automated systems to classify message
  content, and no OpenAI employee reviewed customer messages" — Enterprise
  Signals, closing section). The working paper is materially
  higher-credibility: it has five named academic/industry co-authors
  (two OpenAI, one Columbia Business School, one Wharton, one OpenAI),
  discloses regression specifications, sample sizes (1,500+ organizations,
  17M+ messages at the six-month worker-level sample), acknowledges named
  external reviewers and two conference presentations (NBER 2026 Summer
  Institute, Wharton AI and the Future of Work Conference), and explicitly
  labels itself a "working paper, results are subject to change." Two of
  the five authors (David Holtz, Prasanna Tambe) are disclosed as "paid
  contractors for OpenAI," which is a relevant conflict-of-interest
  disclosure the paper itself makes.
- **Scope**: Covers ChatGPT Enterprise and Codex usage telemetry across
  OpenAI's enterprise customer base (June 2025–June 2026 for the blog/Signals
  data, through March 2026 for the linked-financial-data analysis in the
  working paper), enterprise-vs-typical-firm usage gaps, function/industry/
  seniority breakdowns of usage, and (in the working paper only) the
  relationship between usage and public-company financial characteristics.
  Does NOT cover: task success/quality rates, causal productivity effects,
  private/non-public-company financial characteristics, non-OpenAI AI tool
  usage, or usage of personal/individual (non-Enterprise) ChatGPT accounts
  (that population is covered separately in
  `blog-openai-chatgpt-adoption-signals.md`, which this note's population
  does not overlap with).

## Extracted Claims

### Claim 1: Enterprise AI use is becoming more agentic — as of June 2026, Codex generated 64% of combined Codex-and-ChatGPT output tokens among enterprise customers
- **Evidence**: OpenAI enterprise telemetry, aggregate token share between
  the two products.
- **Confidence**: emerging (a specific, dated, single first-party statistic
  with no disclosed sample size or cohort definition, but internally
  consistent between the blog post and the Enterprise Signals page, which
  state it identically)
- **Quote**: "As of June, Codex generated 64% of combined Codex and ChatGPT output tokens among enterprise customers, suggesting that agents are enabling a shift toward more substantive, delegated work."
- **Our assessment**: This is the headline framing statistic for the whole
  post. It is a token-share metric, not a user-count or revenue metric, so
  it says agentic work is disproportionately token-heavy (consistent with
  Enterprise Signals' own caveat that "tokens are an imperfect measure of
  business value") rather than that most enterprise users have switched to
  Codex. Corroborates the general "chatbot-to-agent" shift theme already in
  `blog-openai-agents-transforming-work.md` Claim 5 (OpenAI's own internal
  department-level Codex crossover) and
  `blog-openai-codex-knowledge-work.md`, but this is the first source in
  the corpus to report a cross-enterprise-customer-base token-share number
  rather than an internal-only or Codex-only usage figure.

### Claim 2: The gap between "frontier" and "typical" enterprise firms is widening — frontier firms generated 8.3× as many output tokens per active user as typical firms in June 2026, up from 2.6× in January 2026
- **Evidence**: OpenAI's own monthly firm-ranking methodology: frontier
  firms are defined as the top 10% of enterprise customers by output
  tokens per active user each month; typical firms are the 45th–55th
  percentile band.
- **Confidence**: emerging (a specific, dated, threefold-increase statistic
  with a disclosed percentile definition, repeated identically across the
  blog post and Enterprise Signals page, but the underlying token
  distribution and firm count are not disclosed, and neither page discloses
  whether "frontier firms" in June are the same firms as "frontier firms"
  in January)
- **Quote**: "As of June, frontier firms generated 8.3× as many output tokens per active user as typical firms, a threefold increase compared to the 2.6× gap in January."
- **Our assessment**: This is the post's central and most citable statistic
  — a fast-widening usage gap, not a fast-widening access gap, since the
  post's own framing ("Companies may have access to the same models, but
  frontier firms are putting them to work faster and more deeply") is
  explicit that model access is not the differentiator. This directly
  corroborates `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`
  Claim 6 (competitive advantage comes from orchestration/execution, not
  model choice) and
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
  Claim 1 (enterprise AI initiatives fail from missing organizational
  "operating system," not weak models) — three independent sources (one
  vendor, two consultancy) now converge on "the differentiator is
  organizational execution capability, not model access."

### Claim 3: The frontier gap varies substantially by industry — 11.7× in information and technology versus 5.3× in manufacturing — while typical-firm token growth is comparatively flat and similar across industries (1.9×–2.8× over the past year)
- **Evidence**: OpenAI enterprise telemetry, industry-level breakdown of the
  frontier/typical token-per-active-user ratio.
- **Confidence**: emerging (specific per-industry multipliers from
  first-party telemetry, no disclosed sample size per industry or industry
  taxonomy definition beyond "industries")
- **Quote**: "The frontier gap also extends across industries, with the largest token usage gap in information and technology (11.7×) and the smallest in manufacturing (5.3×). In contrast, token usage among typical firms is similar across industries, with relatively modest growth over the past year (1.9× to 2.8×). This suggests many organizations are still using simple chat assistants, leaving meaningful room to deepen adoption and utilize agents to complete more complex work."
- **Our assessment**: This is the source's own interpretive bridge from "gap
  exists" (Claim 2) to "most firms haven't moved past simple chat
  assistants" — a useful, more specific claim than the aggregate 8.3× figure
  because it shows the gap is not driven by one runaway industry: even the
  narrowest-gap industry (manufacturing) still shows more than a 5×
  frontier/typical difference. This is only found in the Enterprise Signals
  companion page, not the shorter synthesis blog post — a case where
  following the linked source materially deepened the extraction. Novel to
  the corpus; no existing note has industry-level AI-usage-gap data.

### Claim 4: Advanced capabilities (Plugins and skills) are far more common at frontier firms — 21% of frontier-firm weekly active users use Plugins and 19% use skills, versus 9% and 3% at typical firms, while 95% of OpenAI's own employees use Plugins weekly
- **Evidence**: OpenAI enterprise telemetry plus an internal (self-reported)
  OpenAI employee-usage comparison figure.
- **Confidence**: emerging (specific percentages from first-party telemetry,
  and the 95%-of-OpenAI-employees figure is presented as an aspirational
  ceiling rather than a representative benchmark, which the source itself
  flags)
- **Quote**: "Frontier firms have a clear lead in advanced capabilities. Among weekly active users, 21% at frontier firms use plugins and 19% use skills, compared with just 9% and 3% at typical firms. However, frontier firm adoption represents only a fraction of what is possible. OpenAI’s internal usage highlights the potential for deeper usage of these capabilities, with weekly plugin usage at 95% of active users."
- **Our assessment**: The Enterprise Signals page defines Plugins as
  bundling reusable "skills" (instructions) with "apps" (connections to
  company data/tools/actions) — i.e., this is a claim about context-and-tool
  connection depth, not raw model usage. The 95%-of-OpenAI-employees
  comparator is a useful but methodologically weak benchmark: OpenAI is the
  vendor building these features, so its own dogfooding rate is not a
  representative target for external enterprises, only an existence proof
  that near-total weekly adoption is achievable somewhere.

### Claim 5: Agentic AI use is spreading well beyond software engineering — since February 2026, weekly active enterprise Codex users grew 108× in legal, 41× in sales, 41× in recruiting, and 26× in marketing, compared with 5× in engineering
- **Evidence**: OpenAI enterprise Codex telemetry, function-level
  weekly-active-user growth multipliers since February 2026.
- **Confidence**: emerging (specific, dated, function-level multipliers
  repeated identically across the blog post and Enterprise Signals page,
  but growth multipliers from a low base can look dramatic — the source
  gives no absolute headcounts for weekly active Codex users by function,
  so the multipliers alone do not establish which functions have the most
  Codex users in absolute terms)
- **Quote**: "Since February, weekly active enterprise Codex users grew 108× in legal, 41× in sales, 41× in recruiting, and 26× in marketing, compared with 5× in engineering."
- **Our assessment**: This directly corroborates and extends
  `blog-openai-agents-transforming-work.md` Claim 6 (OpenAI's own internal
  department growth: Research 56×, Customer Support 32×, Engineering 27×,
  Legal 13× since November 2025) and Claim 7 (external non-developer growth
  137×/189× since August 2025) — three independent OpenAI reports
  (internal-only, external-enterprise-only, and this cross-customer-base
  figure) now converge on the same directional pattern: engineering has the
  smallest growth multiplier of any function tracked, precisely because it
  started from the highest base. The specific numbers are not the same
  measurement (different time windows, different populations: OpenAI-internal
  vs. external-enterprise-customer-base) and should not be merged into a
  single figure, but the direction — non-engineering functions catching up
  fast from a low base — is now a three-times-corroborated pattern.

### Claim 6: Engineering-vs-general-knowledge-work task differences explain why software moved first — codebases give agents clear context, tests make outputs verifiable, and coding progress feeds back into AI R&D itself, while general knowledge work has "limited context," is "difficult to specify," and lacks "clear criteria for verifying the result"
- **Evidence**: Enterprise Signals page's own interpretive explanation for
  the adoption-order pattern in Claim 5.
- **Confidence**: emerging (a plausible mechanistic explanation offered by
  the vendor for its own observed data, not independently tested or
  measured — it is an inference, not a separate data point)
- **Quote**: "Software moved first for a reason. Codebases give agents clear context, tests make outputs easier to verify, and progress in coding helps accelerate AI research and development... In contrast, progress in general knowledge work has been slower because many tasks provide limited context, can be difficult to specify, and lack clear criteria for verifying the result."
- **Our assessment**: This is a vendor's causal narrative for why agentic
  adoption started in engineering, framed around exactly the three
  properties (context clarity, verifiability, specification difficulty)
  that this guide's own Ch03 (Verification) and Ch04 (Context Engineering)
  treat as central engineering-practice variables — useful as an
  industry-level validation that the guide's core "verification loop" and
  "context budget" concerns are not idiosyncratic to software teams but are
  the exact bottleneck OpenAI identifies for extending agentic AI into
  general knowledge work.

### Claim 7: Across a 10-million-plus-message enterprise sample, writing remains the most common ChatGPT use, while coding plus system/agent operations together account for nearly 75% of agentic (Codex) messages — and this shift toward system/agent-operations work is most pronounced outside technical teams (recruiting 32%, sales 26%, policy 25%, communications 24% of messages) and in design (coding ~60% of agentic messages)
- **Evidence**: Enterprise Signals function-level task-composition analysis,
  "a sample of more than 10 million messages," comparing chat (ChatGPT) vs.
  agentic (Codex) message content by function.
- **Confidence**: emerging (a specific, large-sample-size breakdown by
  function and message type, but the task-classification methodology itself
  is not described beyond "automated systems to classify message content")
- **Quote**: "Writing remains the most common use of ChatGPT, while coding and system or agent operations together account for nearly 75% of agentic messages. This shift is especially pronounced outside traditional technical teams: recruiting (32%), sales (26%), policy (25%), and communications (24%) devote between a quarter and a third of messages to system and agent operations. Technical work is also spreading across functions, with coding accounting for almost 60% of agentic messages in design."
- **Our assessment**: This is the most granular, novel data point in the
  companion Enterprise Signals page — the finding that non-technical
  functions (recruiting, sales, policy, communications) devote a quarter to
  a third of their *agentic* messages specifically to "system and agent
  operations" (not just writing or research) suggests these roles are
  directing agents to take actions, not just draft text. This corroborates
  `blog-openai-agents-transforming-work.md` Claim 8 (over one-fourth of
  business-function Codex work is engineering/coding) and
  `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge workers
  produce artifacts weekly; 46% do code implementation) with a third,
  independently sourced statistic reinforcing the same "developer/
  non-developer task boundary is dissolving" pattern — now corroborated
  across three separate OpenAI reports.

### Claim 8: Early-career employees use AI more intensively than senior employees and executives — contrary to many surveys reporting the opposite — with early-career employees sending 13 more messages per week than executives six months after adoption
- **Evidence**: "Administrative data from millions of conversations,"
  explicitly contrasted by OpenAI against unspecified prior survey findings.
- **Confidence**: emerging (a specific, measured behavioral statistic from
  usage logs rather than self-report, which the source explicitly claims is
  more reliable than survey data on this exact question — though "more
  reliable than surveys" is the source's own framing, not independently
  verified here)
- **Quote**: "Many surveys have reported higher levels of AI use among leaders and executives. However, administrative data from millions of conversations finds the opposite. Six months after adoption, early-career employees sent 13 more messages per week than executives."
- **Our assessment**: This is corroborated with much greater statistical
  rigor by the companion working paper's Claim 8 below (Section 4.3.2:
  early-career workers and trainees send "roughly eight to nine more weekly
  messages than the average active user within the same firm," using
  firm-fixed-effects regressions on a 17-million-message, 1,500+
  organization sample) — the blog post's "13 more than executives" and the
  paper's "8-9 more than the firm average" are different comparison
  baselines (executives vs. firm-wide average) but point in the same
  direction with independently disclosed methodology in the paper. This is
  a genuinely well-evidenced claim for a first-party vendor source, given
  the academic co-authorship and disclosed sample size.

### Claim 9: There is no single enterprise AI adoption leaderboard — industry rankings vary by which metric is used, with Professional/Scientific/Technical Services leading both Codex adoption and API intensity, Arts/Entertainment/Recreation leading ChatGPT adoption, and Manufacturing having the highest ChatGPT intensity despite ranking last in Codex and API intensity
- **Evidence**: An industry-ranking table (Codex adoption, API intensity,
  ChatGPT adoption, ChatGPT intensity) across eight NAICS-style industry
  categories, with month-over-month rank-change indicators.
- **Confidence**: emerging (a specific ranking table across four named
  metrics and eight industries, but absolute values underlying the rankings
  are not disclosed — only relative rank and month-over-month rank change)
- **Quote**: "There is no single AI adoption leaderboard. Industry rankings vary depending on the measure used. In the past month, Professional and Scientific Services led both Codex adoption and API intensity. Arts, Entertainment, and Recreation led ChatGPT adoption, while Manufacturing has the highest ChatGPT intensity despite ranking last in Codex and API intensity."
- **Our assessment**: A genuinely novel and specific finding: Manufacturing
  is simultaneously the industry with the *highest* ChatGPT intensity and
  the *lowest* Codex/API intensity, meaning high chat-assistant engagement
  does not predict agentic-tool engagement even within the same industry.
  This is useful counter-evidence against any assumption that "AI-mature"
  industries are uniformly ahead across every AI product category — maturity
  is metric-specific, not a single latent trait.

### Claim 10: AI agents need three things to complete meaningful work — context, tools, and persistence — with frontier firms distinguished by giving agents company context (memory, voice input, "appshots"), the ability to act (computer/browser use to navigate websites, create files, complete tasks), and the ability to keep working until a task is finished (goals and loops)
- **Evidence**: Enterprise Signals page's own explanatory framework for
  "how frontier firms put agents to work," describing named OpenAI product
  capabilities mapped to each of the three requirements.
- **Confidence**: settled as a vendor product-positioning framework, but
  anecdotal as an empirical claim (no data is given tying specific
  capability adoption to the frontier/typical gap measured elsewhere in the
  same report — it is a conceptual framework, not a measured result)
- **Quote**: "AI agents need three things to complete meaningful work: context, tools, and persistence. Memory, voice input, and appshots help workers to easily share the context and information necessary to successfully complete a task. Computer and browser use allow agents to navigate websites, create files, and complete tasks autonomously or under supervision. Goals and loops keep agents working until a task is finished."
- **Our assessment**: This is OpenAI's own three-part taxonomy for what
  agentic deployment requires, and it maps closely onto categories already
  established independently in the corpus's harness-engineering sources —
  "context" corresponds to this guide's Ch04 (Context Engineering) concerns,
  "tools" to Ch02's permission/tool-access model, and "persistence" (goals
  and loops) to the bounded-autonomy concept in
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
  Claim 10. Useful as a vendor-independent restatement of a three-part
  framework this guide already treats as foundational, not as new evidence
  for any one of the three parts individually.

### Claim 11: Frontier firms explicitly govern agent access — setting clear rules for where agents can operate, what information they can access, when they can take actions, and how people review higher-risk decisions — and treat these controls as something that "must evolve as organizations learn from real deployments"
- **Evidence**: Enterprise Signals page's own narrative description of
  frontier-firm governance practice, not accompanied by a specific
  statistic or named company example.
- **Confidence**: anecdotal (a general governance-practice assertion with no
  named firm, survey data, or specific control mechanism described —
  it is qualitative color, not a measured finding)
- **Quote**: "Giving agents access to company systems also introduces new risks. Frontier firms set clear rules for where agents can operate, what information they can access, when they can take actions, and how people review higher-risk decisions. These controls must evolve as organizations learn from real deployments."
- **Our assessment**: Directionally consistent with, but far less specific
  than, `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
  Claims 2-6 (the four-layer "organizational harness" model, typed
  constraint architecture, steering loops) and
  `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claims 2-4
  (governance must be built into the operating environment's "original DNA,"
  not retrofitted). This OpenAI claim is the vaguest version of the same
  idea in the corpus — it asserts governance matters without describing any
  concrete mechanism — so it should be cited as corroborating color for the
  governance-matters thesis, not as an independent source of governance
  design guidance; the Thoughtworks sources are the higher-value citations
  for actual implementation detail.

### Claim 12: In the academic working paper's linked public-company sample, ChatGPT Enterprise adopters are far larger and more R&D-intensive than non-adopters — median revenue $2,275.1M vs. $209.6M, median total assets $4,394.2M vs. $667.6M, median employment 2,934 vs. 424 workers, and median R&D expense $113.1M vs. $9.9M
- **Evidence**: Descriptive comparison of 2024 firm characteristics for
  ChatGPT Enterprise adopters vs. non-adopters within the Compustat
  U.S. public-company sample (working paper, Section 4.2, Figure 2).
- **Confidence**: emerging (specific, named financial medians from a
  disclosed public-company dataset (Compustat) and disclosed comparison year
  (2024), presented as unadjusted descriptive statistics rather than causal
  estimates — the paper itself flags that the follow-on regressions "should
  not be interpreted causally")
- **Quote**: "Median revenue is $2,275.1M for adopters versus $209.6M for non-adopters. Median total assets are $4,394.2M versus $667.6M, and median employment is 2,934 workers versus 424 workers... Median market value is $4,997.2M versus $316.4M, and the median research and development expenses are $113.1M among adopters, compared with $9.9M among non-adopters."
- **Our assessment**: This is the single most rigorously sourced claim in
  this note — a named, disclosed dataset (Compustat) with specific dollar
  medians, not a vendor-telemetry percentage. It substantiates, with real
  numbers, the blog post's much vaguer Claim (in the main article) that
  "enterprise adopters had stronger financial measures compared to
  non-adopters" — the blog post summarizes this finding without any of the
  specific medians, so a reader relying only on the short blog post would
  miss how large the adopter/non-adopter gap actually is (roughly
  11× revenue, 6.6× total assets, 6.9× employment, 11.4× R&D spend).

### Claim 13: Adoption probability rises sharply with firm scale even within the same industry — firms in the top revenue quartile are 6.9 percentage points more likely to adopt ChatGPT Enterprise than smaller firms, and firms in the top 5% of revenue are 9.8 percentage points more likely to adopt (11.3 percentage points when measured relative to same-industry peers)
- **Evidence**: Regression analysis (working paper Table 3, Section 4.2.3)
  relating lagged firm revenue to ChatGPT Enterprise adoption probability,
  with and without industry-relative scale measures following Autor et al.
  (2020)'s methodology.
- **Confidence**: emerging (disclosed regression specification and
  coefficients, explicitly caveated by the paper as describing "variation
  among relatively large firms" — U.S.-based public companies — and
  explicitly not generalizable to "small private firms, startups, or
  mid-market firms," where the paper says the relationship "could be
  steeper, flatter, or nonlinear")
- **Quote**: "Table 3 shows that a one-log-point increase in lagged revenue is associated with a 1.1 percentage point higher probability of adoption. This relationship is most pronounced at the top of the revenue distribution: firms in the top revenue quartile are 6.9 percentage points more likely to adopt, and firms in the top 5 percent are 9.8 percentage points more likely to adopt."
- **Our assessment**: This is a scale-of-adoption-probability claim, distinct
  from Claim 2's scale-of-usage-intensity claim (frontier vs. typical
  *among adopters*) — together they show large firms are both more likely
  to adopt at all, and (per the paper's Section 4.2.2, not separately
  claimed here) show higher per-employee revenue/valuation once they do,
  though the paper separately finds that *usage intensity per employee*
  among adopters is actually *lower* at larger firms (a mechanical scaling
  effect the paper attributes to organizational size, not weaker
  engagement). No existing source note in the corpus documents a
  firm-scale-vs.-adoption-probability regression; this is the most rigorous
  version of the "big firms adopt AI first" claim in the corpus to date. No
  corpus source directly contradicts this — the case-study sources
  (`blog-cursor-paypal-enterprise-adoption.md`,
  `blog-openai-virgin-atlantic-customer-journeys.md`) describe large
  enterprises moving fast on adoption, which is consistent with, not
  opposed to, this population-level finding, though those are individual
  anecdotes rather than population statistics.

### Claim 14: Within adopting firms, usage is broadly distributed across job functions and seniority levels — engineering/technical practitioners account for only about 11% of weekly active users six months after adoption, roughly matching executives/founders/partners at 9% — but early-career workers and trainees are the most intensive users, sending roughly eight to nine more weekly messages than the average active user at the same firm, while managers, directors, and executives send fewer
- **Evidence**: Working paper Sections 4.3.1–4.3.2 (Figures 5 and 6),
  worker-level analysis using job-title classification and firm-fixed-effects
  regressions on messages per active user, within a subset of firms with
  disclosed high-quality job-title data.
- **Confidence**: emerging (the paper explicitly discloses two
  interpretation limitations: job-title coverage is not universal or firm-
  representative, and active-user composition is not the same as a
  role-specific adoption *rate* since the denominator of all employees by
  role is not observed)
- **Quote**: "At the average firm, engineering and technical practitioners account for approximately 11% of weekly active users after six months, while executives, founders, and partners account for 9%... Among adopters, early-career workers and trainees send roughly eight to nine more weekly messages than the average active user within the same firm, while managers, directors, and executives send fewer messages."
- **Our assessment**: This is the working paper's most guide-relevant
  finding: engineering is not the dominant user population within adopting
  firms even at only 11% of weekly active users, and the intensity gradient
  runs opposite to seniority. This provides rigorous, firm-fixed-effects-
  regression backing for the same directional claim the shorter blog post
  makes more loosely in Claim 8 above, and is a stronger citation for that
  claim than the blog post's own "13 more messages than executives" figure,
  since the paper's methodology and sample are fully disclosed.

## Concrete Artifacts

```
Source: OpenAI, "From assistance to execution: How enterprises put AI to
work," https://openai.com/index/how-enterprises-put-ai-to-work
(August 12, 2026), plus companion pages:
  - "Enterprise Signals," https://openai.com/signals/enterprise-data/
    (updated August 12, 2026)
  - Chatterji, Holtz, Rakholia, Tambe, Weeratunga, "How Organizations Use
    AI: Evidence from ChatGPT" (OpenAI / Columbia Business School / Wharton
    School working paper, last updated August 11, 2026),
    https://cdn.openai.com/pdf/how-organizations-use-chatgpt.pdf

Headline frontier-gap trend (Enterprise Signals + blog post):
  Frontier firms (top 10% by output tokens/active user/month) vs.
  typical firms (45th-55th percentile):
    Jan 2026:  2.6x gap
    Jun 2026:  8.3x gap  (threefold increase in 5 months)
  By industry (Jun 2026):
    Widest gap:    Information and Technology   11.7x
    Narrowest gap: Manufacturing                 5.3x
    Typical-firm growth across industries: 1.9x-2.8x (comparatively flat)

Codex/ChatGPT enterprise token share:
  Jun 2026: Codex = 64% of combined Codex + ChatGPT enterprise output tokens

Advanced-capability weekly adoption (active users):
  Plugins: 21% frontier firms vs. 9% typical firms vs. 95% OpenAI internal
  Skills:  19% frontier firms vs. 3% typical firms

Weekly active enterprise Codex user growth since Feb 2026, by function:
  Legal:       108x
  Sales:        41x
  Recruiting:   41x
  Marketing:    26x
  Engineering:   5x  (smallest multiplier -- highest starting base)

Message-type composition (10M+ message enterprise sample):
  Coding + system/agent operations: ~75% of agentic (Codex) messages
  Non-technical functions' share of messages spent on system/agent ops:
    Recruiting:      32%
    Sales:           26%
    Policy:          25%
    Communications:  24%
  Design: coding = ~60% of agentic messages

Early-career vs. senior usage intensity:
  Blog: early-career workers send 13 more msgs/week than executives
        (6 months post-adoption, admin data from millions of conversations)
  Working paper (firm-fixed-effects regression): early-career workers and
        trainees send ~8-9 more weekly messages than the average active
        user at the same firm; managers/directors/executives send fewer

Industry AI-adoption ranking (no single leader; rankings vary by metric):
  Codex adoption & API intensity leader: Professional, Scientific &
                                          Technical Services
  ChatGPT adoption leader:                Arts, Entertainment & Recreation
  ChatGPT intensity leader:               Manufacturing (despite ranking
                                          LAST in Codex and API intensity)

Working paper (Compustat public-company sample, 2024 medians):
  Metric                     Adopters      Non-adopters
  Revenue                    $2,275.1M     $209.6M
  Total assets               $4,394.2M     $667.6M
  Employment                 2,934         424 workers
  Net PP&E                   $271.2M       $43.7M
  Market value               $4,997.2M     $316.4M
  R&D expense                $113.1M       $9.9M

Working paper (Table 3): adoption probability vs. firm revenue scale
  +1 log-point lagged revenue:        +1.1 pp adoption probability
  Top revenue quartile:                +6.9 pp
  Top 5% of revenue:                   +9.8 pp
  Top 5% of revenue (industry-relative, Autor et al. 2020 method): +11.3 pp

Working paper (Section 4.1): aggregate enterprise growth decomposition
  Total ChatGPT Enterprise output tokens, Jun 2025 -> Mar 2026:  ~7x growth
  Within a fixed Jan 2024-Jun 2025 adoption cohort, same window: ~4x growth
  (i.e., roughly half of aggregate growth came from within already-
  adopting firms, not just new-firm adoption)

Working paper (Section 4.3.1, Figure 5): active-user composition by job
title class, six months post-adoption, average firm:
  Engineering/technical practitioners:      ~11%
  Executives/founders/partners:              ~9%
  Finance & accounting:                      ~5%
  Marketing & communications:                ~5%
  Sales & account management:                ~4%
  (seniority distribution) Managers/directors: ~24%, ICs/professionals: ~15%,
  senior ICs/principals: ~14%, executives: ~10%, early-career/trainees: ~7%

Case study cited in the blog post (Virgin Atlantic, extends
`blog-openai-virgin-atlantic-customer-journeys.md`, which did not cover
this Codex/engineering detail):
  "Engineering teams use Codex to refactor legacy code in 30 minutes
  instead of two weeks. Their product teams use ChatGPT Work to complete
  weeks of competitive research in hours, shaping the airline’s five-year
  digital strategy."
```

## Cross-References

- **Corroborates**:
  - `blog-openai-agents-transforming-work.md` Claims 5-8 (OpenAI's own
    internal department-crossover timeline, non-developer growth
    multipliers, and the >25%-of-business-function-work-is-coding finding)
    — Claim 5 and Claim 7 of this note report an independent,
    cross-customer-base version of the same "non-engineering functions
    growing fastest from a low base" pattern, now a three-times-corroborated
    finding across internal-OpenAI, cross-enterprise, and (via
    `blog-openai-codex-knowledge-work.md` Claim 2) cross-product-wide
    populations.
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 6
    and `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 1 (competitive advantage and enterprise AI success come from
    organizational execution/orchestration, not model choice) — Claim 2 of
    this note (the frontier gap exists despite "the same AI models") is
    OpenAI's own vendor-side statistical confirmation of a thesis two
    independent Thoughtworks consultancy sources had already argued from
    client experience. This is a notable three-source convergence (one
    vendor with usage data, two consultancies with delivery experience)
    worth flagging in the guide as a well-triangulated claim.
  - `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge workers
    produce artifacts weekly, 47% do engineering ops, 46% do code
    implementation) — corroborated by this note's Claim 7 (non-technical
    functions devoting a quarter to a third of agentic messages to
    "system/agent operations").
- **Contradicts**: None identified. No existing source note makes a
  population-level statistical claim that smaller firms or startups adopt
  enterprise AI faster or more intensely than large firms; the closest
  candidates (`blog-cursor-paypal-enterprise-adoption.md`,
  `blog-openai-virgin-atlantic-customer-journeys.md`) are single-company
  case studies of large enterprises moving fast, which do not test the
  same population-level claim this note's Claim 13 makes (working paper,
  Table 3) and so are not in tension with it. No contradiction issue was
  filed per MINER.md §4a.
- **Extends**:
  - `blog-openai-virgin-atlantic-customer-journeys.md` — this note's
    Concrete Artifacts section captures a new Virgin Atlantic data point
    (Codex refactoring legacy code "in 30 minutes instead of two weeks")
    not present in the existing Virgin Atlantic note, which covered only
    the ChatGPT Work customer-journey-research and dashboard use cases
    (Claims 1-8 there). This is a genuinely new engineering-specific
    statistic about the same company, not a restatement.
  - `blog-openai-chatgpt-adoption-signals.md` — that note explicitly scopes
    itself to Individual (consumer) ChatGPT plans and states it should not
    be cited for enterprise/organizational claims (its Claim 7). This note
    is the enterprise-side counterpart the other note's own Guide Impact
    section anticipates needing; the two notes together give the corpus
    matched consumer and enterprise adoption pictures from the same vendor
    over a similar period (mid-2026), though measuring different products
    and populations.
- **Novel**:
  - The frontier/typical firm-gap framework itself (Claims 2-3) — no
    existing source note tracks a longitudinal enterprise usage-inequality
    metric with a disclosed percentile definition; this is the first
    "widening gap between AI leaders and laggards" statistic in the corpus
    backed by a named methodology rather than a single case-study anecdote.
  - The industry-adoption-leaderboard finding (Claim 9) that different AI
    products (ChatGPT vs. Codex vs. API) produce different industry
    leaders, with Manufacturing simultaneously topping ChatGPT intensity and
    trailing last in Codex/API intensity — a genuinely new "adoption
    maturity is metric-specific, not a single latent trait" finding.
  - The public-company financial-characteristics comparison (Claim 12) and
    firm-scale-adoption-probability regression (Claim 13) from the working
    paper — the corpus's first source connecting AI-tool adoption to
    disclosed public-company financial data (Compustat) rather than vendor
    usage telemetry alone.

## Guide Impact

- **Chapter 05 (Team Adoption)**: The frontier/typical gap (Claims 2-3) and
  its explicit "same models, different execution" framing is strong,
  well-triangulated evidence (see Cross-References → Corroborates) for
  Ch05's existing harness-rollout and measurement-framework material — cite
  alongside the Thoughtworks organizational-harness sources as
  quantitative backing for the qualitative "governance and rollout
  maturity separates leaders from laggards" argument already present in
  "The Empirical Anchor" and "Measuring Impact" sections. The
  early-career-usage-intensity finding (Claims 8, 14 — corroborated with
  firm-fixed-effects regression rigor in the working paper) supports any
  discussion in Ch05 of who within an organization to study or showcase
  when trying to spread effective AI practices, since it identifies a
  specific, statistically-grounded population (early-career workers, not
  executives or engineers specifically) as the most intensive users to
  learn from.
- **Chapter 05 (Team Adoption) — governance**: Claim 11 (frontier firms set
  clear rules for agent operating boundaries, data access, and review of
  higher-risk decisions) is directionally supportive but too vague to cite
  as a standalone recommendation; if Ch05 already cites the Thoughtworks
  organizational-harness sources for governance mechanics, this OpenAI
  claim can be added as a one-line "and vendors observe the same pattern
  from the demand side" corroboration, not as a primary source for
  governance design.
- **Chapter 00 (Principles)**: Claim 13's firm-scale-adoption-probability
  finding (working paper Table 3) is useful background for framing
  "AI-native" as currently concentrated among larger, more R&D-intensive
  organizations rather than a universal baseline — but the paper's own
  scope caveat (U.S. public companies only; the pattern "could be steeper,
  flatter, or nonlinear" for smaller/private firms) means this should be
  cited as a bounded, population-specific finding, not generalized to all
  organizations.
- **No chapter should cite the vendor-only statistics (Claims 1, 4, 5, 7, 9,
  10, 11) as precise, load-bearing benchmarks a reader's own organization
  should expect to replicate.** They are unaudited first-party telemetry
  with no disclosed sample sizes or classification methodology. The working
  paper's claims (12, 13, 14) are meaningfully stronger evidence — disclosed
  methodology, named academic co-authors, and an explicit working-paper
  caveat that results are subject to change — and should be preferred as
  citations wherever the guide needs one supporting statistic from this
  note rather than the shorter blog post's looser framing of the same
  underlying findings.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/how-enterprises-put-ai-to-work`)
  returned an HTTP 403 to both direct `curl` (with a browser user-agent) and
  the `WebFetch` tool — the response body was a Cloudflare/OpenAI
  bot-challenge placeholder page (`<meta http-equiv="refresh" content="360">`
  with a ChatGPT-branded loading animation), the same access pattern already
  documented for other `openai.com/index/` posts in this corpus (see
  `blog-openai-agents-transforming-work.md` and
  `blog-openai-virgin-atlantic-customer-journeys.md` Extraction Notes). The
  article was retrieved in full via the `r.jina.ai` reader proxy, fetched
  directly with `curl` (not through `WebFetch`, to avoid an extra
  LLM-summarization pass between the raw page and this note), which returned
  the complete page as Markdown. Every quote from the blog post and the
  Enterprise Signals page above was checked character-for-character against
  that fetched Markdown.
- Per MINER.md §1's instruction to follow substantive linked pages, this
  extraction fetched and fully read both companion sources the blog post
  explicitly announces ("Today we are publishing two complementary
  studies"): the Enterprise Signals page (also via `r.jina.ai`, full page
  recovered) and the linked working-paper PDF, which was directly
  downloadable (no bot-challenge on `cdn.openai.com`) and converted to text
  with `pdftotext -layout`. The paper is roughly 22 pages of body text
  (plus tables, references, and an appendix not read in full); this note
  extracted from the abstract, introduction, and Sections 4.1-4.4 (adoption
  growth, firm financial characteristics, worker composition, and task
  composition) and the conclusion, which together cover the paper's four
  headline "stylized facts." The paper's detailed regression tables
  (Tables 1, 2, and 4, covering additional financial-characteristic
  regressions not summarized above) and its appendix (additional figures
  A1-A8) were not individually extracted as separate claims — they refine
  rather than contradict the headline findings already captured in Claims
  12-14, and extracting each regression coefficient as a separate claim
  would have diluted rather than strengthened this note.
  This note did not attempt to read the paper's Section 3 (data/measurement
  methodology detail beyond what is summarized in the Source Context
  section above) or its full reference list.
- Three additional links from the main blog post were not independently
  fetched because dedicated source notes for them already exist in the
  corpus: `openai.com/index/how-agents-are-transforming-work/`
  (`blog-openai-agents-transforming-work.md`),
  `openai.com/index/virgin-atlantic/` (this note treats the specific "30
  minutes instead of two weeks" Codex-refactoring quote as new since the
  existing Virgin Atlantic note does not contain it, but did not re-extract
  the rest of that case study), and `openai.com/index/chatgpt-for-your-most-ambitious-work/`
  (`blog-openai-chatgpt-work-ambitious-partner.md`). This keeps the "up to
  5 linked pages" extraction budget focused on the two genuinely
  unmined companion studies (Enterprise Signals and the working paper)
  rather than re-extracting already-covered case studies.
- No footnote markers or embedded-chart data-recovery issues were
  encountered in the blog post or Enterprise Signals page text (unlike
  several other OpenAI `index/` posts in this corpus) — the one industry-
  ranking table on the Enterprise Signals page (Claim 9) rendered with
  usable cell values in the `r.jina.ai` Markdown conversion, unlike the
  heat-map chart problem documented in
  `blog-openai-agents-transforming-work.md` Claim 9's Extraction Notes.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- This note deliberately covers three linked documents under one issue/PR
  rather than three separate source notes, because the blog post explicitly
  presents the Enterprise Signals page and the working paper as two halves
  of a single announced finding ("two complementary studies that examine
  this shift"), and the issue (#2861) was filed against the synthesis blog
  post URL specifically. If the Prospector or Assayer judge that the working
  paper warrants its own dedicated source note (it is dense enough — 22
  pages, five tables, an appendix — to support one), a follow-up mining pass
  focused solely on the paper's regression tables and appendix figures could
  extract additional claims beyond what is captured here.
