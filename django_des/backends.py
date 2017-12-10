# -*- coding: utf-8 -*-
import threading

from django.core.exceptions import AppRegistryNotReady
from django.core.mail.backends.smtp import EmailBackend


class ConfiguredEmailBackend(EmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=None, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):

        from django_des.models import DynamicEmailConfiguration
        configuration = DynamicEmailConfiguration.get_solo()

        super(ConfiguredEmailBackend, self).__init__(
             host = configuration.email_host if host is None else host,
             port = configuration.email_port if port is None else port,
             username = configuration.email_host_user if username is None else username,
             password = configuration.email_host_password if password is None else password,
             use_tls = configuration.email_use_tls if use_tls is None else use_tls,
             fail_silently = configuration.email_fail_silently if fail_silently is None else fail_silently,
             use_ssl = configuration.email_use_ssl if use_ssl is None else use_ssl,
             timeout = configuration.email_timeout if timeout is None else timeout,
             ssl_keyfile = ssl_keyfile, # TODO: configuration.email_ssl_keyfile if ssl_keyfile is not None else ssl_keyfile,
             ssl_certfile = ssl_certfile, # TODO: configuration.email_ssl_certfile if ssl_certfile is not None else ssl_certfile,
             **kwargs)


__all__ = ['ConfiguredEmailBackend']
