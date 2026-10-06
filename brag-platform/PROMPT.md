# Platform-video hook — reusable prompt (brag + Hyperframes)

Turns a strategy/business document into a dense 20 s vertical platform intro —
the method behind `brag.mp4` (BuildForge platform: agency → platform shift,
pillar cards, money count-up, VERIFIED stamp, ticket stub).

## How to reuse

Attach the source document and say:

> Make a platform video following `brag-platform/PROMPT.md`.

Then answer the agent's 3 input questions (purpose, format, voice).

## Inputs the agent must ask for

1. **Purpose**: standalone platform explainer (default) OR promo driving traffic
   somewhere (ends on that CTA instead).
2. **Format**: vertical 1080×1920 (default) / landscape / square.
3. **Voiceover**: default OFF — music + SFX only. `--voice` = AI narration with
   music ducking (brag single-provider rule: Kokoro via Hyperframes).

## Method

1. **Source file**: save the document's video-usable facts as `SOURCE.md` —
   positioning line, pillars, numbers, workflow steps, CTA, contacts. Every
   on-screen claim must trace to it.
2. **Plan** (`brag-plan.md`): Hook (reframe/contrast moment, 3s) → Pillars
   (cards arriving on every-other-beat, 5s) → Proof (dark block: count-ups,
   workflow strip, stamp, ticket, 8s) → Outro CTA + contacts (4s). Total 15–25s.
   Hard rule from experience: NO dead holds — motion or sound in every second;
   the outro keeps living accents (breathing dot), never a frozen frame.
3. **Brief** (`composition-brief.md`): storyboard summary, visual identity
   (exact hex), audio map where EVERY sound lands on a visual event, SFX chosen
   after animation exists, 1–3 beat-locked majors via cue presets.
4. **Scaffold**: `npx hyperframes init composition`. Stage ONE music bed +
   a few SFX under `composition/assets/` (relative paths only).
5. **Author** `composition/index.html`: deterministic GSAP on one paused root
   timeline; count-ups via timeline-driven objects (scrub-safe); system font
   stacks (no external @font-face → lint-clean); no transform/GSAP conflicts;
   every `<audio>` needs an id; never tween `.clip` visibility.
6. **Gate**: `npx hyperframes check` must pass — fix every error including WCAG
   contrast (it gates as errors; each finding suggests a compliant color) and
   `content_overlap`. Then snapshots at scene midpoints, eyeball all frames.
7. **Render only on approval**: `--quality high`, poster = best settled frame
   baked as frame 0, `share-copy.txt` (1–3 postable sentences).

## Gotchas learned the hard way

- Purple-on-dark fails contrast: use lavender (#C4B5FD) for small accents on
  dark blocks; check tells you the exact ratio.
- Count-up numbers must fit their cards at final value (₹4,500 wider than ₹0).
- Sequential arrivals need ~1.1s spacing (every other beat at ~110 BPM) or text
  outruns reading.
- Verify the FILE (ffprobe + PNGs from the mp4), not just snapshots.
- A previous cut failed on a static 6 s hold + untimed SFX — density and cued
  sound are the method, not decoration.
