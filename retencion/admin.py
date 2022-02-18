from django.contrib import admin
from retencion.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(retencion)
class RetencionAdmin(admin.ModelAdmin):
    list_display = ['name', "Serie", "sub_Serie", "tipo_documento", 'sub_tipo_documento', 'total_year', "date_joined"]
    search_fields = ['name', "Serie__name", "sub_Serie__name", "tipo_documento__name", 'sub_tipo_documento__name']
    list_filter = ['name', "Serie", "sub_Serie", 'tipo_documento', 'sub_tipo_documento']
    fieldsets = [
        ('Informacion de la retencion', {'fields': [('Serie', 'sub_Serie',), ('tipo_documento', 'sub_tipo_documento',)]}),
        ('Datos de la Retencion', {'fields': [('code', 'name',), ('disposicion', 'procedimiento',)]}),
        ('Tiempo de Resguardo', {'fields': [('res_uno', 'tim_uno',), ('res_dos', 'tim_dos',), ('res_tres', 'tim_tres',)]}),
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


@admin.register(disposicion)
class disposicionAdmin(admin.ModelAdmin):

    pass


@admin.register(procedimiento)
class procedimientoAdmin(admin.ModelAdmin):

    pass