from django.contrib import admin
from inventario.models import *
from django.forms import Textarea
from django.db import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    # fields = (('code', 'name'), 'Sede')
    list_display = ["code", "name", 'Sede', "date_joined"]
    search_fields = ["code", "name", 'Sede']
    list_filter = ["code", "name", 'Sede', "date_joined"]
    fieldsets = [
        ('Informacion de la Bodega', {'fields': [('code', 'name',), 'Sede']}),
        ('Fecha de Creacion', {
            'fields': ['date_joined'],
            'classes': ['collapse']
        }
         ),
    ]
    list_per_page = 5
    readonly_fields = ["date_joined"]
    date_hierarchy = 'date_joined'
    autocomplete_fields = ('Sede',)
    pass
