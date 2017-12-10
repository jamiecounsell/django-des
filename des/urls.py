# -*- coding: utf-8 -*-
from django.conf.urls import url
from des import views


urlpatterns = [
    url(r'^send-test-email', views.send_test_email, name = 'des-test-email'),
]

__all__ = ['urlpatterns']
