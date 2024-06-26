# Generated by Django 5.0.6 on 2024-06-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0006_musicianmodel_musician'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicianmodel',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='musicianmodel',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='musicianmodel',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
