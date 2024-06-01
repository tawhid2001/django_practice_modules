from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.album,name='albumPage'),
    path('edit/<int:id>',views.edit_album,name='edit_album'),
    path('delete/<int:id>',views.delete_all,name='delete_all'),
]