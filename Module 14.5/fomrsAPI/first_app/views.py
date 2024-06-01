from django.shortcuts import render
from .forms import TestForm

# Create your views here.


def home(request):
    form = TestForm
    return render(request,'index.html',{'form':form})