

from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class ZpravyKomunitaTests(TestCase):
    """Testy pro zpravy, domovskou stránku zpráv a sekci komunita."""

    def setUp(self):
        self.client = Client()

    def test_zpravy_a_komunita_stranky_pokud_jsou_nastaveny(self):
        url_candidates = (
            "zpravy",
            "zpravy_domovsky",
            "komunita",
            "komunita_home",
            "seznam_zprav",
            "chat",
        )
        for url_name in url_candidates:
            with self.subTest(url_name=url_name):
                try:
                    url = reverse(url_name)
                except NoReverseMatch:
                    continue

                response = self.client.get(url)
                self.assertIn(response.status_code, (200, 302))