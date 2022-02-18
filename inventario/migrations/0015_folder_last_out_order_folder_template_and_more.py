# Generated by Django 4.0.2 on 2022-02-14 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etiqueta', '0001_initial'),
        ('inventario', '0014_caja_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='last_out_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etiqueta.formfile'),
        ),
        migrations.AddField(
            model_name='folder',
            name='template_data',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]