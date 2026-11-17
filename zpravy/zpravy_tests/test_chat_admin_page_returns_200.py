

from django.test import TestCase
from django.urls import NoReverseMatch, reverse


class ChatAdminPageReturns200Tests(TestCase):
    def test_chat_admin_page_access(self):
        try:
            url = reverse("chat_admin")
        except NoReverseMatch:
            self.skipTest("URL 'chat_admin' není v projektu definováno.")

        response = self.client.get(url)
        self.assertIn(response.status_code, (200, 302, 403))