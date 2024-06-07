from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.editUser,name='edit'),
    path('profile/changepassword',views.changepassword,name='change_password'),
    path('profile/changepassword2',views.changepasswordwoutold,name='changepasswordwoutold'),
]
