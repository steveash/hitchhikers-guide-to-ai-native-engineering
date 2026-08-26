---
source_url: https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/
source_type: blog-post
title: "We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility"
author: Simon Willison, linking/quoting a 404 Media investigation by Emanuel Maiberg
date_published: 2026-08-17
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: emerging
issue: "#2958"
---

# We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training Facility

> A short link-blog post in which Simon Willison curates and excerpts a 404
> Media investigation: a bookseller who received an anonymous, price-
> insensitive ~1,000-book order hid an Apple AirTag in the shipment, which
> traced to the VGT3 area of Amazon's LAS8 facility in Las Vegas — a location
> Amazon workers' own forum discussions confirm destructively scans large
> volumes of books. The full investigative article is paywalled at 404
> Media; this note extracts only what is freely visible on Willison's page.

## Source Context

- **Type**: blog-post — Simon Willison's "link blog" format: a short
  editorial framing paragraph (2 sentences), one blockquote reproduced from
  the linked 404 Media article, a one-sentence factual conclusion, and a
  photo with caption. Not a full standalone article; the primary
  investigative reporting (404 Media, "We Tracked a Shipment of Rare Books.
  It Ended at an Amazon AI Training Facility," byline Emanuel Maiberg) is
  paywalled and this Miner could only access its publicly visible
  introduction (see Extraction Notes).
- **Author credibility**: Simon Willison is this corpus's designated
  `trusted-feed` source (see `blog-simonwillison-stateless-mcp-tooling.md`
  Source Context for his general standing). For this post specifically he is
  a curator, not the investigator — the AirTag tracking, the facility
  identification, and the Amazon-worker forum research are 404 Media's work,
  which Willison quotes and links to. Willison adds his own editorial
  framing (calling it "Excellent piece of reporting") and links to his own
  June 2025 prior coverage of Anthropic's book-scanning practices as
  background — a post this Miner also read in full (see below) because it
  is directly linked as necessary context and is substantive.
- **Scope**: Covers exactly one investigative finding — that a bulk book
  order traced via AirTag ended up at a specific Amazon facility (VGT3,
  part of the LAS8 complex, in northeast Las Vegas) that Amazon workers'
  own forum discussions describe as destructively scanning books at volume.
  Does NOT cover: any Amazon corporate statement or denial (none is quoted
  in the visible portion of either page); confirmation, by Amazon or by
  404 Media, that the scanned books specifically feed AI model training
  (as opposed to some other Amazon books initiative) — that link is
  Willison's and the booksellers' stated *suspicion*, not a confirmed fact
  in the visible text; the scale, frequency, or cost of Amazon's book
  acquisitions (only the single ~1,000-book tracked order is described);
  or any technical detail about how the scanned pages are subsequently used
  in training pipelines.

## Extracted Claims

### Claim 1: Book dealers have, for some time, been receiving large-volume orders from anonymous, price-insensitive buyers, and it is widely suspected (not confirmed in this post) that these buyers are companies acquiring books to scan for AI training data
- **Evidence**: Willison's own framing statement, presented as an ongoing
  pattern he has been tracking (he links to his own June 2025 post on
  Anthropic's book-scanning practices as prior corroborating context).
- **Confidence**: anecdotal (a stated pattern/suspicion, explicitly
  qualified as "widely suspected" rather than confirmed for any specific
  buyer in this sentence)
- **Quote**: "For a while now there have been stories of book dealers receiving orders for large volumes of books from apparently price-insensitive anonymous customers, widely suspected to be companies looking to scan them for AI training"
- **Our assessment**: This is scene-setting rather than new evidence on its
  own — it establishes that the practice described in this post (bulk,
  anonymous, price-insensitive book buying) is a recognized pattern in the
  book-dealer community, not a one-off. Its value is as the premise the
  rest of the post's AirTag investigation is designed to test.

### Claim 2: In July (2026), a bookseller told 404 Media they had received a very large order of around 1,000 books through the Biblio marketplace, and agreed to hide an Apple AirTag (supplied by 404 Media) in one of the shipped books to trace where the order was going and which company was behind it
- **Evidence**: Direct quote, reproduced by Willison as a blockquote from
  the 404 Media article.
- **Confidence**: emerging (first-hand account relayed through the
  investigating outlet; this Miner could not independently verify the
  underlying transaction or the bookseller's identity, since the full 404
  Media article is paywalled)
- **Quote**: "In July, one bookseller told me they received a very large order of around 1,000 books on Biblio, one of these marketplaces. The seller agreed to put an Apple AirTag provided by 404 Media in one of the books included in this order so we could see where the book was going. And by extension, which company, AI or otherwise, was behind this massive order."
- **Our assessment**: This is a concrete, named methodology (physical
  tracking device inside a real commercial shipment) rather than a
  secondhand claim about book-buying patterns — the strongest piece of
  evidence in this post, since it produces a verifiable physical
  destination rather than relying on inference from order size or price
  alone. Note the "AI, or otherwise" hedge in the reporter's own words: even
  404 Media does not claim in this quoted passage that the buyer's purpose
  was necessarily AI training, only that they wanted to find out.

### Claim 3: The tracked book was delivered to the VGT3 corner of Amazon's LAS8 facility in the north east of Las Vegas
- **Evidence**: Willison's own factual statement following the AirTag
  quote, presumably relaying 404 Media's tracking result, with a linked
  Google Maps location for the facility.
- **Confidence**: settled (a specific, named, mappable physical location
  reported as the AirTag's tracked endpoint; the claim is narrow — a
  location, not an inference about purpose)
- **Quote**: "The book ended up delivered to the VGT3 corner of the LAS8 Amazon facility in the north east of Las Vegas, where the entrance carried this on-the-nose logo of a dinosaur with a book!"
- **Our assessment**: This is the investigation's central factual payload —
  it converts "suspected AI-training book buyer" from speculation into a
  named, geolocated Amazon facility. It does not, on its own, establish
  what VGT3 does with the books (that's Claim 5) or that the purpose is AI
  training specifically (see Claim 1's caveat).

### Claim 4: The VGT3 facility entrance displays a logo of a red tyrannosaurus gripping a book with its claws, visually read by the reporter/photographer as signaling destruction rather than reading
- **Evidence**: A photograph included in the post, with descriptive alt
  text/caption credited to 404 Media.
- **Confidence**: anecdotal (a photographed physical sign and one
  observer's interpretive reading of its visual intent — "more interested
  in destruction than reading" is editorializing, not a confirmed
  statement of the facility's purpose from Amazon or its logo designers)
- **Quote**: "Photo of an office entrance. A logo in the window shows a red tyrannosaurus with a book, its claws clearly digging in and with a hint that it is more interested in destruction than reading."
- **Our assessment**: This is color/atmosphere evidence, not proof of
  operational purpose — a corporate mascot's claws are not documentation of
  a destructive-scanning process. It is only meaningful in combination with
  Claim 5 (workers' own forum confirmation), which is the actual operational
  evidence.

### Claim 5: Online forum discussions among Amazon workers confirm that the VGT3 facility destructively scans large volumes of books
- **Evidence**: Willison's summarizing sentence, presented as relaying
  findings from 404 Media's investigation (worker forum research); no forum
  post is quoted directly in the visible portion of either page.
- **Confidence**: emerging (a secondhand characterization of unquoted forum
  discussions, relayed through two layers of curation — 404 Media's
  reporting, then Willison's one-sentence summary — with no verbatim worker
  quote available to this Miner because the full article is paywalled)
- **Quote**: "Online forum discussions between Amazon workers confirmed that VGT3 destructively scans large volumes of books."
- **Our assessment**: This is the closest thing in the visible text to
  operational confirmation — internal, presumably candid worker discussion
  (rather than a company statement) describing large-scale destructive
  scanning at the specific facility the AirTag traced to. It corroborates,
  from a second and independent worker/employee source, the same
  buy-books-then-destructively-scan-them pattern that a US federal court
  documented for Anthropic in June 2025 (see below) — but note this
  sentence alone does not say the scanned books are used for AI training;
  that link is the reader's inference from the facility's context and the
  post's title, not a directly quoted worker statement.

## Concrete Artifacts

```
Full visible text of Simon Willison's post (simonwillison.net,
2026-08-17), reproduced from the raw page HTML:

"We Tracked a Shipment of Rare Books. It Ended at an Amazon AI Training
Facility. Excellent piece of reporting from 404 Media. For a while now
there have been stories of book dealers receiving orders for large
volumes of books from apparently price-insensitive anonymous customers,
widely suspected to be companies looking to scan them for AI training
(see my previous coverage of Anthropic's book scanning from June 2025.)

404 Media investigated with an AirTag!

  [blockquote, from 404 Media, byline Emanuel Maiberg:]
  In July, one bookseller told me they received a very large order of
  around 1,000 books on Biblio, one of these marketplaces. The seller
  agreed to put an Apple AirTag provided by 404 Media in one of the books
  included in this order so we could see where the book was going. And
  by extension, which company, AI or otherwise, was behind this massive
  order.

The book ended up delivered to the VGT3 corner of the LAS8 Amazon
facility in the north east of Las Vegas, where the entrance carried this
on-the-nose logo of a dinosaur with a book!

  [photo, credited "Photo credit: 404 Media"; alt text:]
  Photo of an office entrance. A logo in the window shows a red
  tyrannosaurus with a book, its claws clearly digging in and with a hint
  that it is more interested in destruction than reading.

Online forum discussions between Amazon workers confirmed that VGT3
destructively scans large volumes of books."

Tags applied by Willison: amazon, journalism, ai, training-data,
ai-ethics, 404-media

Facility location linked: LAS8 Amazon facility, VGT3 corner, north east
Las Vegas, Nevada (Google Maps link in original post:
https://maps.app.goo.gl/2hMqbHrovTSZxh1U9)
```

```
Background context — the June 2025 companion post Willison links to as
prior coverage (simonwillison.net/2025/Jun/24/anthropic-training/),
quoting Judge William Alsup's summary judgement in Authors v. Anthropic,
describing Anthropic's 2024 purchase-and-scan book-acquisition method
(read in full by this Miner because it is directly linked and
substantive; not part of the assigned Aug 2026 source, quoted here only
as background for Cross-References/Our assessment):

"To find a new way to get books, in February 2024, Anthropic hired the
former head of partnerships for Google's book-scanning project, Tom
Turvey. He was tasked with obtaining "all the books in the world" while
still avoiding as much "legal/practice/business slog" as possible (Opp.
Exhs. 21, 27). [...] Turvey and his team emailed major book distributors
and retailers about bulk-purchasing their print copies for the AI firm's
"research library" (Opp. Exh. 22 at 145; Opp. Exh. 31 at -035589).
Anthropic spent many millions of dollars to purchase millions of print
books, often in used condition. Then, its service providers stripped the
books from their bindings, cut their pages to size, and scanned the
books into digital form — discarding the paper originals."
```

## Cross-References

- **Corroborates**: No existing source note in this corpus documents
  physical/vendor-level infrastructure for AI training-data book
  acquisition; this is the corpus's first source on that specific topic, so
  there is nothing to corroborate against within the corpus itself. Within
  the source material's own external references, this post's pattern
  (bulk anonymous book purchase → destructive scan → digital training
  corpus) directly matches the court-documented Anthropic method quoted
  above (Turvey's team "bulk-purchasing" print copies, then stripping
  bindings and scanning pages while "discarding the paper originals") —
  the same acquisition-and-destruction shape, now reported for a second
  named company (Amazon) via independent physical tracking rather than
  litigation discovery.
- **Contradicts**: None identified. No existing source note makes a claim
  about training-data book acquisition that this post's claims oppose.
- **Extends**: No existing source note in `source-notes/` covers training
  data physical-media sourcing infrastructure to extend directly (checked
  via full listing of `source-notes/` for `book`, `training-data`, and
  `data-sourcing` naming patterns — no match). The closest corpus material
  is outside `source-notes/` entirely: the June 2025 Anthropic court
  judgement Willison links to (quoted in Concrete Artifacts above), which
  is not itself a source note in this corpus. This post extends that
  courtroom-documented pattern with independent, non-litigation evidence
  (physical package tracking) that a second major company (Amazon) operates
  comparable destructive-scanning infrastructure, and adds a specific,
  named facility (VGT3/LAS8, Las Vegas) rather than only a general
  description of vendor emails and purchase orders.
- **Novel**: (1) The specific identification of an Amazon facility (VGT3,
  part of LAS8, Las Vegas) associated with destructive book scanning —
  no prior corpus material names an Amazon-specific facility for this
  purpose. (2) The AirTag-tracking methodology itself as a way to verify a
  book order's destination independent of the buyer's own disclosures or
  litigation discovery. (3) Amazon-worker forum corroboration of large-
  volume destructive scanning at a named location, an employee-level source
  distinct from the court-filing-based evidence the corpus has (via the
  linked June 2025 background piece) for Anthropic.

## Guide Impact

- **No chapter should currently cite this source as confirmation that
  Amazon uses these specific scanned books for AI model training** — the
  visible text supports "Amazon operates a facility that destructively
  scans large volumes of books" (Claim 5, emerging confidence) but the
  AI-training purpose is presented throughout as suspicion/inference
  (Claim 1, Claim 2's own "AI, or otherwise" hedge), not as something
  Amazon, 404 Media, or the quoted Amazon workers directly confirmed in the
  text available to this Miner. Any guide text drawing on this source
  should preserve that distinction rather than stating flatly that Amazon
  scans purchased books for AI training.
- **Chapter on training-data sourcing / vendor infrastructure (if the guide
  has or adds one covering how frontier labs and large tech companies
  physically acquire training data)**: This source is evidence that
  large-scale, destructive physical-book-to-digital conversion for training
  purposes is not confined to one company (Anthropic, per the June 2025
  court judgement) — a second major company (Amazon) appears, via
  independent investigative tracking, to operate comparable infrastructure
  at a named facility. Recommend citing this alongside the Anthropic court
  judgement as two independently-sourced data points (one litigation
  discovery, one physical tracking + worker testimony) for the same general
  practice, while flagging that this source's link to AI training
  specifically is inferential, not company-confirmed.
- **Chapter on AI ethics / provenance of training data (if present)**: The
  contrast between the destructive process (bindings cut, pages scanned,
  paper discarded — per the Anthropic judgement quoted in Concrete
  Artifacts, and structurally mirrored by Amazon's "destructively scans"
  worker-confirmed process in Claim 5) and the public opacity around it
  (no Amazon statement, dealers only guessing at buyer identity/purpose) is
  a citable illustration of the gap between how training data acquisition
  is publicly discussed versus how it is operationally conducted.

## Extraction Notes

1. **Primary source page is short; secondary source is paywalled**: The
   assigned URL (`simonwillison.net`, Aug 17 2026) is a link-blog post of
   roughly 150 words plus one blockquote and one image caption — Willison's
   full editorial and factual contribution to this topic. The underlying
   investigative reporting it links to and quotes from
   (`404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/`)
   was confirmed paywalled: a direct fetch returned only the article's
   introduction (investigation premise, byline Emanuel Maiberg, a call for
   sources) with worker quotes, any Amazon statement, and scale/frequency
   detail behind the paywall. This note extracts only what is verifiable in
   Willison's freely accessible page (the blockquote he chose to reproduce)
   plus what that blockquote itself contains — it does not extrapolate
   beyond that visible text. Per MINER.md's "aim for 5-15 claims... if you
   only found 1-2, you probably didn't read deeply enough" guidance: this
   note extracts 5 claims, which is the full substantive content available
   in the assigned, freely accessible source (compare
   `blog-simonwillison-sam-altman-quote.md`, extraction note 1, for a
   precedent of a thin Willison link-blog/quotation post extracting a
   similarly small claim count for the same reason).
2. **Verbatim text obtained via direct `curl`, not an AI-summarizing fetch
   tool**: an initial WebFetch pass against the Willison page returned a
   paraphrased rendering rather than verbatim text. Per MINER.md §2a, the
   raw HTML was instead fetched directly via `curl` (browser user agent)
   against `simonwillison.net`, the `data-permalink-context` entry body
   isolated, and every quote in this note copied character-for-character
   from that HTML (including the blockquote and the image alt text) — not
   reconstructed from any AI-generated summary.
3. **One substantive linked page followed, per MINER.md §1**: The post
   links to Willison's own June 2025 coverage of Anthropic's book-scanning
   litigation (`simonwillison.net/2025/Jun/24/anthropic-training/`),
   explicitly presented as necessary background ("see my previous coverage
   of Anthropic's book scanning"). This Miner fetched and read that page in
   full (also via raw `curl`, for the same verbatim-quote reason) since it
   directly informs how to weigh the Amazon claims — it establishes that a
   near-identical acquisition-and-destruction pattern is already
   court-documented for a different company. Its content is used only as
   background/cross-reference context (see Cross-References and Concrete
   Artifacts) and is not treated as part of this note's own numbered claims,
   since the assigned source for issue #2958 is the Amazon/404 Media post,
   not the Anthropic litigation post — a future source submission for that
   litigation judgement, if filed separately, would deserve its own note.
   The 404 Media article's own paywall meant no further linked pages from
   *that* article could be followed.
4. **No contradiction filed**: This source's claims are consistent with,
   and extend, the pattern documented in the June 2025 Anthropic litigation
   background material; no claim here opposes any existing source note
   (there being no existing source note on this topic to oppose).
5. **Confidence grading rationale**: `confidence_overall` is set to
   `emerging`. The facility-location claim (Claim 3) is about as settled as
   a single-shipment physical trace can be, but the operationally important
   claim (Claim 5, destructive scanning at volume) rests on an unquoted,
   secondhand characterization of worker forum discussions relayed through
   two layers of curation, and the AI-training purpose that gives the post
   its title is explicitly a suspicion/inference throughout the visible
   text, not a confirmed fact from Amazon or a named worker. This is
   stronger than a bare editorial opinion (`anecdotal`) because it includes
   a verifiable physical-tracking method and a named, mappable location, but
   not `settled` because the paywall blocks this Miner from the worker
   quotes, any Amazon response, and scale/frequency data that would be
   needed to confirm the practice beyond this one tracked shipment.
