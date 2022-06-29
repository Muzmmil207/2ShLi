from django.contrib import admin
from .models import *
# Register your models here.


class short_urladmin(admin.ModelAdmin):
    list_display = ['short_url', 'long_url', 'user']


admin.site.register(short_url, short_urladmin)
# ////////////////////

admin.site.site_header = '2ShLi administration'
admin.site.site_title = '2ShLi'
# ///////////////////////
