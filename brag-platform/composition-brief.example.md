# Hyperframes Composition Brief: BuildForge Platform

## Objective
Create a short launch-style brag video introducing the BuildForge platform
revamp (marketplace + community + meetups + passport).

## Output
- Composition directory: `C:\Users\HP\OneDrive\Documents\New folder\brag-output-platform\composition/`
- Rendered video: `C:\Users\HP\OneDrive\Documents\New folder\brag-output-platform\brag.mp4`
- Format: vertical — 1080x1920
- Duration: 20 seconds

## Source Material
- Project root: C:\Users\HP\OneDrive\Documents\New folder\brag-output-platform\ (SOURCE.md)
- Primary files read: business revamp plan doc v1.0 (Sept 2026), pasted in chat
- Product name: BuildForge Platform
- Tagline / strongest claim: Where Emerging Talent Meets Opportunity.
- Key UI or visual moment to recreate: pillar cards, money count-up
  (₹5,000 → ₹500 → ₹4,500), VERIFIED passport stamp, Circle ticket stub
- Copy that must appear verbatim:
  - NOT AN AGENCY. / A PLATFORM.
  - Where Emerging Talent Meets Opportunity.
  - TALENT / CONNECT / CIRCLE (+ one-line descriptors from plan)
  - ₹5,000 · ₹500 fee · ₹4,500
  - brief → match → deliver → PASSPORT VERIFIED
  - CIRCLE PILOT · 12–15 seats · ₹2,500
  - START WITH ONE PILOT PROJECT.
  - buildforge.site / ceo@buildforge.site

## Creative Direction
- Tone preset: polished
- Creative direction: premium platform launch film
- Interpretation: Confident restraint, but zero dead air — motion or sound in
  every second; the previous cut's static 6s hold and untimed SFX are banned.
- Angle: The strategic shift itself — from agency to platform — told through
  the doc's own numbers.
- Hook: "NOT AN AGENCY." crossed out into "A PLATFORM." (first 2-3s).
- Outro / punchline: "START WITH ONE PILOT PROJECT." + contacts.
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Static holds longer than 1s without new motion or sound
  - Sounds without simultaneous visuals

## Visual Identity
- Background: #FCFCFA light / #232326 dark proof block
- Text: #111111 / #FFFFFF
- Accent: #7C3AED (purple)
- Accent 2: #C4B5FD (lavender)
- Display font: system stack (no external @font-face)
- Body font: system stack
- Visual references from the project: pillar cards, count-up numbers, stamp
  badge, ticket stub, purple arc

## Storyboard
Use `brag-output-platform/brag-plan.md` as the creative contract.

Scene summary:
1. Hook — 3s — cross-out AGENCY → A PLATFORM + positioning line
2. Pillars — 5s — 3 cards arrive on beats (TALENT/CONNECT/CIRCLE)
3. Proof — 8s — dark; money count-up, workflow strip, VERIFIED stamp, ticket stub
4. Outro — 4s — pilot CTA + contacts, living accents (no frozen frame)

## Audio
- Audio role: warm bed with purpose; every sound lands on a visual
- Audio arc: steady bed, one dip under money count, fade 18-20s
- Music: happy-beats-business-moves-vol-12-by-ende-dot-app.mp3
- Music treatment: volume 0.35, start 0s, dip under count, fade-out last 2s
- Music cue guidance: bundled preset cues/vol-12 JSON; lock "A PLATFORM."
  (~2.5s) and VERIFIED stamp (~13s) within ±0.15s of strong cues; pillar cards
  + steps on every-other-beat grid; or unavailable
- Audio-reactive treatment: subtle; RMS breathes arc glow + card presence only
- Audio-coupled moments:
  - Cross-out snap + PLATFORM bell
  - 3 pillar card-place hits
  - Money count ticks per number
  - VERIFIED deep bell
  - Ticket stub card-slide
  - Outro impactBell_heavy_000, let ring
- SFX selection guidance: sparse professional; card sounds for arrivals, bells
  for payoffs; prefer low/medium HF-risk files per sfx-analysis.md
- SFX analysis guidance: C:\Users\HP\.agents\skills\brag\assets\sfx\sfx-analysis.md
- Exact SFX choice: Hyperframes chooses filenames/timestamps/density/volume
  from the implemented animation.
- Audio files: copy music + selected SFX into composition/assets/

## Hyperframes Instructions
Load hyperframes-core, hyperframes-animation, hyperframes-creative,
hyperframes-keyframes, hyperframes-cli. /brag is its own workflow: no
entry-point interview, no generic promo routing. Prefer native Hyperframes
conventions.

Requirements:
- Show at least one real UI/copy element from the source (all copy is).
- Keep all text readable; keep 15-25s; include planned music/SFX.
- Audio notes are guidance; SFX chosen after animation exists.
- Cue metadata is optional hints; readability first.
- Major reveals may move toward strong cues ±0.15s; sequential entrances snap
  to beats ±0.10s; 1-3 strong locks per video.
- SFX support motion: cards, payoffs, interactions; restraint when busy.
- Honor fades, ducking, beat reveals, final ring.
- Audio-reactive only subtle brand elements; no visualizers.
- Local assets only. `hyperframes check` before render. Local render only.
