# Video Kit — clone, open in opencode, start generating videos

Two proven pipelines for turning content (PDFs, sites, LinkedIn posts) into
finished motion videos. Both were built and battle-tested in this repo's history:
a 23 s seamless UI-morph loop and a 20 s cinematic security explainer.

## 1 · Setup (once per machine)

```bash
pip install -r requirements.txt
python3 -m playwright install chromium
# node 22+, ffmpeg on PATH
npx skills add https://github.com/latent-spaces/brag --skill brag -g -y
npx hyperframes skills update product-launch-video
```

`opencode.json` pins the model this kit was built with
(`openrouter/openrouter/free`) — opencode picks it up automatically, so anyone
cloning gets the same model.

## 2 · Pick a pipeline

### A. Morph-loop (single-shape UI motion, beat-synced, seamless loop)

`morph-loop/` — content truth = your PDF/site, design truth = `PROMPT.md`.

1. Read `morph-loop/PROMPT.md` and follow it (it asks you 3 input questions).
2. Reference implementation: `morph-loop/index.html` (48-beat BuildForge loop).
   Scripts: `scripts/beat_analysis.py` (true BPM via numpy), `render_frames.py`
   (Playwright subframes), `blend_pipe.py` (numpy motion-blur blend → x264),
   `make_clicks.py` (UI sounds on measured peaks).
3. You supply per video: content source, track MP3 (~120 BPM, Mixkit-type
   royalty-free), output folder. Everything generated (mp4/jpg/wav/subs) is
   git-ignored by design.

### B. Brag + Hyperframes (cinematic promo/explainer, 15–25 s)

`brag-linkedin/` — content truth = post draft + carousel PNGs, method in `PROMPT.md`.

1. Read `brag-linkedin/PROMPT.md` (asks purpose / format / voice).
2. Write `brag-plan.md` + `composition-brief.md` (examples alongside as
   `*.example.md`), scaffold with `npx hyperframes init composition`,
   stage music + SFX under `composition/assets/`, author `composition/index.html`.
3. Gate: `npx hyperframes check` must pass → snapshots → render only on approval
   → poster baked as frame 0 → `share-copy.txt`.
4. Reference: `composition/index.html` is the shipped Dell CSM explainer.

## Rules both pipelines share

- All on-screen copy verbatim from the source. No invented claims/numbers.
- Verify the FILE (ffprobe + PNGs pulled from the mp4), never just previews.
- Render only after explicit approval. Keep creation local.
