import sys
from playwright.sync_api import sync_playwright

html_path = sys.argv[1]
png_path = sys.argv[2]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": 1200, "height": 1500})
    page.goto(f"file://{html_path}")
    page.wait_for_timeout(300)  # let webfonts settle
    page.screenshot(path=png_path)
    browser.close()

print(f"Saved {png_path}")
