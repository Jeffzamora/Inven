from django.contrib.auth.models import AbstractUser, Permission, Group
from mrd.models import *
from django.forms import model_to_dict
from cedoc.choices import *
from crum import get_current_request
from django.db import models
from datetime import datetime


class User(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="user_permissions",
        related_query_name="user",
    )

    cargo = models.CharField(max_length=12, verbose_name='Cargo')
    telefono = models.CharField(max_length=8, verbose_name='Telefono')
    exten = models.CharField(max_length=4, blank=True, null=True, verbose_name='Ext del telefono')
    celular = models.CharField(max_length=8, verbose_name='Celular')
    Comp = models.CharField(max_length=5, choices=compañia, verbose_name='Compañia')
    direccion = models.CharField(max_length=50, verbose_name='Direccion Donde habita')
    Sede = models.ForeignKey(Sede, blank=True, null=True, on_delete=models.RESTRICT, verbose_name='Sede')
    Area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Area')
    Proceso = models.ForeignKey(Proceso, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Proceso')


    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        item['user_permissions'] = []
        item['Sede'] = self.Sede.name
        item['Area'] = self.Area.name
        item['Proceso'] = self.Proceso.name
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%d-%m-%y')
        item['date_joined'] = self.date_joined.strftime('%d-%m-%y')
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

