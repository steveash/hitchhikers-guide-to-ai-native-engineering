---
source_url: https://developers.googleblog.com/ml-development-in-vs-code-with-google-cloud-power-workbench-extension-now-available/
source_type: blog-post
title: "ML Development in VS Code with Google Cloud Power: Workbench Extension Now Available"
author: "Andrii Lobanov (Software Engineer), Alex Kallaur (Software Engineering Manager), Diego Granados (Product Manager) — Google"
date_published: 2026-07-01
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1743"
---

# ML Development in VS Code with Google Cloud Power: Workbench Extension Now Available

> Google's July 1, 2026 announcement of an open-source VS Code extension that
> exposes Vertex AI Workbench's managed cloud Jupyter servers through VS Code's
> native kernel picker — a concrete example of "meet developers where they
> already are" tooling design, undercut by the extension's own GitHub metrics
> showing minimal adoption (12 stars, 5 forks, zero tagged releases) six
> months after the repo was created, despite the announcement's framing as a
> significant developer-ecosystem launch.

## Source Context

- **Type**: blog-post (Google Developers Blog, product/feature announcement,
  ~450 words; not a technical deep-dive or research post)
- **Author credibility**: Three named Google employees with production-team
  titles (Software Engineer, Software Engineering Manager, Product Manager)
  — a first-party feature-launch announcement, not a third-party or
  independent report. The existence of the extension, its license, and its
  install/setup mechanics are independently verifiable (GitHub repo, VS Code
  Marketplace listing); the framing claims ("streamline the ML lifecycle,"
  "eliminating context switching") are vendor marketing language for a
  feature that is, at its core, a kernel-provider plugin.
