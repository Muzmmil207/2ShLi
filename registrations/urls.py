from re import template
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('account/edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('account/password/', PasswordsChangeview.as_view(template_name='registration/change-password.html')),
    path('password-changed', views.password_changed, name="password-changed")
]
