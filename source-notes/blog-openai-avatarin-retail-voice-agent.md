---
source_url: https://openai.com/index/avatarin
source_type: blog-post
title: "How avatarin built a 24/7 retail agent with GPT‑Realtime"
author: OpenAI (customer case study; named quotes from Akira Fukabori, CEO, avatarin)
date_published: 2026-07-30
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: anecdotal
issue: "#2570"
---

# How avatarin built a 24/7 retail agent with GPT‑Realtime

> An OpenAI customer case study on avatarin (an ANA Holdings spin-out) building
> the "Kurashi-Marugoto AI Agent" for Yamada Denki — a GPT‑Realtime-based,
> RAG-grounded voice/text/image shopping agent that guided ~30,000 shoppers
> through home-appliance purchase decisions over a two-week public campaign
> with 92% positive survey feedback, plus avatarin's named three-part design
> philosophy (accurate-but-fast grounding, sales-expertise-as-conversation-design,
> proactive questioning) and its "One Intelligence. One Brand. Every interface."
> cross-channel vision.

## Source Context

- **Type**: blog-post (OpenAI "Customer Stories" case study,
  `openai.com/index/avatarin`, published July 30, 2026; ~750 words,
  auto-discovered via the `openai-news` trusted feed). Structured with a
  company metadata block (Company size: Startup, Region: Asia-Pacific &
  Oceania, Industry: Retail, Technology, Products: API) and a two-metric
  "Results" stat callout, consistent with the template already documented
  for Cars24 (`blog-openai-cars24-conversation-scaling.md`), BBVA
  (`blog-openai-bbva-banking-transformation.md`), and Samsung
  (`blog-openai-samsung-chatgpt-codex-deployment.md`).
- **Author credibility**: House-authored OpenAI promotional copy — OpenAI has
  a direct commercial incentive to present GPT‑Realtime favorably. One named
  individual is quoted throughout: Akira Fukabori, CEO of avatarin. No
  Yamada Denki/Yamada Holdings executive is quoted directly, despite Yamada
  being the retail partner whose sales expertise and store brand the agent
  represents. No third-party verification of the two headline metrics
  (~30,000 users, 92% positive) is given — no survey methodology, sample
  size relative to total users, or question wording is disclosed.
- **Scope**: Covers (1) the business context (Japanese home-appliance retail
  staffing/hours constraint), (2) why avatarin selected GPT‑Realtime over
  specialized speech-recognition systems, (3) avatarin's three-part agent
  design philosophy (RAG-grounded accuracy, sales-expertise-encoded
  conversation design, proactive questioning), (4) the nature of OpenAI's
  direct implementation support (prompt structuring, API cost optimization,
  best-practice sharing), (5) outcome figures and qualitative shopper
  feedback from a two-week public campaign, and (6) avatarin's forward-looking
  "One Intelligence. One Brand. Every interface." cross-channel vision. Does
  NOT cover: any technical/architectural detail of the RAG pipeline (retrieval
  method, vector store, index size), specific GPT‑Realtime API parameters or
  version number, latency or cost figures, the campaign's total shopper base
  (needed to contextualize the "~30,000" figure as a rate rather than a raw
  count), escalation-to-human logic, or any account from Yamada Denki's side
  of the partnership.

## Extracted Claims

### Claim 1: Japanese home-appliance retailers face a structural conflict between wanting to extend expert sales support beyond store hours and tight staffing, which avatarin frames as the core problem the 24/7 agent was built to solve
- **Evidence**: Narrator (OpenAI-authored) framing statement opening the article, before introducing the agent itself.
- **Confidence**: anecdotal (unattributed narrator claim about the retail-staffing market condition; not sourced to external labor-market or retail-industry data)
- **Quote**: "Japan's home-appliance retailers face a persistent challenge: extending expert sales support beyond store hours while staffing remains tight."
- **Our assessment**: This framing ties the product's core value proposition (24/7 availability) directly to a named structural constraint (staffing) rather than a generic "AI improves customer service" framing. It is scene-setting, not an evaluable metric, but it is specific enough to explain why a voice-first, always-on agent — rather than, say, extended human staffing hours — was the chosen response.

