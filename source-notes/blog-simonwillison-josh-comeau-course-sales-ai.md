---
source_url: https://simonwillison.net/2026/Jul/3/josh-w-comeau/
source_type: blog-post
title: "Quoting Josh W. Comeau"
author: Josh W. Comeau (quoted by Simon Willison, via Salma Alam-Naylor)
date_published: 2026-07-03
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: anecdotal
issue: "#1646"
---

# Quoting Josh W. Comeau: AI's Impact on Developer-Education Course Sales

> Simon Willison re-quotes a Bluesky thread by developer educator Josh W. Comeau (creator
> of "CSS for JS Devs" and "Whimsical Animations"), in which Comeau reports his new
> course launched at roughly ⅓ of typical sales, attributes the decline mainly to a
> "double whammy" of job-security anxiety and free LLM tutoring, and relays that peer
> course creators are seeing "Revenue down 50%+." The quote was surfaced via a DevRel
> practitioner's essay on leaving the industry, which frames the same trend as "AI is
> killing developer education."

## Source Context

- **Type**: blog-post (Simon Willison's link-blog "quotation" format — a single blockquote
  plus a one-line attribution, no original Willison commentary on this entry). The
  quotation is drawn from a Bluesky thread by Josh W. Comeau and was itself relayed via
  Salma Alam-Naylor's essay "Goodbye, forever, probably." Per MINER.md §1, both the
  original Bluesky thread (fetched via the public Bluesky API, `at://` URI for the root
  post `3mkxyqfwwm22t`) and Alam-Naylor's essay (`whitep4nth3r.com/blog/goodbye-forever-probably/`)
  were read in full as substantive linked pages, since Willison's own page is a single
  four-paragraph blockquote with no additional framing of its own.
- **Author credibility**: Josh W. Comeau is a professional developer educator — creator of
  the paid courses "CSS for JS Devs," "The Joy of React," and "Whimsical Animations," and
  author of a widely-read technical blog (self-reported 1.4 million visitors in 2025, per
  the Bluesky thread). He speaks from direct, first-party business data (his own course
  sales), not survey or secondary reporting. Salma Alam-Naylor, who relayed the quote, is
  a self-described "web developer, international speaker, tech educator" with five and a
  half years in developer relations (DevRel), writing about her own decision to leave the
  industry. Willison is the curator; he adds no independent verification or commentary to
  this specific entry.
- **Scope**: Covers one educator's self-reported course-sales decline, his own causal
  attribution (unverified, first-person), and secondhand claims about "a few" unnamed peer
  course creators' revenue trends. Does NOT cover: audited financial data, a defined
  sample of course creators, control for non-AI causes (e.g., general e-learning market
  saturation, the specific niche appeal of the "Whimsical Animations" topic), or any
  employer-side/aggregate labor-market data.

## Extracted Claims

### Claim 1: Comeau's third course launch sold at roughly ⅓ the volume of a typical course launch, and his two existing courses show a significant year-over-year sales decline
- **Evidence**: First-party, self-reported sales data from the course creator himself, posted publicly on Bluesky.
- **Confidence**: anecdotal (single-source, self-reported, no comparison methodology disclosed for what counts as "typical")
- **Quote**: "I just launched my third course, Whimsical Animations, and so far, it's on track to sell roughly ⅓ as many copies as a typical course launch. It's a similar story with my two existing courses. Sales are down significantly from last year."
- **Our assessment**: A concrete, falsifiable, first-party number, which is stronger evidence than most anecdotal reports in this space. But Comeau himself later qualifies it in the same thread (see Claim 6): the ⅓ figure specifically compares against the course's own "Early Access" launch, not a generic "typical" launch, which is a narrower and more favorable comparison than the quoted sentence implies in isolation.

