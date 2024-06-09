# Generated by Django 5.0.6 on 2024-06-09 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('musician', '0006_musicianmodel_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='musician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musician.musicianmodel'),
        ),
    ]
