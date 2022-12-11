# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from des import views


urlpatterns = [
    url(r'^send-test-email', views.send_test_email, name = 'des-test-email'),
]

__all__ = ['urlpatterns']
