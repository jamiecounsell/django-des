# -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


class DynamicEmailConfiguration(SingletonModel):
    email_host = models.CharField(
        max_length = 100, verbose_name = "Email Host")

    email_port = models.SmallIntegerField(
        blank = False, null = False, default = 25,
        verbose_name = "Email Port")

    email_from_email = models.CharField(
        max_length = 50, verbose_name = "Default From Email")

    email_host_user = models.CharField(
        max_length = 50, verbose_name = "Email User")

    email_host_password = models.CharField(
        max_length = 50, verbose_name = "Email User Password")

    email_use_tls = models.BooleanField(
        default = False, verbose_name = "Use TLS?")

    email_use_ssl = models.BooleanField(
        default = False, verbose_name = "Use SSL? (Requires "
        "EMAIL_SSL_CERTFILE and EMAIL_SSL_KEYFILE to be defined "
        "in settings.py)")

    email_fail_silently = models.BooleanField(
        default = False, verbose_name = "Fail Silently?")

    email_timeout = models.SmallIntegerField(
        blank = False, null = False, default = 60,
        verbose_name = "Email Send Timeout")

    def clean(self):
        if self.email_use_ssl and self.email_use_tls:
            raise ValidationError(
                "\"Use TLS\" and \"Use SSL\" are mutually exclusive, "
                "so only set one of those settings to True.")

    def __str__(self):
        return u"Email Configuration"

    class Meta:
        verbose_name = "Email Configuration"
