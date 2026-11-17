

from playwright.sync_api import sync_playwright

from .test_favorites_ui import run_favorites_test
from .test_gallery_lightbox import run_gallery_lightbox_test
from .test_theme_switcher import run_theme_test


def run_all_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run_theme_test(page)
        run_favorites_test(page)
        run_gallery_lightbox_test(page)
        browser.close()
    print("Všechny E2E UI sekce proběhly úspěšně.")


__all__ = [
    "run_theme_test",
    "run_favorites_test",
    "run_gallery_lightbox_test",
    "run_all_e2e",
]