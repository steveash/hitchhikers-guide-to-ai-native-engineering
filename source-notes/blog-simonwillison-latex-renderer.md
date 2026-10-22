---
source_url: https://simonwillison.net/2026/Oct/15/latex/
source_type: blog-post
title: "LaTeX renderer"
author: Simon Willison
date_published: 2026-10-15
date_extracted: 2026-10-22
last_checked: 2026-10-22
status: current
confidence_overall: anecdotal
issue: "#4267"
---

# LaTeX renderer

> Willison's three-prompt build of a URL-fragment LaTeX renderer with Claude Code shows the security question ("Safe from XSS?") being raised only after the first draft, and answered by pointing the agent at an iframe-sandbox mechanism already present in a sibling tool in the same repo.

## Source Context

- **Type**: blog-post (Willison "tool" entry; about 300 words of prose plus the prompts and a link to the live tool).
- **Author credibility**: Creator of Django and the `llm` CLI; a trusted feed in this corpus. First-party account of his own build.
- **Scope**: Covers the tool's features, its inspiration (Paul Ford / Aboard's Tiny Little Office), the three prompts used, and the library versions. Does NOT include the agent's responses, a session transcript, the actual sandbox attribute values (the post elides them as `<iframe sandbox="...">`), any metrics, or any failures.

## Extracted Claims

### Claim 1: The tool was specified in one dense first prompt that bundled the URL-fragment design, a compression prefix, library selection and the editor/rendered UX
- **Evidence**: The first prompt is reproduced in full in the post.
- **Confidence**: anecdotal (single instance, author-reported)
- **Quote**: "I want a tool where you can link to it with a fragment hash #code-here and it treats that code as LaTeX and renders it really effectively."
- **Our assessment**: Delegating library choice to the agent ("Use the best available latex render library from a CDN (consider WebAssembly too)") worked here: the post reports MathJax 4.1.3 and faster-latex 0.3.1. The post doesn't show whether the agent evaluated alternatives, so this is an outcome, not a demonstrated process.

### Claim 2: The XSS question was not in the initial spec; it was raised as a follow-up prompt, and resolved by referencing an existing in-repo mechanism
- **Evidence**: Prompt order as reported by the author ("Here's the sequence of prompts I used"). The first prompt contains no security requirement; the second is the security prompt. The post does not say whether a working build existed before the second prompt.
- **Confidence**: anecdotal
- **Quote**: "Safe from XSS? We could run in an iframe sandbox like we do on the SVG markdown render project"
- **Our assessment**: This confirms the Prospector's question to verify: the sandbox was added reactively. The post doesn't say whether the agent's first draft was actually unsafe or what it answered, so we can't tell if "Safe from XSS?" exposed a real hole or just prompted hardening. Useful as an example of a human security review prompt that costs one line, but it is also a counterexample to "secure by default" agent output.

### Claim 3: Willison framed the sandbox as reuse of a sibling tool's mechanism because the agent was working inside his tools repo
- **Evidence**: Author's explanation preceding the prompt.
- **Confidence**: anecdotal
- **Quote**: "Since it was working in my tools repo I told it to take inspiration from the <iframe sandbox=\"...\"> mechanism used by my existing SVG in Markdown tool as protection against XSS risks:"
- **Our assessment**: A repo of prior tools acts as a pattern library the agent can be pointed at ("like we do on…") instead of re-specifying the sandbox flags. This is a small, concrete instance of in-repo precedent as context.

### Claim 4: Feature parity was obtained by a one-line "copy that feature from the other tool" prompt
- **Evidence**: Third prompt reproduced in the post.
- **Confidence**: anecdotal
- **Quote**: "We should have an option to load latex from a URL (or gist) similar to the markdown SVG tool"
- **Our assessment**: Same cross-tool reuse as Claim 3. Note the load-from-URL feature enlarges the untrusted-input surface, which the iframe sandbox then has to cover; the post doesn't discuss this.

