from django.urls import path
from . import views
from .views import *
urlpatterns = [
   # path('j/', views.home, name="home"),
    path('', CreateLink.as_view(), name="CreateLink"),
    path('All-Links', homeview.as_view(), name="LinksView"),
    path('linkDetail/<int:pk>/DeleteLink', DeleteLink.as_view(), name="DeleteLink"),
    path('linkDetail/UpdateLink/<int:pk>', UpdateLink.as_view(), name="UpdateLink"),
    path('linkDetail/<int:pk>', LinkView.as_view(), name="LinkView"),
    #path('home/', views.home, name="hhhh")
]