### Claim 2: Comeau attributes the decline mainly to AI, via a "double whammy" — job-security anxiety suppressing skills investment, and free LLM tutoring substituting for paid courses
- **Evidence**: The educator's own causal reasoning, stated as his top-line explanation in the same public thread.
- **Confidence**: anecdotal (stated as personal belief — "I think" — not measured or attributed to any data source)
- **Quote**: "There are likely a lot of reasons for this, but I think the biggest is AI. There's sort of a double whammy with AI: 1. Many people are wondering whether developer jobs will even exist in a few months, so they're reluctant to spend time/money learning new dev skills. 2. Even if they do want to learn new dev skills, LLMs can provide personalized tutoring, so there's less incentive to buy a paid course."
- **Our assessment**: Comeau explicitly flags this as a belief ("I think"), not a measured finding — no A/B test or survey isolates AI from other explanations (economic conditions, market saturation, the niche appeal of animation as a topic). Still, the two-mechanism framing is useful: it separates a *perception* effect (job anxiety, regardless of whether layoffs are real) from a *substitution* effect (LLMs as free competing product), which are analytically distinct and each independently checkable against other sources.

### Claim 3: Comeau personally pushes back on his own "job security" explanation — he does not believe full automation of engineering is imminent
- **Evidence**: The same author's immediate self-qualification, later in the same thread.
- **Confidence**: anecdotal (personal opinion)
- **Quote**: "For #1, I really don't believe we're on the cusp of being able to hand all engineering off to robots."
- **Our assessment**: Notable because Comeau is describing a behavioral effect (reduced training spend) that he attributes to a belief he personally thinks is mistaken. This matches the "AI washing" / perception-vs-reality gap already documented in this guide's corpus (see Cross-References) — the anxiety driving reduced course purchases doesn't require the underlying "developer jobs won't exist" belief to be true, only widely held.

### Claim 4: On the "free AI tutoring" mechanism, Comeau argues LLMs cannot replace a course's curated learning path because they can only answer questions the learner already knows to ask
- **Evidence**: The author's own argument, drawing on his experience designing structured curricula.
- **Confidence**: anecdotal (practitioner reasoning, not tested)
- **Quote**: "it's absolutely true that AI can be fantastic learning tool, but it can only answer the questions that you know to ask. There's a vast ocean of knowledge out there, and until you become an expert, it's hard to tell which parts are important (or true, for that matter 😅)."
- **Our assessment**: A specific, checkable mechanism (curation vs. Q&A retrieval) rather than a vague "AI is bad for learning" claim. It identifies a structural limitation of LLM tutoring — the "unknown unknowns" problem — that is independent of model capability and therefore unlikely to be resolved by better models alone, which is a useful framing for any guide section that touches on using LLMs for self-directed upskilling.

### Claim 5: Comeau relays that multiple (unnamed) peer course creators report the same trend: revenue down 50%+, falling engagement, and users switching to LLMs that "slurp up" their content without compensation
- **Evidence**: Secondhand, informal conversations with "a few course creators" — not named, sized, or sourced beyond the author's own network.
- **Confidence**: anecdotal (secondhand, unnamed sample, no size or selection methodology given)
- **Quote**: "I've spoken to a few course creators now, and we're all seeing the same trend. Revenue down 50%+. Fewer people engaging with our content. People switching to LLMs, which slurp up all of our work and regurgitate it, without consent or compensation."
- **Our assessment**: The weakest-sourced claim in the thread — an informal, self-selected sample reported secondhand with no names or numbers beyond "a few" and "50%+." The "consent or compensation" framing is an IP/training-data-ethics complaint layered onto the revenue claim, not a separate empirical observation. Useful only as color/directional signal, not as a market-size estimate.

### Claim 6: Comeau later qualifies the ⅓-of-typical figure — it specifically compares against the same course's own Early Access launch, and the course remains profitable even at ⅓ volume
- **Evidence**: The author's own follow-up reply in the same thread, responding to a commenter.
- **Confidence**: anecdotal (self-reported, but this is the author correcting/narrowing his own headline claim, which increases trust in this specific correction)
- **Quote**: "that 1/3rd number is actually compared to the \"Early Access\" launch of the same animations course... But yeah, truthfully even at 1/3rd it's still profitable. It's just hard to know if this is the floor or not 😅. It takes me like 2 years to make a course, so it's hard to commit to that without knowing whether anyone will want it when it's ready."
- **Our assessment**: This materially softens Claim 1. The headline "⅓ as many copies as a typical course launch" (as quoted by Willison, without this follow-up context) reads as a business in crisis; the fuller thread shows a business that is down but still profitable, with genuine uncertainty about the trend line rather than a confirmed collapse. Any guide citation of the "⅓" figure should include this qualification — Willison's re-quote (the actual issue source) omits it entirely.

