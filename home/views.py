from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import short_url2
from .forms import *
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


# class CreateLink(CreateView):
#     model = short_url2
#     form_class = UrlForm
#     template_name =
#     #fields = "__all__"


# class LinkView(DetailView):
#     model = short_url2
#     template_name = 'home/LinkDetail.html'
