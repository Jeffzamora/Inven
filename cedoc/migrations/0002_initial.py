# Generated by Django 4.0.2 on 2022-02-09 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cedoc', '0001_initial'),
        ('mrd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalbodega',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bodega',
            name='Sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mrd.sede', verbose_name='Sede'),
        ),
    ]