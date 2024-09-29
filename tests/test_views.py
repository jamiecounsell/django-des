# -*- coding: utf-8 -*-
from smtplib import SMTPException

from django.contrib.auth.models import User
from django.test import Client, TestCase, override_settings
from mock.mock import patch

from des.models import DynamicEmailConfiguration

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        self.password = "secret"
        self.admin = User.objects.create_superuser(
            "admin", "example-email@website.com", self.password
        )
        self.non_admin = User.objects.create_user(
            "notadmin", "example-email@anotherwebsite.com", self.password
        )
        self.client = Client()
        self.client.login(username=self.admin.username, password=self.password)
        self.configuration = DynamicEmailConfiguration()

    @patch("des.views.send_mail", return_value=1)
    def test_send_test_email_send_mail_invoked(self, send_mail):
        url = reverse("des-test-email")
        email = "testemail@website.com"
        response = self.client.post(url, {"email": email})

        self.assertTrue(send_mail.call_count)

    @patch("des.views.send_mail", return_value=1)
    def test_send_test_email_send_mail_not_invoked_for_non_admin(self, send_mail):
        self.client.logout()
        self.client.login(username=self.non_admin.username, password=self.password)
        url = reverse("des-test-email")
        email = "testemail@website.com"
        response = self.client.post(url, {"email": email})

    @patch("des.views.send_mail", return_value=1)
    def test_send_test_email_hides_endpoint_for_non_admin(self, send_mail):
        self.client.logout()
        self.client.login(username=self.non_admin.username, password=self.password)
        url = reverse("des-test-email")
        email = "testemail@website.com"
        response = self.client.post(url, {"email": email})

        self.assertEqual(response.status_code, 404)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    @patch("des.views.send_mail", return_value=1)
    def test_send_test_email_returns_error_for_send_mail_exception(self, send_mail):
        send_mail.side_effect = SMTPException()
        url = reverse("des-test-email")
        email = "testemail@website.com"
        response = self.client.post(url, {"email": email})
        self.assertIsNotNone(response.wsgi_request._messages)
        messages = list(response.wsgi_request._messages)
        self.assertTrue("messages" in response.cookies)
        self.assertEqual(len(messages), 1)
        self.assertIn("Could not send email", messages[0].message)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    def test_send_test_email_returns_error_for_no_email(self):
        url = reverse("des-test-email")
        response = self.client.post(url, {})
        self.assertIsNotNone(response.wsgi_request._messages)
        messages = list(response.wsgi_request._messages)
        self.assertTrue("messages" in response.cookies)
        self.assertEqual(len(messages), 1)
        self.assertIn("You must provide an email address", messages[0].message)

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.dummy.EmailBackend")
    @patch("des.views.send_mail", return_value=1)
    def test_send_test_email_does_not_invoke_send_mail_for_empty_email(self, send_mail):
        send_mail.side_effect = SMTPException()
        url = reverse("des-test-email")
        self.client.post(url, {})
        self.assertEqual(send_mail.call_count, 0)