- **Scope**: Covers what the extension does (connects VS Code notebooks to
  Google Cloud Workbench/Vertex AI compute), how to install and use it
  (three-step Quick Start), and its open-source/licensing status. Does NOT
  cover: pricing or billing for the underlying Workbench compute, performance
  benchmarks, comparison to alternative remote-Jupyter-in-VS-Code approaches
  (e.g., `code-server`, Jupyter's own remote-kernel support, SageMaker
  Studio's VS Code integration), or any first-party usage/adoption data.

## Extracted Claims

### Claim 1: Google is launching a VS Code extension whose explicit design goal is to combine "the familiarity of a local IDE with the heavy-lifting capabilities of the cloud," eliminating context switching between local experimentation and cloud compute

- **Evidence**: Opening framing paragraph and "streamline the ML lifecycle"
  section of the announcement.
- **Confidence**: emerging (vendor framing of intent; the extension's
  mechanics that implement this framing — kernel-picker integration — are
  independently verifiable, but "streamlines the ML lifecycle" and
  "eliminating context switching" are unmeasured marketing claims)
- **Quote**: "For data scientists and developers, the ideal workflow combines the familiarity of a local IDE with the heavy-lifting capabilities of the cloud. Today, we are bridging that gap with the launch of the Google Cloud Workbench Notebooks extension for VS Code."
- **Our assessment**: This is the standard "meet developers where they already
  are" pitch also seen in `blog-google-gemma-4-12b-developer-guide.md` Claim 9
  (local model served via an OpenAI-compatible endpoint so existing coding-agent
  harnesses don't need reconfiguring) — except inverted: here it's cloud
  compute being surfaced inside an existing local tool (VS Code's kernel
  picker), rather than a local model being surfaced through an existing
  remote-API interface. Both are instances of the same design principle:
  extend the surface developers already use rather than requiring a new one.

### Claim 2: The extension does not replace VS Code's notebook experience — it is built to "work in tandem with" (per the blog) and is "built atop" (per the extension's own README) the existing Microsoft Jupyter extension

- **Evidence**: Both the blog's Step 1 instructions and the GitHub README's
  opening description independently state the same dependency relationship.
- **Confidence**: settled (two independently-published first-party texts —
  the blog and the README — describe the same technical dependency;
  internally consistent)
- **Quote (blog)**: "This extension works in tandem with the Jupyter extension to provide a seamless notebook experience."
- **Quote (README, github.com/GoogleCloudPlatform/colab-enterprise-vscode)**: "Built atop the Jupyter extension, this extension exposes Workbench Jupyter servers directly in VS Code!"
- **Our assessment**: This is a real architectural fact, not marketing: the
  Workbench extension is a kernel-source provider for Microsoft's Jupyter
  extension, not a standalone notebook UI. Practically, this means
  installing it requires (and depends on the continued compatibility of) the
  `ms-toolsai.jupyter` extension — a third-party dependency risk for Google's
  own extension that the blog post does not mention but the README's Quick
  Start step 3 makes explicit ("Install the Jupyter extension if not already
  installed").

### Claim 3: Connecting to cloud compute is done entirely through VS Code's native "Select Kernel" picker — choosing Google Cloud → Workbench as a compute provider — rather than a separate console, panel, or web UI

- **Evidence**: Step-by-step Quick Start instructions given identically (in
  substance) in both the blog post and the GitHub README.
- **Confidence**: settled (concrete, specific, verifiable UX description
  given consistently across two first-party sources)
- **Quote (blog)**: "Open a notebook (.ipynb) and use the Select Kernel option located in the editor's toolbar. Navigate through the Google Cloud menu and choose Workbench as your compute provider."
- **Quote (README)**: "Click `Select Kernel` > `Google Cloud` > `Workbench`."
- **Our assessment**: This is the most concrete evidence for the "no context
  switching" claim in Claim 1: the cloud-compute selection genuinely reuses
  an existing VS Code affordance (the kernel picker) instead of adding a new
  top-level UI surface. Whether this constitutes a materially different
  workflow from opening a browser tab to a cloud console is a matter of
  degree, but the mechanism itself is real and specific enough to be a
  useful UX pattern reference: treat a remote managed-compute environment as
  just another kernel choice.

### Claim 4: The extension is fully open-sourced under an Apache-2.0 license, published to a public GitHub repository the announcement invites contributions to

- **Evidence**: Blog framing plus independent verification via the GitHub
  API (`api.github.com/repos/GoogleCloudPlatform/colab-enterprise-vscode`),
  which confirms `license.spdx_id: Apache-2.0`.
- **Confidence**: settled (license is a factual, independently checked claim)
- **Quote**: "In line with our commitment to the developer ecosystem, the extension is fully open-sourced, allowing for community-driven contributions and transparency."
- **Our assessment**: The license claim checks out. But "community-driven
  contributions" is not yet borne out by the repo's own metrics: as of
  extraction (July 11, 2026, ~6 months after the repo's January 12, 2026
  creation date), the repo has 12 stars, 5 forks, and zero tagged releases
  (verified via the GitHub API). This is a useful counterpoint the blog post
  itself does not mention — "fully open-sourced" describes the license, not
  the level of actual community engagement. See Concrete Artifacts for the
  full metrics snapshot.

### Claim 5: The extension "does not collect any client-side usage data within VS Code"

- **Evidence**: Explicit statement in the GitHub README's "Data and
  Telemetry" section.
- **Confidence**: settled (explicit first-party technical/privacy claim from
  the extension's own documentation; not independently audited by us, but
  it is a specific, falsifiable claim rather than vague marketing language)
- **Quote (README)**: "The extension does not collect any client-side usage data within VS Code. See the Google Cloud Terms of Service and the Google Cloud Privacy for more information."
- **Our assessment**: This claim is absent from the blog post entirely — it
  only appears in the README, which the blog does not link to directly (the
  blog links to the GitHub repo root, not this specific section). A
  practitioner who reads only the announcement would not learn the
  extension's telemetry posture; they would need to follow through to the
  repository documentation, which is exactly the kind of "read past the
  announcement" step MINER.md's sub-page-following guidance exists for.

### Claim 6: The extension's own security guidance warns that malicious lookalike extensions could access a user's OAuth credentials, and recommends installing only from a trusted marketplace and verifying the "GoogleCloudTools" verified-publisher badge

- **Evidence**: GitHub README "Security" section, an explicit named risk with
  a named mitigation, not present anywhere in the blog announcement.
- **Confidence**: settled (explicit first-party risk disclosure with a
  specific mitigation, not a vague security platitude)
- **Quote (README)**: "To mitigate the risk of malicious extensions accessing your OAuth credentials, ensure the extension is installed from a trusted source (such as the Visual Studio Marketplace or Open VSX) and is authored by the verified publisher (GoogleCloudTools)."
- **Our assessment**: This is the single most guide-relevant claim in the
  source. It is Google naming a concrete, extension-specific supply-chain
  risk (a fake "Google Cloud Workbench Notebooks" lookalike extension
  phishing for OAuth tokens) and prescribing a specific, checkable
  mitigation (verified-publisher badge). This is directly analogous to the
  skill-supply-chain caution documented in `docs-github-copilot-agent-skills-cli.md`
  Claim 6 (skills may carry hidden instructions or malicious scripts,
  verify before installing) — except for VS Code extensions with OAuth
  scopes rather than agent skill packages. Notably, this warning is entirely
  absent from the announcement blog post itself; it only exists in the
  README, reinforcing Claim 5's point about the value of reading past the
  announcement.

### Claim 7: The announcement names the underlying cloud product "Gemini Enterprise Agent Platform Workbench," while the extension's own GitHub repository and README consistently call the same product "Vertex AI Workbench"

- **Evidence**: Direct textual comparison between the blog post's own
  product-naming language and the README/repo's product-naming language,
  both first-party Google sources published around the same time (repo
  created January 12, 2026; blog post published July 1, 2026).
- **Confidence**: settled (both phrasings are independently verified verbatim
  text from the two respective sources; the discrepancy itself is a
  directly observable fact)
- **Quote (blog)**: "Gemini Enterprise Agent Platform Workbench has long been a go-to platform for managed Jupyter environments optimized for data science."
- **Quote (README)**: "[Workbench Notebooks](https://cloud.google.com/vertex-ai/docs/workbench/introduction) instances are Jupyter notebook-based development environments for the entire data science workflow." — the README's own link target is `cloud.google.com/vertex-ai/docs/workbench`, and the GitHub repo's one-line description (verified via API) is "A Visual Studio Code extension for Vertex AI Workbench."
- **Our assessment**: This is not a claim the source makes about itself — it's
  a discrepancy we observed by cross-checking the blog against its own
  linked repository. The blog's marketing copy uses the newer "Gemini
  Enterprise Agent Platform" branding umbrella while the actual product
  documentation, GitHub description, and README all still use "Vertex AI
  Workbench." This reads as branding churn (Google folding Vertex AI
  products under a "Gemini Enterprise" umbrella in blog copy faster than the
  underlying product surfaces and docs are relabeled) rather than two
  different products. Practitioners following the blog's terminology into
  Google Cloud Console or search would need to know "Vertex AI Workbench" is
  the actual product/menu name as of this writing.

## Concrete Artifacts

### Quick Start steps (blog post, "Launch your Workbench Workflow in VS Code")

```
1. Equip your IDE: Search VS Code Extensions for "Google Cloud Workbench
   Notebooks"; install the official package (GoogleCloudTools.workbench-notebooks).
   Works in tandem with the Jupyter extension.
2. Initiate a Cloud Connection: Open a .ipynb file, use Select Kernel >
   Google Cloud > Workbench.
3. Authenticate and Access: Sign in, pick a GCP project, select an active
   Workbench instance.

Source: developers.googleblog.com/ml-development-in-vs-code-with-google-cloud-power-workbench-extension-now-available/
```

### GitHub README Quick Start (verbatim, github.com/GoogleCloudPlatform/colab-enterprise-vscode)

```
1. Install VS Code.
1. Install the Workbench extension from either the Visual Studio
   Marketplace or Open VSX.
1. Install the Jupyter extension if not already installed.
1. Open or create a notebook file.
1. Click `Select Kernel` > `Google Cloud` > `Workbench`.
1. When prompted, sign in.
1. Search and select a GCP project.
1. Select an active Workbench instance.
1. 😎 Enjoy!
```

### Repo metrics snapshot (verified via `api.github.com/repos/GoogleCloudPlatform/colab-enterprise-vscode`, checked July 11, 2026 — not stated in the source, independently retrieved to test the "community-driven contributions" framing in Claim 4)

```
Description:  "A Visual Studio Code extension for Vertex AI Workbench."
License:      Apache-2.0
Language mix: TypeScript 247,195 bytes / Shell 4,197 bytes / JavaScript 668 bytes
              (~98% TypeScript, ~1.7% Shell, ~0.3% JavaScript)
Created:      2026-01-12
Last push:    2026-07-10 (actively maintained — pushed the day before extraction)
Stars:        12
Forks:        5
Open issues:  0
Releases:     0 tagged releases
```

### README "Data and Telemetry" and "Security" sections (verbatim)

```
## Data and Telemetry

The extension does not collect any client-side usage data within VS Code. See
the Google Cloud Terms of Service and the Google Cloud Privacy for more
information.

## Security

To mitigate the risk of malicious extensions accessing your OAuth
credentials, ensure the extension is installed from a trusted source (such
as the Visual Studio Marketplace or Open VSX) and is authored by the
verified publisher (GoogleCloudTools).

Please see our security disclosure process. All security advisories are
managed on GitHub.

Source: raw.githubusercontent.com/GoogleCloudPlatform/colab-enterprise-vscode/main/README.md
```

## Cross-References

- **Corroborates**: No existing source note documents this specific
  local-IDE-to-managed-cloud-notebook integration pattern; nothing in the
  corpus directly corroborates or duplicates this claim set.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Vertex AI Workbench, VS Code kernel providers, or this extension
  that this source materially opposes. No contradiction issue filed.

- **Extends**: `blog-google-gemma-4-12b-developer-guide.md` Claim 9 (the
  `litert-lm serve` CLI turns a local Gemma 4 12B model into an
  OpenAI-compatible endpoint so existing coding-agent tools — Continue,
  Aider, OpenClaw, Hermes, OpenCode — can point at it without
  reconfiguration). Both sources are Google-published examples of the same
  underlying design principle — surface new compute (a local model there, a
  remote managed notebook kernel here) through an interface developers
  already use, rather than requiring a new tool — but in opposite
  directions: that source pushes a local model out through a remote-API-shaped
  interface; this source pulls remote compute in through a local-IDE-shaped
  interface (the kernel picker). Worth citing together as two data points for
  a "meet developers in their existing interface" pattern, not as the same
  claim restated.

- **Novel**: The following are not documented in any other source note:
  - **VS Code's native kernel-picker used as the sole cloud-compute-provider
    selection UI**: No other corpus source describes a cloud vendor
    integrating managed compute access through an existing IDE affordance
    (the Jupyter kernel picker) rather than a bespoke panel, sidebar, or
    web console.
  - **A trusted-feed source with verified-but-minimal adoption**: This is
    the first corpus instance where we independently checked a trusted-feed
    vendor announcement's own GitHub repo and found adoption metrics (12
    stars, 5 forks, 0 releases after ~6 months) that undercut the
    announcement's "community-driven contributions" framing. This is a
    useful data point for the Prospector's own trusted-feed calibration:
    "trusted feed" (i.e., a credible publisher) is not the same guarantee as
    "significant or widely-adopted."
  - **Named OAuth-credential-phishing risk via lookalike VS Code
    extensions, with a verified-publisher mitigation**: No prior corpus
    source names this specific extension-marketplace supply-chain risk
    (malicious extensions impersonating a legitimate cloud-vendor extension
    to harvest OAuth tokens) or its mitigation (checking the verified
    publisher badge).
  - **"Gemini Enterprise Agent Platform" vs. "Vertex AI Workbench" naming
    discrepancy**: First corpus instance of a same-day/same-source branding
    inconsistency between a vendor's marketing copy and its own linked
    product documentation for the same underlying product.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 3 (kernel-picker-as-
  cloud-compute-selector) as a concrete UX pattern example for "extend an
  existing local surface instead of building a new one" — cite alongside
  `blog-google-gemma-4-12b-developer-guide.md` Claim 9 as two vendor
  examples (one Google-internal-compute-out, one Google-local-model-out) of
  the same principle. Do not cite adoption numbers as evidence the pattern
  works at scale — Claim 4's repo metrics (12 stars, 0 releases) show this
  specific implementation has not yet demonstrated traction; the guide
  should present the UX pattern, not this extension's popularity, as the
  takeaway.

- **Chapter 06 (Security and Threat Model)**: Add Claim 6 (OAuth-credential
  phishing risk via lookalike VS Code extensions, mitigated by checking the
  verified-publisher badge) as a named, vendor-acknowledged risk in any
  section on IDE extension supply-chain hygiene. This is a concrete,
  first-party-disclosed risk category distinct from the skill-file risks
  already covered via `docs-github-copilot-agent-skills-cli.md` — extension
  marketplaces carry OAuth-scope risk that skill-file installers may not.

## Extraction Notes

- The blog post itself is short (~450 words) with no linked sub-pages
  beyond the VS Code Marketplace listing and the GitHub repository. Both
  were followed per MINER.md's sub-page guidance: the GitHub repository
  (README fetched verbatim from `raw.githubusercontent.com`, plus repo
  metadata independently verified via the GitHub REST API) and the VS Code
  Marketplace listing (fetched, but install-count/rating data is rendered
  client-side and was not recoverable from the static HTML — that data
  point could not be verified and is not claimed in this note).
- All blog-post quotes were verified against a raw `curl`-fetched copy of
  the page (tags stripped, text compared line-by-line against the initial
  WebFetch summary) rather than taken from the WebFetch summary alone, per
  the verbatim-quote requirement in MINER.md §2a — the WebFetch summary and
  raw HTML text matched closely for this source, but the raw fetch was
  treated as authoritative for exact wording.
- This is a genuinely thin source: a ~450-word feature announcement with no
  metrics, no code beyond a three-step setup flow, and no named customer or
  practitioner testimonial. Seven claims were extracted by reading the
  announcement together with its two linked first-party artifacts (GitHub
  README, GitHub API repo metadata) rather than padding out claims from the
  announcement text alone — several of the most useful claims here (Claims
  5, 6, and 7) come from the README and repo metadata, not the blog post
  itself, and would have been missed by reading only the announcement.
- No contradiction with existing corpus sources was found, so no
  contradiction issue was filed per MINER.md §4a.
