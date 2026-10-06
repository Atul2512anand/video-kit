import os, sys
from playwright.sync_api import sync_playwright

ROOT = r"C:\Users\HP\OneDrive\Documents\New folder\morph-loop"
D = 13.6528
FPS, SUB = 60, 4
NFR = int(sys.argv[3]) if len(sys.argv) > 3 else 819  # 819
os.makedirs(ROOT + r"\subs", exist_ok=True)

a0, a1 = int(sys.argv[1]), int(sys.argv[2])
print(f"frames {a0}..{a1} of {NFR}", flush=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1440, "height": 1440})
    pg.goto("file:///" + ROOT.replace("\\", "/") + "/index.html?t=0")
    pg.wait_for_timeout(1500)
    el = pg.locator("#frame")
    for f in range(a0, min(a1, NFR)):
        base = f / FPS
        for k in range(SUB):
            idx = f * SUB + k
            path = f"{ROOT}\\subs\\sub_{idx:05d}.jpg"
            if os.path.exists(path):
                continue
            pg.evaluate(f"seek({base + k / (FPS * SUB):.5f})")
            el.screenshot(path=path, type="jpeg", quality=88)
        if (f - a0) % 25 == 0:
            print(f"  frame {f}", flush=True)
    b.close()
print("chunk done", flush=True)
