from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.Profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('add/',views.AddMusicianCreateView.as_view(),name='add_musician'),
    path('edit/<int:id>/',views.EditMusicianView.as_view(),name='edit_musician'),
    path('delete/<int:id>/',views.DeleteMusicianView.as_view(),name='delete_musician'),
    # path('logout/',views.PageLogoutView.as_view(),name='logout'),
    path('logout/',views.user_logout,name='logout'),
]