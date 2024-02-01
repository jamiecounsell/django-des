# -*- coding: utf-8 -*-
from django.urls import path
from des import views


urlpatterns = [
    path('send-test-email', views.send_test_email, name='des-test-email'),
]

__all__ = ['urlpatterns']
