# Generated by Django 4.0.2 on 2022-02-14 21:01

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etiqueta', '0001_initial'),
        ('inventario', '0015_folder_last_out_order_folder_template_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='last_out_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='caja',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etiqueta.formbox', verbose_name='tipo de etiqueta'),
        ),
        migrations.AddField(
            model_name='caja',
            name='template_data',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='datos de la etiqueta'),
        ),
        migrations.AddField(
            model_name='document',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de salida'),
        ),
        migrations.AddField(
            model_name='document',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etiqueta.formdoc'),
        ),
        migrations.AddField(
            model_name='document',
            name='template_data',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de salida'),
        ),
        migrations.AlterField(
            model_name='document',
            name='media_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url=None, location='D:\\PROJECT\\inventario\\app\\media'), upload_to='documentos'),
        ),
    ]