### Claim 7: Comeau's business model depends on a very small conversion rate from a large free blog audience — a "fraction of 1%" of ~1.4 million annual blog visitors fund his ~10-15 hours/week of blog writing by buying courses
- **Evidence**: The author's own description of his funnel and time allocation.
- **Confidence**: anecdotal (self-reported, no verification of visitor or conversion figures)
- **Quote**: "In 2025, 1.4 million people visited the blog, a number that still blows my mind. 😅" / "I am able to dedicate that much time because a tiny percentage (a fraction of 1%) will go on to buy one of my courses."
- **Our assessment**: This is the structural context that makes Claims 1 and 5 consequential rather than incidental — because the free content (blog) is subsidized entirely by course conversions, even a moderate drop in course sales threatens the free content pipeline too, not just the paid product. This is the same free-content-subsidized-by-a-tiny-paid-tail model that underlies much independent technical blogging and open-source-adjacent education.

### Claim 8: Salma Alam-Naylor, writing independently as a DevRel practitioner, frames the same trend as "AI is killing developer education," citing search-traffic fragmentation and the disappearance of developer community spaces alongside Comeau's numbers
- **Evidence**: A named DevRel practitioner's own essay (not Comeau's data), published the day before Willison's post, explaining her decision to leave the DevRel industry.
- **Confidence**: anecdotal (a second practitioner's independent first-person account, but still self-reported and not measured)
- **Quote**: "People aren't seeking information in the ways we once knew; The Internet and its communities have fragmented. It is now more and more difficult to use search engines to actually search for real and accurate information as a result of imposing AI overviews and the swathes of new AI slop articles that are poor regurgitations of stolen content that have been eating themselves for quite some time."
- **Our assessment**: This is independent corroboration from a different practitioner in a related-but-distinct role (DevRel/community, not direct course sales), citing a different mechanism (search/discovery fragmentation rather than direct LLM substitution) for a similar outcome — developer-facing content and community engagement declining. Two independent first-person accounts converging on "AI is disrupting developer-education economics," via different causal paths, is more useful than either alone, though both remain anecdotal.

### Claim 9: A second, unnamed "very talented developer educator" (quoted by Alam-Naylor) describes online developer community spaces as having emptied out across every major platform
- **Evidence**: A third, anonymous practitioner's account, relayed by Alam-Naylor within her essay.
- **Confidence**: anecdotal (anonymous, secondhand within a secondhand source)
- **Quote**: "The entire vibe has shifted. The majority of [community] folks are still on Twitter but there's so much AI grifting and misery and hate in that place. LinkedIn is a parody of itself at this point. Bluesky feels reasonably cosy but way too much of a bubble. The community isn't there. The forums are dead, the new Discord is quiet."
- **Our assessment**: Third-hand and anonymous, so treat as the weakest evidence in this note — included only because it's a concrete, specific description (named platforms, specific complaint per platform) rather than a vague "things feel different," which makes it at least a checkable set of claims if corroborated elsewhere in the corpus later.

## Concrete Artifacts

```
Source: Josh W. Comeau, Bluesky thread, root post at://did:plc:zivbusxwcsom5o6mf7kljzms/
        app.bsky.feed.post/3mkxyqfwwm22t, posted 2026-05-03T20:29:45Z (fetched via the
        public Bluesky API, app.bsky.feed.getPostThread). Willison's page quotes only a
        contiguous subset of this thread (paragraphs 5-6 and 11 below), joined with "[...]".

Full first-party thread, in order (each paragraph = one Bluesky post in the same thread):

  1. "For the past 6 years, I've been working on developer education full time, on my
     online courses + blog. It's been an incredible privilege to be able to focus on this
     stuff. ✨ I'm starting to wonder, though, whether the business model I've chosen is
     sustainable."

  2. "Most people discover my work through my blog (www.joshwcomeau.com). My blog is not
     directly monetized at all: no ads, no affiliate links, no sponsored content. In 2025,
     1.4 million people visited the blog, a number that still blows my mind. 😅"

  3. "I put a lot of work into my blog. On average, I spend ~10-15 hours/week on the blog.
     It's basically a part-time job. I am able to dedicate that much time because a tiny
     percentage (a fraction of 1%) will go on to buy one of my courses."

  4. "It's actually quite lovely; everyone who buys one of my courses effectively makes it
     possible for hundreds of other people to benefit from my work for free. ❤️ This model
     worked incredibly well for me, from 2020 to 2025, but it's a bit of a different story
     in 2026. 😕"

  5. "I just launched my third course, Whimsical Animations, and so far, it's on track to
     sell roughly ⅓ as many copies as a typical course launch. It's a similar story with my
     two existing courses. Sales are down significantly from last year."

  6. "There are likely a lot of reasons for this, but I think the biggest is AI. There's
     sort of a double whammy with AI: 1. Many people are wondering whether developer jobs
     will even exist in a few months, so they're reluctant to spend time/money learning new
     dev skills."

  7. "2. Even if they do want to learn new dev skills, LLMs can provide personalized
     tutoring, so there's less incentive to buy a paid course. For #1, I really don't
     believe we're on the cusp of being able to hand all engineering off to robots."

  8. "And for #2, it's absolutely true that AI can be fantastic learning tool, but it can
     only answer the questions that you know to ask. There's a vast ocean of knowledge out
     there, and until you become an expert, it's hard to tell which parts are important (or
     true, for that matter 😅)."

  9. "One of the biggest benefits of a course, IMO, is that it provides a curated learning
     path. I've learned a lot of random stuff throughout my career, and in my courses, I
     try to shuck away all of the inessential bits so that students don't have to waste as
     much time as I did. 😂"

 10. "And maybe LLMs can provide that too, when given the right prompts. And maybe that's a
     good thing; ideally, it shouldn't cost any money to learn stuff. But I sorta worry
     about how this is supposed to work, going forwards, if there's no incentive for people
     to make high-quality free content."

 11. "I've spoken to a few course creators now, and we're all seeing the same trend.
     Revenue down 50%+. Fewer people engaging with our content. People switching to LLMs,
     which slurp up all of our work and regurgitate it, without consent or compensation. It
     feels pretty bleak. 😅"

Later thread reply (2026-05-05, to a commenter named Alexandre):
  "And yeah, I can definitely see how my CSS/React courses are more practical, they have a
  more obvious benefit when it comes to your career. But that 1/3rd number is actually
  compared to the "Early Access" launch of the same animations course. Which could mean
  that most people who wanted that course already bought it when it first went on sale, in
  Sept 2025. But with my previous courses, the EA launch and the full launch were similar
  in size, so it does break the trend a bit. But yeah, truthfully even at 1/3rd it's still
  profitable. It's just hard to know if this is the floor or not 😅. It takes me like 2
  years to make a course, so it's hard to commit to that without knowing whether anyone
  will want it when it's ready."
```

```
Source: Simon Willison's page (simonwillison.net/2026/Jul/3/josh-w-comeau/) — the actual
        blockquote text as re-published, showing which parts of the thread Willison chose
        to quote and where he elided text with "[...]":

  "I just launched my third course, Whimsical Animations, and so far, it's on track to
  sell roughly ⅓ as many copies as a typical course launch.

  It's a similar story with my two existing courses. Sales are down significantly from
  last year.

  There are likely a lot of reasons for this, but I think the biggest is AI. There's sort
  of a double whammy with AI:

  1. Many people are wondering whether developer jobs will even exist in a few months, so
  they're reluctant to spend time/money learning new dev skills.
  2. Even if they do want to learn new dev skills, LLMs can provide personalized tutoring,
  so there's less incentive to buy a paid course.

  [...] I've spoken to a few course creators now, and we're all seeing the same trend.
  Revenue down 50%+. Fewer people engaging with our content. People switching to LLMs,
  which slurp up all of our work and regurgitate it, without consent or compensation."

  — Josh W. Comeau, via Salma Alam-Naylor

Tags on Willison's page: careers, ai, generative-ai, llms, josh-comeau, ai-ethics.
```

```
Source: Salma Alam-Naylor, "Goodbye, forever, probably." (whitep4nth3r.com), 2026-07-02,
        section "AI is killing developer education":

  "These feelings of instability, anxiety and unease are even more pervasive now in 2026,
  as the way people learn and explore technology has changed significantly since the
  mass-adoption of generative AI tools. Google has declared war on the web. People aren't
  seeking information in the ways we once knew; The Internet and its communities have
  fragmented."

  "Freelance educators are also being impacted by this shift. Josh W. Comeau, author of
  incredible industry-defining courses like Whimsical Animations, recently shared on
  Bluesky that he has doubts about how sustainable his business model is:" [followed by
  the Comeau quote reproduced above]

  "The future feels bleak for educators. Rich curriculums we craft intentionally and
  carefully for real human audiences are now routinely stolen and regurgitated by
  predictive algorithms. The Chat Bots, with their sycophantic tone of voice, are
  deliberately engineered to erase our own personalities, hard work and craft entirely
  from the equation."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 11
  ("aggregate software labor demand will likely remain healthy but individual engineers
  may still face rocky career paths as roles and expectations shift") and Claim 2 ("AI
  washing" — companies and, by extension, individuals over-attribute economic pressure to
  AI relative to what employment data supports). Comeau's Claim 2 and Claim 3 in this note
  are a concrete, first-person instance of exactly the psychological/behavioral effect
  that source describes: he names "job security uncertainty" as suppressing his students'
  training spend while explicitly *not believing* the underlying "developer jobs won't
  exist" premise himself (Claim 3) — i.e., the perception is driving economic behavior
  independent of whether it is empirically justified, which is the same dynamic that
  source's "AI washing" finding describes from the employer side.
- **Corroborates**: `discussion-hn-agentic-coding-jobs.md` Claim 1 (Zapier now explicitly
  requiring agentic-only coding as a baseline job expectation) — an employer-side signal
  consistent with the job-security anxiety Comeau reports his prospective students feeling
  (Claim 2), even though neither source establishes that the anxiety is proportionate to
  actual displacement risk.
- **Extends**: `blog-openai-codex-knowledge-work.md` Claim 3 (OpenAI reports Codex's
  "personal users" segment growing faster than developers, with substantial use in
  "education and self-learning"). That source documents the demand-side of the same
  phenomenon Comeau describes from the supply side: OpenAI's own telemetry shows people
  using an AI agent for self-directed learning, and Comeau's course-sales data is a
  concrete casualty report from a paid-education business competing with that same free
  substitute. The two sources were not previously connected in the corpus.
- **Contradicts**: No contradiction issue filed. `blog-simonwillison-why-ai-hasnt-
  replaced-engineers.md`'s WARN Act finding (zero AI-attributed layoffs in the first full
  year of mandatory NY disclosure) could superficially appear to conflict with Comeau's
  claim that "many people are wondering whether developer jobs will even exist in a few
  months," but these are different claims about different things — one is measured
  employment-loss data, the other is self-reported anxiety/perception among Comeau's
  prospective customers. Per MINER.md §4a, this is a conditioning-variable distinction
  (actual layoffs vs. perceived job-security risk), not a factual contradiction, so no
  issue was filed.
- **Novel**: This is the first source note in the corpus with first-party, named-creator
  revenue/sales figures for a developer-education business directly attributed to AI
  (course-launch volume, blog-to-course conversion funnel economics), the "double whammy"
  framing (job-anxiety-driven training pullback + free-AI-tutoring substitution) as a
  named educator's own analytical model, and the "slurp up... without consent or
  compensation" framing of LLM training-data use as a lived economic grievance rather than
  an abstract IP-policy debate. Salma Alam-Naylor's independent corroboration (Claim 8-9)
  is also the corpus's first DevRel-practitioner account of AI-driven search/community
  fragmentation as a parallel, distinct mechanism affecting the same market.

## Guide Impact

- **Chapter 05 (Team Adoption)**: The Prospector's triage correctly scopes this as
  market-context evidence, not harness-engineering guidance. Specific, actionable use: if
  the guide discusses building *internal* enablement/training programs for AI-native
  engineering, this source is evidence that the *external* paid-training market
  (courses, workshops) is contracting under the same AI pressure the guide is trying to
  help teams navigate — meaning teams may increasingly need to build internal training
  capacity rather than assume external courses will remain available or current. This
  should be cited as anecdotal, single-practitioner-plus-corroboration evidence, not as a
  market-size statistic (per Claim 5 and Claim 6's caveats).
- **Chapter 05 (Team Adoption)**: Claim 4 (LLMs "can only answer the questions that you
  know to ask," so curated learning paths retain value over ad hoc LLM tutoring) is a
  specific, reusable argument for any guide section that discusses using LLMs for
  onboarding or upskilling engineers — it identifies a concrete limitation (the
  unknown-unknowns problem) rather than a vague objection, and pairs well with a
  recommendation that teams pair LLM-assisted self-study with structured curricula rather
  than treating LLM Q&A as a full substitute.
- No other chapter should cite the "50%+" revenue-decline figure (Claim 5) or the "⅓"
  launch figure (Claim 1) as load-bearing quantitative evidence — both are unaudited,
  single-source or unnamed-secondhand self-reports, and Claim 6 shows the headline figure
  softens materially under the author's own follow-up context.

## Extraction Notes

- The issue's source URL is Simon Willison's page, which is a single re-quoted blockquote
  with no original Willison commentary — a genuinely thin primary source on its own. Per
  MINER.md §1, two linked pages were followed and read in full: (1) the original Bluesky
  thread (fetched via the public, unauthenticated Bluesky AppView API rather than the
  bsky.app web UI, since the web UI requires a logged-in session to render), which
  contains substantially more context than Willison's excerpt, including Comeau's own
  self-qualification of the headline "⅓" figure (Claim 6) that does not appear anywhere
  in Willison's re-quote; and (2) Salma Alam-Naylor's essay, which is where Willison's
  "via" attribution points and which independently corroborates the same trend from a
  DevRel/community-fragmentation angle (Claims 8-9).
- All direct quotes from the Bluesky thread are copied verbatim from the `record.text`
  field of the Bluesky API's `app.bsky.feed.getPostThread` response (JSON), which
  preserves the author's original curly-apostrophe/em-dash typography; quotes from
  Willison's and Alam-Naylor's pages are copied verbatim from their rendered HTML with
  only HTML entities (`&#39;`, `&quot;`, `&rsquo;`, `&mdash;`) resolved to their literal
  characters, no other changes.
- date_published in the frontmatter is Willison's post date (2026-07-03), the canonical
  source URL per the issue. The underlying Bluesky thread was originally posted
  2026-05-03; Alam-Naylor's essay was published 2026-07-02. All three dates are noted
  inline in the Concrete Artifacts section above.
- This source is thin by design (a single social-media quotation), which caps how many
  genuinely distinct claims it can support even after following linked context — 9 claims
  were extracted, at the lower end of MINER.md's 5-15 guideline, and three of them
  (Claims 3, 4, 9) are short single-sentence asides rather than fully developed arguments.
  No further substantive linked pages were identified beyond the two followed (Comeau's
  linked newsletter post, referenced in passing in thread post 7, was not followed, since
  it is about AI capability limits generally and not about course-sales economics — it
  would extend `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`'s territory rather
  than this note's).
