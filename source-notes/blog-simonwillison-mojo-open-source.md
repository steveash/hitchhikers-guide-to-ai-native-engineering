---
source_url: https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/
source_type: blog-post
title: "Mojo🔥 is now open source"
author: Simon Willison, summarizing and linking to Modular's own announcements
date_published: 2026-08-18
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: emerging
issue: "#2960"
---

# Mojo🔥 is now open source

> Simon Willison's short link-post on Modular open-sourcing the Mojo compiler
> and toolchain under Apache 2.0 (with LLVM exceptions), a week after Mojo hit
> 1.0. The Miner followed Willison's links into Modular's own two source blog
> posts (the open-source announcement and the 1.0 release notes) and the
> Modular forum thread Willison cites for the August 2025 pivot away from
> "full Python superset" as Mojo's stated goal — together these give a fuller
> picture than Willison's ~120-word post alone: a staged, deliberately
> paced open-sourcing strategy, an explicit "not yet accepting outside
> contributions to the compiler" policy justified partly by "today's era of
> AI coding," and a company (recently acquired by Qualcomm) betting that a
> Python-flavored-but-not-Python-compatible language is the right vehicle for
> GPU/accelerator programming now that AI-assisted tooling narrows the
> language-familiarity gap.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "Link Blog" format — a short
  post built around a single external link, `trusted-feed` source per this
  corpus's existing scan conventions). Willison's own text is ~120 words: a
  timeline framing (promised in May 2023, delivered today), one quote from
  Modular's own August 2025 forum post explaining the abandonment of the
  Python-superset goal, and a one-sentence characterization of what Mojo is
  today.
- **Author credibility**: Simon Willison is an established high-signal
  practitioner source already extensively mined in this corpus. He is not a
  Mojo/Modular insider and adds no independent technical claims beyond
  selecting and framing the quote — the substantive claims in this note come
  from Modular's own first-party posts, which the Miner followed per MINER.md
  §1 because Willison's post is thin and points directly at them.
- **Scope**: Covers the open-source release itself (license, components,
  build process, contribution policy), the immediately preceding Mojo 1.0
  release (stability commitments, production-readiness claim, community
  contribution metrics, roadmap), and the August 2025 policy shift away from
  "Mojo as Python superset." Does NOT cover independent benchmarks of Mojo's
  performance claims, adoption numbers beyond the contributor/PR counts
  Modular itself reports, or any critical/skeptical outside commentary — no
  such commentary was found linked from or alongside this post.

## Extracted Claims

### Claim 1: Modular has released the Mojo compiler and full toolchain as open source under the Apache 2.0 license with LLVM exceptions, fulfilling a promise first made in May 2023
- **Evidence**: Willison's own framing plus Modular's announcement post, which states the license terms directly.
- **Confidence**: settled (a verifiable, dated product release event)
- **Quote**: "The Mojo programming language has been promising an open source release since May 2023. Last week they shipped their 1.0 and today they have followed through on that original promise, releasing the compiler and toolchain under an Apache 2 license." (Simon Willison)
- **Our assessment**: A straightforwardly verifiable release event. The three-year gap between promise (May 2023) and delivery (August 2026) is itself notable context for how long "we will open source this eventually" can stretch for a VC-backed language/toolchain project — worth noting if the guide ever discusses open-source timelines for AI-infrastructure vendors' promised releases.

