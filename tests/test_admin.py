# -*- coding: utf-8 -*-
from __future__ import print_function

from django.contrib.auth.models import User
from django.test import Client, TestCase
from des.helpers import get_configuration_admin_url


class AdminTestCase(TestCase):

    def setUp(self):
        self.password = 'secret'
        self.admin= User.objects.create_superuser(
            'admin', 'example-email@website.com', self.password)
        self.client = Client()

    def test_custom_form_displays(self):
        url = get_configuration_admin_url()
        self.client.login(
            username = self.admin.username,
            password = self.password)
        response = self.client.get(url)
        self.assertIn('des--test-button', str(response.content))