### Claim 2: avatarin, an AI customer service company spun out of ANA Holdings, partnered with Yamada Holdings to build the Kurashi-Marugoto AI Agent, a 24/7 multilingual shopping agent built on GPT‑Realtime that supports natural voice conversation and guides shoppers from product discovery through purchase decisions
- **Evidence**: Direct narrator description of the company relationship and the product.
- **Confidence**: settled (factual description of the named companies, product name, and underlying model, stated directly by the vendor as the article's basic premise)
- **Quote**: "avatarin, an AI customer service company spun out of ANA Holdings, partnered with Yamada Holdings to turn experienced associates' knowledge into a 24/7 multilingual shopping agent." / "Built on OpenAI's GPT‑Realtime, the Kurashi-Marugoto AI Agent supports natural voice conversations and guides shoppers from product discovery to purchase decisions."
- **Our assessment**: Notable detail: avatarin is explicitly an ANA Holdings (the Japanese airline group) spin-out applying its AI customer-service capability to a retail partner (Yamada Holdings) outside its parent's industry — a cross-industry AI-services-company pattern rather than a retailer building its own in-house agent. The product name "Kurashi-Marugoto AI Agent" ("kurashi" ≈ "daily life/living" in Japanese) is given but not explained or translated in the source itself.

### Claim 3: In a two-week public campaign on Yamada Denki's online store, approximately 30,000 people used the agent, and 92% of post-use survey responses were positive
- **Evidence**: Headline result figures, stated both in the article body and repeated in the case-study stat box.
- **Confidence**: emerging (a specific, named campaign duration, a specific headcount, and a specific survey-positivity percentage; still self-reported with no disclosed total addressable shopper count, survey response rate, question wording, or definition of "positive")
- **Quote**: "In a two-week public campaign on Yamada Denki's online store, approximately 30,000 people used the agent; 92% of survey responses were positive." (body text) / "30,000 — shoppers engaged during a two-week public experience" and "92% — of post-use survey responses were positive" (stat box)
- **Our assessment**: This is the source's most concrete, checkable claim, but it has real evidentiary gaps: no figure is given for how many shoppers visited Yamada Denki's online store during the same two weeks (so "30,000" cannot be read as a conversion or engagement rate), and "92% positive" says nothing about the survey's response rate (how many of the 30,000 actually completed the post-conversation voice survey) or how "positive" was scored. Treat both figures as a self-reported vendor telemetry snapshot from a single two-week pilot, not a durable production-scale metric — the source gives no indication the campaign continued past two weeks or became a permanent deployment.

### Claim 4: Akira Fukabori, CEO of avatarin, frames the agent as not an extension of conventional chatbots but the beginning of an "interface revolution" in retail
- **Evidence**: Direct named-executive quote, presented prominently near the top of the article.
- **Confidence**: anecdotal (single named individual's characterization of the product's significance)
- **Quote**: "This is not an extension of the conventional chatbot. It is an attempt to expand what customer service can be with AI. We see it as the beginning of an 'interface revolution' in retail." — Akira Fukabori, CEO, avatarin
- **Our assessment**: A framing/positioning quote rather than a technical or outcome claim — useful for understanding how avatarin markets the product's ambition (interface paradigm shift, not incremental chatbot improvement) but not independently verifiable from the article's content alone.

### Claim 5: avatarin had used the OpenAI API for speech recognition, inquiry analysis, and employee training before the Yamada Denki project, and frames those earlier engagements as the practical experience that prepared the team for this larger deployment
- **Evidence**: Narrator description of avatarin's prior OpenAI-API usage history, presented as context for why the Yamada Denki project could move quickly.
- **Confidence**: anecdotal (narrator claim about prior engagement history; no dates, project names, or scale given for the earlier speech-recognition/inquiry-analysis/training work)
- **Quote**: "avatarin had worked with OpenAI well before the Yamada Denki project, using the OpenAI API for speech recognition, inquiry analysis, and employee training. Those earlier efforts helped the team understand what it takes to apply AI in practice. The shopping agent was its first major opportunity to bring those lessons directly to customers."
- **Our assessment**: This establishes the Yamada Denki agent as avatarin's first *customer-facing* deployment of OpenAI-API-based AI, following internal/operational uses (employee training, inquiry analysis) — a build-internal-competence-before-customer-facing-deployment sequencing pattern, though the source gives no detail on what those earlier projects specifically involved or how long they ran.

### Claim 6: Fukabori states GPT‑Realtime's single-model performance across speech, text, and images with low latency exceeded what avatarin had seen from specialized speech-recognition systems, and this multimodal-in-one-model property was the deciding factor in choosing GPT‑Realtime
- **Evidence**: Direct named-executive quote explaining the model-selection rationale.
- **Confidence**: anecdotal (single practitioner's comparative characterization; no named alternative systems, no benchmark, latency figures, or accuracy comparison given)
- **Quote**: "For us, the performance of a single model went beyond what we had seen from specialized speech recognition systems. It can work across speech, text, and images with low latency. That is why we chose GPT‑Realtime. Instead of asking people to adapt to the rules of a machine, the technology can adapt much more naturally to the way people communicate." — Akira Fukabori, CEO, avatarin
- **Our assessment**: The specific decision driver named here is consolidation — one model spanning speech, text, and image understanding — replacing what was previously a "specialized speech recognition system" (implying a prior or alternative pipeline of separate, task-specific models). No latency numbers, accuracy comparison, or named competing system are given, so this should be cited as a practitioner's qualitative rationale for model consolidation, not a benchmarked claim that GPT‑Realtime outperforms specialized ASR systems.

### Claim 7: Fukabori illustrates the gap between conventional chatbots and the agent using a concrete example question ("I need a refrigerator for a family of four, but my kitchen is small. Which one should I choose?"), framing real customer service as the ability to answer that kind of underspecified, context-dependent question
- **Evidence**: Direct named-executive quote using a specific hypothetical customer question as an illustrative example.
- **Confidence**: anecdotal (illustrative example from a named executive; not a logged real customer transcript)
- **Quote**: "Customers do not want a chatbot. They want intelligence. 'I need a refrigerator for a family of four, but my kitchen is small. Which one should I choose?' Real customer service means being able to answer that question."
- **Our assessment**: This is a concrete, product-relevant example of the underspecified-constraint-satisfaction shopping query (household size + space constraint → product recommendation) that a retrieval-grounded conversational agent is being asked to resolve — useful as a worked example of "what does a hard retail query actually look like," though it is a hypothetical illustration in the quote, not a transcript excerpt from an actual logged conversation.

### Claim 8: avatarin designed the agent around three named qualities: (1) a RAG system grounds responses in product data while GPT‑Realtime keeps the voice interaction responsive, (2) Yamada Denki's category-specific sales-associate knowledge was encoded directly into the agent's conversation flows and prompting, with guardrails to keep off-topic detours from derailing the shopping conversation, and (3) the agent proactively asks follow-up questions to uncover a customer's actual needs rather than only answering what is asked
- **Evidence**: Direct narrator description under the "Giving retail expertise a voice" section, presented as avatarin's own named design framework.
- **Confidence**: emerging (a specific, named three-part architecture/design framework stated as fact; the underlying mechanisms — RAG grounding, guardrails, proactive questioning — are concretely described, though no implementation detail, such as retrieval method or guardrail enforcement mechanism, is given for any of the three)
- **Quote**: "A retrieval-augmented generation system grounds the agent's responses in product information, while GPT‑Realtime keeps the interaction responsive. This allows shoppers to have a fluid voice conversation while still receiving information based on relevant product data." / "avatarin incorporated Yamada Denki's customer service knowledge into the agent's conversation flows and prompting. The system is designed to adapt when customers change their requirements or move temporarily off topic, while guardrails help keep the conversation focused on the shopping experience." / "Many traditional chatbot experiences wait for the customer to provide the next instruction. avatarin took a more proactive approach. The agent asks follow-up questions to uncover the customer's actual needs, helping move the conversation from a simple question-and-answer exchange toward guided product discovery."
- **Our assessment**: This is the single most reusable pattern in the source for harness/context-engineering purposes: a named three-part design split between (a) a retrieval layer for factual grounding, (b) domain-expert knowledge encoded as conversation flow/prompt design (not just a knowledge base), and (c) an explicit proactive-questioning behavior distinct from reactive Q&A. The "guardrails help keep the conversation focused" line is a concrete, if underspecified, scope-control mechanism — no detail is given on whether guardrails are prompt-based, a separate classifier, or a platform-level control, so practitioners should not assume a specific implementation from this description alone.

### Claim 9: OpenAI directly supported avatarin's implementation by helping structure complex prompts, optimize API costs for an always-on voice service, and share implementation best practices, which avatarin frames as freeing it to focus on translating Yamada Denki's service model into an accurate, responsive, on-brand experience
- **Evidence**: Direct narrator statement describing the vendor-customer implementation relationship.
- **Confidence**: anecdotal (narrator claim about the nature of OpenAI's support; no specifics on what "structuring complex prompts" or "optimizing API costs" concretely involved, no cost figures before/after)
- **Quote**: "OpenAI worked with avatarin to structure complex prompts, optimize API costs for always-on voice service, and share implementation best practices. That support helped avatarin focus on translating Yamada Denki's service model into an experience that felt accurate, responsive, and distinctly on-brand."
- **Our assessment**: The explicit naming of "optimize API costs for always-on voice service" as a distinct support activity is notable — it names cost management for continuous (not session-bounded) voice-agent operation as a real, nontrivial implementation concern significant enough for OpenAI's field team to help directly with, though no cost figures, technique (e.g., model-tier switching, session-length limits, caching), or before/after comparison are disclosed.

### Claim 10: Fukabori states the most important discovery from the campaign was not the usage scale itself but that every conversation revealed what shoppers cared about, why they hesitated, and what might help them decide — insight he says was difficult to see with conventional online shopping
- **Evidence**: Direct named-executive quote paired with narrator framing under the "When a conversation becomes an insight" section.
- **Confidence**: anecdotal (single executive's qualitative characterization of the campaign's value; no data or examples of the specific insights surfaced are given)
- **Quote**: "With conventional online shopping, those insights were difficult to see. With an AI agent, they become part of the conversation." — Akira Fukabori, CEO, avatarin
- **Our assessment**: This reframes the conversational agent as a market-research/customer-insight instrument, not just a sales-conversion tool — a distinct value proposition from pure automation or cost reduction. No concrete example insight (a specific hesitation pattern, a specific decision driver uncovered) is given in the source, so this should be cited as the vendor's stated value framing, not as evidence of a specific insight actually captured and acted on.

### Claim 11: The service let customers ask questions after stores closed and discuss budgets or uncertainty candidly without feeling sales pressure, and each conversation ended with a short voice survey, making feedback a natural continuation of the shopping experience; customers described the agent as "easier to talk to than an actual sales associate"
- **Evidence**: Narrator description of the after-hours access pattern and the survey mechanism, paired with an unattributed customer-description quote (not linked to a named individual or a count of how many customers said this).
- **Confidence**: anecdotal (narrator claims about candor and comfort are unattributed and unquantified; the "easier to talk to" description is presented as representative customer language but not sourced to a specific respondent or count)
- **Quote**: "The service also opened new moments for retail. Customers could ask questions after stores closed and speak candidly about budgets or uncertainty without feeling sales pressure." / "Each conversation ended with a short voice survey, making feedback a natural continuation of the shopping experience." / "Customers described the agent as 'easier to talk to than an actual sales associate' and appreciated being able to ask questions again without feeling stressed."
- **Our assessment**: The "voice survey appended to the end of every conversation" is a concrete, reusable feedback-collection mechanism (feedback embedded in the same voice modality and session as the interaction, rather than a separate follow-up channel) — this is likely the source of the 92%-positive figure in Claim 3, though the source does not explicitly state that the stat-box percentage comes from this specific survey mechanism. The "easier to talk to than an actual sales associate" line is presented as a paraphrased composite of customer sentiment, not a single attributed quote, and should be treated as vendor-selected representative feedback rather than a verified aggregate finding.

### Claim 12: avatarin envisions a single AI agent serving customers seamlessly across web, phone, and physical stores — carrying customer context forward across channels — under the framing "One Intelligence. One Brand. Every interface.", explicitly rejecting the idea that different companies' AI agents should sound the same
- **Evidence**: Narrator description of avatarin's stated cross-channel product vision, paired with two Fukabori quotes closing the article.
- **Confidence**: anecdotal (forward-looking vision statement from a named executive; no committed roadmap, timeline, or technical detail on how cross-channel context-carrying would be implemented)
- **Quote**: "avatarin envisions a world where a single AI agent serves customers seamlessly across the web, phone, and physical stores. Instead of separate systems for each channel, the same intelligence carries the customer's context forward. The result is continuity: one customer, one conversation, and one brand, wherever the interaction takes place." / "We want people to experience one intelligence that embodies each company's identity and brand across every interface. That is what we mean by 'One Intelligence. One Brand. Every interface.' The era of single purpose AI is over. I believe OpenAI will lead the next era of general purpose, multimodal intelligence." — Akira Fukabori, CEO, avatarin
- **Our assessment**: This is avatarin's named product thesis for future work, not a description of a shipped capability — the Yamada Denki deployment described elsewhere in the article is a single-channel (online store) voice agent, and no evidence is given that cross-channel (web + phone + physical store) context-carrying has actually been built or piloted. The claim that "the era of single purpose AI is over" is a rhetorical/marketing statement about the industry, not a technical claim; the guide should treat this section as vision/positioning rather than a documented deployment pattern.

## Concrete Artifacts

### Case study metadata and results stat box (verbatim)

```
Source: https://openai.com/index/avatarin (July 30, 2026)

Company size: Startup
Region:       Asia-Pacific & Oceania
Industry:     Retail, Technology
Products:     API

Results:
  30,000  shoppers engaged during a two-week public experience
  92%     of post-use survey responses were positive
```

### avatarin's three-part agent design philosophy (verbatim, from "Giving retail expertise a voice")

```
Source: https://openai.com/index/avatarin (July 30, 2026)

1. Keeping product information accurate without slowing the conversation.
   "A retrieval-augmented generation system grounds the agent's responses
   in product information, while GPT-Realtime keeps the interaction
   responsive. This allows shoppers to have a fluid voice conversation
   while still receiving information based on relevant product data."

2. Translating Yamada Denki's sales expertise into conversation design.
   "The information a sales associate needs to gather varies significantly
   by product category. avatarin incorporated Yamada Denki's customer
   service knowledge into the agent's conversation flows and prompting.
   The system is designed to adapt when customers change their
   requirements or move temporarily off topic, while guardrails help keep
   the conversation focused on the shopping experience."

3. Designing an agent that asks, rather than only answers.
   "Many traditional chatbot experiences wait for the customer to provide
   the next instruction. avatarin took a more proactive approach. The
   agent asks follow-up questions to uncover the customer's actual needs,
   helping move the conversation from a simple question-and-answer
   exchange toward guided product discovery."
```

### Named-practitioner quotes, verbatim, in order of appearance

```
Source: https://openai.com/index/avatarin (July 30, 2026)

Akira Fukabori, CEO, avatarin:

1. "This is not an extension of the conventional chatbot. It is an attempt
   to expand what customer service can be with AI. We see it as the
   beginning of an 'interface revolution' in retail."

2. "For us, the performance of a single model went beyond what we had seen
   from specialized speech recognition systems. It can work across speech,
   text, and images with low latency. That is why we chose GPT-Realtime.
   Instead of asking people to adapt to the rules of a machine, the
   technology can adapt much more naturally to the way people communicate."

3. "Customers do not want a chatbot. They want intelligence. 'I need a
   refrigerator for a family of four, but my kitchen is small. Which one
   should I choose?' Real customer service means being able to answer that
   question."

4. "I'm excited by how naturally it understands our intentions, and by
   glimpses of intelligence that sometimes go beyond what people can do."

5. "With conventional online shopping, those insights were difficult to
   see. With an AI agent, they become part of the conversation."

6. "AI has clearly shifted into a higher gear. I can't wait to see what we
   can build with this extraordinary intelligence."

7. "We want people to experience one intelligence that embodies each
   company's identity and brand across every interface. That is what we
   mean by 'One Intelligence. One Brand. Every interface.' The era of
   single purpose AI is over. I believe OpenAI will lead the next era of
   general purpose, multimodal intelligence."
```

### Section headings (verbatim, in order)

```
Source: https://openai.com/index/avatarin (July 30, 2026)

1. From answering questions to understanding people
2. Giving retail expertise a voice
3. When a conversation becomes an insight
4. One Intelligence. One Brand. Every interface.
```

## Cross-References

- **Corroborates**:
  - `blog-openai-cars24-conversation-scaling.md` Claim 2 (Cars24's voice/chat
    agent carries a buyer through a multi-step journey — budget/needs
    intake, recommendation, booking, follow-up, post-purchase support) and
    Claim 4 (Vikram Chopra's framing that AI gives "every customer a
    high-quality experience at any scale" versus an experience that
    "depended on who picked up the phone"): This note's Claim 8 (guided,
    multi-turn product-discovery conversation replacing simple Q&A) and
    Claim 6/7 (consistent, always-available expert-level interaction) are
    the same underlying pattern — a persistent conversational agent acting
    as a *consistency and availability* mechanism for a high-touch,
    consultative sales process — independently reported by OpenAI for two
    different verticals (used cars in India, home appliances in Japan) in
    the same case-study template, three weeks apart (July 16 and July 30,
    2026).
  - `blog-simonwillison-openai-webrtc-document-context.md` Claim 5
    (GPT‑Realtime‑2 "supports speech-to-speech interactions with
    configurable reasoning effort, stronger instruction following, and more
    reliable tool use for complex voice-agent workflows") and
    `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 7 (naming
    `openai/gpt-realtime-2` as a single speech-to-speech model, audio in/
    audio out): This note's Claim 6 (Fukabori: "It can work across speech,
    text, and images with low latency... performance of a single model
    went beyond what we had seen from specialized speech recognition
    systems") independently corroborates, from a production customer's
    perspective, the same "one model replaces a pipeline of
    specialized/separate systems" value proposition those two sources
    document from the API/infrastructure side.
  - `blog-anthropic-voice-mode-tools-multilingual.md` Claim 6 (Claude's
    voice mode added support for 11 languages) and Claim 4 (voice mode can
    execute actions in connected tools behind a permission gate): This
    note's Claim 2 (a "24/7 multilingual shopping agent") corroborates the
    general industry direction — both Anthropic (consumer product) and
    avatarin (an OpenAI enterprise customer) shipped multilingual
    voice-agent capability within roughly the same one-week window (July
    23 and July 30, 2026) — though this source gives no language count or
    list, unlike the Anthropic note's explicit 11-language enumeration.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about avatarin, Yamada Denki/Yamada Holdings, or GPT‑Realtime's retail
  use that this source disagrees with.

- **Extends**:
  - `blog-fowler-bayer-prince-agentic-rag.md` (Bayer AG's PRINCE platform —
    a detailed, architecturally deep account of agentic RAG for preclinical
    drug research, including retrieval pipeline internals, a three-tier
    reflection architecture, and a documented decision to remove an
    over-rejecting LLM verifier step): This note's Claim 8 names RAG
    grounding as one of three design pillars ("A retrieval-augmented
    generation system grounds the agent's responses in product
    information") but gives none of PRINCE's architectural detail — no
    retrieval method, no verification/reflection step, no evaluation
    framework. Read together, PRINCE demonstrates what a fully-specified
    agentic RAG architecture looks like, while this source shows the same
    RAG-for-grounding pattern applied in a real-time, low-latency,
    voice-first product context where architectural depth is not
    disclosed — a reminder that "RAG grounds the responses" is stated as a
    given in customer-facing OpenAI case studies without the implementation
    detail PRINCE's engineering-authored account provides.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (the
    April 2026 Andon Labs autonomous retail agent — given a lease, $100,000,
    and the single directive "make a profit," which made unsupervised
    hiring and inventory decisions and hit governance gaps when it made
    operational errors): Both sources describe an autonomous AI system
    operating in a retail context, but the contrast is instructive rather
    than corroborating. avatarin's agent (per this source's own
    description) only recommends, converses, and gathers information — it
    does not appear to autonomously execute purchases, place orders, or
    take actions with financial or contractual consequences; nothing in
    this source describes a "designated principal," authority scope, or
    governance document of the kind the Andon Labs case exposed the absence
    of. This source gives no indication avatarin's agent needed, or was
    given, that kind of write/transaction authority — worth noting as an
    example of a retail-facing conversational agent kept to a narrower,
    lower-autonomy scope (recommend and converse, not transact) than either
    the Andon Labs failure case or `blog-openai-cars24-conversation-scaling.md`
    Claim 9 (a Cars24 finance workflow where Codex auto-approves purchase
    orders above a threshold).

- **Novel**:
  - **A named three-part conversational-agent design framework pairing RAG
    grounding, domain-expert-knowledge-as-prompt-design, and proactive
    (rather than reactive) questioning** (Claim 8): No existing corpus
    source states this specific three-part split (accuracy-without-latency,
    expertise-encoded-in-conversation-flow, proactive-questioning-over-Q&A)
    as an explicit named design philosophy for a production voice agent.
  - **End-of-conversation voice survey as the feedback-collection mechanism
    for a voice-first agent** (Claim 11): No existing corpus source
    documents appending a short voice survey to the end of every
    AI-agent conversation as a feedback mechanism in the same modality as
    the interaction itself.
  - **API cost optimization for "always-on voice service" named as a
    distinct vendor implementation-support activity** (Claim 9): No
    existing corpus source names ongoing/continuous (not session-bounded)
    voice-service cost management as a specific area where the model
    vendor's field team directly assisted a customer's implementation.
  - **"One Intelligence. One Brand. Every interface." as a named
    cross-channel agent-identity vision** (Claim 12): No existing corpus
    source documents a company's stated ambition to unify a single AI
    agent's context and identity across web, phone, and physical-store
    channels under one branded framing.

## Guide Impact

- **`04-context-engineering.md` (grounding real-time/voice agents)**: Add
  Claim 8's first design pillar (RAG grounds responses while GPT‑Realtime
  keeps the interaction responsive) as a named example of combining
  retrieval-based grounding with a low-latency conversational layer — a
  lighter-weight, customer-facing counterpart to the deeply-documented
  agentic RAG architecture in `blog-fowler-bayer-prince-agentic-rag.md`.
  The guide should note the accuracy/latency tension this pairing is
  explicitly designed to resolve (grounding without slowing the
  conversation) as a named requirement for voice-first RAG use cases
  specifically, distinct from batch or async RAG contexts.
- **`02-harness-engineering.md` (conversation design / guardrails /
  proactive agent behavior)**: Add Claim 8's second and third design
  pillars — domain-expert knowledge encoded directly into conversation
  flow and prompting (not just retrievable documents), and an agent
  designed to proactively ask follow-up questions rather than only
  respond reactively — as a named pattern for guided, consultative
  agent conversations. Flag that the source names "guardrails" to keep
  conversations on-topic but gives no implementation detail (prompt-based
  vs. classifier vs. platform-level), so this cannot be cited as a
  specific guardrail technique, only as a named requirement.
- **`05-team-adoption.md` (vendor implementation support / adoption
  mechanics)**: Add Claim 9 (OpenAI directly helped structure prompts,
  optimize always-on voice API costs, and share implementation best
  practices) as another named example — alongside similar vendor-support
  patterns documented in other OpenAI case studies in this corpus — of
  what direct vendor field-team support concretely looks like during a
  production agent rollout, with the caveat that no specifics or cost
  figures are disclosed.
- **Any chapter discussing agent autonomy/authority scope**: If a future
  chapter revision addresses the spectrum from "agent recommends" to
  "agent transacts," cite this source (recommend/converse-only, per the
  Extends note above) as one end of that spectrum, contrasted with
  `blog-openai-cars24-conversation-scaling.md` Claim 9 (agent auto-approves
  purchase orders) and the Andon Labs case in
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` at the
  higher-autonomy end.

## Extraction Notes

- **The live OpenAI URL (`https://openai.com/index/avatarin`) returned HTTP
  403 to both the WebFetch tool and a direct `curl` with a browser
  user-agent** — a Cloudflare bot-challenge page, consistent with the
  OpenAI-domain bot-blocking behavior already documented in
  `blog-openai-cars24-conversation-scaling.md`,
  `blog-openai-notion-codex-case-study.md`, and
  `blog-openai-samsung-chatgpt-codex-deployment.md`'s Extraction Notes. The
  `WebFetch` tool additionally refused to fetch `web.archive.org` URLs
  directly in this environment (same restriction documented in those prior
  notes). The article was retrieved via a Wayback Machine snapshot
  (`http://web.archive.org/web/20260801031728/https://openai.com/index/avatarin/`,
  crawled August 1, 2026, two days after publication), fetched with `curl`
  and parsed by stripping `<script>`/`<style>` blocks and remaining HTML
  tags with a local Python script, specifically to guarantee the `Quote`
  fields above are copied character-for-character rather than paraphrased,
  per MINER.md §2a.
- **Model version ambiguity**: The article consistently refers to the
  underlying model as "GPT‑Realtime" without a version suffix, never as
  "GPT‑Realtime‑2." Other corpus sources
  (`blog-simonwillison-openai-webrtc-document-context.md`,
  `blog-vercel-ai-gateway-realtime-voice-speech.md`) specifically document
  "GPT‑Realtime‑2" (released May 2026, "GPT‑5‑class reasoning," September
  30, 2024 knowledge cutoff) as a distinct, later model in OpenAI's
  Realtime API line. This source gives no release date, model ID string,
  or version number for the "GPT‑Realtime" it names, so the guide should
  **not** assume avatarin's deployment specifically uses GPT‑Realtime‑2 —
  it may be the original `gpt-realtime` model or an unspecified point in
  the product line. This ambiguity is the article's own, not an extraction
  error.
- **No named Yamada Denki/Yamada Holdings executive is quoted.** Every
  direct quote in the source is from Akira Fukabori (avatarin's CEO); the
  retail partner whose sales expertise and brand the agent represents is
  described only in the third person by the OpenAI narrator. The guide
  should not attribute any first-person endorsement or account to Yamada
  Denki/Yamada Holdings from this source.
- **No sub-pages followed.** The archived snapshot's body content is a
  single self-contained case study (~750 words) with no inline links to
  further avatarin or Yamada Denki documentation; the page's "Keep
  reading" footer links to three unrelated OpenAI posts (Advancing
  responsible AI across Europe, Building abundant intelligence, Univé
  builds an AI-ready workforce), none of which concern avatarin or
  GPT‑Realtime and were not followed.
- **Cross-reference verification**: `blog-openai-cars24-conversation-scaling.md`,
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
  `blog-anthropic-voice-mode-tools-multilingual.md`,
  `blog-simonwillison-gptlive-voice-delegation.md`,
  `blog-simonwillison-openai-webrtc-document-context.md`,
  `blog-vercel-ai-gateway-realtime-voice-speech.md`, and
  `blog-fowler-bayer-prince-agentic-rag.md` were each read in full (or, for
  the longer ones, their relevant sections and headers) before citing.
  Claim numbers cited above were verified against each note's numbered
  `### Claim N:` headings in document order.
- **No contradiction identified during extraction**; nothing in this
  source disagrees with an existing corpus note (see Cross-References →
  Contradicts), so no contradiction issue was filed per MINER.md §4a.
- **`confidence_overall` set to anecdotal**, matching
  `blog-openai-cars24-conversation-scaling.md`'s rating for the same
  case-study template: every quantitative figure in this source (~30,000
  users, 92% positive) is self-reported by OpenAI/avatarin with no
  disclosed methodology, baseline, survey response rate, or total-shopper
  denominator, and the source's most reusable content (the three-part
  design philosophy, the vendor-support description) is qualitative
  narrator/executive framing rather than measured outcome data.
