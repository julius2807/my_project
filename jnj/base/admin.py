# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                   , {'fields': ['organization_code', 'organization_name', 'business_area', 'enabled']} ),
        ('Address'              , {'fields': ['address_line_1', 'address_line_2', 'address_line_3', 'city', 'state', 'country', 'zip_code']} ),
        ('Contact'              , {'fields': ['business_phone_number', 'fax_number', 'email']} ),
    ]
    list_display = ( 'organization_code' , 'organization_name' )
    search_fields = ['organization_code', 'organization_name']

admin.site.register( Organization, OrganizationAdmin )

class BranchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                   , {'fields': ['organization', 'branch_code', 'branch_name', 'enabled']} ),
        ('Address'              , {'fields': ['address_line_1', 'address_line_2', 'address_line_3', 'city', 'state', 'country', 'zip_code']} ),
        ('Contact'              , {'fields': ['business_phone_number', 'fax_number', 'email']} ),
    ]
    list_display = ( 'organization' , 'branch_code' , 'branch_name' )
    search_fields = ['branch_code' , 'branch_name']

admin.site.register( Branch, BranchAdmin )

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ( 'currency_code' , 'currency_name' )
    search_fields = ['currency_code' , 'currency_name']

admin.site.register( Currency, CurrencyAdmin )

class ApplicationParameterAdmin(admin.ModelAdmin):
    list_display = ( 'organization_id' , 'parameter_name' )
    search_fields = ['parameter_name']

admin.site.register( ApplicationParameter, ApplicationParameterAdmin )

class LookupCodeInline(admin.TabularInline):
    model = LookupCode

class LookupTypeAdmin(admin.ModelAdmin):
    list_display = ('lookup_type', 'application_owner', 'description')
    inlines = [LookupCodeInline]
    search_fields = ['lookup_type', 'description']

class LookupCodeAdmin(admin.ModelAdmin):
    list_display = ('lookup_type_id', 'lookup_code', 'sequence', 'description')

admin.site.register(LookupType, LookupTypeAdmin)

class PopupTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                   , {'fields': ['popup_name', 'application_owner', 'description', 'query']} ),
        ('Key Fields'           , {'fields': ['key_field', 'parent_field_1', 'parent_field_2', 'parent_field_3', 'parent_field_4', 'parent_field_5'] , 'classes': ['collapse']} ),
        ('Criteria & Ordering'  , {'fields': ['criteria_field_1', 'criteria_field_label_1', 'criteria_field_2', 'criteria_field_label_2', 'order_field_1', 'order_field_2'] , 'classes': ['collapse']} ),
        ('Value Fields'         , {'fields': ['value_field_1', 'value_field_2', 'value_field_3', 'value_field_4', 'value_field_5', 'displayed_field'] , 'classes': ['collapse']} ),
    ]
    list_display = ( 'popup_name' , 'application_owner', 'description' )
    search_fields = ['popup_name', 'description']

admin.site.register( PopupType, PopupTypeAdmin )

class HolidayAdmin(admin.ModelAdmin):
    list_display = ( 'holiday_date' , 'description' )
    search_fields = ['holiday_date']

admin.site.register( Holiday, HolidayAdmin )

class UnitOfMeasurementAdmin(admin.ModelAdmin):
    list_display = ( 'uom_name' , 'uom_long_name' )
    search_fields = ['uom_name']

admin.site.register( UnitOfMeasurement, UnitOfMeasurementAdmin )

class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ( 'subject' , 'receive_timestamp' , 'is_read' , 'is_actioned' )
    search_fields = ['subject']

admin.site.register( UserNotification, UserNotificationAdmin )
