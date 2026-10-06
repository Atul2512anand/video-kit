# Hyperframes Composition Brief: Dell CSM CVSS 10.0 Explainer

## Objective
Create a short cinematic security-news explainer video for the author's Dell CSM
LinkedIn post.

## Output
- Composition directory: `C:\Users\HP\OneDrive\Documents\New folder\brag-output-dell-csm\composition/`
- Rendered video: `C:\Users\HP\OneDrive\Documents\New folder\brag-output-dell-csm\brag.mp4`
- Format: vertical — 1080x1920
- Duration: 20 seconds

## Source Material
- Project root: C:\Users\HP\OneDrive\Documents\content automation\drafts\
- Primary files read: 2026-10-05_1510.md (post text), assets/carousel_2026-10-05_1510_slide1-6.png (real visuals)
- Product name: Dell CSM CVSS 10.0 explainer (Atul Anand)
- Tagline / strongest claim: CVSS 10.0 on Dell storage with NO login required? And it leads straight to root on Kubernetes?
- Key UI or visual moment to recreate: the 6 real carousel slides (navy/cyan), CVE-2026-63688 chip, 3-step kill chain diagram
- Copy that must appear verbatim:
  - CVSS 10.0
  - NO LOGIN. ROOT ON KUBERNETES.
  - CVE-2026-63688
  - missing authentication for critical function
  - UNAUTHENTICATED CALL / ADMIN ACCESS / ROOT ON THE NODE
  - PATCH NOW. NOT NEXT SPRINT.
  - Audit your internal services.
  - ATUL ANAND / Source: The Hacker News

## Creative Direction
- Tone preset: cinematic
- Creative direction: trailer-scale security alert
- Interpretation: Big motion, bigger claims. Hard impacts on severity beats, restraint elsewhere.
- Angle: "Internal is a myth" — max severity with no login, told as a 3-step kill chain, closed with the engineer's lesson.
- Hook: Giant "CVSS 10.0" slam over the ghosted cover slide (first 2-3s).
- Outro / punchline: "PATCH NOW. NOT NEXT SPRINT." + audit CTA + masthead.
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign
  - New colors (stay navy #0A0F1E / cyan #22D3EE / off-white)

## Visual Identity
- Background: #0A0F1E (carousel navy)
- Text: #F2F5F9 on dark
- Accent: #22D3EE (carousel cyan)
- Display font: Inter / system-ui 800/900 (fallback stack, no external @font-face)
- Body font: Inter / system-ui
- Visual references from the project: 6 carousel slides under assets/slides/, cyan left rule, ATUL ANAND masthead, progress dots

## Storyboard
Use the storyboard in `C:\Users\HP\OneDrive\Documents\New folder\brag-output-dell-csm\brag-plan.md` as the creative contract.

Scene summary:
1. Hook — 3s — CVSS 10.0 slam + NO LOGIN. ROOT ON KUBERNETES. over ghosted slide1
2. Reveal — 4s — DELL CSM bridge line + CVE-2026-63688 chip + missing-auth line
3. Kill chain — 9s — 3 steps slide in on beats (call → admin → ROOT) + lesson row
4. Outro — 4s — PATCH NOW + audit CTA + ATUL ANAND + source

## Audio
- Audio role: cinematic support
- Audio arc: steady low bed, dips under ROOT hit with a 0.4s near-silence pocket, fades 18-20s
- Music: happy-beats-business-moves-vol-12-by-ende-dot-app.mp3
- Music treatment: volume 0.3, start 0s, dip under ROOT, fade-out last 2s; final bell rings over fade
- Music cue guidance: detect at composition via hyperframes beats; lock CVSS slam + ROOT reveal within ±0.15s of strong beats; kill-chain steps on consecutive beats ±0.10s; or unavailable
- Audio-reactive treatment: subtle; RMS swells cyan glow behind CVSS/ROOT cards only. No waveform/equalizer, no notes, no strobing.
- Audio-coupled moments:
  - Scene 1 hook slam — impactBell_heavy_000
  - Scene 2 CVE chip — card-place (sparse, one accent)
  - Scene 3 steps — card-slide-1 matched to each arrival
  - Scene 3 ROOT — impactBell_heavy_003 or _004, then silence pocket
  - Scene 4 CTA — impactBell_heavy_000, let ring
- SFX selection guidance: sparse cinematic restraint; card sounds for step reveals, deep bells for severity payoffs, restraint when the edit is busy
- SFX analysis guidance: C:\Users\HP\.agents\skills\brag\assets\sfx\sfx-analysis.md — prefer low/medium HF-risk files
- Exact SFX choice: Hyperframes should choose filenames, timestamps, density, and volume based on the implemented animation.
- Audio files: copy the chosen music and any Hyperframes-selected SFX into `C:\Users\HP\OneDrive\Documents\New folder\brag-output-dell-csm\composition/assets/`

## Hyperframes Instructions
Load the composition-building Hyperframes domain skills — `hyperframes-core` (composition contract + `data-*` timing), `hyperframes-animation` (motion), `hyperframes-creative` (design spec, beats, audio-reactive), `hyperframes-keyframes` (seek-safe keyframes), and `hyperframes-cli` (lint/check/render). /brag is its own workflow: do not enter the `hyperframes` entry-point intent interview and do not route into its generic promo / launch-video workflow. Prefer native Hyperframes conventions over anything in `/brag`.

Requirements:
- Show at least one real visual from the source project (the carousel slides).
- Keep all text readable in the final render.
- Keep the video within 15-25 seconds.
- Include the planned music/SFX layer unless audio was explicitly disabled or documented as intentionally silent.
- Treat `/brag` audio notes as guidance, not a fixed cue sheet. Choose SFX after the visual animation exists.
- Treat music cue metadata as optional timing hints. Hyperframes decides exact animation timing and should ignore cues that hurt readability, scene pacing, or the product story.
- Major reveals may move toward nearby strong cues within about 0.15s. Smaller entrances may align to nearby beat points within about 0.10s. Use only 1-3 strong cue locks in a 15-25s video unless the edit clearly benefits from more.
- Use SFX to support motion and interaction: card sounds for card-like reveals, short announcement cues for major payoffs, key/click sounds for text or user actions, and restraint when the edit is already busy.
- Honor planned music treatment such as fade-outs, ducking, beat-aligned reveals, or letting a final SFX ring over the music, using the best Hyperframes-supported implementation.
- When music is present and the treatment is not `none`, consider Hyperframes audio-reactive workflow: extract audio data and use RMS/frequency bands for subtle, brand-specific motion. Good targets are glow, depth, background warmth, card presence, title emphasis, or other existing visual elements. Avoid waveform/equalizer visuals, musical-note graphics, generic particle systems, strobing, or heavy pulsing.
- Use local assets for audio and any required runtime/media dependencies when possible.
- Run `hyperframes check` before render — it is brag's single gate.
- Keep creation and rendering local. Remote or publishing workflows require a separate explicit user request.
