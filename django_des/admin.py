## -*- coding: utf-8 -*-
from django_des.models import DynamicEmailConfiguration
from django.contrib import admin
from solo.admin import SingletonModelAdmin


class DynamicEmailConfigurationAdmin(SingletonModelAdmin):
    class Media:
        js = ('js/django_des.js'),
        css = {
            'all': ('css/django_des.css',)
        }

admin.site.register(DynamicEmailConfiguration, DynamicEmailConfigurationAdmin)
