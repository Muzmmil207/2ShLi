from django import forms
from .models import short_url2
from .shortner import shortner


class UrlForm(forms.ModelForm):

    short_url = forms.CharField(max_length=200)
    long_url = forms.URLField(max_length=200, label='Enter URL:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = short_url2
        fields = ('long_url', 'short_url','qr_code')

        widgets = {
            'short_url': forms.TextInput(attrs={'class': 'form-control'}),
            # 'user': forms.Select(attrs={'class': 'form-control'}),
        }

