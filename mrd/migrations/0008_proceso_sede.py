# Generated by Django 4.0.2 on 2022-02-18 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrd', '0007_serie_area_serie_sede_sub_serie_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='Sede',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrd.sede', verbose_name='Sede Cual pertenece'),
            preserve_default=False,
        ),
    ]
