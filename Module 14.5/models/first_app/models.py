from django.db import models

# Create your models here.

class Mymoder(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    email = models.EmailField()