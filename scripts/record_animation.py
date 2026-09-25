import sys, os
from playwright.sync_api import sync_playwright

html_path = sys.argv[1]
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir=out_dir,
        record_video_size={"width": 1920, "height": 1080},
    )
    page = context.new_page()
    page.goto(f"file://{html_path}")
    page.wait_for_timeout(13500)  # cover full two-scene animation incl. final hold
    context.close()  # finalizes the video file
    browser.close()

# find the produced webm
for f in os.listdir(out_dir):
    if f.endswith(".webm"):
        print(os.path.join(out_dir, f))
