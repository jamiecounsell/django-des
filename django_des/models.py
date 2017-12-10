# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


class DynamicEmailConfiguration(SingletonModel):
    email_host = models.CharField(
        default = 'localhost',
        max_length = 256, verbose_name = _("Email Host"))

    email_port = models.SmallIntegerField(
        blank = False, null = False, default = 25,
        verbose_name = _("Email Port"))

    email_from_email = models.CharField(
        default = 'django@localhost',
        max_length = 256, verbose_name = _("Default From Email"))

    email_host_user = models.CharField(
        blank = True, null = False,
        max_length = 256, verbose_name = _("Email User"))

    email_host_password = models.CharField(
        blank = True, null = False,
        max_length = 256, verbose_name = _("Email User Password"))

    email_use_tls = models.BooleanField(
        default = False, verbose_name = _("Use TLS"))

    email_use_ssl = models.BooleanField(
        default = False, verbose_name = _("Use SSL"))

    email_fail_silently = models.BooleanField(
        default = False, verbose_name = _("Fail Silently"))

    email_timeout = models.SmallIntegerField(
        blank = False, null = False, default = 60,
        verbose_name = _("Email Send Timeout (seconds)"))

    def clean(self):
        if self.email_use_ssl and self.email_use_tls:
            raise ValidationError(
                _("\"Use TLS\" and \"Use SSL\" are mutually exclusive, "
                "so only set one of those settings to True."))

    def __str__(self):
        return _("Email Configuration")

    class Meta:
        verbose_name = _("Email Configuration")


__all__ = ['DynamicEmailConfiguration']
