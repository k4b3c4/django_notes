# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.contrib import admin

# Register your models here.
from .models import Note
from .models import Author
from .models import Book
from .models import Genre
from .models import Type
from .models import Publisher

class PublisherAdmin(admin.ModelAdmin):
    # Campos que serao apresentados
    # fields = ['publisher_name', 'site', 'email']

    # colunas
    list_display = ('publisher_name', 'site', 'email')

    # Apresentacao dos campos em abas
    fieldsets = [
        (None,       {'fields': ['publisher_name']}),
        ('Contacts', {'fields': ['site', 'email']}),
    ]

    # list_filter = ['']
    # search_fields = ['']


admin.site.register(Note)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Publisher,PublisherAdmin)

