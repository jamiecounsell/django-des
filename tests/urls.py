# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_des.urls import urlpatterns as django_des_urls

urlpatterns = [
    url(r'^', include(django_des_urls, namespace='django_des')),
]
