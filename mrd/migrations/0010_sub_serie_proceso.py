# Generated by Django 4.0.2 on 2022-02-18 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrd', '0009_remove_sub_serie_proceso'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_serie',
            name='Proceso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrd.proceso', verbose_name='Proceso'),
            preserve_default=False,
        ),
    ]
