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

    def test_backend_honors_configured_host(self):
        host = 'testhost.mysite.com'
        self.configuration.host = host
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.host, host)

    def test_backend_honors_configured_port(self):
        port = 123
        self.configuration.port = port
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.port, port)

    def test_backend_honors_configured_username(self):
        username = 'awesomeuser'
        self.configuration.username = username
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.username, username)

    def test_backend_honors_configured_password(self):
        password = 'secret'
        self.configuration.password = password
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.password, password)
