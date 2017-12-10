# -*- coding: utf-8 -*-
from django.conf.urls import url
from django_des import views


urlpatterns = [
    url(r'^send-test-email', views.send_test_email, name = 'django-des-test-email'),
]

__all__ = ['urlpatterns']
