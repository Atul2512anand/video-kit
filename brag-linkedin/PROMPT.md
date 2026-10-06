# LinkedIn-post-to-video hook — reusable prompt

Turns a generated LinkedIn post (text + carousel slides) into a short cinematic
vertical explainer with brag + Hyperframes, like `brag.mp4` here (Dell CSM,
20s, 1080×1920, music + SFX, no voice).

## How to reuse

Start a new chat, attach the post draft (`.md`) and its carousel slide PNGs (or
point at `content automation/drafts/`), and say:

> Make a LinkedIn-post video following `brag-output-dell-csm/PROMPT.md`.

Then answer the agent's 3 input questions (purpose, format, voice).

## Inputs the agent must ask for

1. **Purpose**: standalone explainer OR promo driving traffic to the LinkedIn post
   (promo ends on the post CTA instead of the incident lesson).
2. **Format**: vertical 1080×1920 (Reels/Shorts, default) / landscape / square.
3. **Voiceover**: default OFF — music + SFX only. `--voice` = AI narration with
   music ducking (brag single-provider rule: Kokoro via Hyperframes).

## Method (brag workflow, adapted for news explainers)

1. **Inspect**: read the post `.md` for verbatim copy (hook, CVE/numbers, kill
   chain or takeaways, CTA, handle, source line) and 1–2 slide PNGs for the
   visual identity (bg, accent, masthead style). Record exact hex colors.
2. **Plan** (`brag-plan.md`): Hook (severity/number slam, 3s) → Reveal (what +
   where, 4s) → 3 sequential proof steps on beats (9s) → Outro CTA + masthead
   + source (4s). Total 15–25s. Copy must be verbatim from the post.
3. **Brief** (`composition-brief.md`): storyboard summary, visual identity,
   audio role (cinematic bed + sparse deep bells + card sounds), SFX placement
   rules, Hyperframes handoff (no intent interview — /brag owns the brief).
4. **Scaffold**: `npx hyperframes init <out>/composition --non-interactive`.
   Stage under `composition/assets/`: post slides (`slides/`), ONE music bed
   (`music/`), a few SFX (`sfx/impact|casino|interface/`). Relative paths only.
5. **Animate the incident, not just text.** Kinetic type alone gets rejected —
   every video needs topic diagrams drawn as SVG + GSAP on the paused root
   timeline: gauges/counters, architecture with flowing traffic, breaking locks,
   typing terminals, infecting nodes, drawing shields. Deterministic only (no
   clocks/random/network); measure SVG path lengths at runtime for draws.
6. **Gate**: `npx hyperframes check` must pass (fix every error incl. WCAG
   contrast and `content_overlap`). Then `snapshot --at <scene midpoints>`,
   eyeball every frame, fix cramped/overflowing scenes.
7. **Render only after user says render**: `--quality high --output ../brag.mp4`.
   Poster = best settled frame via ffmpeg, baked as frame 0 (overlay trick).
   Write `share-copy.txt` (1–3 sentences, postable as-is).

## Gotchas learned the hard way

- Carousel PNGs are 1080×1350: `object-fit: cover` ghosted behind type, or
  fitted cards — never stretched.
- Ghosted slide text behind foreground type is texture, not content: keep ghost
  opacity ≤ 0.2 so it never competes (contrast gate only checks real text).
- Beat-lock 1–3 major reveals (`hyperframes beats` or strong-cue presets);
  sequential steps snap to consecutive beats; readability floor always wins.
- Danger red (#FF3B5C) is allowed ONLY for breach/compromise accents on top of
  the post's own palette — never as a theme color.
- `transformOrigin` in px misbehaves on SVG — use `svgOrigin`. Duplicate
  fromTo targets and repeated fromTo need `immediateRender: false` or a `tl.set`
  baseline. Never tween `.clip` visibility directly.
- Verify the FILE (ffprobe + PNGs pulled from the mp4), not just snapshots.
