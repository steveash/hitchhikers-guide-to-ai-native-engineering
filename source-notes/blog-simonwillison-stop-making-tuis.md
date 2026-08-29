---
source_url: https://simonwillison.net/2026/Aug/21/stop-making-tuis/
source_type: blog-post
title: "Stop Making TUIs"
author: Simon Willison (relaying Thomas Ptacek)
date_published: 2026-08-21
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3047"
---

# Stop Making TUIs

> Simon Willison relays and endorses Thomas Ptacek's argument that coding agents have
> driven the cost of building a real native GUI down to almost nothing, making "throwaway
> CLI" the wrong default for personal tools — Willison corroborates with his own
> daily-use, vibe-coded SwiftUI menu-bar apps, while admitting he hasn't yet generalized
> the practice to his other 200+ tools.

## Source Context

- **Type**: blog-post (link-blog post; Willison's own original text is three short
  paragraphs plus one block-quoted sentence from Ptacek). The substantive argument lives
  in the linked article, Thomas Ptacek's "Stop Making TUIs" at
  `sockpuppet.org/blog/2026/08/20/stop-making-tuis/` (published one day earlier, 2026-08-20),
  which was fetched in full and read per MINER.md §1 as a linked page that "seems
  substantive." A second linked page, Willison's own "Vibe coding SwiftUI apps is a lot of
  fun" (`simonwillison.net/2026/Mar/27/vibe-coding-swiftui/`, published 2026-03-27), was
  also fetched in full — it is Willison's first-hand account of the two apps he references
  in this post and supplies concrete workflow detail this post only summarizes.
