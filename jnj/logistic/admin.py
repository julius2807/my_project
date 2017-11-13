# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ( 'cargo_type_name' , 'description' , 'enabled')
    search_fields = ['cargo_type_name' , 'description']

admin.site.register( CargoType, CargoTypeAdmin )

class TransportServiceAdmin(admin.ModelAdmin):
    list_display = ('transport_service_name', 'description', 'enabled')
    search_fields = ['transport_service_name' , 'description']

admin.site.register(TransportService, TransportServiceAdmin)

class TransportCategoryAdmin(admin.ModelAdmin):
    list_display = ('transport_category_name', 'description', 'enabled')
    search_fields = ['transport_category_name' , 'description']

admin.site.register(TransportCategory, TransportCategoryAdmin)

class TransportAdmin(admin.ModelAdmin):
    list_display = ('transport_name', 'description', 'enabled')
    search_fields = ['transport_name' , 'description']

admin.site.register(Transport, TransportAdmin)
