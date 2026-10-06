import numpy as np, json

SR = 22050
x = np.fromfile(r"C:\Users\HP\AppData\Local\Temp\opencode\track.raw", dtype=np.float32)

HOP = 256
hop_t = HOP / SR
n = (len(x) - 2048) // HOP
frames = np.lib.stride_tricks.as_strided(
    x[: n * HOP + 2048], shape=(n, 2048), strides=(x.strides[0] * HOP, x.strides[0]))
energy = np.log1p((frames ** 2).sum(axis=1))
novelty = np.maximum(0, np.diff(energy, prepend=energy[0]))

# tempo from first 30s (proven method)
seg = novelty[: int(30 / hop_t)]
ac = np.correlate(seg - seg.mean(), seg - seg.mean(), mode="full")[len(seg) - 1:]
lag_min, lag_max = int(round(60 / 180 / hop_t)), int(round(60 / 80 / hop_t))
lags = np.arange(lag_min, lag_max)
bpm_lags = 60 / (lags * hop_t)
weight = np.exp(-0.5 * ((bpm_lags - 120) / 6) ** 2)
best = lag_min + int(np.argmax(ac[lag_min:lag_max] * weight))
period = best * hop_t
print(f"tempo: {60/period:.2f} BPM period {period:.4f}s")

thr = np.percentile(novelty, 99.2)
cands = np.where(novelty > thr)[0]
cands = cands[cands * hop_t > 0.15]
downbeat = cands[0] * hop_t

beats = []
for i in range(48):
    t = downbeat + i * period
    c = int(round(t / hop_t))
    lo, hi = max(0, c - 5), min(n - 1, c + 5)
    pk = lo + int(np.argmax(novelty[lo:hi + 1]))
    beats.append(round(pk * hop_t, 4))
beats = np.array(beats)
gaps = np.diff(beats)
print(f"window {beats[0]:.3f} -> {beats[-1]:.3f} span {beats[-1]-beats[0]:.3f}s")
print(f"median gap {np.median(gaps):.4f}s max gap {gaps.max():.4f}s")
print("video beats (t - downbeat):", [round(float(b) - downbeat, 4) for b in beats])

out = {"bpm": round(float(60 / period), 2), "period": round(float(period), 4),
       "downbeat": round(float(downbeat), 4),
       "beats": [round(float(b) - downbeat, 4) for b in beats],
       "track": "Tech House Vibes - Alejandro Magana (Mixkit, royalty-free)"}
open(r"C:\Users\HP\OneDrive\Documents\New folder\morph-loop\beatgrid.json", "w").write(json.dumps(out, indent=1))
print("wrote beatgrid.json")
