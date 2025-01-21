## -*- coding: utf-8 -*-
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from des.forms import DynamicEmailConfigurationForm
from des.models import DynamicEmailConfiguration


class DynamicEmailConfigurationAdmin(SingletonModelAdmin):
    form = DynamicEmailConfigurationForm
    change_form_template = "des/change_form.html"

    class Media:
        js = (("js/des.js"),)
        css = {"all": ("css/des.css",)}


admin.site.register(DynamicEmailConfiguration, DynamicEmailConfigurationAdmin)
