from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from mrd.forms import *
from mrd.models import *


class SedeResource(resources.ModelResource):
   class Meta:
       Model = Sede


@admin.register(Sede)
class SedeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["code", "name", "date_joined"]
    search_fields = ["code", "name"]
    list_filter = ["code", "name", "date_joined"]
    formfield_overrides = {
    # models.CharField: {'widget': Textarea(attrs={'style': 'width:90%', 'rows': 5})},
    }
    fieldsets = [
        ('Informacion de la Sede', {'fields': [('code', 'name',)]}),
        ('Fecha de Creacion', {
            'fields': ['date_joined'],
            'classes': ['collapse']
        }
         ),
    ]
    readonly_fields = ["date_joined"]
    date_hierarchy = 'date_joined'
    list_per_page = 50
    resource_class = SedeResource
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["Sede",  "name", "code", "date_joined"]
    search_fields = ["Sede__name",  "name", "code"]
    list_filter = ["Sede",  "name", "code", "date_joined"]
    formfield_overrides = {
        # models.CharField: {'widget': Textarea(attrs={'style': 'width:90%', 'rows': 5})},
    }
    fieldsets = [
        ('Informacion del Area', {'fields': ['Sede', ('code', 'name',)]}),
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


@admin.register(Proceso)
class ProcesoAdmin(admin.ModelAdmin):
    list_display = ["Area", 'Sede', "name", "code", "date_joined"]
    search_fields = ["Area__name",  'Sede__name',  "name", "code"]
    list_filter = ["Area", "name", "code"]
    fieldsets = [
        ('Informacion del Proceso', {'fields': [('Sede', 'Area'), ('code', 'name',)]}),
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


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ["Sede", 'Area', "Proceso", "name", "code", "date_joined"]
    search_fields = ["Sede__name", "Area__name", "Proceso__name", "name", "code"]
    list_filter = ["Proceso", "name", "code", "date_joined"]
    formfield_overrides = {
        # models.CharField: {'widget': Textarea(attrs={'style': 'width:90%', 'rows': 5})},
    }
    fieldsets = [
        ('Informacion de la Serie', {'fields': [('Sede', 'Area', 'Proceso'), ('code', 'name',)]}),
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


@admin.register(sub_Serie)
class sub_SerieAdmin(admin.ModelAdmin):
    list_display = ["Sede", "Area", 'Serie', "name", "code", "date_joined"]
    search_fields = ["Sede__name", "Area__name", "Serie__name", "name", "code"]
    list_filter = ['Serie', "name", "code", "date_joined"]
    formfield_overrides = {
        # models.CharField: {'widget': Textarea(attrs={'style': 'width:90%', 'rows': 5})},
    }
    fieldsets = [
        ('Informacion de la Sub Serie', {'fields': [('Sede', 'Area'), ('Proceso', 'Serie'),  ('code', 'name',)]}),
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


@admin.register(tipo_documento)
class tipo_documentoAdmin(admin.ModelAdmin):
    list_display = ["Sede", "Area", "Proceso",  "sub_Serie", "name", "code", "date_joined"]
    search_fields = ["Sede__name", "Area__name", "Proceso__name", "Serie__name", "sub_Serie__name", "name", "code"]
    list_filter = ["Sede", "Area", "Proceso", "sub_Serie", "name", "code", "date_joined"]
    fieldsets = [
        ('Informacion Tipo Documento', {'fields': [('Sede', 'Area'), ('Proceso', 'Serie', 'sub_Serie'), ('code', 'name',)]}),
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


@admin.register(sub_tipo_documento)
class sub_tipo_documentoAdmin(admin.ModelAdmin):
    list_display = ["Sede", "Area", "Proceso",  "sub_Serie", "name", "code", "tipo_documento", "date_joined"]
    search_fields = ["Sede__name", "Area__name", "Proceso__name", "sub_Serie__name", "name", "code", "tipo_documento__name"]
    list_filter = ["Sede", "Area", "Proceso", "sub_Serie", "name", "code", "tipo_documento", "date_joined"]
    fieldsets = [
        ('Informacion Sub Tipo de Documento',
         {'fields': [('Sede', 'Area'), ('Serie', 'sub_Serie'), ('Proceso', 'tipo_documento'), ('code', 'name',)]}),
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
