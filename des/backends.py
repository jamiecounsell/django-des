# -*- coding: utf-8 -*-
import smtplib

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.message import sanitize_address


class ConfiguredEmailBackend(EmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=None, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):

        from des.models import DynamicEmailConfiguration
        self.configuration = DynamicEmailConfiguration.get_solo()

        super(ConfiguredEmailBackend, self).__init__(
             host = self.configuration.host if host is None else host,
             port = self.configuration.port if port is None else port,
             username = self.configuration.username if username is None else username,
             password = self.configuration.password if password is None else password,
             use_tls = self.configuration.use_tls if use_tls is None else use_tls,
             fail_silently = self.configuration.fail_silently if fail_silently is None else fail_silently,
             use_ssl = self.configuration.use_ssl if use_ssl is None else use_ssl,
             timeout = self.configuration.timeout if timeout is None else timeout,
             ssl_keyfile = ssl_keyfile, # TODO: configuration.ssl_keyfile if ssl_keyfile is not None else ssl_keyfile,
             ssl_certfile = ssl_certfile, # TODO: configuration.ssl_certfile if ssl_certfile is not None else ssl_certfile,
             **kwargs)

    def _send(self, email_message):
        if not email_message.recipients():
            return False
        encoding = email_message.encoding or settings.DEFAULT_CHARSET
        from_email = sanitize_address(
            self.configuration.from_email or email_message.from_email,
            encoding
        )
        recipients = [sanitize_address(addr, encoding) for addr in email_message.recipients()]
        message = email_message.message()
        try:
            self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
            return False
        return True


__all__ = ['ConfiguredEmailBackend']