- **Author credibility**: Simon Willison is the creator of Django and one of the most
  widely-cited independent LLM-tooling commentators, with no vendor affiliation; he
  maintains 200+ personal tools at tools.simonwillison.net. Thomas Ptacek is a veteran
  security engineer and co-founder of Matasano Security / Latacora, a long-time
  Hacker-News-prominent essayist on software engineering practice, and — by his own
  account here — a newcomer to native UI development ("I built my first serious Mac
  application a few months ago"), which makes his conversion narrative first-hand
  practitioner testimony rather than a pre-existing native-app enthusiast's advocacy.
- **Scope**: Covers the claim that coding agents have made native GUI development cheap
  enough to default to for personal/small tools, a structural critique of TUI frameworks
  versus native UI frameworks, a historical reframing of why TUIs exist at all, rebuttals
  to the standard pro-TUI arguments (density, SSH-friendliness, accessibility,
  cross-platform reach), and a concrete workflow (skills, template repo, Makefile build)
  for how Ptacek gets agents to produce native macOS apps. Does NOT cover: Windows/Linux
  native UI tooling in the same first-hand depth (Ptacek explicitly says he can't speak to
  it directly), team-scale or product-shipping GUI development, or any quantitative
  measurement of development-time savings.

## Extracted Claims

### Claim 1: Coding agents have reduced the cost of getting a usable native GUI running to almost nothing, which Ptacek argues should flip the default choice away from throwaway CLIs
- **Evidence**: Willison's framing sentence introducing the linked Ptacek post, plus
  Ptacek's own closing exhortation naming "500 throwaway CLIs" as the thing to reconsider.
- **Confidence**: emerging (two independent, credible practitioners converging on the same
  claim, each with concrete built artifacts as evidence — not a survey or measurement, but
  not a single anecdote either)
- **Quote**: "Thomas Ptacek advocates for building real native user interfaces for even the
  smallest of personal tools, because coding agents have reduced the cost of getting a
  usable-enough GUI up and running to almost nothing."
- **Our assessment**: This is the core claim of the source and the reason it was flagged
  high-novelty by the Prospector. It is a specific economic claim (cost of native UI ≈ cost
  of CLI, now that agents write the UI code), not a vague enthusiasm claim, and it names a
  concrete decision point practitioners face constantly: "do I wrap this in a CLI or build
  it a window?" The claim is credible because both authors back it with shipped,
  daily-used artifacts (see Claims 2 and 9 below), not just stated belief.

### Claim 2: Building good UI code is inherently hard — tedious, repetitive, exacting, and gated by platform-specific conceptual knowledge — which is exactly the kind of work well-suited to delegation to an agent rather than hand-writing
- **Evidence**: Ptacek's own account of building MDV.app, a native macOS Markdown viewer,
  without writing the UI code himself.
- **Confidence**: emerging (first-hand practitioner account with a linked, real artifact —
  github.com/tqbf/mdv — as evidence)
- **Quote**: "I had almost no hand in writing this UI code. Why would I? Like most user
  interfaces, MDV doesn't break any new ground. It's not a challenging problem. But
  building good UI is very hard: this kind of code is tedious, repetitive, exacting, and
  gated by platform conceptual knowledge. It takes years to get good at this kind of work.
  Which is why I would never hand-write this program. Instead, I summoned it."
- **Our assessment**: This reframes the "years to get good at this" barrier as a solved
  problem for agents specifically, not for humans generally — Ptacek is not claiming UI
  work has gotten easier for people, only that it has become cheap to delegate. This is an
  important distinction for the guide: the claim is about a change in the cost of
  delegation, not a change in the intrinsic difficulty of the task.

### Claim 3: TUI frameworks structurally cannot match what native UI frameworks provide by default — scrolling, drag-and-drop, text selection, multiple floating windows, and image handling all require extra work in a TUI and come free in native UI
- **Evidence**: Ptacek's direct technical comparison, naming three specific modern TUI
  frameworks (Ratatui, Textual, Bubbletea) as the state of the art and still finding them
  short of native defaults.
- **Confidence**: emerging (a specific, falsifiable technical claim from a practitioner who
  names concrete frameworks rather than arguing in the abstract)
- **Quote**: "But there's one of the problems with TUIs: even with a good framework, like
  Ratatui, Textual, or Bubbletea, you're fighting the terminal to come asymptotically close
  to what every native framework does well out of the box. Scrolling and scroll targets are
  an obvious example. Drag and drop another. Text selection — it gets tricky when you're
  using in-band signaling to draw window borders! Multiple floating windows. All this is
  before we get to image handling."
- **Our assessment**: This is the mechanistic argument underneath Claim 1 — it explains
  *why* native UI is now the cheaper choice, not just that it is: an agent generating
  native UI code gets these behaviors for free from the platform framework, while an agent
  generating TUI code has to reimplement approximations of them. The cost asymmetry Ptacek
  describes is structural, not just a matter of current framework maturity.

### Claim 4: TUIs exist for two historically contingent reasons — modems and Unix-nerd resistance to learning Motif — not because terminal interfaces have some inherent advantage
- **Evidence**: Ptacek's historical argument, explicitly rebutting the "In the Beginning
  Was the Command Line" (Neal Stephenson) framing of CLI/TUI culture as the natural,
  privileged mode of computing.
- **Confidence**: anecdotal (a historical/rhetorical claim, not empirically testable; framed
  by Ptacek himself as provocative — "set the field of human-computer interaction back
  about 20 years" regarding the Stephenson essay)
- **Quote**: "In reality, terminal interfaces don't exist because of any special machine
  sympathy they create between computers and their operators. Rather, TUIs exist for just
  two reasons: modems, and because Unix nerds didn't want to learn Motif."
- **Our assessment**: This is a deliberately provocative reframing rather than a measured
  claim, and the guide should treat it as rhetorical color supporting Claim 1, not as a
  settled historical fact. Its function in the source is to strip TUIs of the cultural
  legitimacy that might otherwise make "build a TUI" feel like the disciplined, expert
  choice — clearing the way for the economic argument in Claim 1.

### Claim 5: The claim that TUIs are accessible is probably false — screen readers struggle with TUI "chrome" in ways that modern native UI frameworks, which maintain a separate semantic accessibility tree, do not
- **Evidence**: Ptacek cites a talk by an accessibility practitioner describing how screen
  readers announce TUI line-redraws character by character, and contrasts this with
  SwiftUI's dual visual/semantic tree architecture. He explicitly caveats that he is "not a
  customer of accessibility features" and is relaying others' documented experience.
- **Confidence**: anecdotal (Ptacek relays second-hand a11y practitioner testimony rather
  than his own direct experience; he flags this limitation himself)
- **Quote**: "The problem with this argument is that it's probably false. I want to be
  careful with this argument, because I'm not a customer of accessibility features. All I
  can do is go off the experiences of people who do a11y work."
- **Our assessment**: This is the most hedged claim in the source, and the hedging is
  itself useful signal — Ptacek is careful not to overstate secondhand evidence. The guide
  should cite this as a real counter-consideration to "TUIs are more accessible" folk
  wisdom, but flag it as anecdotal/relayed rather than settled, consistent with Ptacek's
  own framing.

### Claim 6: Cross-platform reach over SSH remains the one legitimate structural argument for TUIs, but it doesn't apply to tools built only for the author's own personal, unshared use
- **Evidence**: Ptacek's own concession, immediately followed by his explanation of why it
  doesn't change his personal calculus — he distinguishes "vibe-coding" from
  "vibe-shipping" and states he isn't shipping these apps to other users.
- **Confidence**: emerging (a reasoned concession from the same practitioner making the
  broader argument, which strengthens rather than weakens the overall claim's credibility —
  he is not claiming TUIs have zero use case)
- **Quote**: "I can get an agent to build native UI for me on Windows and Linux and I'm
  confident I'll end up with something reasonable. But I don't have Windows and Linux
  desktops to play with those interfaces on, and while the ground is certainly shifting
  below all of our feet, I think we can all agree there remains an important distinction
  between vibe-coding and vibe-shipping. Somebody soon is going to ship an app that they
  literally haven't looked at or used. But it won't be me."
- **Our assessment**: This is the key conditioning variable the guide needs to preserve:
  Ptacek's argument is scoped to personal/small tools that are built for one user (usually
  the author) and never distributed. Tools that must run over SSH on a remote host, or that
  must reach users on heterogeneous platforms the author cannot test, remain legitimate TUI
  (or CLI) territory. The guide should not present "stop making TUIs" as unconditional
  advice — it is conditional on the tool being personal and undistributed.

### Claim 7: Named, reusable "skills" for platform design conventions, UI frameworks, and language idioms are the concrete mechanism that lets an agent produce above-replacement-level native UI quickly
- **Evidence**: Ptacek names the specific skills he uses — a macOS design skill, a
  typography skill, Paul Hudson's SwiftUI skill, and Airbnb's Swift language skill — with
  a link to the macOS design skill's GitHub repo.
- **Confidence**: emerging (concrete, named, linked artifacts rather than a vague
  "I used some prompts" account)
- **Quote**: "What I did was to go trawling for skills, ending up taking this macOS design
  skill, a basic typography skill (any one you found on Github today would be better than
  what I'm using), and Paul Hudson's SwiftUI skill. I also took Airbnb's Swift language
  skill, because I haven't grown out of caring whether the code I generate is idiomatic."
- **Our assessment**: This ties the native-UI claim directly to the skills mechanism the
  corpus already documents as a harness extension point (see Cross-References). The
  practical implication for the guide: the "build native UI instead of a TUI" advice is not
  just "trust the agent" — it depends on equipping the agent with domain-specific skills
  for the target platform's design language, which is itself a harness-engineering task.

### Claim 8: A full SwiftUI macOS app can fit in a single source file small enough that an agent can build and iterate on it without the developer ever opening Xcode
- **Evidence**: Both Ptacek and Willison independently report this. Willison gives file
  sizes for his own apps (GpuerApp.swift at 880 lines, BandwidtherApp.swift at 1063 lines)
  and names the models involved (Claude Opus 4.6, GPT-5.4); Ptacek separately describes a
  Makefile-driven build process that avoids Xcode entirely.
- **Confidence**: emerging (independently corroborated by two practitioners with linked,
  inspectable source repositories — github.com/simonw/gpuer and github.com/simonw/bandwidther)
- **Quote**: "It turns out Claude Opus 4.6 and GPT-5.4 are both very competent at
  SwiftUI—and a full SwiftUI app can fit in a single text file, which means I can use them
  to spin something up without even opening Xcode." (Simon Willison, "Vibe coding SwiftUI
  apps is a lot of fun," 2026-03-27)
- **Our assessment**: This is the concrete tooling-friction claim underneath the broader
  economic argument: part of why native UI got cheap isn't just "agents can write UI code,"
  it's that the surrounding toolchain friction (opening Xcode, managing an Xcode project)
  can also be avoided or delegated. For the guide, this is an actionable detail: the
  single-file-app-plus-Makefile pattern is what makes SwiftUI tractable as an agent target
  in the first place.

### Claim 9: Practitioners are shipping and daily-using AI-built personal tools whose correctness they have not verified and, in at least one documented case, that reported clearly wrong data
- **Evidence**: Willison's own account of his Gpuer app misreporting available memory,
  caught by comparison against Activity Monitor and then "fixed" by pasting a screenshot
  back to Claude Code — with no independent confirmation the fix is correct. Ptacek makes
  the parallel observation about his AI-assisted music player.
- **Confidence**: anecdotal (two first-hand practitioner accounts, not measured, but both
  practitioners volunteer the caveat unprompted rather than glossing over it)
- **Quote**: "This morning I caught Gpuer reporting that I had just 5GB of memory left when
  that clearly wasn't the case (according to Activity Monitor)." (Simon Willison, March
  2026 post) / "I don't really know what to think about programs like this. It's an
  AI-assisted music player that includes 90% of the interface of Music.app. Music.app. My
  ever-present personal computing nemesis. This is the personal computing equivalent of
  slaying a dragon. But I didn't write a single line of code in it. Am I developing
  software, or just configuring my computer?" (Thomas Ptacek)
- **Our assessment**: This is the load-bearing caveat the guide must not drop when citing
  the "stop making TUIs, build native UI" advice: the same agent fluency that makes native
  UI cheap to build also makes it easy to ship uninspected, unverified code for tools the
  author trusts daily. Willison's own quality-signal framework (see Cross-References) says
  use-evidence should replace artifact inspection as the trust signal — but "used daily for
  months" clearly did not catch a wrong memory reading here, which is a real limit on that
  heuristic, not just a hypothetical one.

### Claim 10: Recombining working code from one agent-built app as a reference for building a similar app accelerates development of the second app
- **Evidence**: Willison's own account of building Bandwidther and Gpuer in parallel agent
  sessions and explicitly instructing one session to imitate a UI pattern ("sys tray icon")
  that had just been added in the other.
- **Confidence**: anecdotal (single practitioner, single instance, but a concrete and
  reproducible workflow description)
- **Quote**: "Now take a look at recent changes in /tmp/bandwidther—that app now uses a sys
  tray icon, imitate that." (prompt to the agent, quoted verbatim in Willison's March 2026
  post) / "This remains one of my favorite tricks for using coding agents: having them
  recombine elements from other projects."
