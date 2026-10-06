# Brag Plan: Dell CSM CVSS 10.0 Explainer

## What is this app?
Not an app — a security news explainer. Dell Container Storage Modules shipped a
missing-auth flaw (CVE-2026-63688, CVSS 10.0) letting unauthenticated callers go
from zero credentials to admin to root on Kubernetes nodes. The video makes that
escalation path visceral in 20 seconds.

## The angle
"Internal is a myth." The hook is the absurdity (max severity, no login), the
middle is the 3-step kill chain told as one moving diagram, the close is the
engineer's lesson: every internal service authenticates. All copy is verbatim
from the author's LinkedIn post + carousel — nothing invented.

## Hook (first 2-3 seconds)
Giant "CVSS 10.0" slamming in over the carousel cover slide, subline "NO login
required. Root on Kubernetes." No setup — severity first.

## Key moments (the middle)
- CVE-2026-63688 chip + "missing authentication for critical function" on the
  csm-authorization-storage gRPC server.
- Kill chain in 3 steps arriving one by one: unauthenticated call → admin access
  → ROOT on the node (then: secrets, pod-hopping, whole cluster).
- Lesson cards: mTLS everywhere / default-deny networking / storage plugins are
  Tier-0.

## Outro / punchline
"Patch NOW — not next sprint." + "Audit your internal services." + ATUL ANAND.
Purple-to-cyan? No — keep the carousel's own navy/cyan identity.

## User flow worth showing
none — landing-page only equivalent: news explainer, no working app. Rely on the
6 real carousel slides + recreated kill-chain diagram instead.

## Tone
- Preset: cinematic
- Creative direction: trailer-scale security alert
- Interpretation: Wide shots, big type, dramatic reveals. Hard impacts on the
  severity beats, restraint everywhere else so the words stay readable.

## Format: vertical — 1080x1920
## Duration: 20 seconds

## Visual identity (from the project)
- Background: #0A0F1E (carousel navy)
- Accent: #22D3EE (carousel cyan)
- Text: #F2F5F9 on dark
- Display font: system stack (Inter/system-ui — no external @font-face, lint-clean)
- Body font: Inter / system-ui
- Strongest visual element: the 6 real carousel slides (1080x1350), cyan rule
  bars, "ATUL ANAND" masthead, CVSS severity treatment

## Share copy (draft)
CVSS 10.0. No login. Root on Kubernetes. The Dell CSM flaw and the 3-step kill
chain — plus the patch-NOW checklist.

## Audio direction
- Role: cinematic support
- Music: happy-beats-business-moves-vol-12-by-ende-dot-app.mp3 (steady bed under
  dramatic SFX; vol-12 doubles for cinematic at low volume)
- Music treatment: start at 0s, volume 0.3 bed, dip slightly under the ROOT hit,
  fade out over final 2s (18-20s), let final impact ring over fade
- Music cue guidance: to be detected at composition time via hyperframes beats;
  lock the CVSS slam and the ROOT reveal within ±0.15s of strong beats, snap the
  3 kill-chain steps to consecutive beats
- Audio-reactive treatment: subtle; RMS swells the cyan glow behind CVSS/ROOT
  cards only. No waveform/equalizer visuals.
- SFX posture: sparse / moderate; motion-matched; cinematic restraint
- Audio-coupled moments:
  - Hook CVSS slam — deep resonant bell, let ring
  - CVE chip reveal — soft announcement hit
  - 3 kill-chain steps arriving one by one — card-slide sounds matched to each
  - ROOT landing — heavy impact, brief silence after for weight
  - Final CTA — one deep bell, let ring over fade
- Restraint rule: SFX support the edit; no glitch spam, no stacked hits, never
  under readable text holds

## Storyboard

### Scene 1 — Hook — 3s
On screen: navy #0A0F1E, cover slide (slide1) ghosted behind, giant "CVSS 10.0"
slamming to center, then "NO LOGIN. ROOT ON KUBERNETES." locking beneath it.
Cyan left rule draws in.
Sequential/interaction: none — one slam, then hold (hook gets max hold).
Audio intent: bed establishes, one deep bell under the slam.
Audio-coupled idea: single impactBell_heavy hit at "10.0" landing.
Music: vol-12 bed from 0s
Transition mood: hard cut → Scene 2

### Scene 2 — Reveal — 4s
On screen: "DELL CSM" eyebrow, "The bridge between Kubernetes and Dell
storage." CVE-2026-63688 chip + "missing authentication for critical function".
Slide2 visual at reduced opacity behind.
Sequential/interaction: yes — CVE chip pops after the bridge line (two beats).
Audio intent: tension builds, quiet confidence.
Audio-coupled idea: card-place accent on the CVE chip only.
Music: same bed
Transition mood: dramatic wipe → Scene 3

### Scene 3 — Kill chain — 9s
On screen: dark, 3 steps sliding in one by one with connecting line:
1. "UNAUTHENTICATED CALL — no password, no token, no account"
2. "ADMIN ACCESS — the server never asked WHO"
3. "ROOT ON THE NODE — secrets, pods, volumes, cluster" (accent red? No —
   keep cyan; weight comes from scale + sound, not new colors)
Then mini-lesson row: "mTLS everywhere · default-deny · Tier-0 storage".
Sequential/interaction: yes — 3 steps on consecutive beats, each with card sound;
ROOT lands bigger with heavy impact.
Audio intent: rhythmic dread, then weight on ROOT.
Audio-coupled idea: card-slide sounds per step, impactBell on ROOT, 0.4s of
near-silence after for weight (bed dips, no SFX).
Music: bed dips under ROOT, recovers for lessons; align ROOT reveal toward a
strong cue ±0.15s
Transition mood: clean wipe → Scene 4

### Scene 4 — Outro — 4s
On screen: "PATCH NOW. NOT NEXT SPRINT." then "Audit your internal services."
+ "ATUL ANAND" + "Source: The Hacker News". Full 4s hold for the CTA.
Sequential/interaction: none — settled holds, poster-safe tail.
Audio intent: bed fades 18-20s, final bell rings over fade.
Audio-coupled idea: final logo — impactBell_heavy_000, let ring.
Music: fade out 18-20s
Transition mood: end (hold 0.5s tail for poster safety)

**Music mood for this video:** steady cinematic bed, restrained
**Audio summary:** Low steady bed at 0.3 with fade-out, sparse deep bells on
severity beats, card sounds on sequential steps, one heavy ROOT hit with a
silence pocket after — dread through restraint.
