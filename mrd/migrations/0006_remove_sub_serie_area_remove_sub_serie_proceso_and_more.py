# Generated by Django 4.0.2 on 2022-02-18 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrd', '0005_remove_serie_area_remove_serie_sede'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_serie',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='sub_serie',
            name='Proceso',
        ),
        migrations.RemoveField(
            model_name='sub_serie',
            name='Sede',
        ),
    ]
