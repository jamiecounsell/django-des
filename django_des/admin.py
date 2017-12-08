## -*- coding: utf-8 -*-
from django_des.models import DynamicEmailConfiguration
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django_des.forms import DynamicEmailConfigurationForm


class DynamicEmailConfigurationAdmin(SingletonModelAdmin):
    form = DynamicEmailConfigurationForm
    class Media:
        js = ('js/django_des.js'),
        css = {
            'all': ('css/django_des.css',)
        }

admin.site.register(DynamicEmailConfiguration, DynamicEmailConfigurationAdmin)
