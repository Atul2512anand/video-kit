# Morph-loop video hook — reusable prompt

Use this file to spin up another morph-loop video like `morph.mp4` (one shape,
no cuts, UI states morphing on a measured beat grid, cursor-driven, seamless loop).

## How to reuse

Start a new chat, attach the new content source (PDF / site URL / brief), and say:

> Make a morph-loop video following `morph-loop/PROMPT.md`. Content truth = the
> attached source. Design/motion truth = this prompt.

Then answer the agent's 3 input questions (states, palette, track).

## Inputs the agent must ask for

1. **8–14 UI states** the shape turns into (default list below — confirm or edit).
2. **Palette**: pure black-and-white, or B&W + one accent color (recommend pulling
   the accent + bg + font from the content source).
3. **Track**: royalty-free ~120 BPM (Mixkit etc.). Agent downloads it and measures
   the TRUE BPM with numpy — never trust the nominal tempo.

## Default structure (adapt counts to the beat grid)

120-ish BPM, 12 bars (48 beats), action on every beat. Beat = ~0.49s.
Button → loader → check → dynamic island → music player (play/pause morph) →
scrub (drag) → volume slider (stretch past max) → toggle → trio tabs → case/study
tabs → self-drawing chart + tooltip → ⌘K (type to filter, ~2s per query) →
Enter → toast → back to button.

## Build (scripts live in `morph-loop/scripts/` — adapt hardcoded paths per project)

1. **Inspect** the content source. All on-screen copy must be verbatim lines from
   it. Note bg color, accent color, fonts.
2. **Beat analysis** (`beat_analysis.py`): ffmpeg-decode track to mono raw, build a
   log-energy onset envelope, autocorrelate for tempo, take the first strong
   transient as downbeat, snap each beat to its local onset peak. Write
   `beatgrid.json`. Set bars × beats × period = duration D.
3. **Write `index.html`** (1440×1440, local `@font-face` only):
   - Every style computed from time inside `seek(t)`. No CSS transitions, timers,
     or carried state. Expose `window.seek`, `window.DUR`, `?t=` preview + spacebar.
   - Closed-form damped-spring step responses; one spring per target change
     (superposition). Slight overshoot only (z≈0.7).
   - Tab-indicator/toggle-knob leading + trailing edges on separate springs.
   - Drags read the value from the cursor position while held.
   - Tab labels turn white ONLY where the pill rect covers the label center —
     never white-on-light.
   - Text swaps get separate enter/exit timing + blur. Final frame identical to
     first (cursor static, scale 1.0) or the loop stutters.
   - Camera zooms per state; no `will-change` on scaled nodes.
4. **Beat frames first**: screenshot one frame per beat, tile a contact sheet,
   fix anything off-grid, cramped, or unreadable. Never skip this.
5. **Full render**: Playwright screenshots at 60fps × 4 subframes, numpy-average
   each group (see `render_frames.py` + `blend_pipe.py` — the in-Python blend is
   far faster than an ffmpeg tmix graph), pipe rawvideo to x264.
6. **Audio**: slice the track at [downbeat, downbeat+D], synth UI clicks on the
   measured peaks (`make_clicks.py`), amix under the bed.
7. **Verify the FILE, not just frames**: ffprobe streams/duration, first-vs-last
   frame diff (~0.1/255 = seamless), and eyeball 2–3 PNGs pulled from the mp4.

## Gotchas learned the hard way

- PowerShell: `Remove-Item -LiteralPath '...\*.jpg'` does NOT glob — pipe
  `Get-ChildItem -Filter` into `Remove-Item`, and always re-check the count.
- Launch long ffmpeg/python jobs detached (`Start-Process`) and poll; keep
  everything resumable (render script skips existing subframes).
- `Start-Process` mangles spaces/quotes: pre-quote paths, avoid spaces inside
  filter args, prefer `-nostdin`, never rely on single quotes to protect spaces.
- Python `python3 -c` breaks under PowerShell quoting — put helpers in script
  files and run them.
- Gyan ffmpeg builds here lack glob input and `-vsync` (use `-fps_mode passthrough`).
- Deterministic pipelines re-encode byte-identical output — if a re-render looks
  unchanged, suspect stale subframes before suspecting the code.