### Claim 2: Modular chose Apache 2.0 with LLVM exceptions specifically because it is, in their words, the "gold standard" permissive license for programming languages and compilers, maximizing freedom to build and distribute compiled binaries
- **Evidence**: Direct quote from Modular's own open-source announcement post, under a section titled "Apache 2: A permissive license."
- **Confidence**: settled (a direct, verifiable statement of the vendor's own stated rationale)
- **Quote**: "The Apache 2.0 license is the gold standard for programming languages and compilers, because it provides great flexibility to be used in all sorts of applications. The LLVM extensions to the license further expand those freedoms for building and distributing binaries compiled from Mojo."
- **Our assessment**: A conventional, well-precedented licensing choice (LLVM, Clang, Rust, Swift all use similar permissive terms) — not a novel claim, but establishes that Mojo's open-source terms impose no unusual restriction on commercial or redistribution use, which matters if the guide ever recommends or evaluates Mojo for production GPU workloads.

### Claim 3: Modular abandoned Mojo's original stated goal of becoming a full syntactic/semantic superset of Python around August 2025, explicitly citing confidence that AI-assisted coding tools already handle Python-to-Mojo migration well enough that an official compatibility layer is no longer necessary
- **Evidence**: A quote from a Modular forum post ("Mojo Vision Document and Roadmap," dated August 26, 2025) that Willison cites directly.
- **Confidence**: emerging (a stated strategic pivot, not yet validated by independent evidence that AI-assisted migration tooling actually performs well at Python-to-Mojo translation)
- **Quote**: "Mojo may or may not evolve into a full superset of Python, and it's okay if it doesn't. We're encouraged by how well AI-assisted coding tools already help migrate Python to Mojo today, and we're confident that future tooling and ecosystem maturity will make this evolution even smoother."
- **Our assessment**: This is a striking design-strategy claim for this corpus's focus: a language vendor explicitly deciding *not* to build a compatibility/migration feature because they believe general-purpose AI coding tools already substitute for it, and betting that trend will only improve. This is a concrete instance of "AI-assisted tooling changes what a vendor needs to build" — worth flagging for any guide discussion of how AI coding assistants are reshaping product/language design decisions, not just individual developer workflows. It is Modular's own unverified confidence claim, not a measured migration-quality benchmark.

### Claim 4: Today, Mojo is positioned as its own distinct language rather than a Python-compatible one — Python-inspired syntax but not guaranteed source compatibility — explicitly optimized to make GPU programming as painless as possible
- **Evidence**: Willison's closing characterization, consistent with Modular's own "novel general purpose programming language" framing.
- **Confidence**: emerging (a characterization/interpretation, not a technical specification)
- **Quote**: "Today Mojo is its own language, optimized to make GPU programming as painless as possible using syntax inspired by Python, if not 100% compatible with existing code."
- **Our assessment**: Consistent with Modular's own framing ("Mojo integrates the latest in compiler and programming language research to unlock GPUs, AI accelerators, and other advanced compute" — Claim 5 below). This positions Mojo as a GPU/accelerator-first systems language with Python-like ergonomics, not a Python replacement or drop-in accelerator for existing Python codebases — a distinction the guide should preserve if it ever discusses Mojo as an option for performance-critical AI infrastructure code.

### Claim 5: Modular deliberately staged Mojo's open-sourcing over multiple years (standard library in 2024, hundreds of thousands of lines of kernel code next, the compiler and toolchain last), justified by a stated belief that small design teams — not committees — find a language's design "soul," while broader community feedback is still necessary to avoid an echo chamber
- **Evidence**: Modular's own announcement post, under the section explaining their open-sourcing philosophy.
- **Confidence**: settled (a direct, verifiable statement of the vendor's own stated design philosophy and the sequence of what was actually released when)
- **Quote**: "We believe that small and tight-knit design teams (not committees) are the best for finding the 'soul' of a language, but that feedback from a broader community is essential to escape an echo chamber. As such, we first open-sourced the Mojo standard library, then released hundreds of thousands of lines of kernel code written in Mojo, tools, and support."
- **Our assessment**: This is a coherent, explicit governance philosophy for language development — sequence exposure (stdlib, then kernels, then compiler) so community feedback shapes evolution without ceding design authority to open contribution from day one. It is a specific, named alternative to both "fully closed development" and "open contributions from the start," relevant to any guide discussion of how AI-infrastructure vendors balance open governance against maintaining design coherence.

### Claim 6: Despite open-sourcing the compiler source code, Modular is explicitly not yet accepting external contributions to the compiler and tooling, and frames this restraint as a lesson learned from operating a contribution pipeline "particularly in today's era of AI coding" — with a stated (non-binding) goal of opening contributions by the end of 2026
- **Evidence**: Modular's own announcement post, under a section titled "Contributions."
- **Confidence**: emerging (a stated policy and target date, not yet realized — the "by the end of this year" commitment is explicitly hedged)
- **Quote**: "The Mojo standard library has been accepting contributions since 2024, and we're grateful for everyone that has helped advance the language. One learning (particularly in today's era of AI coding) is that we need to be deliberate about how we handle contributions. As such, we aren't ready to take contributions to the compiler and tooling. We aim to accept contributions to the compiler and tooling by the end of this year, and we'll share more details when we can."
- **Our assessment**: This is the most directly AI-native-engineering-relevant claim in the source. Modular is saying, in effect, that running an open-source contribution pipeline for a compiler has gotten harder specifically because of AI-assisted contributions, severely enough that they are delaying opening a major new contribution surface (the compiler) until they have "more deliberate" handling in place — without specifying what changed or what the new process will look like. This corroborates (from the vendor side, for a compiler rather than a general-purpose OSS project) the same underlying pressure `blog-simonwillison-zig-anti-ai.md` documents Zig responding to with an outright ban — but Modular's response is different in kind: a temporary pause with an intent to eventually accept contributions under some unspecified new process, not a permanent prohibition. See Cross-References.

### Claim 7: Mojo reached 1.0 with an explicit commitment that, during the 1.x line, language changes will be primarily additive rather than breaking, with any breaking changes handled the way mature languages like C++ manage them
- **Evidence**: Modular's Mojo 1.0 release announcement.
- **Confidence**: settled (a direct, verifiable statement of the vendor's stated stability policy)
- **Quote**: "During the 1.x timeframe, changes should primarily be additive, giving developers confidence that the language will not continually shift beneath them. Breaking changes may still be made, but will be managed with care, following the standards of how mature languages (e.g. C++) evolve over time."
- **Our assessment**: A standard, well-understood semantic-versioning-style stability commitment for a systems language. Relevant to any guide discussion of Mojo adoption risk for production systems: teams can treat post-1.0 Mojo similarly to how they'd treat a mature C++ standard revision, rather than expecting Rust-edition- or Python-2-to-3-style breakage.

### Claim 8: Modular states that Mojo has moved beyond being a language under development to being production infrastructure the company itself depends on daily, as the foundation of its commercial MAX and Modular Cloud products
- **Evidence**: Modular's Mojo 1.0 release announcement, stated as the primary justification for calling the release "1.0" and making the stability commitment in Claim 7.
- **Confidence**: emerging (a first-party claim about internal production dependency; no independent verification of MAX/Modular Cloud's actual Mojo usage was found or attempted)
- **Quote**: "We are making that commitment today because Mojo is ready: it is no longer just a language we are developing; it is a language we rely on every day in production as the foundation of our commercial infrastructure, MAX and Modular Cloud."
- **Our assessment**: This is the vendor's own dogfooding claim, which is the strongest evidence available (a company betting its own commercial infrastructure on the language) but is still self-reported and unaudited. Worth citing as a data point for "does this language have a real production user," but should be presented as a vendor claim, not an independently confirmed fact.

### Claim 9: Since the Mojo standard library was open-sourced in 2024, nearly 200 outside contributors have landed more than 1,100 pull requests changing over 200,000 lines of code, with more than a thousand additional people filing issues that shaped the language
- **Evidence**: Modular's Mojo 1.0 release announcement, stated as a measured community-contribution tally.
- **Confidence**: settled (a specific, falsifiable numeric claim about a public GitHub repository's contribution history — though not independently re-verified by the Miner against the repository itself)
- **Quote**: "Since we open-sourced the standard library, nearly 200 contributors have landed more than 1,100 pull requests, changing over 200,000 lines of code, and more than a thousand others have filed issues that shaped the language."
- **Our assessment**: A concrete, checkable community-engagement metric (unlike Claim 6's forward-looking, unspecified compiler contribution plan). This is stdlib-only engagement over roughly two years — useful baseline if the guide later wants to track whether opening the compiler itself (once contributions are accepted, per Claim 6) produces comparable or larger community engagement.

### Claim 10: Mojo's open-source release happened after Modular itself was acquired by Qualcomm, with the acquisition completing on July 29, 2026 — roughly three weeks before the compiler open-sourcing announcement
- **Evidence**: Modular's own website footer copyright line and its blog post archive listing, both retrieved directly from the live site.
- **Confidence**: settled (directly observable on Modular's own site; not mentioned in Willison's post or in the two blog posts analyzed above, so this is Miner-added context from following the source further than the linked articles themselves)
- **Quote**: "Copyright © 2026 Modular Inc, A Qualcomm Company" (site footer); blog archive listing shows "Qualcomm Completes Acquisition of Modular — July 29, 2026" and "Qualcomm to Acquire Modular — June 24, 2026" as the two entries immediately preceding the Mojo open-source and 1.0 posts.
- **Our assessment**: Not mentioned anywhere in the three articles the Miner read in depth, but directly relevant context the guide should not omit: Mojo's open-sourcing and 1.0 stability commitment happened under new corporate ownership, not as an independent startup's decision. Whether Qualcomm's acquisition motivated or accelerated the long-promised (since May 2023, per Claim 1) open-source release is not addressed by any source found — flagging as an open question rather than asserting causation.

### Claim 11: Modular's stated roadmap beyond 1.0 includes asynchronous programming, pattern matching, and unions, framed as steps toward making Mojo "a truly great general-purpose systems programming language" for CPUs, GPUs, and accelerators — not a narrowly-scoped AI/ML-only language
- **Evidence**: Modular's Mojo 1.0 release announcement, closing "Future Direction" section.
- **Confidence**: emerging (a stated intention/roadmap, not yet delivered)
- **Quote**: "Mojo has already established itself as a powerful language for writing high-performance code across modern CPUs, GPUs, and accelerators. The next phase of its evolution is to broaden that foundation and make Mojo a truly great general-purpose systems programming language. That means continuing to invest in the core language and developer experience, with major capabilities ahead including a robust asynchronous programming model, pattern matching and unions, and much more."
- **Our assessment**: Notable ambition-scope claim: Modular explicitly frames general-purpose systems programming (not just GPU/AI-accelerator kernels) as the language's eventual target, despite Mojo's origin and current adoption being almost entirely in the GPU/AI-kernel niche (per the contributor bios on Modular's own "Community Champions" page, which skew heavily toward HPC, compiler, and AI-infrastructure backgrounds). Whether Mojo actually displaces general-purpose systems languages (C++, Rust, Zig) outside the AI/GPU niche is untested and should be treated as aspiration, not trend.

## Concrete Artifacts

Build instructions from Modular's compiler open-source announcement (verbatim):

```
git clone https://github.com/modular/modular.git
cd modular
./bazelw run --config=build-mojo KGEN:mojo -- run hello.mojo
```

Testing standard library modifications:

```
./bazelw test --config=build-mojo mojo/stdlib/test/...
```

Upgrading to Mojo 1.0 (from Modular's 1.0 release notes):

```
uv pip install --upgrade mojo
uv pip install max[all]
```

Modular's own philosophy statement on staged open-sourcing (source: Mojo
open-source announcement, "A staged approach" framing, verbatim):

```
"We believe that small and tight-knit design teams (not committees) are the
best for finding the 'soul' of a language, but that feedback from a broader
community is essential to escape an echo chamber. As such, we first
open-sourced the Mojo standard library, then released hundreds of thousands
of lines of kernel code written in Mojo, tools, and support. We built
together with community feedback and public design proposals, and are now
open sourcing the compiler. We will continue to open our processes further
as Mojo keeps maturing."
```

## Cross-References

- **Corroborates**: `blog-ronacher-fast-hard-code.md`, which argues that
  LLM-assisted coding has eroded programming-language-familiarity friction
  and made "hard languages" more broadly accessible — Claim 3's account of
  Modular explicitly relying on "AI-assisted coding tools" to handle
  Python-to-Mojo migration, instead of building an official compatibility
  layer, is a concrete, named instance of a vendor betting on exactly the
  dynamic Ronacher describes in the abstract.
- **Contradicts**: None identified as a direct factual conflict. Claim 6
  (Modular delaying compiler contributions, citing "today's era of AI
  coding," while planning to eventually accept them under stricter, unspecified
  handling) is a *different institutional response* to the same underlying
  pressure that `blog-simonwillison-zig-anti-ai.md` documents Zig responding
  to with a total, permanent ban on LLM-assisted contributions across all
  channels. These are not a contradiction in the MINER.md §4a sense — both
  sources agree AI-assisted contributions strain OSS review capacity; they
  differ in remedy (Zig: outright ban; Modular: temporary pause plus
  intent to reopen under a to-be-defined process) and in scope (Zig: all
  contribution channels, including a project with a long-established
  external contributor base; Modular: specifically the compiler/tooling,
  a brand-new contribution surface with no prior external-contribution
  history). No contradiction issue filed; flagging the comparison for the
  Assayer/Smith as a useful "two vendors, two different policy responses to
  the same pressure" pairing if the guide ever surveys OSS-maintainer
  responses to AI-assisted contributions.
- **Extends**: No existing source note documents Mojo, Modular, or Chris
  Lattner's post-Swift/LLVM work, so this note does not extend prior
  coverage of this specific project. It does extend the corpus's existing
  "systems-language-in-the-LLM-era" thread (`blog-ronacher-fast-hard-code.md`,
  `blog-simonwillison-zig-anti-ai.md`, `blog-simonwillison-andrew-kelley.md`)
  with a first-party vendor account rather than outside commentary.
- **Novel**: Mojo, Modular, and the entire GPU-accelerator-programming-language
  angle are new to this corpus — no existing source note mentions Mojo,
  Modular, or Chris Lattner. The Qualcomm acquisition of Modular (Claim 10)
  is also new and not mentioned in any existing note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Claim 6 (Modular pausing compiler
  contributions and citing "today's era of AI coding" as a reason to be more
  deliberate about contribution handling) is a concrete, named data point for
  any section on how AI-assisted contributions are straining open-source
  maintainer capacity — pair it with `blog-simonwillison-zig-anti-ai.md`'s
  contrasting "ban everything" response and `blog-simonwillison-andrew-kelley.md`'s
  "digital smell" detection claim to show a spectrum of institutional
  responses (ban vs. pause-and-redesign vs. detect-and-reject-individually)
  to the same underlying pressure, rather than treating Zig's ban as the only
  documented reaction.
- **Chapter 04 (Context Engineering) / language and tooling landscape**:
  Claim 3 (Modular explicitly declining to build Python-compatibility tooling
  because AI-assisted coding tools already handle the migration) is a
  concrete example, if the guide ever discusses how AI coding assistants
  change vendor build-vs-rely-on-AI decisions, of a vendor choosing "rely on
  general AI tooling" over "build a dedicated compatibility feature" — worth
  flagging as an early, checkable instance of this pattern, alongside
  Ronacher's more general argument in `blog-ronacher-fast-hard-code.md`.
- **Do not cite as settled**: Claims 3, 4, 6, 8, and 11 are vendor
  self-characterizations or forward-looking commitments, not independently
  verified outcomes — the guide should attribute these to Modular rather than
  stating them as established fact if it draws on this note.

## Extraction Notes

- Willison's original post is very short (~120 words); per MINER.md §1 the
  Miner followed three outbound links to substantive pages: Modular's
  open-source announcement (`modular.com/blog/mojo-open-source`), Modular's
  Mojo 1.0 release notes (`modular.com/blog/modular-26-5-mojo-1-0-is-here`),
  and the Modular forum thread Willison quotes from
  (`forum.modular.com/t/mojo-vision-document-and-roadmap/2187`). The May 2023
  original-announcement link (`simonwillison.net/2023/May/4/mojo/`) was not
  separately fetched — it predates the AI-native-engineering scope of this
  corpus and Willison's current post already summarizes its relevance (the
  original open-source promise).
- All quotes in this note were verified character-for-character against raw
  HTML fetched directly via `curl` (not the AI-summarized WebFetch tool
  output, which was used only for initial orientation/triage of each page,
  per the caution in MINER.md §2a and the extraction-notes precedent in
  `blog-thoughtworks-singh-shaik-performance-engineering.md`). Curly
  apostrophes/quotation marks in the original HTML were normalized to
  straight ASCII quotes for this note's markdown, consistent with how
  Willison's own site renders `&#8217;` etc.; no wording was altered.
- Claim 10 (the Qualcomm acquisition) is not mentioned in any of the three
  articles the Miner read for substance — it was found by inspecting
  Modular's own site chrome (footer copyright line, blog archive listing)
  while verifying the other quotes. This is Miner-added context beyond what
  the source itself states, flagged explicitly in the claim's evidence line
  rather than presented as if Willison or Modular's blog posts discussed it.
- Did not fetch or verify Modular's separate "Qualcomm Completes Acquisition
  of Modular" (July 29, 2026) or "Qualcomm to Acquire Modular" (June 24,
  2026) blog posts in depth — Claim 10 relies only on the dated headline
  text and footer copyright line visible in the pages already fetched.
  Flagging both as candidate future sources if the guide ever needs deeper
  detail on the terms or stated rationale for the acquisition.
- The Modular "Community Champions" page content (contributor bios) was
  incidentally captured while fetching the open-source announcement page (it
  appears to be assembled via client-side JS injection sharing the same page
  bundle) and is referenced only briefly in Claim 11's assessment as color
  for who Mojo's current contributor base actually is; it was not
  systematically extracted as a separate source.
