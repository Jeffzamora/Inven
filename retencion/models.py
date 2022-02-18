from mrd.models import *
from retencion.choices import *
# from custodia.login.models import BaseModel


class disposicion(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Nombre")

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Disposicion Final'
        verbose_name_plural = 'Disposiciones'
        db_table = 'disposicion'
        ordering = ['id']


class procedimiento(models.Model):
    disposicion = models.ForeignKey(disposicion, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Disposicion Final')
    name = models.CharField(max_length=100, null=True, verbose_name="Nombre")

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'
        db_table = 'procedimiento'
        ordering = ['id']


class retencion(models.Model):
    Serie = models.ForeignKey(Serie, null=True, blank=True, verbose_name="Serie", on_delete=models.SET_NULL)
    sub_Serie = models.ForeignKey(sub_Serie, null=True, blank=True, verbose_name="Sub Serie", on_delete=models.SET_NULL)
    tipo_documento = models.ForeignKey(tipo_documento, null=True, blank=True, verbose_name="Tipo de Documento", on_delete=models.SET_NULL)
    sub_tipo_documento = models.ForeignKey(sub_tipo_documento, null=True, blank=True, verbose_name="Sub Tipo de Documento", on_delete=models.SET_NULL)
    res_uno = models.CharField(max_length=150, choices=resguardo, verbose_name="Resguardo uno")
    tim_uno = models.CharField(max_length=150, choices=YEAR_CHOICES, verbose_name="Años del Resguardo uno")
    res_dos = models.CharField(max_length=150, choices=resguardo, verbose_name="Resguardo Dos")
    tim_dos = models.CharField(max_length=150, choices=YEAR_CHOICES, verbose_name="Años del Resguardo Dos")
    res_tres = models.CharField(max_length=150, choices=resguardo, verbose_name="Resguardo Tres")
    tim_tres = models.CharField(max_length=150, choices=YEAR_CHOICES, verbose_name="Años del Resguardo Tres")
    code = models.CharField(max_length=10, null=True, verbose_name="Codigo")
    name = models.CharField(max_length=100, null=True, verbose_name="Nombre")
    disposicion = models.ForeignKey(disposicion, null=True, on_delete=models.SET_NULL, verbose_name="Disposicion Final")
    procedimiento = models.ForeignKey(procedimiento, null=True, on_delete=models.SET_NULL, verbose_name="Procedimiento")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    def total_year(self):
        year = self.tim_uno + self.tim_dos + self.tim_tres
        return year

    def total_mes(self):
        mes = self.total_year * 12
        return mes

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Retencion'
        verbose_name_plural = 'Retenciones'
        db_table = 'Retencion'
        ordering = ['id']

from django.db import models

# Create your models here.
