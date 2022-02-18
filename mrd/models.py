from crum import get_current_user
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from mrd.choices import *
from inventario.models import *
from user.models import *
from multiselectfield import MultiSelectField as BaseMultiSelect


# from custodia.login.models import BaseModel


class Sede(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de la Sede")
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre de la Sede")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        db_table = 'Sede'
        ordering = ['code']


class Area(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede Cual pertenece")
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre del Area")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de Area")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Sede.name
        return item

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        db_table = 'Area'
        ordering = ['name']


class Proceso(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area Cual pertenece")
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo ")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    @property
    def Sede(self):
        return self.Area.Sede

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Area.Sede.name
        item['Area'] = self.Area.name
        return item

    class Meta:
        verbose_name = 'Proceso'
        verbose_name_plural = 'Procesos'
        db_table = 'Proceso'
        ordering = ['name']


class Serie(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name='Proceso')
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre de la Serie")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de la Serie")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    @property
    def Area(self):
        return self.Proceso.Area

    @property
    def Sede(self):
        return self.Proceso.Sede

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Proceso.Sede
        item['Area'] = self.Proceso.Area
        item['Proceso'] = self.Proceso.name
        return item

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
        db_table = 'Serie'
        ordering = ['id']


class sub_Serie(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name='Serie')
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre de la Sub Serie")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de la Sub Serie")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    @property
    def Proceso(self):
        return self.Serie.Proceso

    @property
    def Area(self):
        return self.Serie.Area

    @property
    def Sede(self):
        return self.Serie.Sede


    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Serie.Proceso.Sede.name
        item['Area'] = self.Serie.Proceso.Area.name
        item['Proceso'] = self.Serie.Proceso.name
        item['Serie'] = self.Serie.name
        return item

    class Meta:
        verbose_name = 'sub Serie'
        verbose_name_plural = 'sub Series'
        db_table = 'sub_Serie'
        ordering = ['id']


class MultiSelectField(BaseMultiSelect):
    def validate(self, value, model_instance):
        pass


def DOCUMENTOS():
    try:
        documento_choices = list()
        for sede in Sede.objects.all():
            documento_choices += sede.tipo_documento()
        return documento_choices
    except:
        return (
            ('', 'Aún no hay Documentos definidos'),
        )



class tipo_documento(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name='Sede de la que pertenece')
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,
                             verbose_name='Area al que pertenece')
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name='Proceso')
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name='Serie')
    sub_Serie = models.ForeignKey(sub_Serie, on_delete=models.CASCADE, verbose_name='Sub Serie')
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre tipo documento")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de tipo documento")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Sede.name
        item['Area'] = self.Area.name
        item['Serie'] = self.Area.Sede.name
        item['Proceso'] = self.Proceso.name
        item['sub_serie'] = self.sub_Serie.name
        return item

    class Meta:
        verbose_name = 'tipo documento'
        verbose_name_plural = 'tipo documento'
        db_table = 'tipo_documento'
        ordering = ['id']


class sub_tipo_documento(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name='Sede de la que pertenece')
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,
                             verbose_name='Area al que pertenece')
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name='Proceso')
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name='Serie')
    sub_Serie = models.ForeignKey(sub_Serie, on_delete=models.CASCADE, verbose_name='Sub Serie')
    tipo_documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE, verbose_name="Nombre tipo documento")
    name = models.CharField(max_length=300, unique=True, verbose_name="Nombre sub tipo documento")
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo de sub tipo documento")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Sede.name
        item['Area'] = self.Area.name
        item['Serie'] = self.Area.Sede.name
        item['Proceso'] = self.Proceso.name
        item['sub_serie'] = self.sub_Serie.name
        item['tipo_documento'] = self.tipo_documento.name
        return item

    class Meta:
        verbose_name = 'Sub tipo documento'
        verbose_name_plural = 'Sub tipos de documentos'
        db_table = 'sub_tipo_documento'
        ordering = ['id']
