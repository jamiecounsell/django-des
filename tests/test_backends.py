# -*- coding: utf-8 -*-
import traceback
from django.test import TestCase, override_settings
from des.models import DynamicEmailConfiguration
from des.backends import ConfiguredEmailBackend
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class ConfiguredEmailBackendDynamicSettingsTestCase(TestCase):

    def setUp(self):
        self.configuration = DynamicEmailConfiguration()

    def test_backend_does_not_permit_mutex_tls_and_ssl(self):
        try:
            ConfiguredEmailBackend(
                use_tls = True,
                use_ssl = True
            )
            self.fail("No exception thrown. Expected ValueError")
        except ValueError:
            pass  # Test succeeded
        except Exception:
            self.fail("Incorrect exception thrown: {}".format(
                traceback.format_exc()
            ))

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

    def test_backend_honors_configured_use_tls_true(self):
        use_tls = True
        self.configuration.use_tls = use_tls
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.use_tls, use_tls)

    def test_backend_honors_configured_use_ssl_true(self):
        use_ssl = True
        self.configuration.use_ssl = use_ssl
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.use_ssl, use_ssl)

    def test_backend_honors_configured_fail_silently_true(self):
        fail_silently = True
        self.configuration.fail_silently = fail_silently
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.fail_silently, fail_silently)

    def test_backend_honors_configured_use_tls_false(self):
        use_tls = False
        self.configuration.use_tls = use_tls
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.use_tls, use_tls)

    def test_backend_honors_configured_use_ssl_false(self):
        use_ssl = False
        self.configuration.use_ssl = use_ssl
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.use_ssl, use_ssl)

    def test_backend_honors_configured_fail_silently_false(self):
        fail_silently = False
        self.configuration.fail_silently = fail_silently
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.fail_silently, fail_silently)

    def test_backend_honors_configured_timeout(self):
        timeout = 12345
        self.configuration.timeout = timeout
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.timeout, timeout)


class ConfiguredEmailBackendSettingsFallbackTestCase(TestCase):

    def setUp(self):
        self.configuration = DynamicEmailConfiguration()

    def test_backend_does_not_permit_mutex_tls_and_ssl(self):
        try:
            ConfiguredEmailBackend(
                use_tls = True,
                use_ssl = True
            )
            self.fail("No exception thrown. Expected ValueError")
        except ValueError:
            pass  # Test succeeded
        except Exception:
            self.fail("Incorrect exception thrown: {}".format(
                traceback.format_exc()
            ))

    @override_settings(EMAIL_HOST = 'testhost.mysite.com')
    def test_backend_honors_fallback_host(self):
        host = 'testhost.mysite.com'
        self.configuration.host = None
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.host, host)

    @override_settings(EMAIL_PORT = 123)
    def test_backend_honors_fallback_port(self):
        port = 123
        self.configuration.port = None
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.port, port)

    @override_settings(EMAIL_HOST_USER = 'awesomeuser')
    def test_backend_honors_fallback_username(self):
        username = 'awesomeuser'
        self.configuration.username = None
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.username, username)

    @override_settings(EMAIL_HOST_PASSWORD = 'secret')
    def test_backend_honors_fallback_password(self):
        password = 'secret'
        self.configuration.password = None
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.password, password)

    @override_settings(EMAIL_TIMEOUT = 12345)
    def test_backend_honors_fallback_timeout(self):
        timeout = 12345
        self.configuration.timeout = None
        self.configuration.save()
        backend = ConfiguredEmailBackend()
        self.assertEqual(backend.timeout, timeout)


class ConfiguredEmailBackendExplicitSettingsTestCase(TestCase):

    def setUp(self):
        self.configuration = DynamicEmailConfiguration()

    def test_backend_does_not_permit_mutex_tls_and_ssl(self):
        try:
            ConfiguredEmailBackend(
                use_tls = True,
                use_ssl = True
            )
            self.fail("No exception thrown. Expected ValueError")
        except ValueError:
            pass  # Test succeeded
        except Exception:
            self.fail("Incorrect exception thrown: {}".format(
                traceback.format_exc()
            ))

    def test_backend_honors_explicit_host(self):
        host = 'testhost.mysite.com'
        explicit_host = 'anotherhost.mysite.com'
        self.configuration.host = host
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            host = explicit_host
        )
        self.assertEqual(backend.host, explicit_host)

    def test_backend_honors_explicit_port(self):
        port = 123
        explicit_port = 321
        self.configuration.port = port
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            port = explicit_port
        )
        self.assertEqual(backend.port, explicit_port)

    def test_backend_honors_explicit_username(self):
        username = 'awesomeuser'
        explicit_username = 'anotheruser'
        self.configuration.username = username
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            username = explicit_username
        )
        self.assertEqual(backend.username, explicit_username)

    def test_backend_honors_explicit_password(self):
        password = 'secret'
        explicit_password = 'anothersecret'
        self.configuration.password = password
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            password = explicit_password
        )
        self.assertEqual(backend.password, explicit_password)

    def test_backend_honors_explicit_use_tls_true(self):
        use_tls = True
        explicit_use_tls = False
        self.configuration.use_tls = use_tls
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            use_tls = explicit_use_tls
        )
        self.assertEqual(backend.use_tls, explicit_use_tls)

    def test_backend_honors_explicit_use_ssl_true(self):
        use_ssl = True
        explicit_use_ssl = False
        self.configuration.use_ssl = use_ssl
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            use_ssl = explicit_use_ssl
        )
        self.assertEqual(backend.use_ssl, explicit_use_ssl)

    def test_backend_honors_explicit_fail_silently_true(self):
        fail_silently = True
        explicit_fail_silently = False
        self.configuration.fail_silently = fail_silently
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            fail_silently = explicit_fail_silently
        )
        self.assertEqual(backend.fail_silently, explicit_fail_silently)

    def test_backend_honors_explicit_use_tls_false(self):
        use_tls = False
        explicit_use_tls = True
        self.configuration.use_tls = use_tls
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            use_tls = explicit_use_tls
        )
        self.assertEqual(backend.use_tls, explicit_use_tls)

    def test_backend_honors_explicit_use_ssl_false(self):
        use_ssl = False
        explicit_use_ssl = True
        self.configuration.use_ssl = use_ssl
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            use_ssl = explicit_use_ssl
        )
        self.assertEqual(backend.use_ssl, explicit_use_ssl)

    def test_backend_honors_explicit_fail_silently_false(self):
        fail_silently = False
        explicit_fail_silently = True
        self.configuration.fail_silently = fail_silently
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            fail_silently = explicit_fail_silently
        )
        self.assertEqual(backend.fail_silently, explicit_fail_silently)

    def test_backend_honors_explicit_timeout(self):
        timeout = 12345
        explicit_timeout = 54321
        self.configuration.timeout = timeout
        self.configuration.save()
        backend = ConfiguredEmailBackend(
            timeout = explicit_timeout
        )
        self.assertEqual(backend.timeout, explicit_timeout)
