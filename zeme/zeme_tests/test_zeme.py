

from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse


class ZemeZemeTests(TestCase):
    """Testy pro sekci zemí, detailů a jejich galerií."""

    def setUp(self):
        self.client = Client()
        self.destinations = ("egypt", "kapverdy", "tunisko", "turecko")

    def test_seznam_zemi_returns_200_if_configured(self):
        try:
            url = reverse("seznam_zemi")
        except NoReverseMatch:
            self.skipTest("URL 'seznam_zemi' není definováno.")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_zeme_detail_and_gallery_pages_if_configured(self):
        for slug in self.destinations:
            for suffix in ("detail", "galerie"):
                url_name = f"{slug}_{suffix}"
                with self.subTest(url_name=url_name):
                    try:
                        url = reverse(url_name)
                    except NoReverseMatch:
                        continue

                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)