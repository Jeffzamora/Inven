from django.contrib import admin
from ordenes.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin



@admin.register(ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ["code", 'name', 'Sede', "date_joined"]
    search_fields = ["name", "code", 'Sede__name']
    list_filter = ["name", "code", 'Sede', "date_joined"]
    fieldsets = [
        ('Informacion de Orden de Trabajo', {'fields': ['Sede', ('code', 'name',)]}),
        ('Fecha de Creacion', {
            'fields': ['date_joined'],
            'classes': ['collapse']
        }
         ),
    ]
    readonly_fields = ["date_joined"]
    date_hierarchy = 'date_joined'
    list_per_page = 50
    pass