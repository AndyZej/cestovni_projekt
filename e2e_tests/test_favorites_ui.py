

import os
from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:8000")


def run_favorites_test(page):
    page.goto(f"{BASE_URL}/oblibene/")
    if page.locator("button:has-text('Možnosti')").count() > 0:
        page.click("button:has-text('Možnosti')")
        checkboxes = page.locator(".sec-check")
        total = checkboxes.count()
        if total >= 5:
            for i in range(4):
                checkboxes.nth(i).check()
            assert page.locator("#selectedCount").inner_text().strip() == "4"
            assert checkboxes.nth(4).is_disabled() is True

            checkboxes.nth(0).uncheck()
            assert page.locator("#selectedCount").inner_text().strip() == "3"
            assert checkboxes.nth(4).is_disabled() is False


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        run_favorites_test(browser.new_page())
        browser.close()