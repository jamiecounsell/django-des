# -*- coding: utf-8 -*-
from django.test import TestCase
from django_des.models import DynamicEmailConfiguration
from django_des.backends import ConfiguredEmailBackend
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class ConfiguredEmailBackendTestCase(TestCase):

    def setUp(self):
        self.configuration = DynamicEmailConfiguration()
        self.backend = ConfiguredEmailBackend()
