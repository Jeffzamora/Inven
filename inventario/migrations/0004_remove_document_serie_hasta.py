# Generated by Django 4.0.2 on 2022-02-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_remove_document_deleted_pages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='Serie_hasta',
        ),
    ]
