# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin
from django_des import urls as django_des_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django-des/', include(django_des_urls))
]
