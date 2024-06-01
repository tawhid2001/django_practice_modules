from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.musician,name='musicianPage'),
    path('editMusician/<int:id>',views.edit_musician,name='editMusician'),
]