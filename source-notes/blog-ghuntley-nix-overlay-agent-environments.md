---
source_url: https://ghuntley.com/nix/
source_type: blog-post
title: "the world hasn't figured out yet that you can literally just fix everything with a Nix overlay"
author: Geoffrey Huntley
date_published: 2026-10-07
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: anecdotal
issue: "#3988"
---

# the world hasn't figured out yet that you can literally just fix everything with a Nix overlay

> An opinion-led, first-person advocacy post arguing that Nix (devenv, `buildLayeredImage`, NixOS `runNixOSTest`, overlays) gives agents one reproducible environment definition, a whole-OS test substrate, and a way to remove dangerous capabilities (e.g. `git push --force`) from the binary itself — with concrete config but no metrics, comparisons, or failure cases.

## Source Context

- **Type**: blog-post (personal blog, ghuntley.com, 07 Oct 2026). Long mostly because of a ~150-line embedded NixOS test; prose is short. Linked demo repo `ghuntley/nix-demo` (not read in this extraction; only the post's description of it is used).
- **Author credibility**: Geoffrey Huntley, known for agentic-coding techniques (Ralph loops); states ~13 years of Nix experience. Claims rest on personal practice, not measurements.
- **Scope**: Covers devenv as shared environment definition, Nix-built Docker images, NixOS as an agent-`sudo`-safe OS, whole-OS VM testing as the loop's system under test, and overlays for patching tools/dependencies. Does NOT cover: rollback limits, any quantitative comparison with mise/Docker/cloud, failure modes, or how agents actually performed.

## Extracted Claims

### Claim 1: A single devenv.nix can be the source of truth for toolchain and dependencies across humans, CI/CD, and ephemeral agent sandboxes
- **Evidence**: A short `devenv.nix` (rust, postgres, `prek` package, rustfmt git hook) plus `devenv up`. No evidence of use at scale beyond the author's assertion.
- **Confidence**: emerging
- **Quote**: "you can define a single source of truth for your compilation toolchain and required third-party dependencies. Humans can use this single source of truth in CI/CD and in ephemeral sandbox development environments used by agents."
- **Our assessment**: Plausible and consistent with how devenv/Nix work; the config is concrete. "Just works across all operating systems" is unverified (Nix on Windows is not native). Useful as a pattern, not as proven benefit.

### Claim 2: Environment drift between laptop, CI, and agent sandboxes is a real, growing problem that this unification removes
- **Evidence**: Anecdote from client work ("I keep coming across clients..."); no counts.
- **Confidence**: anecdotal
- **Quote**: "And now we've got ephemeral sandbox environments; they're heading down a path of triplicating that drift."
- **Our assessment**: Believable framing (three environments instead of two), but unmeasured.

### Claim 3: The same toolchain expression that defines the dev environment can build the Docker image, which could also be the production runtime
- **Evidence**: `pkgs.dockerTools.buildLayeredImage` example producing an image with git and cacert.
- **Confidence**: emerging
- **Quote**: "That same expression that defines your human developer environment setup, your CI/CD setup, and your ephemeral sandbox setup can also be reused to build performant Docker images."
- **Our assessment**: Technically accurate in general (buildLayeredImage is real). Note the example image contains only git and does not reuse the devenv expression, so the "same expression" claim is asserted, not shown inline.

### Claim 4: Letting agents use `sudo` is safe on NixOS because it is "nearly impossible to break" and any change can be rolled back instantly
- **Evidence**: None beyond assertion; author says he does this in his own loops.
- **Confidence**: anecdotal
- **Quote**: "it is safe because NixOS is designed to make it nearly impossible to break a machine, and if it does, you can instantly roll back that change."
- **Our assessment**: The riskiest claim. NixOS generation rollback restores system configuration, but does not undo state outside the declarative system (data in /home, /var, databases, secrets exfiltrated, network side effects, deleted non-store files), and root can still `rm -rf` or alter the bootloader/store. Rollback contains misconfiguration, not a malicious or destructive agent. Treat as unsupported for Ch06 (this assessment is ours, not the post's; the post makes no mention of limits).

### Claim 5: Putting the entire operating system under test (not just app + Postgres) is what distinguishes the author's loop engineering from others'
- **Evidence**: Assertion about "others", plus the HAProxy/firewall NixOS VM test.
- **Confidence**: anecdotal
- **Quote**: "when I run loops, I put the entire system under test, and the entire System Under Test IS the operating system."
- **Our assessment**: Claim about what others do is unevidenced. The underlying idea (OS-level, multi-machine assertions as agent backpressure) is novel to our corpus and worth recording.

### Claim 6: NixOS's built-in `runNixOSTest` framework can spin up multi-machine clusters and assert network/firewall behavior before deploy
- **Evidence**: Full worked test: two QEMU nodes on separate VLANs, HAProxy frontend, Python backend, iptables allow-only-from-proxy and no-new-outbound rules, a negative-control source address, subtests with `succeed`/`fail`.
- **Confidence**: settled (that the mechanism exists and works as shown); anecdotal (that it improves agent outcomes)
- **Quote**: "You can use a number of machines in a test, assert the network rules between them are correct, and that the right IP tables are forwarded or dropped."
- **Our assessment**: Strong concrete artifact. The test includes negative controls (untrusted source IP must be rejected), a good verification pattern. Post does not show an agent writing or iterating on this test.

### Claim 7: A single overlay can patch a transitive dependency (OpenSSL) fleet-wide, answering a critical CVE in "a couple of lines"
- **Evidence**: Overlay snippet pinning openssl 3.0.7 with `overrideAttrs`. Snippet in the post is truncated (unbalanced braces, `hash = "sha256-..."`), so it is illustrative, not runnable.
- **Confidence**: emerging
- **Quote**: "With nix, this can be achieved through a couple of lines"
- **Our assessment**: Mechanism is real, but "rebuild the world" cost (acknowledged by the author) and testing burden are glossed. Note the example sets version 3.0.7, an older release, as the "fix" — illustrative only.

### Claim 8: Patching a tool's binary with an overlay enforces a safety constraint — e.g. removing `git push --force` from git in agent sandboxes — that prompts or permission rules cannot
- **Evidence**: Author says he has used this "for years"; linked repo `ghuntley/nix-demo` reportedly includes a NixOS VM test asserting force-push is gone. The post gives no diff of the patch itself.
- **Confidence**: emerging
- **Quote**: "in my agent sandbox environments, I customize the Git binary and remove the agent's ability to force-push by removing that functionality from Git itself."
- **Our assessment**: Conceptually interesting: capability removal at the binary level is stronger than a deny rule, since there is no instruction to ignore. Caveat (ours): an agent with `sudo`/network can still use other clients (libgit2, raw HTTP, another git build) unless the sandbox also restricts those; the server-side branch protection is the robust control. Also in tension with Claim 4 (agent has sudo yet is constrained at binary level).

### Claim 9: Nix makes "all software infinitely customizable" and you can patch anything by asking an agent to do it
- **Evidence**: Rhetorical; no example of an agent producing an overlay.
- **Confidence**: anecdotal
- **Quote**: "you can patch anything by asking an agent to customize it."
- **Our assessment**: Unevidenced. Related claim that "These LLMs know Nix very well" is also unmeasured.

### Claim 10: mise is "not good enough" for agent environments
- **Evidence**: None.
- **Confidence**: anecdotal
- **Quote**: "Trust me, mise isn't good enough."
- **Our assessment**: Pure opinion; no comparison. Do not cite as a finding.

### Claim 11: Bare metal plus NixOS beats hyperscalers, with 1–2 experienced sysadmins matching a team of 50
- **Evidence**: None.
- **Confidence**: anecdotal
- **Quote**: "one or two of those people can operate with leverage equivalent to a team of 50 \"cloud certified\" monkeys."
- **Our assessment**: Unevidenced and off-topic for the guide. Excluded from Guide Impact.

### Claim 12: Nix's learning cliff, previously prohibitive, is now crossable because AI lets you "prompt for outcomes"
- **Evidence**: Author's own experience (took "a couple of years" to master pre-AI).
- **Confidence**: anecdotal
- **Quote**: "Now that we have AI, things that used to be advanced power tools, hard to use or designed for masters, are now accessible to everyone."
- **Our assessment**: Plausible direction; no evidence. Also candidly self-admits Nix is "a terrible programming language" and has real downsides (incremental caching vs Bazel/Buck2), which temper the advocacy.

## Concrete Artifacts

```nix
# Source: ghuntley.com/nix/ — devenv.nix example
packages = [ pkgs.prek ];
languages = { rust.enable = true; };
services = { postgres.enable = true; };
git-hooks = { hooks = { rustfmt.enable = true; }; };
# then: $ devenv up
```

```nix
# Source: ghuntley.com/nix/ — Docker image from Nix
pkgs.dockerTools.buildLayeredImage {
  name = "git";
  tag = "latest";
  contents = [ (pkgs.buildEnv { name = "image-root"; paths = [ pkgs.git pkgs.cacert ]; pathsToLink = [ "/bin" "/etc" ]; }) ];
  config.Env = [ "PATH=/bin" "SSL_CERT_FILE=/etc/ssl/certs/ca-bundle.crt" ];
  config.Cmd = [ "/bin/git" "--version" ];
};
```

Whole-OS test (ghuntley.com/nix/, summarized; full ~150-line `runNixOSTest` in source): two nodes (`haproxy` on vlans 1+2, `web` on vlan 2); web firewall accepts TCP 8080 only from the proxy's backend IP and rejects new outbound; an extra address 192.168.2.50 on haproxy is a negative control that must be refused. Run with `nix build .#checks.x86_64-linux.haproxy-hello`; interactive via `nix run .#driverInteractive`. Subtests: "backend accepts only haproxy on the hello port", "haproxy on the frontend vlan proxies to python", "python host cannot open new outbound connections".

```nix
# Source: ghuntley.com/nix/ — overlay (truncated in the source)
nixpkgs.overlays = [
  (final: prev: {
    openssl = prev.openssl.overrideAttrs (old: {
    version = "3.0.7";
    src = prev.fetchurl { url = "https://www.openssl.org/source/openssl-3.0.7.tar.gz"; hash = "sha256-..."; };
```

## Cross-References

- **Corroborates**: None directly. Loosely consistent with [blog-vercel-herdr-agent-sandboxes](blog-vercel-herdr-agent-sandboxes.md) (agents work best in isolated, disposable environments), but via a different mechanism.
- **Contradicts**: None filed. Mild tension with [blog-green-sandboxing-rogue-agents](blog-green-sandboxing-rogue-agents.md) Claim 5 ("Sandboxes cannot perfectly isolate useful agents because usefulness requires information access"): Huntley's rollback/sudo-safety argument addresses system integrity only, not information flow or exfiltration, which Green's note treats as the core sandbox problem. Different problem scopes, so not a formal contradiction.
- **Extends**: [blog-ghuntley-engineer-away-slop](blog-ghuntley-engineer-away-slop.md) Claims 6 and 8 (deterministic system testing / simulators as verification) — this post is a lighter-weight, OS-level VM-test variant of the same "verify the whole system" idea. [blog-simonwillison-smolmachines-untrusted-sandbox](blog-simonwillison-smolmachines-untrusted-sandbox.md): that note tests VM-based sandbox isolation (Claims 1–2) with measured results; this post offers VM-based testing of the OS config, not isolation of the agent.
- **Novel**: Nix/devenv as a unified agent-environment definition; NixOS multi-VM tests as agent backpressure; overlay-based capability removal from binaries (force-push removal); OS rollback as a claimed `sudo` containment strategy. Prior notes (e.g. [practitioner-getsentry-sentry](practitioner-getsentry-sentry.md)) mention devenv only for dev setup.

## Guide Impact

- **Chapter 02**: Candidate sidebar/example: one declarative environment definition (devenv) shared by laptop, CI and agent sandbox to avoid drift; cite as a single anecdotal practitioner pattern, with the concrete `devenv.nix` snippet.
- **Chapter 03**: Add as an example of OS-level verification — multi-VM `runNixOSTest` with negative controls (untrusted source must fail) as loop backpressure. Do not claim demonstrated agent benefit.
- **Chapter 06**: Add "remove the capability from the binary" (patched git without force-push) as a defense-in-depth option beyond prompt/permission rules, with the caveats above. Do NOT repeat the "sudo is safe because rollback" claim without the stated limits (rollback does not cover state outside the system generation or exfiltration).

## Extraction Notes

- Fetched the full page HTML via curl and read all prose and code; quotes copied from the extracted text. One quote in Claim 11 includes the source's escaped inner quotes.
- Did not read `ghuntley/nix-demo`; statements about its content come from the post. A follow-up could verify that the force-push patch and VM test exist as described.
- Per triage: lab-economics, bare-metal and RSI remarks are recorded as anecdotal and are not findings. Post is opinion-led with no metrics, comparisons or failure cases.
