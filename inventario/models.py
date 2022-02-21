from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.contenttypes.models import ContentType
from user.models import *
from etiqueta.models import *
from mrd.models import *
from cedoc.models import *
from inventario.choices import *
import os
import json
from json.decoder import JSONDecodeError
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from user.models import *


# from custodia.login.models import BaseModel

SECURE_MEDIA = os.path.join(settings.BASE_DIR, 'media')
secure_storage = FileSystemStorage(location=SECURE_MEDIA, base_url=None)


def get_media_path(model, filename):
    class_name = model.type.model.__class__.__name__
    code = str(model.key)
    return os.path.join(class_name, code, filename)


OBJECT_STATUS = (

    ('IN', 'En custodia'),
    ('OUT', 'Fuera de custodia'),
    ('DELETE', 'Borrado'),
    ('DESTROYED', 'Destruido'),
    ('TRANSFERRED', 'Transferido'),

    ('PRE ADD', 'En proceso de ingreso'),
    ('ON_DESTRUCTION', 'En proceso de destruccion'),
    ('ON_TRANSFER', 'En transferencia'),
    ('ON_DELETION', 'En procedo de borrado'),
    ('SELECTED', 'En proceso de transferencia'),

    ('TRUCK', 'En solicitud de retiro'),
    ('OUT-BOX', 'Fuera de la caja'),

)


class ObjectStatus:
    IN = 'IN'
    OUT = 'OUT'
    DELETE = 'DELETE'
    DESTROYED = 'DESTROYED'
    TRANSFERRED = 'TRANSFERRED'
    PRE_ADD = 'PRE ADD'
    ON_DESTRUCTION = 'ON_DESTRUCTION'
    ON_TRANSFER = 'ON_TRANSFER'
    ON_DELETION = 'ON_DELETION'
    SELECTED = 'SELECTED'
    TRUCK = 'TRUCK'
    OUT_BOX = 'OUT-BOX'

    @classmethod
    def choices(cls):
        return (cls.IN, 'En custodia'), (cls.OUT, 'Fuera de custodia'), (cls.DELETE, 'Borrado'), \
               (cls.DESTROYED, 'Destruido'), (cls.TRANSFERRED, 'Transferido'), \
               (cls.PRE_ADD, 'En proceso de ingreso'), (cls.ON_DESTRUCTION, 'En proceso de destruccion'), \
               (cls.ON_TRANSFER, 'En transferencia'), (cls.ON_DELETION, 'En procedo de borrado'), \
               (cls.SELECTED, 'En proceso de transferencia'), (cls.TRUCK, 'En solicitud de retiro'), \
               (cls.OUT_BOX, 'Fuera de la caja')


