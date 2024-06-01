from django.shortcuts import render,redirect
from .forms import musicianForm
from albums.models import albumsModel
# Create your views here.

def musician(request):
    if request.method == 'POST':
        form = musicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = musicianForm(request.POST)
    return render(request,'musician.html',{'form':form})


def edit_musician(request,id):
    albumCreator = albumsModel.objects.get(pk=id)
    musicianInstance = albumCreator.musician
    musician_form = musicianForm(instance=musicianInstance)

    if request.method == 'POST':
        musician_form = musicianForm(request.POST,instance=musicianInstance)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
        
    return render(request,'musician.html',{'form':musician_form})