- **Our assessment**: This is a specific, actionable delegation pattern distinct from the
  main native-UI argument: point one agent session at another project's working code and
  ask it to imitate a feature, rather than re-specifying the feature from scratch. It
  applies generally to agent-built tooling, not just SwiftUI apps.

### Claim 11: Even a practitioner who has personally validated the native-UI approach and endorses it publicly has not yet generalized it to the rest of his tool portfolio
- **Evidence**: Willison's own closing admission in the source post itself, distinguishing
  his two SwiftUI apps (built and daily-used since March) from his broader body of tools.
- **Confidence**: anecdotal (single practitioner's stated personal practice at time of
  writing)
- **Quote**: "I'm not habitually knocking out real UIs for my other projects yet, but I'm
  running out of excuses!"
- **Our assessment**: This is a useful honesty signal for the guide: adoption lag exists
  even among practitioners who have already done the work and confirmed the benefit for
  themselves. The guide should not present "practitioners have already fully shifted to
  native UI defaults" as the current state — the more accurate framing is "the economic
  argument is now credible and the barrier to trying it is low, but even believers haven't
  fully operationalized it yet."

## Concrete Artifacts

### Ptacek's shipped native-UI portfolio (from sockpuppet.org, verbatim names and repos)

```
Thomas Ptacek, "Stop Making TUIs" (sockpuppet.org/blog/2026/08/20/stop-making-tuis/):

- MDV.app — native macOS Markdown viewer (github.com/tqbf/mdv)
- A native calculator-style frontend for SageMath (unpackaged; "screenshot this
  section of the post and give it to Claude")
- DJ Roomba — Apple Music player with embedded LLM agent (tool calls into music
  library/last-played/upcoming tracks), backed by SQLite
- Self Driving Wiki.app — LLM wiki that drives `claude -p` under the hood via a
  macOS virtual filesystem extension exposing a read-only SQLite view
- A semiautomated food macro tracker fronting GPT-5
- Thermite — menu-bar thermometer reading TP-Link temperature sensors
- A menu-bar Apple TV / Roku / Denon universal remote control
```

