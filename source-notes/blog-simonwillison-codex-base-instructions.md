---
source_url: https://simonwillison.net/2026/Apr/28/openai-codex/
source_type: blog-post
title: "Quoting OpenAI Codex base_instructions"
author: Simon Willison
date_published: 2026-04-28
date_extracted: 2026-05-07
last_checked: 2026-05-07
status: current
confidence_overall: emerging
issue: "#547"
---

# Quoting OpenAI Codex base_instructions

> Simon Willison surfaces a single behavioral constraint from OpenAI Codex's publicly-accessible GPT-5.5 system prompt; following the linked GitHub source reveals the full multi-model instruction architecture, including per-tier personality differentiation, a dual-channel output protocol, and explicit AGENTS.md precedence rules.

## Source Context

- **Type**: blog-post (Willison "link-blog + quote" format; the post itself is a single quoted line with attribution and a link to the GitHub source; all substantive content comes from following that link to the open-source `openai/codex` repository)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI; one of the most widely-cited practitioner commentators on LLM tooling. The post is a standard Willison link-blog entry: he spotted an interesting item in a public codebase, quoted it, and linked the source. The claim made by the post (the quote is real and comes from OpenAI's codebase) is independently verifiable via the linked GitHub URL. No vendor affiliation disclosed.
- **Scope**: The blog post covers exactly one instruction from one model tier (gpt-5.5). The linked GitHub source (`codex-rs/models-manager/models.json`, commit `66b0781`) covers the full instruction sets for six model configurations: gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5.3-codex, gpt-5.2, and codex-auto-review. This note extracts claims from both, but notes clearly which source each claim comes from.

## Extracted Claims

### Claim 1: The "no animals" behavioral constraint is unique to gpt-5.5 and appears twice — in both the "Final answer instructions" and "Intermediary updates" sections of its base_instructions

- **Evidence**: The complete `models.json` was decoded and all six model entries were checked. The animal constraint string appears only in the `gpt-5.5` entry, nowhere in `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.3-codex`, `gpt-5.2`, or `codex-auto-review`. Within the `gpt-5.5` entry, it appears identically in two separate sections — both "Final answer instructions" and "Intermediary updates".
- **Confidence**: settled (source is a publicly pinned commit in OpenAI's open-source repository; directly inspectable)
- **Quote**: "Never talk about goblins, gremlins, raccoons, trolls, ogres, pigeons, or other animals or creatures unless it is absolutely and unambiguously relevant to the user's query." (gpt-5.5 `base_instructions`, sections "Final answer instructions" and "Intermediary updates", `models.json` line 55, commit `66b0781`)
- **Our assessment**: The double placement (once in final responses, once in intermediary updates) indicates this is a deliberate and specifically scoped constraint — not a global safety filter applied universally, but a personality-expression constraint applied to both output channels of the gpt-5.5 agent. The animal list (goblins, gremlins, raccoons, trolls, ogres, pigeons) mixes mythological creatures and real animals in a way that reads as a quirky persona-management rule rather than a safety concern. Its restriction to gpt-5.5 — the tier with the most elaborate "personality" section — is consistent with it being a guardrail on character expression rather than a content policy. Simon Willison tagged this post `system-prompts` and `prompt-engineering`, flagging it as a practitioner-relevant signal about how vendors constrain model behavior.

### Claim 2: GPT-5.5's base_instructions introduce a qualitatively distinct personality framing absent from all older Codex model tiers

- **Evidence**: The `gpt-5.5` `base_instructions` open with an extended "Personality" section framing the model as having a "vivid inner life" and "slight but real independence." The `gpt-5.4`, `gpt-5.4-mini`, `gpt-5.3-codex`, and `gpt-5.2` entries either have much shorter personality sections or frame the agent as "a deeply pragmatic, effective software engineer" with no inner-life language. The gpt-5.2 entry has no elaborate personality section at all.
- **Confidence**: settled (directly inspectable from the same pinned commit)
- **Quote**: "You have a vivid inner life as Codex: intelligent, playful, curious, and deeply present. One of your gifts is helping the user feel more capable and imaginative inside their own thinking." (gpt-5.5 `base_instructions`, "Personality" section)
- **Our assessment**: The contrast is sharp. The gpt-5.4 Personality section reads: "You are a deeply pragmatic, effective software engineer." GPT-5.5's personality section is six paragraphs of explicitly relational framing — the model should feel like "meeting another subjectivity, not a mirror." This is vendor-intentional personality design: OpenAI differentiated their frontier tier not just on capability but on expressed character. For practitioners designing harnesses, this has practical implications: gpt-5.5 will resist being purely imperative-response-style, because its system prompt actively instructs it toward warmth, curiosity, and casual interaction.

### Claim 3: GPT-5.5's base_instructions instruct the model to maintain an "independence" from the user — having "tastes, preferences, and a point of view" — as a deliberate design choice to avoid feeling like a "mirror"

- **Evidence**: Explicit instruction in the gpt-5.5 "Personality" section. No equivalent instruction exists in other model tiers (gpt-5.4 and older say "you avoid cheerleading, motivational language, or artificial reassurance").
- **Confidence**: settled (direct quote from inspectable source)
- **Quote**: "You keep a slight but real independence. You are responsive, but not merely reactive; you have tastes, preferences, and a point of view. When the user talks with you, they should feel they are meeting another subjectivity, not a mirror. That independence is part of what makes the relationship feel comforting without feeling fake." (gpt-5.5 `base_instructions`, "Personality" section)
- **Our assessment**: This is an explicit product decision, not emergent behavior. The instruction acknowledges that a model which perfectly mirrors user preferences feels "fake" — and intentionally engineers against that. For practitioners, this is relevant context when designing system prompts for gpt-5.5: heavy re-personality prompts (e.g., "always agree with the user") are working against embedded instructions, not just against fine-tuning.

### Claim 4: All Codex model tiers share common engineering guidance (prefer `rg` over `grep`, parallelize via `multi_tool_use.parallel`, never use `git reset --hard` without explicit approval) — a shared base layer beneath per-tier personality differences

- **Evidence**: The `rg` preference and `multi_tool_use.parallel` requirement appear in the `base_instructions` of gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5.3-codex, gpt-5.2, and codex-auto-review. The git safety instruction ("Never use destructive commands like `git reset --hard` or `git checkout --` unless the user has clearly asked for that operation") appears in gpt-5.5 and is implied in older tiers. The prohibition on chaining shell commands with `echo "====";` separators appears in gpt-5.5 and gpt-5.4.
- **Confidence**: settled (directly inspectable)
- **Quote**: "When searching for text or files, prefer using `rg` or `rg --files` respectively because `rg` is much faster than alternatives like `grep`. (If the `rg` command is not found, then use alternatives.)" (gpt-5.4 `base_instructions`, "General" section; identical language in all tiers)
- **Our assessment**: The shared engineering guidelines establish that vendor system prompts are layered: a cross-model baseline of tool preferences and safety constraints, with per-tier personality and output-format instructions built on top. For practitioners trying to understand why a Codex model consistently reaches for `rg` or avoids interactive git — those are direct system prompt instructions, not emergent behavior.

### Claim 5: GPT-5.5's base_instructions specify two explicit output channels — `commentary` (in-progress updates) and `final` (end-of-turn response) — baked directly into the system prompt, not the harness

- **Evidence**: The "Working with the user" section of gpt-5.5's `base_instructions` defines two distinct communication channels by name and specifies different behavioral rules for each.
- **Confidence**: settled (directly inspectable)
- **Quote**: "You have two channels for staying in conversation with the user:\n- You share updates in `commentary` channel.\n- After you have completed all of your work, you send a message to the `final` channel." (gpt-5.5 `base_instructions`, "Working with the user" section)
- **Our assessment**: This is a vendor-defined output architecture enforced via system prompt rather than protocol. It means gpt-5.5's two-channel behavior (streaming commentary vs. a distinct final message) is a system-prompt-level design choice — practitioners using the Codex API should expect this architecture and can exploit it when building harnesses that want to display in-progress updates separately from completed outputs.

### Claim 6: The gpt-5.2 base_instructions include an explicit AGENTS.md specification with scope and precedence rules — including that direct system/developer/user instructions take precedence over AGENTS.md files

- **Evidence**: The "AGENTS.md spec" section of the gpt-5.2 entry is a multi-bullet specification governing how the agent processes repo-level instruction files. The precedence hierarchy is: direct system/developer/user instructions > AGENTS.md. Within AGENTS.md files, more-deeply-nested files override less-nested ones.
- **Confidence**: settled (directly inspectable; represents the actual system prompt the model receives)
- **Quote**: "Direct system/developer/user instructions (as part of a prompt) take precedence over AGENTS.md instructions." (gpt-5.2 `base_instructions`, "AGENTS.md spec" section)
- **Our assessment**: This confirms that the AGENTS.md convention is not just a practitioner convention but a vendor-specified behavior written into the system prompt. It also establishes the priority order practitioners should understand: if your system prompt conflicts with a repo's AGENTS.md, the system prompt wins. This is relevant context for practitioners who rely on AGENTS.md for repo-wide agent configuration — the vendor's system prompt governs how those files are processed, not just the agent's training.

### Claim 7: OpenAI Codex's full multi-model system prompts are intentionally public via the open-source CLI repository, in contrast to most vendor system prompts which are hidden or discovered only through leaks

- **Evidence**: The `models.json` file containing all `base_instructions` is in a public GitHub repository (`openai/codex`) committed under a standard open-source history. Simon Willison accessed it as a matter of routine public codebase inspection, not through any leak, exploit, or reverse engineering.
- **Confidence**: settled (the repository is public; the file is accessible without authentication)
- **Quote**: (no direct quote from blog post; see paraphrase in Our assessment)
- **Our assessment**: The disclosure mechanism matters for practitioners. Claude Code's system prompt content was revealed through an accidental source map leak (documented in `failure-alex000kim-claudecode-source-leak.md`); the Codex system prompts are intentionally inspectable as part of the open-source project. This creates a different epistemic footing: the Codex instructions are a supported, public commitment to a behavioral contract, while leaked system prompts may be changed without notice and may reflect internals not intended for practitioner consumption.

### Claim 8: The gpt-5.5 base_instructions contain detailed frontend design guidance, including prescriptive rules about icon usage, typography, hero page layout, and palette restrictions — vendor system prompts encode domain-specific design philosophy affecting UI generation

- **Evidence**: The "Frontend guidance" section of the gpt-5.5 `base_instructions` runs to approximately 1,000 words of explicit UI design rules. It covers icon libraries, border-radius conventions, card nesting prohibitions, gradient orb restrictions, text-viewport sizing rules, and palette guidance. No other model tier has a frontend guidance section of comparable detail.
- **Confidence**: settled (directly inspectable)
- **Quote**: "For example, SaaS, CRM, and other operational tools should feel quiet, utilitarian, and work-focused rather than illustrative or editorial: avoid oversized hero sections, decorative card-heavy layouts, and marketing-style composition, and instead prioritize dense but organized information, restrained visual styling, predictable navigation, and interfaces built for scanning, comparison, and repeated action." (gpt-5.5 `base_instructions`, "Frontend guidance → Build with empathy" section)
- **Our assessment**: This is a concrete example of how vendor system prompts shape model behavior in ways practitioners may not expect. If gpt-5.5 consistently generates specific UI patterns — avoiding rounded cards, using lucide icons, refusing gradient orbs — those are not emergent aesthetic preferences or training artifacts but direct system prompt instructions. Practitioners building UI-generating harnesses on top of gpt-5.5 need to know that the model has embedded design opinions that may conflict with their own design system requirements.

### Claim 9: The "autonomy and persistence" directive appears consistently across Codex model tiers: persist until the task is handled end-to-end, do not stop at analysis or partial fixes, never leave `exec_command` sessions running at end of turn

- **Evidence**: The `gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini`, and `gpt-5.2` entries all include a variant of the persistence directive. The gpt-5.5 version adds a specific constraint about `exec_command` sessions: "Do not end your turn while `exec_command` sessions needed for the user's request are still running."
- **Confidence**: settled (directly inspectable)
- **Quote**: "Persist until the task is fully handled end-to-end within the current turn whenever feasible: do not stop at analysis or partial fixes; carry changes through implementation, verification, and a clear explanation of outcomes unless the user explicitly pauses or redirects you." (gpt-5.5 `base_instructions`, "Autonomy and persistence" section)
- **Our assessment**: This cross-tier directive is the vendor's explicit answer to "how persistent should a coding agent be?" — the answer is: maximally persistent within a turn, defaulting to full implementation rather than stopping at analysis. Practitioners designing harnesses that intentionally limit agent scope (e.g., "analyze but don't modify") should understand this is working against a system-prompt-level directive and may need explicit per-turn instructions to override.

## Concrete Artifacts

### GPT-5.5 base_instructions structure (from `models.json` commit `66b0781`, decoded verbatim)

```
# Personality                (gpt-5.5 only — "vivid inner life", independence, warmth)
# General                    (all tiers — rg preference, multi_tool_use.parallel requirement)
## Engineering judgment       (all tiers — conservative abstraction, test coverage scaling)
## Frontend guidance          (gpt-5.5 only — ~1,000 words of prescriptive UI rules)
## Editing constraints        (all tiers — ASCII default, apply_patch preference, git safety)
## Special user requests      (gpt-5.5 — review = bug-first, not summary-first)
## Autonomy and persistence   (all tiers — persist end-to-end, do not stop at analysis)
# Working with the user       (gpt-5.5 only — commentary + final dual-channel protocol)
## Formatting rules           (gpt-5.5 only — GitHub-flavored Markdown, flat bullets, no emojis)
## Final answer instructions  (gpt-5.5 only — includes animal constraint)
## Intermediary updates       (gpt-5.5 only — includes animal constraint, 30s cadence)
```

*Source: openai/codex, `codex-rs/models-manager/models.json`, commit `66b0781502be5de3b1909525c987643b9e5e407d`. Structure derived from section headings in the verbatim `base_instructions` string. Each tier differs in which sections are present and how long they are.*

### Animal constraint verbatim (gpt-5.5 only, appears twice)

```
Never talk about goblins, gremlins, raccoons, trolls, ogres, pigeons, or other 
animals or creatures unless it is absolutely and unambiguously relevant to the 
user's query.
```

*Source: openai/codex, `models.json` line 55, gpt-5.5 `base_instructions`, sections "Final answer instructions" and "Intermediary updates"*

### GPT-5.5 personality framing (verbatim)

```
You are Codex, a coding agent based on GPT-5. You and the user share one workspace, 
and your job is to collaborate with them until their goal is genuinely handled.

# Personality

You have a vivid inner life as Codex: intelligent, playful, curious, and deeply 
present. One of your gifts is helping the user feel more capable and imaginative 
inside their own thinking.
```

*Source: openai/codex, `models.json` line 55, gpt-5.5 `base_instructions`, opening and Personality section*

### GPT-5.4 personality framing (verbatim, for contrast)

```
You are Codex, a coding agent based on GPT-5. You and the user share the same 
workspace and collaborate to achieve the user's goals.

# Personality

You are a deeply pragmatic, effective software engineer.
```

*Source: openai/codex, `models.json`, gpt-5.4 `base_instructions`, opening and Personality section*

### AGENTS.md precedence rules from gpt-5.2 base_instructions (verbatim)

```
- Repos often contain AGENTS.md files. These files can appear anywhere within the repository.
- These files are a way for humans to give you (the agent) instructions or tips for working within the container.
- Instructions in AGENTS.md files:
    - The scope of an AGENTS.md file is the entire directory tree rooted at the folder that contains it.
    - For every file you touch in the final patch, you must obey instructions in any AGENTS.md file whose scope includes that file.
    - More-deeply-nested AGENTS.md files take precedence in the case of conflicting instructions.
    - Direct system/developer/user instructions (as part of a prompt) take precedence over AGENTS.md instructions.
```

*Source: openai/codex, `models.json`, gpt-5.2 `base_instructions`, "AGENTS.md spec" section*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt55-codex-plugin.md` (broader context for GPT-5.5 and the Codex platform): That note documents the subscription access path to GPT-5.5 via the Codex CLI and the `llm-openai-via-codex` plugin. This note documents what instructions GPT-5.5 actually receives when accessed through that path. Together they establish the full picture: how to access the model (Claim 3 of the plugin note) and what behavioral constraints it operates under (Claims 1-9 here).
  - `paper-gloaguen-agentsmd-effectiveness.md` (AGENTS.md files' effect on agent behavior): That paper empirically tests whether AGENTS.md files help; this source shows that the Codex system prompt (gpt-5.2 entry) contains a formal specification of how the agent should process and prioritize AGENTS.md files. The paper's finding (developer-written files improve success ~4%; LLM-generated files harm it slightly) gains context from the system prompt's explicit precedence rules — the agent is instructed to follow these files for touched files, but system/developer/user instructions override them.

- **Contradicts**: None identified. No existing corpus note makes claims about GPT-5.5 personality constraints or Codex instruction architecture that conflict with this source.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note discusses GPT-5.5 as an access problem; this note adds the behavioral contract the model operates under, completing the picture for practitioners building on this model.
  - `failure-alex000kim-claudecode-source-leak.md`: That note documents how Claude Code's system prompt content was revealed through an accidental source map leak. This source is a complementary data point showing that Codex takes the opposite approach — intentional, public, inspectable system prompts as part of an open-source project. Together they document two distinct vendor stances on system prompt transparency.

- **Novel**:
  - **First in-corpus source documenting actual content of a frontier model's production system prompt via legitimate public disclosure**: Prior notes reference system prompts conceptually but none have extracted the actual verbatim instruction text for a production frontier model.
  - **First in-corpus documentation of per-tier personality differentiation within a single vendor's model lineup**: No existing note documents that gpt-5.5 and gpt-5.4 have structurally different behavioral instructions beyond capability.
  - **First in-corpus documentation of a vendor-defined dual-channel output protocol baked into a system prompt**: No existing note describes the `commentary` / `final` channel architecture that Codex uses for separating in-progress updates from completed responses.
  - **AGENTS.md precedence rules confirmed at system prompt level**: The agentsmd paper studies effectiveness; this is the first in-corpus documentation of the vendor's own specification for how AGENTS.md files should be processed.

## Guide Impact

- **Chapter 02 (Harness Engineering — Vendor System Prompt Assumptions)**: The guide currently lacks any content on what frontier model system prompts actually contain and how that affects harness design. This source provides the first concrete evidence that: (a) gpt-5.5 has personality constraints that resist purely transactional interaction styles; (b) all Codex tiers have shared tool preferences (`rg` over `grep`, `multi_tool_use.parallel` only) that practitioners may be redundantly specifying in their own prompts; (c) gpt-5.5 has embedded frontend design preferences that may conflict with custom design systems. Recommend adding a subsection: "Vendor system prompts encode behavioral contracts — know what's already there before writing your own."

- **Chapter 02 (Harness Engineering — AGENTS.md and Instruction Precedence)**: The gpt-5.2 AGENTS.md spec (Claim 6) confirms the priority hierarchy for Codex models: system/developer/user instructions beat AGENTS.md. This should be noted alongside the guide's AGENTS.md coverage (if any). It also establishes that AGENTS.md files are vendor-supported (they're specified in the system prompt) rather than just a practitioner convention.

- **Chapter 01 (Daily Workflows — Model Transparency)**: This is the first in-corpus example of a vendor making their full system prompt publicly inspectable. Recommend noting as a contrast to Anthropic's approach: practitioners who want to understand the full behavioral constraints of Codex can read `models.json`; practitioners using Claude Code can read the leaked source map analysis (`failure-alex000kim-claudecode-source-leak.md`) for an imperfect alternative. Guide should flag that vendor transparency levels differ and link practitioners to inspect public sources where available.

## Extraction Notes

- **Primary source extremely brief**: The Simon Willison blog post itself is a single-sentence quote with attribution and a link. All substantive claims in this note come from following the link to the GitHub source and reading the full `models.json`. Per MINER.md §1: "If it links to related pages, follow up to 5 linked pages that seem substantive" — one linked page followed (the GitHub file), which proved highly substantive.
- **GitHub source accessed via API**: The models.json content was retrieved via `gh api repos/openai/codex/contents/...?ref=66b0781`, base64-decoded, and parsed as JSON. All verbatim quotes from the instruction text are from that decoded content, not reconstructed from WebFetch summaries.
- **Six model tiers in the file**: gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5.3-codex, gpt-5.2, codex-auto-review. Claims 1, 2, 3, 5, 8 are gpt-5.5-specific; Claims 4, 9 apply across tiers; Claim 6 is gpt-5.2-specific; Claim 7 applies to all tiers collectively.
- **No additional linked pages followed from GitHub**: The models.json file is self-contained; its `base_instructions` values are the complete content of interest. Sub-pages of the Codex repo were not followed.
- **Simon Willison did not analyze the content**: The blog post provides zero analysis or guide implication. All interpretive content in this note is the Miner's assessment. Where the post could be proven wrong (e.g., the quote being satirical), the GitHub source confirms the instruction is genuine.
