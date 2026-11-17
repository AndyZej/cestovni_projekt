
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()

    page.goto("https://example.com")
    print("Titulek stránky:", page.title())

    browser.close()
