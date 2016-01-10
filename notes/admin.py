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

admin.site.register(Note)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Publisher)

