

from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class DestinationsAndItinerariesTests(TestCase):
    """B. & C. Země, itineráře, fotogalerie a spodní navigace."""

    def setUp(self):
        self.client = Client()
        self.destinations = ("egypt", "kapverdy", "tunisko", "turecko")

    def test_seznam_zemi_and_seznam_itineraru_return_200(self):
        for url_name in ("seznam_zemi", "seznam_itineraru"):
            with self.subTest(url_name=url_name):
                try:
                    url = reverse(url_name)
                except NoReverseMatch:
                    self.skipTest(f"URL '{url_name}' není v projektu definováno.")
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_destination_details_and_galleries_if_configured(self):
        for slug in self.destinations:
            for suffix in ("detail", "galerie", "itinerar", "itinerar_galerie"):
                url_name = f"{slug}_{suffix}"
                with self.subTest(url_name=url_name):
                    try:
                        url = reverse(url_name)
                    except NoReverseMatch:
                        continue
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)
                    self.assertContains(response, reverse("domovsky"))
                    self.assertContains(response, reverse("menu"))