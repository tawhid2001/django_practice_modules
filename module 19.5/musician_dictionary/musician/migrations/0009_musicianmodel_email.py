# Generated by Django 5.0.6 on 2024-06-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0008_remove_musicianmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicianmodel',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
