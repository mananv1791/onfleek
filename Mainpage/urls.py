from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage),
    path('pranjul.html', views.Pranjul),
    path('ganesha.html', views.Ganesha),
    path('lado.html', views.Lado),
    path('others.html', views.Others),
]
