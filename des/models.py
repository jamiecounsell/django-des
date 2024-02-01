# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _
from solo.models import SingletonModel
from django.core.exceptions import ValidationError


class DynamicEmailConfiguration(SingletonModel):
    host = models.CharField(
        blank = True, null = True,
        max_length = 256, verbose_name = _("Email Host"))

    port = models.SmallIntegerField(
        blank = True, null = True,
        verbose_name = _("Email Port"))

    from_email = models.CharField(
        blank = True, null = True,
        max_length = 256, verbose_name = _("Default From Email"))

    username = models.CharField(
        blank = True, null = True,
        max_length = 256, verbose_name = _("Email Authentication Username"))

    password = models.CharField(
        blank = True, null = True,
        max_length = 256, verbose_name = _("Email Authentication Password"))

    use_tls = models.BooleanField(
        default = False, verbose_name = _("Use TLS"))

    use_ssl = models.BooleanField(
        default = False, verbose_name = _("Use SSL"))

    fail_silently = models.BooleanField(
        default = False, verbose_name = _("Fail Silently"))

    timeout = models.SmallIntegerField(
        blank = True, null = True,
        verbose_name = _("Email Send Timeout (seconds)"))

    def clean(self):
        if self.use_ssl and self.use_tls:
            raise ValidationError(
                _("\"Use TLS\" and \"Use SSL\" are mutually exclusive, "
                "so only set one of those settings to True."))

    def __str__(self):
        return _("Email Configuration")

    class Meta:
        verbose_name = _("Email Configuration")


__all__ = ['DynamicEmailConfiguration']
