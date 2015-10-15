# -*- coding: utf-8 -*-

'''
Created on November 25, 2012

@author: noraini
'''
from django.db import models

class CommonModel(models.Model):
    """
    Default fields for all models in Alivematrix.
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

