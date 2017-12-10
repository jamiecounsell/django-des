# -*- coding: utf-8 -*-
from django.test import TestCase, Client, override_settings
from smtplib import SMTPException
from django.contrib.auth.models import User
from django_des.models import DynamicEmailConfiguration
from mock.mock import patch
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        self.password = 'secret'
        self.admin= User.objects.create_superuser(
            'admin', 'example-email@website.com', self.password)
        self.client = Client()
        self.client.login(
            username = self.admin.username,
            password = self.password)
        self.configuration = DynamicEmailConfiguration()


    @patch('django_des.views.send_mail', return_value = 1)
    def test_send_test_email_send_mail_invoked(self, send_mail):
        url = reverse('django-des-test-email')
        email = 'testemail@website.com'
        response = self.client.post(url, {
            'email': email
        })

        self.assertTrue(send_mail.call_count)

    @override_settings(EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend')
    @patch('django_des.views.send_mail', return_value = 1)
    def test_send_test_email_returns_error_for_send_mail_exception(self, send_mail):
        send_mail.side_effect = SMTPException()
        url = reverse('django-des-test-email')
        email = 'testemail@website.com'
        response = self.client.post(url, {
            'email': email
        })
        self.assertIsNotNone(response.wsgi_request._messages)
        messages = list(response.wsgi_request._messages)
        self.assertTrue('messages' in response.cookies)
        self.assertEqual(len(messages), 1)
        self.assertIn('Could not send email', messages[0].message)

    @override_settings(EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend')
    def test_send_test_email_returns_error_for_no_email(self):
        url = reverse('django-des-test-email')
        response = self.client.post(url, {})
        self.assertIsNotNone(response.wsgi_request._messages)
        messages = list(response.wsgi_request._messages)
        self.assertTrue('messages' in response.cookies)
        self.assertEqual(len(messages), 1)
        self.assertIn('You must provide an email address', messages[0].message)

    @override_settings(EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend')
    @patch('django_des.views.send_mail', return_value = 1)
    def test_send_test_email_does_not_invoke_send_mail_for_empty_email(self, send_mail):
        send_mail.side_effect = SMTPException()
        url = reverse('django-des-test-email')
        self.client.post(url, {})
        self.assertEqual(send_mail.call_count, 0)
