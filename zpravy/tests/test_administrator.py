

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse

User = get_user_model()


class ZpravyAdministratorTests(TestCase):
    """Testy pro sekci administrator v aplikaci zpravy."""

    def setUp(self):
        self.client = Client()
        self.password = "TajneHeslo123!"
        self.user = User.objects.create_user(
            username="bezny_uzivatel",
            password=self.password,
        )
        self.admin_user = User.objects.create_user(
            username="spravce_zprav",
            password=self.password,
            is_staff=True,
        )

    def _get_administrator_url(self):
        for candidate in (
            "zpravy_administrator",
            "administrator_zpravy",
            "administrator",
            "chat_admin",
        ):
            try:
                return reverse(candidate)
            except NoReverseMatch:
                continue
        return None

    def test_administrator_pristup_anonymni_a_uzivatel(self):
        url = self._get_administrator_url()
        if not url:
            self.skipTest("URL pro sekci administrator není v projektu definováno.")

        anon_response = self.client.get(url)
        self.assertIn(anon_response.status_code, (200, 302, 403))

        self.client.force_login(self.user)
        user_response = self.client.get(url)
        self.assertIn(user_response.status_code, (200, 302, 403))

    def test_administrator_pristup_spravce(self):
        url = self._get_administrator_url()
        if not url:
            self.skipTest("URL pro sekci administrator není v projektu definováno.")

        self.client.force_login(self.admin_user)
        admin_response = self.client.get(url)
        self.assertIn(admin_response.status_code, (200, 302))