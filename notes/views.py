# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'AlexandrePinheiro'

from django.shortcuts import render
from django.http import HttpResponse
from .models import Publisher, Note

# Create your views here.
def notes_list(request):
    #return HttpResponse("NOTES LIST.")
    return render(request, 'notes/notes_list.html', {})

def publisher_list(request):
    plist = Publisher.objects.all()
    return render(request, 'notes/publisher_list.html', {'plist': plist})

