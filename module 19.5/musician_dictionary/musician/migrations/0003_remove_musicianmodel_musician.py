# Generated by Django 5.0.6 on 2024-06-09 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_remove_musicianmodel_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicianmodel',
            name='musician',
        ),
    ]