### Claim 5: The design stores the entire document in the URL fragment (optionally compressed), making every document a shareable link
- **Evidence**: Tool description; the idea is credited to Tiny Little Office.
- **Confidence**: emerging (the pattern recurs across Willison's tools, e.g. CORS Chat, GitHub code component)
- **Quote**: "Tiny Little Office's signature trick is to store all of the document data in the #fragment section of the URL, so every document created using it becomes a bookmarkable and shareable link."
- **Our assessment**: The post doesn't claim the server never sees content (the Prospector's hypothesis); that is a property of how fragments work, not stated by the author. The post also doesn't discuss the privacy trade-off of leaking via shared links.

### Claim 6: Tiny Little Office ships an llms.txt so agents can construct renderable document URLs
- **Evidence**: Author states Claude used it to generate a link to a deck.
- **Confidence**: anecdotal (second-hand description of a third-party product)
- **Quote**: "It also has an llms.txt file telling agents how to construct URLs that will render as documents."
- **Our assessment**: Interesting agent-facing-interface angle (URL-as-document-API), but only described, not evaluated.

### Claim 7: The build relied on pinned CDN libraries including DOMPurify
- **Evidence**: Version list at the end of the post.
- **Confidence**: anecdotal
- **Quote**: "The tool uses Pako 2.1.0, MathJax 4.1.3, faster-latex 0.3.1, and DOMPurify 3.4.16."
- **Our assessment**: Shows a defence-in-depth pairing (sanitizer + iframe sandbox). The post only lists DOMPurify; it doesn't say how it's applied or that it was agent-chosen.

## Concrete Artifacts

```
Prompt 1 (Simon Willison, "LaTeX renderer", 2026-10-15; Claude Code, Opus 5.5 Extra):
I want a tool where you can link to it with a fragment hash #code-here and it treats that code as LaTeX and renders it really effectively. It should also support a prefix which means the latex is compressed with a custom compression dictionary optimized for latex. Use the best available latex render library from a CDN (consider WebAssembly too). If loaded without a fragment hash show an editor you can paste latex into and then toggle to a "rendered" view. That rendered view should be bookmarkable. The #fragment view should let you switch to edit source too.

Prompt 2:
Safe from XSS? We could run in an iframe sandbox like we do on the SVG markdown render project

Prompt 3:
We should have an option to load latex from a URL (or gist) similar to the markdown SVG tool
```

## Cross-References

- **Corroborates**: `blog-simonwillison-cors-chat.md` — Claim 6 (config in the shareable URL fragment) and Claim 3 (model/untrusted output rendered into an iframe); this note adds the XSS-prompting sequence and fragment-as-document-state. `blog-simonwillison-github-code-component.md` — Claim 9 (fragment-based state persistence).
- **Contradicts**: none. Note the contrast with `blog-simonwillison-github-code-component.md` Claim 2, where the agent reasoned about untrusted content safety unprompted; here the human had to ask.
- **Extends**: `blog-simonwillison-github-code-component.md` (same single-purpose browser-tool genre).
- **Novel**: Explicit post-hoc "Safe from XSS?" prompt as the trigger for sandboxing, and referencing a sibling tool's sandbox as the spec. Everything else is low novelty.

## Guide Impact

- **Chapter 06**: Could cite this as a one-line anecdote that agent-built tools that render untrusted input need a human (or checklist) security prompt after the first draft, pointing to an existing sandbox pattern; pair with `blog-simonwillison-cors-chat.md` Claim 3. No measured evidence, so anecdotal strength only.
- **Chapter 01**: Optional example of a three-prompt build (spec, security follow-up, feature-parity). Low priority.

## Extraction Notes

Read the full post (single page, no sub-pages). The sandbox attribute values are elided in the post, and no agent responses are shown. I did not fetch the live tool or its source, so claims about the actual sandbox flags or DOMPurify usage are unverified. Cross-references were checked against the claim headings in the cited notes.
