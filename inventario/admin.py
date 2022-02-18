from django.contrib import admin
from inventario.models import *
from django.forms import Textarea
from django.db import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from inventario.forms import *


class DocumentList(admin.TabularInline):
    model = Document
    extra = 0
    classes = ('collapse', 'open')


@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    # Form = CajaForm
    list_display = ["rc", "descripcion", "tipo_documento", "Location", "status", "seguridad", "Proceso"]
    search_fields = ["rc", "Sede__name", "Area__name", "Proceso__name", "tipo_documento__name", "Location__name",
                     "status", "Serie__name", "sub_Serie__name"]
    list_filter = ["rc", "Sede", "Area", "Proceso", "tipo_documento", "Location", "status", 'Mes_de', 'Mes_hasta',
                   'year_de', 'year_hasta', 'fecha_inicio', 'fecha_fin']
    fieldsets = [
        ('Ubicacion', {'fields': (('Location', 'Sede'), ('Area', 'Proceso'),), 'classes': ['collapse']}),
        ('Retencion', {'fields': ('Retencion', ('Serie', 'sub_Serie'), ('tipo_documento', 'sub_tipo_documento'),),
                       'classes': ['collapse']}),
        ('Informacion de la Caja', {
            'fields': (
                ('descripcion', 'rc'), ('Serie_de', 'Serie_hasta'), ('Mes_de', 'Mes_hasta'), ('year_de', 'year_hasta'),
                ('fecha_inicio', 'fecha_fin'),),
            'classes': ['collapse']}),
        ('Seguridad', {
            'fields': (('status', 'seguridad'), ('fun', 'Sopo', 'ord'),), 'classes': ['collapse'],
        }),
        ('Información adicional', {
            'classes': ['collapse'],
            'fields': ['template', 'template_data'],
        }),
        ('Fecha Importante', {
            'fields': ['date_joined'],
            'classes': ['collapse'],
        }),
        # ('Folder que Contiene', {
        #     # 'fields': ['date_joined'],
        #     'classes': ['collapse'],
        # }),
    ]
    readonly_fields = ["date_joined", 'status']
    date_hierarchy = 'date_joined'
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        if not change:
            obj.status = 'PRE ADD'
        super().save_model(request, obj, form, change)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ["caja", "rc", "descripcion", "tipo_documento", "Location", "status", "seguridad", "Proceso"]
    search_fields = ["rc", "Sede__name", "Area__name", "Proceso__name", "tipo_documento__name", "Location__name",
                     "status", "sub_Serie__name", "Serie__name"]
    list_filter = ["rc", "Sede", "Proceso", "tipo_documento", "Location", "status", 'Mes_de', 'Mes_hasta', 'year_de',
                   'year_hasta', 'fecha_inicio', 'fecha_fin']
    fieldsets = [
        ('Ubicacion', {'fields': (('Location', 'Sede'), ('Area', 'Proceso'),), 'classes': ['collapse']}),
        ('Retencion', {'fields': ('Retencion', ('Serie', 'sub_Serie'), ('tipo_documento', 'sub_tipo_documento'),),
                       'classes': ['collapse']}),
        ('Informacion del Folder', {
            'fields': (
                'descripcion', ('rc', 'caja'), ('Serie_de', 'Serie_hasta'), ('Mes_de', 'Mes_hasta'),
                ('year_de', 'year_hasta'), ('fecha_inicio', 'fecha_fin'),),
            'classes': ['collapse']}),
        ('Seguridad', {
            'fields': (('status', 'seguridad'), ('fun', 'Sopo', 'ord'),), 'classes': ['collapse'],
        }),
        ('Información adicional', {
            'classes': ['collapse'],
            'fields': ['template', 'template_data'],
        }),
        ('Fecha Importante', {
            'fields': ['date_joined'],
            'classes': ['collapse'],
        }),
        # ('Documentos que Contiene', {
        #     # 'fields': ['date_joined'],
        #     'classes': ['collapse'],
        # }),
    ]
    readonly_fields = ["date_joined", 'status']
    date_hierarchy = 'date_joined'
    list_per_page = 50
    pass


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocForm
    list_display = ["caja", "folder", "rc", "descripcion", "tipo_documento", "Location", "status", "seguridad",
                    "Proceso"]
    search_fields = ["rc", "Sede__name", "Area__name", "Proceso__name", "tipo_documento__name", "Location__name",
                     "Serie__name", "sub_Serie__name"]
    list_filter = ["rc", "Sede", "Area", "Proceso", "tipo_documento", "Location", "status", "Serie_de", "Mes_de",
                   "year_de"]
    fieldsets = [
        ('Ubicacion', {'fields': (('Location', 'Sede'), ('Area', 'Proceso'),), 'classes': ['collapse']}),
        ('Retencion', {'fields': ('Retencion', ('Serie', 'sub_Serie'), ('tipo_documento', 'sub_tipo_documento'),),
                       'classes': ['collapse']}),
        ('Informacion del Folder',
         {'fields': (('caja', 'folder'), ('descripcion', 'rc'), ('Serie_de'), ('Mes_de'), ('year_de'),),
          'classes': ['collapse']}),
        ('Seguridad', {'fields': (('status', 'seguridad'), ('fun', 'Sopo', 'ord'),), 'classes': ['collapse'], }),
        ('Información adicional', {'fields': ['template', 'template_data'], 'classes': ['collapse'], }),
        ('Imagen', {'fields': ['mediafile', 'image_preview'], 'classes': ['collapse'], }),
        ('Fecha Importante', {'fields': ['date_joined'], 'classes': ['collapse'], }),

    ]
    readonly_fields = ["date_joined", 'status']
    date_hierarchy = 'date_joined'
    list_per_page = 50

    def save_model(self, request, obj, form, change):
        if not change:
            obj.status = 'PRE ADD'
        super().save_model(request, obj, form, change)
