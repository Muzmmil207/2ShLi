from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name="home"),
    #path('linkDetail/<int:pk>', LinkView.as_view(), name="LinkView0"),


]
