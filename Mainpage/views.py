from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Dress


def Homepage(request):
    return render(request, 'Homepage.html')


def Pranjul(request):
    dress = Dress.objects.all()
    context = { 'dress':dress }
    return render(request, 'pranjul.html',context)


def Ganesha(request):
    return render(request, 'ganesha.html')


def Lado(request):
    return render(request, 'lado.html')


def Others(request):
    return render(request, 'others.html')
