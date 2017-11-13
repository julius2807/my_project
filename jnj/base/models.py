# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import os

import datetime

# Create your models here.

YESNO_CHOICES = (
    ('Y' , 'Yes') ,
    ('N' , 'No'),
)

UOM_TYPE_CHOICES = (
    ('W', 'Weight') ,
    ('L', 'Length or Distance') ,
    ('U', 'Unit') ,
)

class Organization(models.Model):
    organization_code = models.CharField(max_length=30, unique=True)
    organization_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    address_line_3 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    business_area = models.CharField(max_length=30)
    enabled = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')
    business_phone_number = models.CharField(max_length=30, blank=True)
    fax_number = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(null=True,blank=True)

    def __unicode__(self):
        return self.organization_code + r' - ' + self.organization_name

    class Meta:
        ordering = ['organization_code']

class Branch(models.Model):
    organization = models.ForeignKey(Organization)
    branch_code = models.CharField(max_length=30)
    branch_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    address_line_3 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    business_area = models.CharField(max_length=30)
    enabled = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')
    business_phone_number = models.CharField(max_length=30, blank=True)
    fax_number = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.organization.organization_code + r' - ' + self.branch_code + ' - ' + self.branch_name

    class Meta:
        ordering = ['branch_code']
        verbose_name_plural = 'branches'

class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    currency_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    enabled = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')

    def __unicode__(self):
        return self.currency_code

    class Meta:
        ordering = ['currency_code']
        verbose_name_plural = 'currencies'

class ApplicationParameter(models.Model):
    organization = models.ForeignKey(Organization)
    parameter_name = models.CharField(max_length=100)
    parameter_value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.organization.organization_code + r' - ' + self.param_name

    class Meta:
        ordering = ['organization_id', 'parameter_name']


class LookupType(models.Model):
    lookup_type = models.CharField(max_length=30, unique=True)
    application_owner = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100)
    parent_type_1 = models.CharField(max_length=30, blank=True)
    parent_type_2 = models.CharField(max_length=30, blank=True)
    enabled = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')

    def __unicode__(self):
        return self.lookup_type

    class Meta:
        ordering = ['lookup_type']

class LookupCode(models.Model):
    lookup_type = models.ForeignKey(LookupType, on_delete=models.CASCADE)
    lookup_code = models.CharField(max_length=30)
    sequence = models.IntegerField()
    displayed_field = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    parent_code_1 = models.CharField(max_length=30, blank=True)
    parent_code_2 = models.CharField(max_length=30, blank=True)
    enabled = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')

    def __unicode__(self):
        return self.lookup_code

    class Meta:
        ordering = ['lookup_type_id', 'sequence']


class PopupType(models.Model):
    popup_name = models.CharField(max_length=30, unique=True)
    application_owner = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100)
    query = models.TextField()
    key_field = models.CharField(max_length=50, blank=True)
    parent_field_1 = models.CharField(max_length=50, blank=True)
    parent_field_2 = models.CharField(max_length=50, blank=True)
    parent_field_3 = models.CharField(max_length=50, blank=True)
    parent_field_4 = models.CharField(max_length=50, blank=True)
    parent_field_5 = models.CharField(max_length=50, blank=True)
    criteria_field_1 = models.CharField(max_length=50, blank=True)
    criteria_field_label_1 = models.CharField(max_length=50, blank=True)
    criteria_field_2 = models.CharField(max_length=50, blank=True)
    criteria_field_label_2 = models.CharField(max_length=50, blank=True)
    order_field_1 = models.CharField(max_length=50, blank=True)
    order_field_2 = models.CharField(max_length=50, blank=True)
    value_field_1 = models.CharField(max_length=50, blank=True)
    value_field_2 = models.CharField(max_length=50, blank=True)
    value_field_3 = models.CharField(max_length=50, blank=True)
    value_field_4 = models.CharField(max_length=50, blank=True)
    value_field_5 = models.CharField(max_length=50, blank=True)
    displayed_field = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.popup_name

    class Meta:
        ordering = ['popup_name']

class Holiday(models.Model):
    holiday_date = models.DateField(unique=True)
    description = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.holiday_date.strftime('%Y-%m-%d')

    class Meta:
        ordering = ['holiday_date']

class UnitOfMeasurement(models.Model):
    uom_name = models.CharField(max_length=15)
    uom_long_name = models.CharField(max_length=100, blank=True)
    uom_type = models.CharField(max_length=1, choices=UOM_TYPE_CHOICES)

    def __unicode__(self):
        return self.uom_name

    class Meta:
        ordering = ['uom_name']

class UserNotification(models.Model):
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=255)
    receive_timestamp = models.DateTimeField(blank=True)
    source = models.CharField(max_length=100)
    body = models.TextField()
    action_generic = models.CharField(max_length=1000, blank=True)
    action_yes = models.CharField(max_length=1000, blank=True)
    action_no = models.CharField(max_length=1000, blank=True)
    is_read = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')
    read_timestamp = models.DateTimeField(null=True,blank=True)
    is_actioned = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')
    action_timestamp = models.DateTimeField(null=True,blank=True)
    is_archived = models.CharField(max_length=1, choices=YESNO_CHOICES, default='N')
    archived_timestamp = models.DateTimeField(null=True,blank=True)

    def __unicode__(self):
        return self.subject

    class Meta:
        ordering = ['-receive_timestamp']
