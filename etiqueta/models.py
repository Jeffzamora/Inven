from crum import get_current_user
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from mrd.models import *
from etiqueta.choices import *
from retencion.models import *
import json
# from custodia.login.models import BaseModel


class BaseForm(models.Model):
    name = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=5, null=True, blank=True, verbose_name="Código")
    active_years = models.PositiveSmallIntegerField(default=10, verbose_name="Años estado activo")
    active_months = models.PositiveSmallIntegerField(default=120, verbose_name="Meses estado activo")
    semiactive_years = models.PositiveSmallIntegerField(default=2, verbose_name="Años estado semi-activo")
    semiactive_months = models.PositiveSmallIntegerField(default=24, verbose_name="Meses estado semi-activo")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BaseField(models.Model):
    FIELDS = (
        ('input', 'Input'),
        ('textarea', 'Textarea'),
    )
    position = models.PositiveSmallIntegerField("Position", null=True)
    name = models.CharField(max_length=255, null=True)
    label = models.CharField(max_length=255, null=True)
    field = models.CharField(max_length=10, choices=FIELDS, null=True)
    show = models.BooleanField(default=False)

    class Meta:

        abstract = True
        ordering = ['position']

    def __str__(self):
        return self.name


class FormBox(BaseForm):

    def fields(self):
        return FieldBox.objects.filter(form=self).order_by('position')

    def to_json(self):
        o = super().to_json()
        o['campos'] = [x.to_json() for x in self.fields()]
        # o['dispositions'] = [x.to_json() for x in self.dispositions.all()]
        return o

    def json_instance(self):
        o = dict()
        for f in self.fields():
            o[f.name] = ''
        return o

    class Meta:
        verbose_name = "record serie"
        verbose_name_plural = "Etiqueta - cajas"
        ordering = ['name', ]


class FieldBox(BaseField):
    form = models.ForeignKey(FormBox, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "campo"
        verbose_name_plural = "campos disponibles"
        ordering = ['name', ]


class FormFile(BaseForm):

    def fields(self):
        return FieldFile.objects.filter(form=self).order_by('position')

    def to_json(self):
        o = super().to_json()
        o['campos'] = [x.to_json() for x in self.fields()]
        # o['dispositions'] = [x.to_json() for x in self.dispositions.all()]
        return o

    def json_instance(self):
        o = dict()
        for f in self.fields():
            o[f.name] = ''
        return o

    class Meta:
        verbose_name = "record serie"
        verbose_name_plural = "Etiquetas folder"


class FieldFile(BaseField):
    form = models.ForeignKey(FormFile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "campo"
        verbose_name_plural = "campos disponibles"


class FormDoc(BaseForm):

    def fields(self):
        return FieldDoc.objects.filter(form=self).order_by('position')

    def to_json(self):
        o = super().to_json()
        o['campos'] = [x.to_json() for x in self.fields()]
        return o

    def json_instance(self):
        o = dict()
        for f in self.fields():
            o[f.name] = ''
        return o

    class Meta:
        verbose_name = "record serie"
        verbose_name_plural = "Etqiueta - Documentos"


class FieldDoc(BaseField):
    form = models.ForeignKey(FormDoc, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "campo"
        verbose_name_plural = "campos disponibles"

