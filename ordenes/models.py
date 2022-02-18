from crum import get_current_user
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from simple_history.models import HistoricalRecords
from mrd.models import *
from inventario.choices import *
# from custodia.login.models import BaseModel


class ordenes(models.Model):
    code = models.CharField(max_length=10, null=True, verbose_name="Codigo")
    name = models.CharField(max_length=100, null=True, verbose_name="Nombre")
    Sede = models.ForeignKey(Sede, null=True, blank=True, verbose_name="Sede", on_delete=models.SET_NULL)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name


    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Orden de trabajo'
        verbose_name_plural = 'Ordenes de trabajo'
        db_table = 'ordenes'
        ordering = ['id']

from django.db import models

# Create your models here.
