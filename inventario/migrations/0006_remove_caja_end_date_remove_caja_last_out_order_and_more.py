# Generated by Django 4.0.2 on 2022-02-11 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_caja_mes_de_alter_caja_mes_hasta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='last_out_order',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='template',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='template_data',
        ),
        migrations.RemoveField(
            model_name='document',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='index_date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='index_user',
        ),
        migrations.RemoveField(
            model_name='document',
            name='scan_date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='template',
        ),
        migrations.RemoveField(
            model_name='document',
            name='template_data',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='last_out_order',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='template',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='template_data',
        ),
    ]