### Ptacek's agent-assisted native-UI build process (verbatim)

```
Thomas Ptacek, sockpuppet.org/blog/2026/08/20/stop-making-tuis/:

"What I did was to go trawling for skills, ending up taking this macOS design skill,
a basic typography skill (any one you found on Github today would be better than
what I'm using), and Paul Hudson's SwiftUI skill. I also took Airbnb's Swift language
skill, because I haven't grown out of caring whether the code I generate is idiomatic."

"You want to make sure you've got computer-use, or whatever Codex calls it, enabled.
You want to be able to fire this off, go make lunch, and come back to an app that
works well enough to be pleasant to debug."

"My biggest quality-of-life win is never having to open Xcode. Thankfully, my friend
Josh built a purely Makefile-driven build process after trying to compile MDV for
himself. I've just had Claude copy it to every new project I do."

"In fact, that's my entire process at this point: I copy a template app directory,
open Claude or Codex in it, and tell it what I want to build."

Skills referenced (as linked in source):
  macOS design skill: github.com/ceorkm/macos-design-skill
  Paul Hudson's SwiftUI skill: github.com/twostraws/swiftui-agent-skill
  Airbnb's Swift language skill: swift.airbnb.tech/skill
  Ptacek's template app directory: github.com/tqbf/swiftui-app
```

