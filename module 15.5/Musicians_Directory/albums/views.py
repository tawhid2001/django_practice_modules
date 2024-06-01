from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def album(request):
    if request.method == 'POST':
        form = forms.albumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.albumForm(request.POST)
    return render(request,'album.html',{'form':form})


def edit_album(request,id):
    album = models.albumsModel.objects.get(pk=id)
    album_form = forms.albumForm(instance = album)
    if request.method == "POST":
        album_form = forms.albumForm(request.POST, instance= album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request,'album.html',{'form':album_form})

def delete_all(request,id):
    album = models.albumsModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')