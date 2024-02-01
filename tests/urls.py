# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path, include
from django.contrib import admin
from des import urls as des_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('django-des/', include(des_urls))
]