### Ptacek's rebuttal structure to standard pro-TUI arguments (verbatim, condensed)

```
Thomas Ptacek, sockpuppet.org/blog/2026/08/20/stop-making-tuis/:

Argument: "TUIs are economical and fast interfaces with high information density."
Rebuttal: "Nothing is stopping you from designing a dense and economical GUI.
It's been done!" [links Bloomberg Terminal]

Argument: "TUIs work over SSH connections. If you need a user interface on prod,
it's going to be a TUI."
Rebuttal: "The problem with this argument is that you probably don't need a user
interface on prod. You need a command line interface on prod that a user interface
on your Macbook can drive." [cites Emacs TRAMP as precedent]

Argument: "TUIs are accessible."
Rebuttal: "The problem with this argument is that it's probably false." [cites a
talk on screen readers and TUI chrome; SwiftUI's dual visual/accessibility tree]

Argument: "TUIs are cross-platform."
Rebuttal: conceded as the one strong argument, but scoped away for tools the author
builds only for himself and does not ship to others ("vibe-coding" vs "vibe-shipping").
```

### Willison's SwiftUI workflow, prompt sequence (verbatim, from the March 2026 linked post)

```
Simon Willison, simonwillison.net/2026/Mar/27/vibe-coding-swiftui/:

Prompt 1: "Show me how much network bandwidth is in use from this machine to the
internet as opposed to local LAN"
Prompt 2: "mkdir /tmp/bandwidther and write a native Swift UI app in there that
shows me these details on a live ongoing basis"
Prompt 3: "git init and git commit what you have so far"
Prompt 4: "Now suggest features we could add to that app, the goal is to provide
as much detail as possible concerning network usage including by different apps"
Prompt 5: "add Per-Process Bandwidth, relaunch the app once that is done"
Prompt 6: "now add the reverse DNS feature but make sure original IP addresses are
still visible too, albeit in smaller typeface"
Prompt 7: "redesign the app so that it is wider, I want two columns—the per-process
one on the left and the rest on the right"
Prompt 8: "OK make it a task bar icon thing, when I click the icon I want the app to
appear, the icon itself should be a neat minimal little thing"

Repos: github.com/simonw/bandwidther, github.com/simonw/gpuer
File sizes: GpuerApp.swift (880 lines), BandwidtherApp.swift (1063 lines)
Models used: Claude Opus 4.6, GPT-5.4
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 2 ("Vibe-coded apps trend toward
    being more personal, more situated, and more frequent"): Ptacek's entire portfolio
    (MDV, DJ Roomba, Self Driving Wiki, the macro tracker, Thermite, the Apple TV remote)
    is a concrete, named instance of exactly this pattern — tools built for one person's
    specific situation, several explicitly never packaged for distribution ("I'm not
    packaging this application up").
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 4 and Claim 5 (broken
    artifact-quality signals; use-evidence as the replacement heuristic): Willison's own
    "used daily since March" framing of his SwiftUI apps in this post is a direct
    application of his own use-evidence heuristic from that earlier post. Claim 9 above
    (the Gpuer wrong-memory-reading incident) is a concrete case where that heuristic still
    let a real defect through, which the guide should note as a limit on the heuristic, not
    just an application of it.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 4 ("Skills are folders that can
    include scripts, assets, data, and other resources — not just markdown files"):
    Ptacek's named skills (macOS design skill, SwiftUI skill, Swift language skill) are a
    real-world, external (non-Anthropic) instance of the skills pattern that note
    documents from the inside of the Claude Code team. This source is independent
    confirmation that the skills mechanism is being used by practitioners outside
    Anthropic for exactly the kind of domain-specific knowledge injection that note
    describes.
  - `blog-ronacher-fast-hard-code.md` Claim 10 ("LLM assistance is also making 'much
    harder' technologies ... newly approachable for developers who previously could not
    work in these domains"): Ptacek's claim that native UI development — "gated by
    platform conceptual knowledge," taking "years to get good at" — has become
    delegable to an agent is the UI-development instance of the same general pattern
    Ronacher documents for DWARF, eBPF, and cryptography. Both sources independently
    describe agents dissolving a previously expertise-gated technical domain.

- **Extends**:
  - `blog-simonwillison-rss-vibe-coded-apps.md`: that note covers the *distribution*
    problem created by abundant vibe-coded tools (how do people discover 80-200+ tools?).
    This source is entirely about a prior question — *what form should the tool take in
    the first place* (CLI/TUI vs. native GUI) — that precedes the distribution question.
    Together they cover more of the tool lifecycle: build-form decision (this source) →
    distribution (the RSS note).
  - `blog-kentbeck-yagni-economics.md` Claim 6 ("Cheap/free AI code generation collapses
    the thrift-based justification for YAGNI... but leaves both the optionality and NPV
    bills fully intact"): Beck's essay is about *not* building speculative structure just
    because it's cheap now. Ptacek's argument is compatible, not contradictory, because
    Ptacek is not arguing for speculative structure — he is arguing for building the UI
    for tools that already exist and are already in active use (his "500 throwaway CLIs"
    are existing, used tools, not speculative future features). The guide should present
    these as answering different questions: Beck says cheap code generation doesn't
    justify building things you don't need; Ptacek says cheap code generation does justify
    upgrading the interface of things you already use.

- **Contradicts**: None filed. There is a real tension worth flagging for the Smith,
  short of a filable contradiction under MINER.md §4a: `blog-ccunpacked-claude-code-
  architecture.md` Claim 6 documents that Claude Code itself is built as a
  sophisticated, "game engine"-style TUI, not a native GUI. This is not a contradiction
  under the §4a criteria ("claims differ only in context... that's a conditioning
  variable") — Ptacek explicitly carves out SSH-compatible, genuinely cross-platform,
  distributed tools as the one legitimate remaining TUI use case (Claim 6 above), and
  Claude Code is exactly that kind of tool (runs on a remote host over SSH, ships to
  users across Mac/Linux/Windows). The two sources are consistent once the conditioning
  variable (personal/undistributed vs. distributed/SSH-dependent tooling) is made
  explicit; the guide should state that variable clearly rather than presenting "stop
  making TUIs" as a universal rule that Anthropic's own flagship product violates.

- **Novel**: The specific economic argument — that native UI has become the *cheaper*
  default relative to a CLI/TUI, rather than merely a nicer-but-more-expensive option —
  is new to the corpus. Prior vibe-coding sources (`blog-simonwillison-rss-vibe-coded-
  apps.md`, `blog-simonwillison-vibe-coding-agentic-engineering.md`) address development
  speed and distribution but do not address the CLI-vs-GUI architectural decision itself.
  The named skills-based workflow for native macOS app development (design skill +
  framework skill + language skill + template repo + Makefile build, avoiding Xcode
  entirely) is also new concrete tooling detail not previously captured in the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add "native UI vs. CLI/TUI" as an explicit decision
  point when building a personal tool, citing Claim 1, Claim 3, and Claim 6. State the
  conditioning variable plainly: for a tool built for yourself and not shipped to others,
  the guide should recommend defaulting to a native GUI (agents now produce this cheaply
  and it comes with free scrolling/drag-and-drop/accessibility-tree support per Claim 3);
  for a tool that must run over SSH on a remote host or reach users on platforms you can't
  test, CLI/TUI remains the right call (Claim 6). This directly updates any existing "just
  build a quick CLI" default guidance for personal tooling.

- **Chapter 02 (Harness Engineering)**: Claim 7 and the Concrete Artifacts skills list
  give a specific, actionable pattern: domain skills (platform design conventions, UI
  framework conventions, language idioms) plus a reusable template repo plus a
  Makefile-driven build are what make native UI a low-friction agent target. This extends
  the existing skills-as-harness-extension-point material (`blog-anthropic-claude-code-
  skills-lessons.md`) with an external, independently-verified example of the pattern in
  use.

- **Chapter 02 or 04 (Responsible AI Use / Operational Concerns)**: Claim 9 is a
  necessary caveat wherever the guide cites "use-evidence over artifact inspection" as a
  quality heuristic (per `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5).
  The Gpuer wrong-memory-reading incident is a concrete counter-example: daily use for
  weeks did not catch a real defect. The guide should present use-evidence as a
  risk-reducing heuristic, not a correctness guarantee, and should note that this
  limitation applies specifically to tools whose correctness the user is not equipped to
  independently verify (Willison, in the March 2026 post that supplies the Claim 9
  evidence: "I am completely unqualified to evaluate if the numbers and charts being spat
  out by these tools are credible or accurate!").

- **Chapter 00 (Principles) or wherever CLAUDE.md/Claude Code's own architecture is
  discussed**: If the guide ever cites Ptacek's "stop making TUIs" advice, it should
  explicitly reconcile it with the fact that Claude Code itself is a sophisticated TUI
  (per `blog-ccunpacked-claude-code-architecture.md` Claim 6), using the SSH/cross-platform
  conditioning variable from Claim 6 above, so the two pieces of guidance don't read as
  contradictory to an attentive reader.

## Extraction Notes

- **Both linked pages fetched and read in full**: Ptacek's "Stop Making TUIs"
  (sockpuppet.org/blog/2026/08/20/stop-making-tuis/) and Willison's own March 2026
  "Vibe coding SwiftUI apps is a lot of fun" were both fetched via direct HTTP request
  (not WebFetch's summarizing tool, which returned only lossy paraphrase summaries for
  both the Willison Aug 21 post and the Ptacek post on first attempt) and read in full as
  raw HTML, with all quotes in this note copied character-for-character from that raw
  HTML, including the source's own curly-quote/straight-quote inconsistencies (Willison's
  original prose uses straight apostrophes; the blockquoted Ptacek sentence and Ptacek's
  own site both use curly quotes — both are preserved as they appear in the source).
