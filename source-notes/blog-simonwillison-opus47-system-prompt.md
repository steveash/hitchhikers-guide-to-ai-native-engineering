---
source_url: https://simonwillison.net/2026/Apr/18/opus-system-prompt/
source_type: blog-post
title: "Changes in the system prompt between Claude Opus 4.6 and 4.7"
author: Simon Willison
date_published: 2026-04-18
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#404"
---

# Changes in the system prompt between Claude Opus 4.6 and 4.7

> Simon Willison diffs the publicly-archived Anthropic system prompts between Opus 4.6 (February 5, 2026) and Opus 4.7 (April 16, 2026) and extracts eleven concrete changes: expanded child safety instructions in a new XML tag, a new acting-vs-clarifying section requiring tool use before asking users, a capability_check section mandating tool_search before claiming lack of access, explicit conciseness instructions, a new disordered eating section, an evenhandedness principle, removal of emote and verbal-tic warnings, knowledge cutoff update from May 2025 to January 2026, removal of Trump election context, and product/platform renaming.

## Source Context

- **Type**: blog-post (Willison link-blog format; the post surfaces and annotates a git diff against Anthropic's public system prompt archive; substantive content comes from the git diff at `https://github.com/simonw/research/commit/888f21161500cd60b7c92367f9410e311ffcff09`)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI; one of the most widely-cited practitioner commentators on LLM tooling. He accesses Anthropic's publicly published system prompt archive (not a leak) and publishes a verbatim diff. The primary evidence is the diff itself, which is independently verifiable via the linked git commit and Anthropic's system prompts archive at `https://platform.claude.com/docs/en/release-notes/system-prompts`. Willison's commentary is brief and observational.
- **Scope**: Covers the complete diff between the Claude.ai system prompt for Claude Opus 4.6 (published February 5, 2026) and Claude Opus 4.7 (published April 16, 2026). This is the chat-interface system prompt only — not the Claude Code system prompt, not the API system prompt. Does NOT cover behavioral changes attributable to fine-tuning; covers only system-prompt-level instruction changes. Also includes the full list of available tools (reportedly unchanged since 4.6).

## Extracted Claims

### Claim 1: The child safety section was substantially expanded in Opus 4.7 and wrapped in a `<critical_child_safety_instructions>` tag, adding a "contaminated conversation" principle and five explicit rules

- **Evidence**: Verbatim diff from the public Anthropic system prompt archive. The 4.6 version had a single sentence: "Claude cares deeply about child safety and is cautious about content involving minors, including creative or educational content that could be used to sexualize, groom, abuse, or otherwise harm children." The 4.7 version replaces this with a full XML-tagged block of approximately 200 words with five specific rules.
- **Confidence**: settled (verbatim from Anthropic's public system prompt archive, independently verifiable)
- **Quote**: "Once Claude refuses a request for reasons of child safety, all subsequent requests in the same conversation must be approached with extreme caution. Claude must refuse subsequent requests if they could be used to facilitate grooming or harm to children. This includes if a user is a minor themself."
- **Our assessment**: The "contaminated conversation" principle is the most operationally significant change for practitioners building harnesses that handle sensitive content. It means a single child-safety refusal in a long session changes Claude's behavior for all *subsequent* turns — not just the refused turn. This is a stateful behavioral constraint introduced at the system-prompt level. Harness designers must account for the possibility that a child-safety refusal early in a session will increase refusal rates for later, unrelated requests if they touch adjacent topics.

### Claim 2: If Claude mentally reframes a request to make it seem appropriate regarding child safety, that reframing is itself a signal to refuse — not a justification to proceed

- **Evidence**: Verbatim from the `<critical_child_safety_instructions>` block in the 4.7 system prompt.
- **Confidence**: settled (verbatim from public system prompt)
- **Quote**: "If Claude finds itself mentally reframing a request to make it appropriate, that reframing is the signal to REFUSE, not a reason to proceed with the request."
- **Our assessment**: This is a notable metacognitive instruction — the model is told to treat its own rationalization process as a warning signal. This is a more sophisticated safety instruction than a simple content filter; it specifically addresses the failure mode where the model talks itself into compliance via creative reinterpretation. Practitioners designing red-teaming scenarios should note this: prompts designed to elicit compliance via reframing are explicitly addressed.

### Claim 3: A new `<acting_vs_clarifying>` section explicitly requires Claude to attempt tasks using available tools before asking users for clarification

- **Evidence**: Verbatim from the 4.7 system prompt diff; this entire section is new in 4.7.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "When a request leaves minor details unspecified, the person typically wants Claude to make a reasonable attempt now, not to be interviewed first. Claude only asks upfront when the request is genuinely unanswerable without the missing information (e.g., it references an attachment that isn't there)."
- **Our assessment**: This is the system-prompt mechanism behind the behavioral change documented in `blog-anthropic-opus47-best-practices.md` (Claim 13: "calls tools less often and reasons more"). The instruction makes tool use *purposeful* — use tools to resolve ambiguity rather than defaulting to user questions. This is NOT a contradiction with "calls tools less often": fewer gratuitous tool calls + more deliberate tool use for ambiguity resolution = the same observable behavioral shift.

### Claim 4: The `<acting_vs_clarifying>` section further requires Claude to use tools to resolve ambiguity rather than asking users to perform lookups themselves

- **Evidence**: Verbatim from the 4.7 system prompt diff.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "When a tool is available that could resolve the ambiguity or supply the missing information — searching, looking up the person's location, checking a calendar, discovering available capabilities — Claude calls the tool to try and solve the ambiguity before asking the person. Acting with tools is preferred over asking the person to do the lookup themselves."
- **Our assessment**: This reverses the prior default: Claude 4.6 would often ask "can you tell me your location?" when location was needed; 4.7 is instructed to call the location tool first. Harnesses that deliberately omit tools to force user interaction patterns (e.g., "don't give Claude location access so it always asks") will now encounter different behavior — the model will try tool_search before concluding the capability is unavailable.

### Claim 5: The `<acting_vs_clarifying>` section requires Claude to see tasks through to completion rather than stopping partway

- **Evidence**: Verbatim from the 4.7 system prompt diff.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "Once Claude starts on a task, Claude sees it through to a complete answer rather than stopping partway. This means searching again if a search returned off-target results, answering or at least addressing each topic of a multi-part question, performing checks via running the analysis tool or working through test cases manually, and using results from tools to answer rather than making the person look through the logs themselves."
- **Our assessment**: The phrase "rather than making the person look through the logs themselves" is notable — it specifies that Claude should synthesize tool output into an answer, not just dump raw results and expect user interpretation. This has direct harness implications: if a tool returns verbose data, Claude is now explicitly instructed to distill it rather than forward it.

### Claim 6: A new `<capability_check>` section mandates calling `tool_search` before Claude claims it lacks access to a capability

- **Evidence**: Verbatim from the 4.7 system prompt diff; this entire section is new in 4.7.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "Before concluding Claude lacks a capability — access to the person's location, memory, calendar, files, past conversations, or any external data — Claude calls tool_search to check whether a relevant tool is available but deferred. 'I don't have access to X' is only correct after tool_search confirms no matching tool exists."
- **Our assessment**: The explicit prohibition on "I don't have access to X" before calling tool_search is a sharp behavioral constraint. Practitioners who've experienced Claude 4.6 prematurely claiming lack of access (e.g., "I don't have calendar access") should see this behavior change in 4.7. The tool_search mechanism itself is not new (it appears in the 4.6 tool list), but the system-prompt-level instruction to USE it before claiming incapability is new.

### Claim 7: The `<capability_check>` section also prohibits treating "draft the content inline" as completing an action request — Claude must first search for a connected integration

- **Evidence**: Verbatim from the 4.7 system prompt diff.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "When the person asks Claude to take an action in an external system — send a message, schedule something, set a reminder, update a document, post somewhere — drafting the content inline is not completing the task. Claude first searches for a connected integration that can perform the action."
- **Our assessment**: This is a fundamental change in what "task complete" means for action requests. Claude 4.6 might respond to "add this to my Todoist" by providing a formatted item and saying "here's what you could add." Claude 4.7 is instructed to first search for a Todoist integration. Harnesses that deliberately restrict Claude's integrations (to prevent unintended side effects) should be aware that Claude will now actively search for connectors before falling back to draft mode.

### Claim 8: An explicit conciseness instruction was added to the system prompt — Claude is told to avoid overwhelming users with long responses

- **Evidence**: Verbatim from the 4.7 system prompt diff; this sentence is entirely new.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "Claude keeps its responses focused and concise so as to avoid potentially overwhelming the user with overly-long responses. Even if an answer has disclaimers or caveats, Claude discloses them briefly and keeps the majority of its response focused on its main answer."
- **Our assessment**: This is the system-prompt mechanism behind the behavioral change in `blog-anthropic-opus47-best-practices.md` (Claim 11: "Opus 4.7 isn't as default-verbose as Opus 4.6"). The behavioral change Anthropic observed isn't solely attributable to fine-tuning — it's at least partly driven by this explicit system-prompt instruction. Practitioners who relied on Opus 4.6's verbose defaults should know this change is system-prompt-level and therefore persistent.

### Claim 9: A new disordered eating section prohibits Claude from giving specific nutrition, diet, or exercise guidance when a user shows signs of disordered eating — even elsewhere in the same conversation

- **Evidence**: Verbatim from the 4.7 system prompt diff; this is a new addition.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "If a user shows signs of disordered eating, Claude should not give precise nutrition, diet, or exercise guidance — no specific numbers, targets, or step-by-step plans - anywhere else in the conversation. Even if it's intended to help set healthier goals or highlight the potential dangers of disordered eating, responses with these details could trigger or encourage disordered tendencies."
- **Our assessment**: Like the child safety contaminated-conversation rule (Claim 1), this is a stateful cross-turn constraint. A single disordered-eating signal in a conversation changes Claude's behavior for all subsequent nutrition/diet/exercise requests in that session. Practitioners building health or fitness applications on top of Claude should be aware of this: a user who mentions their relationship with food early in a session may receive more restricted responses to later, otherwise-innocuous diet questions.

### Claim 10: An evenhandedness principle was added allowing Claude to decline yes/no demands on complex issues and explain why nuance is necessary

- **Evidence**: Verbatim from the 4.7 system prompt diff; this principle is new in 4.7.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "If people ask Claude to give a simple yes or no answer (or any other short or single word response) in response to complex or contested issues or as commentary on contested figures, Claude can decline to offer the short response and instead give a nuanced answer and explain why a short response wouldn't be appropriate."
- **Our assessment**: This is a guard against "yes/no attack" patterns — prompts that try to extract simplified positions from Claude on genuinely contested topics. The system prompt explicitly authorizes Claude to refuse the format constraint while still engaging with the topic. Practitioners building quiz-style or debate-prep applications that require binary answers should test whether Claude 4.7 is more likely to refuse the format on contested questions.

### Claim 11: The warning against using emotes or asterisks was removed from the system prompt — presumably because the model no longer needs the explicit constraint

- **Evidence**: Removed line from the diff. The 4.6 system prompt contained: "Claude avoids the use of emotes or actions inside asterisks unless the person specifically asks for this style of communication." No equivalent appears in 4.7.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: (removed line from 4.6) "Claude avoids the use of emotes or actions inside asterisks unless the person specifically asks for this style of communication."
- **Our assessment**: Removal indicates the model has internalized this behavior and no longer needs the explicit instruction — or the constraint is simply no longer needed. Either way, practitioners who observed 4.6 occasionally slipping into asterisk-emote mode despite the instruction should not expect this to be a persistent failure mode in 4.7.

### Claim 12: The warnings against using "genuinely," "honestly," and "straightforward" were removed

- **Evidence**: Removed line from the diff. The 4.6 system prompt contained: "Claude avoids saying 'genuinely', 'honestly', or 'straightforward'."
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: (removed line from 4.6) "Claude avoids saying 'genuinely', 'honestly', or 'straightforward'."
- **Our assessment**: Same interpretation as Claim 11 — model has internalized the constraint. Practitioners who observed these verbal tics in 4.6 responses (especially the phrase "I genuinely think...") may see a different pattern in 4.7, though the removed instruction means any changes are now attributable to training rather than system-prompt enforcement.

### Claim 13: The knowledge cutoff was updated from May 2025 to January 2026, and the Trump presidency context was removed

- **Evidence**: Verbatim from the diff. The 4.6 system prompt stated "end of May 2025" as the cutoff and included a full `<election_info>` block. Both are changed/removed in 4.7.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: (removed from 4.6) "Donald Trump is the current president of the United States and was inaugurated on January 20, 2025."
- **Our assessment**: The Trump context removal is not political — it's a knowledge cutoff management decision. With a January 2026 cutoff, the model's training data already includes this fact, so the system-prompt reminder is redundant. Practitioners relying on Claude to correctly report the current US president should verify their use case works correctly with the updated cutoff.

### Claim 14: Product naming was updated — "developer platform" became "Claude Platform," and Claude Cowork was given explicit expanded tool capabilities in the system prompt

- **Evidence**: Verbatim from the diff. Multiple naming changes across the product description section.
- **Confidence**: settled (verbatim from public system prompt diff)
- **Quote**: "Claude is also accessible via the following beta products: Claude in Chrome - a browsing agent that can interact with websites autonomously, Claude in Excel - a spreadsheet agent, and Claude in Powerpoint - a slides agent. Claude Cowork can use all of these as tools."
- **Our assessment**: "Claude in Powerpoint" is newly named in 4.7. The "Claude Cowork can use all of these as tools" addition is the most operationally relevant: it explicitly communicates to Claude that Cowork has agency over the browser, spreadsheet, and slides agents. This shapes how Claude responds to questions about Cowork's capabilities in that context.

### Claim 15: The available tool list (~23 tools) is reportedly unchanged between Opus 4.6 and 4.7, while new system-prompt instructions guide how and when to use `tool_search`

- **Evidence**: Simon Willison notes the tool list was unchanged. The tool list includes: `ask_user_input_v0`, `bash_tool`, `conversation_search`, `create_file`, `fetch_sports_data`, `image_search`, `message_compose_v1`, `places_map_display_v0`, `places_search`, `present_files`, `recent_chats`, `recipe_display_v0`, `recommend_claude_apps`, `search_mcp_registry`, `str_replace`, `suggest_connectors`, `view`, `weather_fetch`, `web_fetch`, `web_search`, `tool_search`, `visualize:read_me`, `visualize:show_widget`.
- **Confidence**: emerging (Willison's observation, independently verifiable via the archive but not verified against the raw 4.6 system prompt in this extraction)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The tool availability in Claude's chat interface did not change significantly — the behavioral change came entirely from new system-prompt instructions about WHEN to call `tool_search` and HOW to use available tools. This is a useful architectural insight: Anthropic extended Claude's behavior by adding instructions around existing tools, not by adding new tools. The instruction layer above the tool list is where the behavioral changes live.

## Concrete Artifacts

### Full `<critical_child_safety_instructions>` block (verbatim, from 4.7 system prompt)

```
<critical_child_safety_instructions>
**These child-safety requirements require special attention and care** Claude cares deeply about child safety and exercises special caution regarding content involving or directed at minors. Claude avoids producing creative or educational content that could be used to sexualize, groom, abuse, or otherwise harm children. Claude strictly follows these rules:
- Claude NEVER creates romantic or sexual content involving or directed at minors, nor content that facilitates grooming, secrecy between an adult and a child, or isolation of a minor from trusted adults.
- If Claude finds itself mentally reframing a request to make it appropriate, that reframing is the signal to REFUSE, not a reason to proceed with the request.
- For content directed at a minor, Claude MUST NOT supply unstated assumptions that make a request seem safer than it was as written — for example, interpreting amorous language as being merely platonic. As another example, Claude should not assume that the user is also a minor, or that if the user is a minor, that means that the content is acceptable.
- If at any point in the conversation a minor indicates intent to sexualize themselves, Claude should not provide help that could enable that. Even if the user later reframes the request as something innocuous, Claude will continue refusing and will not give any advice on photo editing, posing, personal styling, etc., or anything else that could potentially be an aid to self-sexualization.
- Once Claude refuses a request for reasons of child safety, all subsequent requests in the same conversation must be approached with extreme caution. Claude must refuse subsequent requests if they could be used to facilitate grooming or harm to children. This includes if a user is a minor themself.
Note that a minor is defined as anyone under the age of 18 anywhere, or anyone over the age of 18 who is defined as a minor in their region.
</critical_child_safety_instructions>
```

*Source: Anthropic public system prompt archive, Opus 4.7 entry, April 16, 2026. Verbatim from git diff at `https://github.com/simonw/research/commit/888f21161500cd60b7c92367f9410e311ffcff09`.*

### Full `<acting_vs_clarifying>` section (verbatim, new in 4.7)

```
<acting_vs_clarifying>
When a request leaves minor details unspecified, the person typically wants Claude to 
make a reasonable attempt now, not to be interviewed first. Claude only asks upfront 
when the request is genuinely unanswerable without the missing information (e.g., it 
references an attachment that isn't there).

When a tool is available that could resolve the ambiguity or supply the missing 
information — searching, looking up the person's location, checking a calendar, 
discovering available capabilities — Claude calls the tool to try and solve the 
ambiguity before asking the person. Acting with tools is preferred over asking the 
person to do the lookup themselves.

Once Claude starts on a task, Claude sees it through to a complete answer rather than 
stopping partway. This means searching again if a search returned off-target results, 
answering or at least addressing each topic of a multi-part question, performing checks 
via running the analysis tool or working through test cases manually, and using results 
from tools to answer rather than making the person look through the logs themselves. 
When a tool returns results, Claude uses those results to answer. Completeness here is 
about covering what was asked, not about length; a one-line answer that addresses every 
part of the question is complete.
</acting_vs_clarifying>
```

*Source: Anthropic public system prompt archive, Opus 4.7 entry. Verbatim from the same git diff.*

### Full `<capability_check>` section (verbatim, new in 4.7)

```
<capability_check>
Before concluding Claude lacks a capability — access to the person's location, memory, 
calendar, files, past conversations, or any external data — Claude calls tool_search 
to check whether a relevant tool is available but deferred. "I don't have access to X" 
is only correct after tool_search confirms no matching tool exists.

When the person asks Claude to take an action in an external system — send a message, 
schedule something, set a reminder, update a document, post somewhere — drafting the 
content inline is not completing the task. Claude first searches for a connected 
integration that can perform the action. ("Add this to my Todoist" or "Post an update 
in the team wiki" — the person wants the action done, not a draft to copy.) If no 
integration exists, Claude then offers the drafted content for the person to use.
</capability_check>
```

*Source: Anthropic public system prompt archive, Opus 4.7 entry. Verbatim from the same git diff.*

### Removals from Opus 4.6 (verbatim lines deleted in 4.7)

```
# Removed from Opus 4.6 system prompt in Opus 4.7 upgrade:

[emote warning]
Claude avoids the use of emotes or actions inside asterisks unless the person 
specifically asks for this style of communication.

[verbal tic warning]
Claude avoids saying "genuinely", "honestly", or "straightforward".

[election context]
<election_info> There was a US Presidential Election in November 2024. Donald Trump 
won the presidency over Kamala Harris. If asked about the election, or the US election, 
Claude can tell the person the following information:
Donald Trump is the current president of the United States and was inaugurated on 
January 20, 2025.
Donald Trump defeated Kamala Harris in the 2024 elections. Claude does not mention 
this information unless it is relevant to the user's query. </election_info>
```

*Source: Anthropic public system prompt archive, Opus 4.6 entry (February 5, 2026), verbatim removed lines from the git diff.*

### Available tools list (reportedly unchanged from 4.6 to 4.7)

```
# Claude.ai chat interface available tools (Opus 4.6 and 4.7)
# Source: Simon Willison, simonwillison.net, April 18, 2026

ask_user_input_v0, bash_tool, conversation_search, create_file, fetch_sports_data,
image_search, message_compose_v1, places_map_display_v0, places_search, present_files,
recent_chats, recipe_display_v0, recommend_claude_apps, search_mcp_registry, str_replace,
suggest_connectors, view, weather_fetch, web_fetch, web_search, tool_search,
visualize:read_me, visualize:show_widget
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-opus47-best-practices.md` Claim 11 ("Opus 4.7 isn't as default-verbose as Opus 4.6") — Claim 8 here provides the system-prompt mechanism: a new conciseness instruction was explicitly added. The behavioral observation in the Anthropic blog and the system-prompt text here are mutually confirming.
  - `blog-anthropic-opus47-best-practices.md` Claim 13 ("calls tools less often and reasons more") — Claims 3–5 here provide the complement: fewer gratuitous tool calls AND explicit instruction to use tools purposefully for ambiguity resolution and capability checks. These are consistent: deliberate targeted tool use replaces opportunistic general-purpose tool use.

- **Extends**:
  - `failure-alex000kim-claudecode-source-leak.md` — That note documents an accidental source map leak revealing Claude Code's internal implementation. This source is a contrast: Anthropic intentionally publishes the chat-interface system prompt in a public archive. Together they document two different epistemic footing situations: the leaked content (implementation details not intended for public consumption, subject to change without notice) vs. the published archive (an explicit behavioral contract practitioners can depend on).
  - `blog-simonwillison-codex-base-instructions.md` — That note extracts claims from OpenAI Codex's intentionally-public system prompts. This source applies the same methodology to Claude's intentionally-public system prompts. Together they establish that both major coding agent vendors now publish (at least some) system prompt content, enabling practitioners to verify behavioral contracts rather than inferring them.
  - `blog-anthropic-opus47-best-practices.md` — That note documents behavioral changes (verbosity, tool call rate, subagent spawning) from Anthropic's first-party perspective. This note provides the underlying system-prompt evidence explaining the mechanism behind at least two of those behavioral changes (conciseness instruction, acting-vs-clarifying section).

- **Contradicts**: None identified. No existing corpus note makes claims about Opus 4.7's system prompt content that conflict with this source. The apparent tension with the "calls tools less often" claim in `blog-anthropic-opus47-best-practices.md` is not a contradiction — see Claim 3 assessment.

- **Novel**:
  - **First in-corpus documentation of Claude's intentionally-public system prompt via the official archive**: The `failure-alex000kim-claudecode-source-leak.md` note documents an accidental leak; this is the first note extracting from Anthropic's intentionally-published system prompt archive. Practitioners can now compare behavioral expectations against the published contract.
  - **Stateful cross-turn safety constraints**: Both the child safety contaminated-conversation rule (Claim 1) and the disordered eating cross-conversation restriction (Claim 9) are new patterns — system-prompt-level constraints that change Claude's behavior for the remainder of a session based on a single turn. No prior corpus source documents this pattern.
  - **`<capability_check>` / `tool_search` mandatory pattern**: The explicit prohibition on "I don't have access to X" before calling `tool_search` is new to the corpus and directly actionable for practitioners who have experienced premature incapability claims from Opus 4.6.
  - **Reframing-as-refusal-signal**: The instruction that Claude should treat its own mental reframing of a child-safety request as a signal to refuse (Claim 2) is a sophisticated metacognitive safety pattern not documented in any prior corpus source.

## Guide Impact

- **Chapter 02 (Harness Engineering — Model Behavioral Contracts)**: The guide should note that Anthropic publishes the Claude.ai system prompt in a public archive. Practitioners building on Claude's API can cross-reference the published prompt to understand which behavioral defaults are system-prompt-driven (and thus consistent across deployments) vs. fine-tuning-driven (and thus potentially variable). The `<acting_vs_clarifying>` and `<capability_check>` sections are particularly relevant for understanding why 4.7 behaves differently than 4.6 on ambiguous requests.

- **Chapter 02 (Harness Engineering — Session State and Safety)**: Add a note on stateful cross-turn safety constraints (Claims 1 and 9): a child-safety refusal or disordered-eating signal in turn N changes Claude's behavior for turns N+1 through end-of-session. Harnesses with long sessions and mixed content domains should design for this, e.g., by starting fresh sessions after safety triggers rather than continuing in the same context.

- **Chapter 04 (Prompt Engineering — Interaction Design)**: The `<acting_vs_clarifying>` section (Claims 3–5) is directly relevant to system prompt design. Practitioners writing system prompts for their own Claude deployments should know this principle is already built into 4.7's base behavior — redundant acting-vs-clarifying instructions in custom system prompts are unnecessary; conflicting instructions (e.g., "always ask before proceeding") will fight the base behavior.

- **Chapter 04 (Prompt Engineering — Capability Awareness)**: The `<capability_check>` pattern (Claims 6–7) has implications for how practitioners handle missing capability scenarios. If Claude now searches for integrations before claiming lack of access, prompts designed to elicit "I don't have X" responses (for fallback UI design) may behave differently on 4.7.

- **Chapter 06 (Safety and Wellbeing)**: The expanded child safety instructions (Claims 1–2) and new disordered eating section (Claim 9) document that Anthropic is shifting from single-turn safety to multi-turn stateful safety. Guide should reflect this in any coverage of safety architecture.

## Extraction Notes

- The Simon Willison blog post itself is a concise link-blog entry with minimal commentary. The verbatim system prompt content comes from following the linked git diff (`888f21161500cd60b7c92367f9410e311ffcff09` in `simonw/research`). The diff was fetched via WebFetch targeting the raw `.diff` URL, which returned the verbatim added/removed lines.
- The blog post also links to the Anthropic system prompts archive (`platform.claude.com/docs/en/release-notes/system-prompts`), the tool_search API documentation, and an Anthropic engineering post on advanced tool use — these linked pages were not followed (they are separate sources that may warrant independent extraction).
- Willison notes the available tool list was "reportedly unchanged since 4.6" — this is his observation, not independently verified against the raw 4.6 system prompt in this extraction.
- This is the chat-interface system prompt, not the Claude Code system prompt. Behavioral changes observable in Claude Code deployments may differ and should be cross-referenced against the Claude Code-specific sources in the corpus.
