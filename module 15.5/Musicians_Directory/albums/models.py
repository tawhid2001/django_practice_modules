from django.db import models
from musician.models import musicianModel

# Create your models here.

class albumsModel(models.Model):
    choices_rating = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    album_name = models.TextField()
    musician = models.ForeignKey(musicianModel, on_delete=models.CASCADE)
    release_date = models.DateField()
    ratings = models.IntegerField(choices=choices_rating)

    def __str__(self):
        return self.album_name