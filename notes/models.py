# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'AlexandrePinheiro'
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True, default='')

    def __unicode__(self):
        return self.last_name+', '+self.first_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    site = models.URLField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True, default='')
    # relacao onetomany
    # book =

    def __unicode__(self):
        return self.publisher_name

class Genre(models.Model):
    description = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.description

class Type(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.type

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    publication_year = models.DateField
    # cover = models.
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL,blank=True,null=True)
    type = models.ForeignKey(Type,on_delete=models.SET_NULL,blank=True,null=True)
    genre = models.ForeignKey(Genre,on_delete=models.SET_NULL,blank=True,null=True)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title

class Note(models.Model):
    user = models.ForeignKey('auth.User')
    book = models.ForeignKey(Book)
    capture_date = models.DateTimeField(default=timezone.now())
    capture_text = models.CharField(max_length=500)
    capture_page = models.CharField(max_length=3)
    notes = models.CharField(max_length=100)
