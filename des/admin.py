## -*- coding: utf-8 -*-
from des.models import DynamicEmailConfiguration
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from des.forms import DynamicEmailConfigurationForm


class DynamicEmailConfigurationAdmin(SingletonModelAdmin):
    form = DynamicEmailConfigurationForm
    change_form_template = 'des/change_form.html'
    class Media:
        js = ('js/des.js'),
        css = {
            'all': ('css/des.css',)
        }

admin.site.register(DynamicEmailConfiguration, DynamicEmailConfigurationAdmin)
