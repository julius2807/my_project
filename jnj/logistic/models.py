# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import os

import datetime

from base.models import Organization

# Create your models here.

ENABLE_CHOICES = (
    ('Y' , 'Yes') ,
    ('N' , 'No'),
)

class CargoType(models.Model):
    organization = models.ForeignKey(Organization)
    cargo_type_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sequence = models.IntegerField(default=0)
    enabled = models.CharField(max_length=1, choices=ENABLE_CHOICES, default='N')
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.cargo_type_name

    class Meta:
        ordering = ['sequence', 'cargo_type_name']

class TransportService(models.Model):
    organization = models.ForeignKey(Organization)
    transport_service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sequence = models.IntegerField(default=0)
    enabled = models.CharField(max_length=1, choices=ENABLE_CHOICES, default='N')
    transport_service_page = models.CharField(max_length=500,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.transport_service_name

    class Meta:
        ordering = ['sequence', 'transport_service_name']

class TransportCategory(models.Model):
    organization = models.ForeignKey(Organization)
    transport_category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sequence = models.IntegerField(default=0)
    enabled = models.CharField(max_length=1, choices=ENABLE_CHOICES, default='N')

    def __str__(self):
        return self.transport_category_name

    class Meta:
        ordering = ['sequence','transport_category_name']
        verbose_name_plural = 'Transport categories'

class Transport(models.Model):
    organization = models.ForeignKey(Organization)
    transport_category = models.ForeignKey(TransportCategory)
    transport_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sequence = models.IntegerField(default=0)
    dimension_description = models.CharField(max_length=150,blank=True)
    image = models.ImageField(null=True,blank=True)
    enabled = models.CharField(max_length=1, choices=ENABLE_CHOICES, default='N')

    def __str__(self):
        return self.transport_name

    class Meta:
        ordering = ['sequence','transport_name']
