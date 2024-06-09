from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import SignupForm,MusicianForm
from . import models

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('homepage')
    else:
        user_form = SignupForm()
    
    return render(request, 'signup.html', {'user_form': user_form})

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)
    

@login_required
def Profile(request):
    return render(request,'profile.html')


@method_decorator(login_required,name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self,form):
        return super().form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class EditMusicianView(UpdateView):
    model = models.MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


class DeleteMusicianView(DeleteView):
    model = models.MusicianModel
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
    

# class PageLogoutView(LogoutView):
#     next_page = reverse_lazy('signup')

#     def dispatch(self, request, *args, **kwargs):
#         print(f"User {request.user} is logging out")
#         return super().dispatch(request, *args, **kwargs)

def user_logout(request):
    logout(request)
    return redirect('signup')