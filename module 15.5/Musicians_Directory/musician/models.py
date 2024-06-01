from django.db import models

# Create your models here.

class musicianModel(models.Model):
    instruments = (
        ('jazz','Jazz'),
        ('classic','Classic'),
        ('pop','Pop'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=20,choices=instruments)

    def __str__(self):
        return self.first_name