

import os
from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:8000")


def run_gallery_lightbox_test(page):
    cards_with_images = page.locator(".gallery-card[data-images]")
    if cards_with_images.count() > 0:
        cards_with_images.first.click()
        lightbox = page.locator("#lightbox")
        assert lightbox.is_visible()
        page.keyboard.press("Escape")
        assert not lightbox.is_visible()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        run_gallery_lightbox_test(browser.new_page())
        browser.close()