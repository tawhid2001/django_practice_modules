from django.shortcuts import render,redirect
from albums.models import albumsModel

def home(request):
    data = albumsModel.objects.all()
    return render(request,'home.html',{'data':data})
