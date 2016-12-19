'''
filehand

'''
# -*- coding: utf-8 -*-
import os, sys  # THIS SOLVED PROBLEM OF NOT ACCEPTING ACCENT IN VERVOSE NAME (Raz�n Social) (non ascii accent utf8 language)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible # only if you need to support Python 2
from datetime import datetime, time, date, timedelta
from django.shortcuts import get_object_or_404
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import FilePathField
from django.core.validators import MinLengthValidator
from django import forms
#from tinymce import models as tinymce_models
#from filehand.forms import ArticlesForm
'''
'''
def article_upload_to(instance, filename):
    return 'articles/' + filename
'''
'''
@python_2_unicode_compatible
class Articles(models.Model):
    #file = models.FileField ( upload_to = 'articles', null = False )
    file = models.FileField ( upload_to = article_upload_to )
    file_name = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
        verbose_name = 'Archivo',
        )
    author = models.ForeignKey('auth.user', null=True, blank=True,)
    clas = models.ForeignKey('Clas', null=True, blank=True,)
    subClas = models.ForeignKey('SubClas', null=True, blank=True,)
    docType = models.ForeignKey('DocType', null=True, blank=True,)
    #clas = models.ForeignKey('Clas', )
    #subClas = models.ForeignKey('SubClas', )
    #docType = models.ForeignKey('DocType', )
    access_by_group = models.ForeignKey('auth.group', null=True, blank=True, )
    status_choices = (
        ("anonimous", "ANONIMO"),
        ("is_authenticated", "REGISTRADO"),
        ("is_staff", "STAFF"),
        ("is_superuser", "SUPERUSER"),
        )
    access_by_status = models.CharField(
        max_length = 20,
        null = True,
        blank = True,
        choices = status_choices,
        verbose_name = 'Status',
        )

    def __str__(self):
        return '%s' % (self.file)
'''
'''
class Clas(models.Model):
    code = models.CharField(
        max_length = 2,
        validators = [MinLengthValidator(2)],
        #unique=True,
        #blank=False,
        #null=False,
        verbose_name = 'código'
        )
    name = models.CharField(
        max_length = 24,
        unique=True,
        blank=False,
        null=False,
        verbose_name = 'nombre'
        )
    class Meta:
        ordering = ['name']
        verbose_name = ['clasificacion']
        verbose_name_plural = ['clasificaciones']
    def first(self):
        if self[0]:
            return self[0]
        else:
            return 'cosa'
    def __str__(self):
        return '%s' % (self.name)

'''
'''
class SubClas(models.Model):
    code = models.CharField(
        max_length = 2,
        validators = [MinLengthValidator(2)],
        verbose_name = 'código'
        )
    name = models.CharField(
        max_length = 24,
        unique=True,
        blank=False,
        null=False,
        verbose_name = 'nombre'
        )
    subClasOf = models.ForeignKey('Clas', null=True, blank=True,)
    class Meta:
        ordering = ['name']
        verbose_name = ['subclasificacion']
        verbose_name_plural = ['subclasificaciones']
    def first(self):
        if self[0]:
            return self[0]
        else:
            return 'cosa'
    def __str__(self):
        return '%s' % (self.name)
'''
'''
class DocType(models.Model):
    code = models.CharField(
        max_length = 2,
        validators = [MinLengthValidator(2)],
        verbose_name = 'código'
        )
    name = models.CharField(
        max_length = 24,
        unique=True,
        blank=False,
        null=False,
        verbose_name = 'nombre'
        )
    class Meta:
        ordering = ['name']
        verbose_name = ['tipo de documento']
        verbose_name_plural = ['tipos de documento']
    def first(self):
        if self[0]:
            return self[0]
        else:
            return 'cosa'
    def __str__(self):
        return '%s' % (self.name)
'''
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
''' 
def article_images_upload_to(instance, filename):
    return 'img/articles/' + filename

@python_2_unicode_compatible
class ArticleImages(models.Model):
    file = models.ImageField ( upload_to = article_images_upload_to )
    file_name = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
        verbose_name = 'nombre',
        )
    def clean(self):
        # self.file_name is not filled in in the form for file uploads so fill it in here
        if self.file_name == '' or self.file_name == None:
            self.file_name = self.file.name
        
    def __str__(self):
        return '%s' % (self.file.name)    
'''
'''
class GalleryDocument(models.Model):
    docfile = models.FileField ( upload_to = 'documents/%Y/%m/%d' )