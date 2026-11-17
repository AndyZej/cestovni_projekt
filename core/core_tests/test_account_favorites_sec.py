


from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings
from django.urls import NoReverseMatch, reverse

from core.models import UzivatelskaObdobnaCast

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

    def _reverse_first(self, candidates):
        for candidate in candidates:
            try:
                return reverse(candidate)
            except NoReverseMatch:
                continue
        return None

    def _get_favorites_url(self):
        candidates = (
            "upravit_oblibene",
            "dashboard_uctu:upravit_oblibene",
            "oblibene_sekce",
            "moje_oblibene",
            "oblibene",
            "oblibene_casti",
        )
        url = self._reverse_first(candidates)
        if url:
            return url
        self.skipTest(
            "Nenalezen žádný očekávaný název URL pro oblíbené sekce "
            f"({', '.join(repr(c) for c in candidates)})."
        )

    def _get_login_url(self):
        url = self._reverse_first(("login", "account_login", "auth:login"))
        if url:
            return url
        self.skipTest("URL pro přihlášení ('login') není v projektu nalezeno.")

    def _get_home_url(self):
        url = self._reverse_first(("domovsky", "domov", "home", "index"))
        if url:
            return url
        self.skipTest("Domovská URL ('domovsky' / 'domov') není v projektu nalezena.")

    def _saved_keys_for_user(self, user):
        return list(
            UzivatelskaObdobnaCast.objects.filter(uzivatel=user)
            .order_by("poradi")
            .values_list("url_name", flat=True)
        )

    def test_protected_pages_redirect_anonymous_user_to_login(self):
        favorites_url = self._get_favorites_url()
        login_url = self._get_login_url()
        urls_to_check = [favorites_url]

        dashboard_url = self._reverse_first(
            ("dashboard_uctu", "dashboard_uctu:dashboard_uctu")
        )
        if dashboard_url:
            urls_to_check.append(dashboard_url)

        for url in urls_to_check:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertIn(login_url, response.url)

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

        saved_many = self._saved_keys_for_user(self.user_a)
        self.assertLessEqual(len(saved_many), 4)
        self.assertEqual(
            saved_many,
            ["egypt_detail", "egypt_galerie", "kapverdy_detail", "tunisko_detail"],
        )

        if response_many.context and "vybrane_klice" in response_many.context:
            self.assertLessEqual(len(response_many.context["vybrane_klice"]), 4)

        # Prázdný POST smaže uložené položky uživatele
        response_empty = self.client.post(url, data={})
        self.assertIn(response_empty.status_code, (200, 302))
        self.assertEqual(self._saved_keys_for_user(self.user_a), [])

        # Neplatný klíč se neuloží
        response_invalid = self.client.post(
            url, data={"oblibene_sekce": ["neexistujici_sekce_xyz"]}
        )
        self.assertIn(response_invalid.status_code, (200, 302))
        self.assertNotIn(
            "neexistujici_sekce_xyz", self._saved_keys_for_user(self.user_a)
        )

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

        saved_b = self._saved_keys_for_user(self.user_b)
        self.assertNotIn("egypt_detail", saved_b)
        self.assertNotIn("kapverdy_detail", saved_b)

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
        home_url = self._get_home_url()
        response = self.client.get(home_url, data={"q": payload})
        self.assertNotIn(payload, response.content.decode("utf-8"))

    @override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver", "localhost"])
    def test_domovsky_query_count_and_production_debug_false(self):
        home_url = self._get_home_url()
        with self.assertNumQueries(0):
            response = self.client.get(home_url)
        self.assertEqual(response.status_code, 200)

    def test_chat_admin_page_access(self):
        url = self._reverse_first(("chat_admin",))
        if not url:
            self.skipTest("URL 'chat_admin' není v projektu definováno.")
        response = self.client.get(url)
        self.assertIn(response.status_code, (200, 302, 403))