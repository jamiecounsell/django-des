# -*- coding: utf-8 -*-
from django.test import TestCase

from des.helpers import get_configuration_admin_url

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class HelpersTestCase(TestCase):

    def test_get_configuration_admin_url_returns_correct_url(self):
        url = get_configuration_admin_url()
        correct_url = reverse("admin:des_dynamicemailconfiguration_change")
        self.assertEqual(url, correct_url)
