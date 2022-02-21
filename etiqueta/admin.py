from django.contrib import admin
from etiqueta.models import *
from inventario.forms import *


class FieldsBox(admin.TabularInline):
    model = FieldBox
    extra = 0
    fields = ('name', 'label', 'field', 'show', 'position')
    sortable_field_name = "position"
    classes = ['collapse']


class FieldsFolder(admin.TabularInline):
    model = FieldFile
    extra = 0
    fields = ('name', 'label', 'field', 'show', 'position')
    sortable_field_name = "position"
    classes = ['collapse']


class FieldsDoc(admin.TabularInline):
    model = FieldDoc
    extra = 0
    fields = ('name', 'label', 'field', 'show', 'position')
    sortable_field_name = "position"
    classes = ['collapse']


@admin.register(FormBox)
class FormBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)
    inlines = [FieldsBox, ]
    save_as = True
    # change_form_template = "custodia/form-box.html"
    fieldsets = (
        ('Datos de la etiqueta', {
            'classes': ['collapse'],
            'fields': ('name', 'code'),
        }),
    )


@admin.register(FormFile)
class FormFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)
    inlines = [FieldsFolder, ]
    save_as = True
    fields = ('name', 'code')


@admin.register(FormDoc)
class FormDocAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)
    inlines = [FieldsDoc, ]
    save_as = True
    fields = ('name', 'code')
