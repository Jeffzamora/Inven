from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import *
from user.forms import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'Sede', 'is_staff', 'is_active')
    form = UserForm
    fieldsets = (
        ('Usuario', {'fields': ('username', 'password'), 'classes': ['collapse']}),
        ('Datos personales', {'fields': ('first_name', 'last_name', 'email'), 'classes': ['collapse']}),
        ('Adicional', {'fields': ('Sede',  'Area', 'Proceso'), 'classes': ['collapse']}),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), 'classes': ['collapse']
        }),
        ('Fecha Importante', {
            'fields': ['date_joined', 'last_login'],
            'classes': ['collapse']
        }
         ),
    )

    list_filter = ('username', 'is_staff', 'first_name', 'is_superuser', 'is_active', 'groups', 'Sede')
    list_per_page = 10
    readonly_fields = ["date_joined"]
    date_hierarchy = 'date_joined'
