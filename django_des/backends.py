# -*- coding: utf-8 -*-
import threading

from django.core.exceptions import AppRegistryNotReady
from django.core.mail.backends.smtp import EmailBackend


class ConfiguredEmailBackend(EmailBackend):
    def __init__(self, host = None, port = None, username = None, password = None,
                 use_tls = None, fail_silently = False, use_ssl = None, timeout = None,
                 ssl_keyfile = None, ssl_certfile = None,
                 **kwargs):

        from django_des.models import DynamicEmailConfiguration
        configuration = DynamicEmailConfiguration.get_solo()

        super(ConfiguredEmailBackend, self).__init__(
            fail_silently = configuration.email_fail_silently)

        self.host = host or configuration.email_host
        self.port = port or configuration.email_port
        self.username = username or configuration.email_host_user
        self.password = password or configuration.email_host_password
        self.use_tls = use_tls or configuration.email_use_tls
        self.use_ssl = use_ssl or configuration.email_use_ssl
        self.timeout = timeout or configuration.email_timeout
        self.ssl_keyfile = ssl_keyfile # TODO: support this in admin
        self.ssl_certfile = ssl_certfile # TODO: support this in admin
        if self.use_ssl and self.use_tls:
            raise ValueError(
                "EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, "
                "so only set one of those settings to True.")
        self.connection = None
        self._lock = threading.RLock()
