from django.shortcuts import render, redirect
from .models import short_url
from .forms import UpdateUrl, UrlForm
from .shortner import *
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy



def home(requset):
    #img = short_url.objects.get(id=int)
    form = UrlForm(requset.POST)
    a = ""
    if requset.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = 'invalid URL'
    return render(requset, 'account/home.html', {"form":form, "a":a})



def TheLink(requset, token):
    long_url = short_url.objects.filter(short_url= token)[0] 
    return redirect(long_url.long_url)

# VIEWS//////////////////////////////////////////////////a



class CreateLink(CreateView):
    model =  short_url
    form_class = UrlForm
    template_name = 'account/CreateLink.html'
    #fields = "__all__"

class LinkView(DetailView):
    model = short_url
    template_name = 'account/LinkView.html'


class homeview(ListView):
    model = short_url
    template_name = 'account/LinksView.html'
    ordering = ['-id']




class DeleteLink(DeleteView):
    model = short_url
    template_name = 'account/DeleteLink.html'
    success_url = reverse_lazy('CreateLink')





class UpdateLink(UpdateView):
    model = short_url
    form_class = UpdateUrl
    template_name = 'account/UpdateLink.html'
    #fields = ('long_url')