# Generated by Django 4.0.2 on 2022-02-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_alter_caja_descripcion_alter_document_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de salida'),
        ),
    ]
