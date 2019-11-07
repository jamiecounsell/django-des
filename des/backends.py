# -*- coding: utf-8 -*-
from django.core.mail.backends.smtp import EmailBackend


class ConfiguredEmailBackend(EmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=None, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):

        from des.models import DynamicEmailConfiguration
        configuration = DynamicEmailConfiguration.get_solo()

        super(ConfiguredEmailBackend, self).__init__(
             host = configuration.host if host is None else host,
             port = configuration.port if port is None else port,
             username = configuration.username.decode('utf-8').encode("idna") if username is None else username,
             password = configuration.password if password is None else password,
             use_tls = configuration.use_tls if use_tls is None else use_tls,
             fail_silently = configuration.fail_silently if fail_silently is None else fail_silently,
             use_ssl = configuration.use_ssl if use_ssl is None else use_ssl,
             timeout = configuration.timeout if timeout is None else timeout,
             ssl_keyfile = ssl_keyfile, # TODO: configuration.ssl_keyfile if ssl_keyfile is not None else ssl_keyfile,
             ssl_certfile = ssl_certfile, # TODO: configuration.ssl_certfile if ssl_certfile is not None else ssl_certfile,
             **kwargs)


__all__ = ['ConfiguredEmailBackend']