- **WebFetch limitation encountered**: WebFetch's model-summarization step returned only a
  paraphrased summary of both the Willison and Ptacek pages on the first pass, including a
  truncated/inaccurate rendering of the closing Ptacek quote ("It'll..." with the rest cut
  off). This was not used for any quote in this note — all quotes were independently
  verified against directly-fetched raw HTML before being included, per MINER.md §2a.
- **No other Ptacek links followed**: Ptacek's post links to several tangential
  references (Neal Stephenson's "In the Beginning Was the Command Line," a Bloomberg
  Terminal product page, an OSNews accessibility article, an accessibility conference
  talk, Emacs TRAMP documentation, and his own earlier "emacsification" post about MDV).
  These were treated as supporting citations within Ptacek's argument rather than
  independently substantive linked pages, consistent with MINER.md's "up to 5 linked
  pages that seem substantive" guidance — the two pages fetched (the primary argument
  and Willison's own corroborating account) were judged to be the substantive ones.
- **Cross-reference verification**: All cited claim numbers were verified by re-reading
  and counting claims in document order in each cited note:
  `blog-simonwillison-rss-vibe-coded-apps.md` Claim 2 (line 65);
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 4 (line 105) and Claim 5
  (line 125); `blog-anthropic-claude-code-skills-lessons.md` Claim 4 (line 47);
  `blog-ronacher-fast-hard-code.md` Claim 10 (line 115); `blog-kentbeck-yagni-economics.md`
  Claim 6 (line 72); `blog-ccunpacked-claude-code-architecture.md` Claim 6 (line 147). All
  verified against the cited files directly.
- **Confidence ceiling: emerging**: The core economic claim is corroborated by two
  independent, credible practitioners with linked, inspectable artifacts (not just stated
  belief), which is stronger than a single-source anecdote. It falls short of "settled"
  because there is no measurement of development-time or cost savings, no survey of
  broader practitioner adoption, and Willison himself has not yet generalized the practice
  beyond two apps (Claim 11) — the guide should cite this as a credible, actionable
  emerging pattern, not as an established best practice with quantified benefits.
