# Generated by Django 4.0.2 on 2022-02-21 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrd', '0010_sub_serie_proceso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='created',
        ),
        migrations.RemoveField(
            model_name='area',
            name='updated',
        ),
    ]