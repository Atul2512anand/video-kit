import numpy as np

SR = 44100
D = 23.4048
N = int(D * SR)
mix = np.zeros(N, dtype=np.float64)

def blip(t0, f=2500, dur=0.045, gain=0.5):
    i0 = int(t0 * SR)
    n = int(dur * SR)
    if i0 + n >= N:
        return
    env = np.exp(-np.arange(n) / (n / 4))
    tone = np.sin(2 * np.pi * f * np.arange(n) / SR) * env * gain
    tone += (np.random.default_rng(int(t0 * 1000)).standard_normal(n) *
             np.exp(-np.arange(n) / (n / 8)) * gain * 0.35)
    mix[i0:i0 + n] += tone

# strong clicks on cursor clicks (measured beats)
for t in (0.4992, 4.435, 7.3723, 21.3):
    blip(t, 2400, 0.05, 0.55)
# medium blips: scrub grab/release, volume grab/release, query starts
for t in (4.9226, 6.06, 6.1, 6.6, 12.6781, 14.6518, 16.6023, 18.4715, 20.538):
    blip(t, 3200, 0.035, 0.32)
# soft ticks on state-boundary beats
for t in (0.9868, 1.9621, 2.8676, 3.9358, 5.9095, 6.8731, 7.7555,
          9.2067, 10.7857, 12.6781, 20.538, 21.4668, 22.384):
    blip(t, 4200, 0.022, 0.16)

mix = mix / max(1.0, np.abs(mix).max())
stereo = np.stack([mix, mix], axis=1)
(stereo * 32767).astype(np.int16).tofile(
    r"C:\Users\HP\AppData\Local\Temp\opencode\clicks.raw")
print("clicks written, peak:", round(float(np.abs(mix).max()), 3))
