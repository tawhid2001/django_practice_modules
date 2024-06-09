from django.shortcuts import render,redirect
from album.models import MusicianModel,AlbumModel


def home(request):
    musician = MusicianModel.objects.all()
    album = AlbumModel.objects.all()
    return render(request, 'home.html',{'musician':musician,'album':album})