class Caja(models.Model):
    Location = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Bodega")
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede el Cual pertenece", related_name='Cajas')
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,
                             verbose_name="Area el cual pertenece")
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name="Tipo de proceso")
    Retencion = models.ForeignKey(retencion, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Retencion")
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Serie")
    sub_Serie = models.ForeignKey(sub_Serie, on_delete=models.CASCADE, verbose_name="Sub serie")
    tipo_documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE, verbose_name="Tipo de Documento")
    sub_tipo_documento = models.ForeignKey(sub_tipo_documento, null=True, blank=True, on_delete=models.CASCADE,
                                           verbose_name="Sub Tipo de Documento")
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="Descripcion")
    rc = models.BigIntegerField(unique=True, verbose_name="RC")
    Serie_de = models.CharField(max_length=150, null=True, blank=True, verbose_name="Serie de:")
    Serie_hasta = models.CharField(max_length=150, null=True, blank=True, verbose_name="Serie hasta:")
    Mes_de = models.CharField(max_length=20, null=True, blank=True, choices=MONTH_CHOICES, verbose_name="Mes de:")
    Mes_hasta = models.CharField(max_length=20, null=True, blank=True, choices=MONTH_CHOICES, verbose_name="Mes hasta:")
    year_de = models.CharField(max_length=5, null=True, blank=True, choices=YEAR_CHOICES, verbose_name='Año de')
    year_hasta = models.CharField(max_length=5, null=True, blank=True,  choices=YEAR_CHOICES, verbose_name='Año hasta')
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Final")
    status = models.CharField(max_length=50, choices=ObjectStatus.choices(), null=True, blank=True)
    files = models.IntegerField(null=True, blank=True)
    seguridad = models.CharField(max_length=15, choices=SEGURIDAD_CHOICES, default="Interno",
                                 verbose_name='Nivel de Seguridad')
    fun = models.CharField(max_length=15, choices=FUNCIONES_CHOICES, default="Interno",
                           verbose_name='Funciones')
    Sopo = models.CharField(max_length=15, choices=SOPORTE_CHOICES, default="Interno",
                            verbose_name='Soporte')
    ord = models.CharField(max_length=15, choices=ORDENACION_CHOICES, default="Interno",
                           verbose_name='Ordenacion')
    template = models.ForeignKey(FormBox, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="tipo de etiqueta")
    template_data = models.CharField(max_length=10000, null=True, blank=True,
                                      verbose_name="datos de la etiqueta")
    last_out_order = models.IntegerField(null=True, blank=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de salida")

    def __str__(self):
        return '%s' % self.rc

    def usuario_ultima_salida(self):
        if self.last_out_order:
            return self.last_out_order.user
        else:
            return None

    def folders(self):
        return Folder.objects.filter(Caja=self)

    def json_template_data(self):
        try:
            return json.loads(self.template_data)
        except:
            return {}

    def obj_json(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'template_data': self.json_template_data(),
            'status': self.status,
            'Location': self.Location
        }

    @property
    def total_folders(self):
        return self.folders().filter(status__in=['IN', 'OUT']).count()

    @property
    def total_in(self):
        return self.folders().filter(status='IN').count()

    @property
    def total_out(self):
        return self.folders().filter(status='OUT').count()

    @property
    def total_delete(self):
        return self.folders().filter(status='DELETE').count()

    def to_JSON(self):
        item = model_to_dict(self)
        item['template_data'] = self.json_template_data()
        item['Sede'] = self.Sede.name
        item['Location'] = self.Location
        item['Area'] = self.Area.name
        item['Proceso'] = self.Proceso.name
        item['Serie'] = self.Serie.name
        item['sub_Serie'] = self.sub_Serie.name
        item['tipo_documento'] = self.tipo_documento.name
        item['Retencion'] = self.Retencion.name
        item['folders'] = [f.obj_json() for f in self.folders()]
        item['estado'] = self.get_status_display()
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        return item

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
        db_table = 'Caja'
        ordering = ['rc']


class Folder(models.Model):
    Location = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Bodega")
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede el Cual pertenece")
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,
                             verbose_name="Area el cual pertenece")
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name="Tipo de proceso")
    Retencion = models.ForeignKey(retencion, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Retencion")
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Serie")
    sub_Serie = models.ForeignKey(sub_Serie, on_delete=models.CASCADE, verbose_name="Sub serie")
    tipo_documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE, verbose_name="Tipo de Documento")
    sub_tipo_documento = models.ForeignKey(sub_tipo_documento, null=True, blank=True, on_delete=models.CASCADE,
                                           verbose_name="Sub Tipo de Documento")
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="Descripcion")
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, verbose_name="RC Caja")
    rc = models.BigIntegerField(unique=True, verbose_name="RC Folder")
    code = models.CharField(max_length=250, null=True, verbose_name="código / número",
                            help_text="referencia para el cliente")
    Serie_de = models.CharField(max_length=150, null=True, blank=True, verbose_name="Serie de:")
    Serie_hasta = models.CharField(max_length=150, null=True, blank=True, verbose_name="Serie hasta:")
    Mes_de = models.CharField(max_length=20, null=True, blank=True, choices=MONTH_CHOICES, verbose_name="Mes de:")
    Mes_hasta = models.CharField(max_length=20, null=True, blank=True, choices=MONTH_CHOICES, verbose_name="Mes hasta:")
    year_de = models.CharField(max_length=5, null=True, blank=True, choices=YEAR_CHOICES, verbose_name='Año de')
    year_hasta = models.CharField(max_length=5, null=True, blank=True, choices=YEAR_CHOICES, verbose_name='Año hasta')
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha Final")
    status = models.CharField(max_length=50, choices=ObjectStatus.choices(), null=True, blank=True)
    seguridad = models.CharField(max_length=15, choices=SEGURIDAD_CHOICES, default="Interno",
                                 verbose_name='Nivel de Seguridad')
    fun = models.CharField(max_length=15, choices=FUNCIONES_CHOICES, default="Interno",
                           verbose_name='Funciones')
    Sopo = models.CharField(max_length=15, choices=SOPORTE_CHOICES, default="Interno",
                            verbose_name='Soporte')
    ord = models.CharField(max_length=15, choices=ORDENACION_CHOICES, default="Interno",
                           verbose_name='Ordenacion')
    template = models.ForeignKey(FormFile, on_delete=models.SET_NULL, null=True, blank=True,)
    template_data = models.CharField(max_length=10000, null=True, blank=True)
    last_out_order = models.IntegerField(null=True, blank=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de salida")

    def __str__(self):
        return '%s' % self.rc

    def get_end_date(self):
        return self.caja.get_end_date()

    def fecha_ultima_salida(self):
        if self.last_out_order:
            return self.last_out_order.created
        else:
            return None

    def usuario_ultima_salida(self):
        if self.last_out_order:
            return self.last_out_order.user
        else:
            return None

    def documents_count(self):
        return self.Document.all().count()

    def json_template_data(self):
        try:
            return json.loads(self.template_data)
        except:
            return {}

    def obj_json(self):
        try:
            return dict(id=self.id, code=self.code, description=self.descripcion, status=self.status,
                        html_label="",)
        except JSONDecodeError:
            return dict(id=self.id, code=self.code, description=self.descripcion, status=self.status,
                        html_label="", )

    def docs(self):
        return Document.objects.filter(file=self)

    def toJSON(self):
        item = model_to_dict(self)
        item['Sede'] = self.Sede.name
        item['Location'] = self.Location
        item['Area'] = self.Area.name
        item['Proceso'] = self.Proceso.name
        item['Serie'] = self.Serie.name
        item['sub_Serie'] = self.sub_Serie.name
        item['tipo_documento'] = self.tipo_documento.name
        item['caja'] = self.caja.rc
        item['Retencion'] = self.Retencion.name
        item['estado'] = self.get_status_display()
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        if self.template_data:
            item['template_data'] = self.json_template_data()
        return item

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
        db_table = 'Folder'
        ordering = ('rc',)
        unique_together = ('rc', 'Sede')


class Document(models.Model):
    Location = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Bodega")
    Sede = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede el Cual pertenece")
    Area = models.ForeignKey(Area, on_delete=models.CASCADE,
                             verbose_name="Area el cual pertenece")
    Proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, verbose_name="Tipo de proceso")
    Retencion = models.ForeignKey(retencion, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Retencion")
    Serie = models.ForeignKey(Serie, on_delete=models.CASCADE, verbose_name="Serie")
    sub_Serie = models.ForeignKey(sub_Serie, on_delete=models.CASCADE, verbose_name="Sub serie")
    tipo_documento = models.ForeignKey(tipo_documento, on_delete=models.CASCADE, verbose_name="Tipo de Documento")
    sub_tipo_documento = models.ForeignKey(sub_tipo_documento, null=True, blank=True, on_delete=models.CASCADE,
                                           verbose_name="Sub Tipo de Documento")
    descripcion = models.CharField(max_length=300, null=True, blank=True, verbose_name="Descripcion")
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, verbose_name="RC Caja")
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE,  verbose_name="RC folder")
    rc = models.BigIntegerField(unique=True, verbose_name="RC documento")
    Serie_de = models.CharField(max_length=150, null=True, blank=True, verbose_name="Serie de:")
    Mes_de = models.CharField(max_length=20, null=True, blank=True, choices=MONTH_CHOICES, verbose_name="Mes de:")
    year_de = models.CharField(max_length=5, null=True, blank=True, choices=YEAR_CHOICES, verbose_name='Año de')
    mediafile = models.FileField(upload_to="documentos", null=True, blank=True,
                                  storage=secure_storage)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="En Custodia", verbose_name='Estatus')
    template = models.ForeignKey(FormDoc, null=True, blank=True, on_delete=models.SET_NULL)
    template_data = models.CharField(max_length=10000, null=True, blank=True)
    seguridad = models.CharField(max_length=15, choices=SEGURIDAD_CHOICES, default="Interno",
                                 verbose_name='Nivel de Seguridad')
    fun = models.CharField(max_length=15, choices=FUNCIONES_CHOICES, default="Interno",
                                 verbose_name='Funciones')
    Sopo = models.CharField(max_length=15, choices=SOPORTE_CHOICES, default="Interno",
                           verbose_name='Soporte')
    ord = models.CharField(max_length=15, choices=ORDENACION_CHOICES, default="Interno",
                            verbose_name='Ordenacion')
    # scan_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Escaneo')
    # index_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Indexado')
    # index_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Usuario que indexa')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de salida")
    media_file = models.FileField(upload_to=get_media_path, null=True, blank=True,
                                  storage=secure_storage)

    def __str__(self):
        return '%s' % self.rc

    def json_template_data(self):
        try:
            return json.loads(self.template_data)
        except:
            return {}

    def css_class(self):
        if self.mediafile:
            return "pdf-document"
        return "pdf-document-empty"

    def obj_json(self):
        try:
            return dict(id=self.id, description=self.descripcion, status=self.status,
                        html_label="",
                        cssclass=self.css_class(),)
        except JSONDecodeError:
            return dict(id=self.id, description=self.descripcion, status=self.status,
                        html_label="", cssclass=self.css_class())

    def to_json(self):
        item = super().to_json()
        item['Sede'] = self.Sede.name
        item['Location'] = self.Location
        item['Area'] = self.Area.name
        item['Proceso'] = self.Proceso.name
        item['Serie'] = self.Serie.name
        item['sub_Serie'] = self.sub_Serie.name
        item['tipo_documento'] = self.tipo_documento.name
        item['caja'] = self.caja.rc
        item['folder'] = self.folder.rc
        item['estado'] = self.get_status_display()
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        if self.mediafile:
            item['name'] = self.mediafile.name
            item['url'] = reverse('media') + f'?app_label=inventario&model_name=document&primary_key={self.id}'
        else:
            item['name'] = ""
            item['url'] = "#"
        return item

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        db_table = 'Documento'
        ordering = ['rc']


from django.db import models

# Create your models here.
