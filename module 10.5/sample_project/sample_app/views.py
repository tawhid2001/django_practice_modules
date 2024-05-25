from django.shortcuts import render
from datetime import datetime,date
# Create your views here.


def home(request):
    d = {'lst':[

        {
            'id':1,
            'course':'python',
            'fee':1000
        },
        {
            'id':2,
            'course':'django',
            'fee':100000
        },
        {
            'id':3,
            'course':'c',
            'fee':10
        }
    ], 'date':datetime.now(), 'postDate' : date(2023, 5, 5) ,'name':'phitron','instructor': 6, 'moto':'Coding is easy','students':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],'val':''}
    return render(request,'sample_app/home.html',d)