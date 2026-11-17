

from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class ZemeItinerarTests(TestCase):
    """Testy pro sekci itinerářů a jejich galerií."""

    def setUp(self):
        self.client = Client()
        self.destinations = ("egypt", "kapverdy", "tunisko", "turecko")

    def test_seznam_itinerar_returns_200_if_configured(self):
        for url_name in ("seznam_itinerar", "seznam_itineraru"):
            try:
                url = reverse(url_name)
                break
            except NoReverseMatch:
                continue
        else:
            self.skipTest("URL pro seznam itinerářů není definováno.")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_itinerar_and_itinerar_gallery_pages_if_configured(self):
        for slug in self.destinations:
            for suffix in ("itinerar", "itinerar_galerie"):
                url_name = f"{slug}_{suffix}"
                with self.subTest(url_name=url_name):
                    try:
                        url = reverse(url_name)
                    except NoReverseMatch:
                        continue

                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)