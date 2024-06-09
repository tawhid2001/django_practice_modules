from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MusicianModel(models.Model):
    instruments = (
        ('jazz','Jazz'),
        ('classic','Classic'),
        ('pop','Pop'),
    )
    first_name = models.CharField(max_length=30,default=None)
    last_name = models.CharField(max_length=30,default=None)
    email = models.EmailField(default=None)
    phone_no = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=20,choices=instruments)

    def __str__(self):
        return self.first_name