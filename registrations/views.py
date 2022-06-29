from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
# Create your views here.

class PasswordsChangeview(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password-changed')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('CreateLink')

    def get_object(self):
        return self.request.user


def password_changed(request):
    return render(request ,'registration/password-changed.html')



