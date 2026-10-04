---
source_url: https://openai.com/index/grab-openai-ai-skills-southeast-asia
source_type: blog-post
title: "Grab and OpenAI bring practical AI skills to Southeast Asia"
author: OpenAI
date_published: 2026-09-23
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: anecdotal
issue: "#3891"
---

# Grab and OpenAI bring practical AI skills to Southeast Asia

> OpenAI and Grab announce "GO Forward with AI", a two-year, 30,000-person workshop programme for gig-economy partners; it contributes a small amount of adoption-survey data and a train-the-trainer rollout pattern, but almost nothing about engineering practice.

## Source Context

- **Type**: blog-post (vendor announcement, OpenAI "Global Affairs" category)
- **Author credibility**: OpenAI corporate. Quotes from OpenAI's Managing Director, International, and Grab's Chief Organisational Capability Officer. The survey figures are attributed to Grab and are not independently documented.
- **Scope**: Announces a skilling programme for Grab driver-, delivery-, and merchant-partners (not employees, not engineers). It covers rollout geography, workshop format, and motivation. It has no outcome metrics, no evaluation design, and no technical detail. The programme has just launched, so there are no results.

## Extracted Claims

### Claim 1: A Grab survey in Singapore found half of driver/delivery partners already use AI tools, and most non-users are open to trying them
- **Evidence**: Grab survey of Singapore driver-partners, cited by OpenAI. No sample size or method given.
- **Confidence**: anecdotal
- **Quote**: "half of Grab’s driver and delivery partners said they use AI tools. Among those who do not, 87% said they were open to trying them."
- **Our assessment**: A rare data point on AI uptake among non-office, non-technical workers. It is a single-city, vendor-cited survey with no methodology, and it concerns general ChatGPT use rather than agentic engineering workflows. The article also says ChatGPT "was the tool they knew best", so the sample is probably skewed toward one tool.

### Claim 2: The programme is designed around the decisions participants already face, rather than around tool features
- **Evidence**: Design description with examples (business idea exploration, sales-pattern analysis, promotion planning, demand changes).
- **Confidence**: anecdotal
- **Quote**: "We’ve designed GO Forward with AI around the decisions many of them face."
- **Our assessment**: This matches the "start from a real problem" enablement pattern in other notes. It is stated as design intent, with no evidence it works better than alternatives.

### Claim 3: Hands-on workshops have participants run agentic tasks on larger work, then review the output and make the follow-on decisions
- **Evidence**: Workshop description. Example tasks are a sales-data dashboard, a simple website, and an expansion plan.
- **Confidence**: anecdotal
- **Quote**: "They’ll review what it produces and make the decisions that follow."
- **Our assessment**: The human-reviews-agent-output loop is in the curriculum for non-engineers too. The article gives no verification technique beyond "review". The agent product is named "ChatGPT Work", and the article does not describe how it works.

### Claim 4: Programme rollout is train-the-trainer, adapted per country
- **Evidence**: Rollout plan: half-day in-person workshops, based on the OpenAI Academy curriculum, with GrabAcademy trainers trained to scale delivery.
- **Confidence**: anecdotal
- **Quote**: "We’ll also train GrabAcademy trainers so they can bring the programme to more people over time."
- **Our assessment**: This is the most transferable operational detail. It reuses an existing internal academy as the distribution channel and uses a vendor curriculum as the base. There are no cost, throughput, or quality figures.

### Claim 5: Rollout is phased by country over roughly two years, starting in Singapore
- **Evidence**: Stated schedule.
- **Confidence**: anecdotal
- **Quote**: "It begins in Singapore and will expand to Thailand, Indonesia and the Philippines later this year, followed by Malaysia and Vietnam in 2027."
- **Our assessment**: The 30,000-person target over two years is a plan, not a result. Treat it as an intention only.

### Claim 6: A prior deployment, the Grab Driver AI Assistant, is the stated precedent, reaching close to 500,000 drivers
- **Evidence**: OpenAI statement about the collaboration since 2024.
- **Confidence**: anecdotal (vendor-reported reach; "reached" is not the same as active use)
- **Quote**: "Powered by OpenAI models, it helps drivers find demand, make the most of their time and get answers to everyday questions. It has reached close to 500,000 drivers."
- **Our assessment**: It shows a product-first, then skilling-second sequence. There is no usage depth, retention, or earnings-impact data.

### Claim 7: The framing is that training lets individuals do work that previously needed a team
- **Evidence**: Grab executive statement (no data).
- **Confidence**: anecdotal
- **Quote**: "With the right training, they can use AI to take on more of that work themselves."
- **Our assessment**: This is the same leverage narrative as Grab's engineering-side account (see Cross-References). Here it is aspirational, aimed at merchants and gig workers.

## Concrete Artifacts

```
Programme facts (OpenAI announcement, 2026-09-23):
- Name: GO Forward with AI (part of "OpenAI for Singapore")
- Target: 30,000 Grab driver-, delivery-, merchant-partners over two years
- Format: half-day, in-person workshops, OpenAI Academy curriculum adapted per country
- Scaling mechanism: GrabAcademy trainers trained to deliver
- Sequence: Singapore -> Thailand, Indonesia, Philippines (2026) -> Malaysia, Vietnam (2027)
- Survey (Grab, Singapore driver-partners): ~50% use AI tools; 87% of non-users open to trying
- Precedent: Driver AI Assistant (OpenAI models, since 2024), ~500,000 drivers reached
```

## Cross-References

- **Corroborates**: `blog-openai-academy-learning-paths.md` Claim 8 (practice on real tasks as the pedagogy). This announcement applies the same workshop-on-real-work approach to a non-office audience. `blog-cursor-grab-cross-functional-adoption.md` Claim 10 (enablement, not mandate, starting from a real problem) and Claim 9 (multi-country workshops) describe the same company running workshops internally.
- **Contradicts**: None found.
- **Extends**: `blog-openai-academy-learning-paths.md` Claim 3 (human retains responsibility for the final result). Here the same review-and-decide framing reaches gig workers. `blog-openai-academy-training-courses.md` is the curriculum base.
- **Novel**: The train-the-trainer delivery through an internal academy and the survey-based adoption baseline for gig workers are new to the corpus. Nothing here concerns coding agents, harnesses, or verification.

## Guide Impact

- **Chapter 05 (Team adoption)**: At most, a one-line supporting example for the claim that adoption programmes work best when anchored to participants' real decisions and scaled through trainers of trainers (Claim 2, Claim 4). Do not add it as evidence of effectiveness. There are no outcome data.
- **Other chapters**: No change recommended. The source is not about engineering workflows.

## Extraction Notes

- The live openai.com URL returned HTTP 403 to automated fetches. The full article text was read from a web.archive.org snapshot of the same URL, and quotes were copied from it. The Assayer may need to check quotes against that snapshot or a browser.
- The article is short and marketing-oriented. No linked sub-pages were followed (OpenAI Academy and OpenAI for Singapore are covered by existing notes or are policy pages).
- The Prospector's triage comments were generic; the source turned out to be a skilling announcement, not a deployment or operations case study. Value to the guide is low.
