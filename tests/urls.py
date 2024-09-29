# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.urls import include, path

from des import urls as des_urls

urlpatterns = [path("admin/", admin.site.urls), path("django-des/", include(des_urls))]
