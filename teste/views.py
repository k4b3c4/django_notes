# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'AlexandrePinheiro'

from django.shortcuts import render

def home(request):
    context = {}
    template = "home.html"

    return render(request, template, context)
