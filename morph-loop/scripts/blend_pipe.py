import subprocess, numpy as np, sys
from PIL import Image

ROOT = r"C:\Users\HP\OneDrive\Documents\New folder\morph-loop"
NFR, W, H = int(sys.argv[1]) if len(sys.argv) > 1 else 819, 1440, 1440
D = NFR / 60

ff = [
    "ffmpeg", "-y", "-nostdin", "-v", "info",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
    "-framerate", "60", "-i", "-",
    "-ss", "2.4265", "-t", f"{D:.4f}", "-i", ROOT + r"\track.mp3",
    "-i", ROOT + r"\clicks.wav",
    "-filter_complex",
    "[1:a]volume=0.8[m];[2:a]volume=0.5[c];[m][c]amix=inputs=2:duration=shortest[a]",
    "-map", "0:v", "-map", "[a]",
    "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
    "-movflags", "+faststart", ROOT + r"\morph.mp4",
]
proc = subprocess.Popen(ff, stdin=subprocess.PIPE,
                        stdout=open(ROOT + r"\mux.log", "w"),
                        stderr=subprocess.STDOUT)
try:
    for f in range(NFR):
        acc = None
        for k in range(4):
            im = np.asarray(Image.open(
                f"{ROOT}\\subs\\sub_{f * 4 + k:05d}.jpg").convert("RGB"),
                dtype=np.float32)
            acc = im if acc is None else acc + im
        proc.stdin.write((acc / 4).astype(np.uint8).tobytes())
        if f % 100 == 0:
            print(f"frame {f}/{NFR}", flush=True)
    proc.stdin.close()
    rc = proc.wait()
    print("ffmpeg exit:", rc, flush=True)
except BrokenPipeError:
    print("ffmpeg died early, exit:", proc.wait(), flush=True)
