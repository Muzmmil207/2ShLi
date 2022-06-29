from django import forms
from .models import short_url
from .shortner import *
import random


class UrlForm(forms.ModelForm):

    a = shortner().issue_token()

    short_url = forms.CharField(max_length=200, initial=a)
    long_url = forms.URLField(max_length=200, label='Enter URL:',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = short_url
        fields = ('long_url', 'short_url', 'user')

        widgets = {
            'short_url': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'hidden': ''}),
            # 'user': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateUrl(forms.ModelForm):
    class Meta:
        model = short_url
        fields = ('short_url', 'long_url')

        widgets = {
            'long_url': forms.TextInput(attrs={'class': 'form-control'}),
            'short_url': forms.TextInput(attrs={'class': 'form-control'}),

        }
