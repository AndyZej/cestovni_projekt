


from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings
from django.urls import NoReverseMatch, reverse

User = get_user_model()


class AccountFavoritesAndSecurityTests(TestCase):
    """D., E., F. & G. Komunita/podpora, účet, oblíbené sekce, bezpečnost a výkon."""

    def setUp(self):
        self.client = Client()
        self.password = "TajneHeslo123!"
        self.user_a = User.objects.create_user(
            username="uzivatel_a",
            password=self.password,
        )
        self.user_b = User.objects.create_user(
            username="uzivatel_b",
            password=self.password,
        )

    def _get_favorites_url(self):
        for candidate in ("oblibene_sekce", "moje_oblibene", "oblibene"):
            try:
                return reverse(candidate)
            except NoReverseMatch:
                continue
        self.fail(
            "Nenalezen žádný očekávaný název URL pro oblíbené sekce "
            "('oblibene_sekce', 'moje_oblibene', 'oblibene')."
        )

    def test_protected_pages_redirect_anonymous_user_to_login(self):
        favorites_url = self._get_favorites_url()
        urls_to_check = [favorites_url]
        try:
            urls_to_check.append(reverse("dashboard_uctu"))
        except NoReverseMatch:
            pass

        for url in urls_to_check:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertIn(reverse("login"), response.url)

    def test_favorites_page_renders_and_hides_top_corner_panels(self):
        self.client.force_login(self.user_a)
        url = self._get_favorites_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Moje 4 oblíbené části")
        self.assertContains(response, ".top-left")
        self.assertContains(response, ".top-right")
        self.assertContains(response, "display: none")

    def test_favorites_post_enforces_max_4_items_and_handles_empty_or_invalid(self):
        self.client.force_login(self.user_a)
        url = self._get_favorites_url()

        many_keys = [
            "egypt_detail",
            "egypt_galerie",
            "kapverdy_detail",
            "tunisko_detail",
            "turecko_detail",
        ]
        response_many = self.client.post(url, data={"oblibene_sekce": many_keys})
        self.assertIn(response_many.status_code, (200, 302))

        if response_many.context and "vybrane_klice" in response_many.context:
            self.assertLessEqual(len(response_many.context["vybrane_klice"]), 4)

        response_empty = self.client.post(url, data={})
        self.assertIn(response_empty.status_code, (200, 302))

        response_invalid = self.client.post(
            url, data={"oblibene_sekce": ["neexistujici_sekce_xyz"]}
        )
        self.assertIn(response_invalid.status_code, (200, 302))

    def test_favorites_are_isolated_between_users(self):
        url = self._get_favorites_url()

        self.client.force_login(self.user_a)
        self.client.post(
            url,
            data={"oblibene_sekce": ["egypt_detail", "kapverdy_detail"]},
            follow=True,
        )

        self.client.force_login(self.user_b)
        response_b = self.client.get(url)
        self.assertEqual(response_b.status_code, 200)
        if response_b.context and "vybrane_klice" in response_b.context:
            self.assertNotIn("egypt_detail", response_b.context["vybrane_klice"])
            self.assertNotIn("kapverdy_detail", response_b.context["vybrane_klice"])

    def test_csrf_enforced_on_post_without_token(self):
        url = self._get_favorites_url()
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.user_a)
        response = csrf_client.post(url, data={"oblibene_sekce": ["egypt_detail"]})
        self.assertEqual(response.status_code, 403)

    def test_xss_payload_is_escaped_in_response(self):
        payload = "<script>alert('xss')</script>"
        response = self.client.get(reverse("domovsky"), data={"q": payload})
        self.assertNotIn(payload, response.content.decode("utf-8"))

    @override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver", "localhost"])
    def test_domovsky_query_count_and_production_debug_false(self):
        with self.assertNumQueries(5):
            response = self.client.get(reverse("domovsky"))
        self.assertEqual(response.status_code, 200)

    def test_chat_admin_page_returns_200(self):
        try:
            url = reverse("chat_admin")
        except NoReverseMatch:
            self.skipTest("URL 'chat_admin' není v projektu definováno.")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)