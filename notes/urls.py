# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'AlexandrePinheiro'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.publisher_list, name='publisher_list'),
    #url(r'^$', views.notes_list, name='notes_list'),
    #url(r'^$', views.index, name='index'),
]
