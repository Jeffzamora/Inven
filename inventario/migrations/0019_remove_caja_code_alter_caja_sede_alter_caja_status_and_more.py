# Generated by Django 4.0.2 on 2022-02-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrd', '0011_remove_area_created_remove_area_updated'),
        ('inventario', '0018_document_media_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='code',
        ),
        migrations.AlterField(
            model_name='caja',
            name='Sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cajas', to='mrd.sede', verbose_name='Sede el Cual pertenece'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='status',
            field=models.CharField(blank=True, choices=[('IN', 'En custodia'), ('OUT', 'Fuera de custodia'), ('DELETE', 'Borrado'), ('DESTROYED', 'Destruido'), ('TRANSFERRED', 'Transferido'), ('PRE ADD', 'En proceso de ingreso'), ('ON_DESTRUCTION', 'En proceso de destruccion'), ('ON_TRANSFER', 'En transferencia'), ('ON_DELETION', 'En procedo de borrado'), ('SELECTED', 'En proceso de transferencia'), ('TRUCK', 'En solicitud de retiro'), ('OUT-BOX', 'Fuera de la caja')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('IN', 'En custodia'), ('OUT', 'Fuera de custodia'), ('DELETE', 'Borrado'), ('DESTROYED', 'Destruido')], default='En Custodia', max_length=15, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='status',
            field=models.CharField(blank=True, choices=[('IN', 'En custodia'), ('OUT', 'Fuera de custodia'), ('DELETE', 'Borrado'), ('DESTROYED', 'Destruido'), ('TRANSFERRED', 'Transferido'), ('PRE ADD', 'En proceso de ingreso'), ('ON_DESTRUCTION', 'En proceso de destruccion'), ('ON_TRANSFER', 'En transferencia'), ('ON_DELETION', 'En procedo de borrado'), ('SELECTED', 'En proceso de transferencia'), ('TRUCK', 'En solicitud de retiro'), ('OUT-BOX', 'Fuera de la caja')], max_length=50, null=True),
        ),
    ]
