# Generated by Django 5.0.6 on 2024-06-09 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0009_musicianmodel_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicianmodel',
            name='musician',
        ),
    ]