

from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class NavigationAndBaseTemplateTests(TestCase):
    """A. Základní struktura, motivy a navigace."""

    def setUp(self):
        self.client = Client()

    def test_domovsky_and_menu_urls_resolve_and_return_200(self):
        for url_name in ("domovsky", "menu"):
            with self.subTest(url_name=url_name):
                try:
                    url = reverse(url_name)
                except NoReverseMatch as exc:
                    self.fail(f"Chybí URL '{url_name}' v urls.py: {exc}")

                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_base_theme_switcher_and_panels_present(self):
        response = self.client.get(reverse("domovsky"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="theme-selector"')
        self.assertContains(response, 'id="bubble-canvas"')
        for theme_class in (
            "theme-forest",
            "theme-gold",
            "theme-laguna",
            "theme-lavender",
            "theme-sunset",
            "theme-scandi",
            "theme-snow",
            "theme-coral",
            "theme-mocha",
            "theme-dark",
        ):
            self.assertContains(response, theme_class)