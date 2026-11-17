


import os
from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:8000")


def run_theme_test(page):
    page.goto(f"{BASE_URL}/")
    page.select_option("#theme-selector", "theme-gold")
    assert "theme-gold" in (page.get_attribute("body", "class") or "")
    page.reload()
    assert page.evaluate("localStorage.getItem('selectedTheme')") == "theme-gold"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        run_theme_test(browser.new_page())
        browser.close()