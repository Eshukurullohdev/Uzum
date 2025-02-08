from django.shortcuts import render
from .models import Uzum



def home(request):
    uzum = Uzum.objects.all()
    return render(request, 'home.html' , {'uzums': uzum})


def navigation(request):
    return render(request, 'navigation.html')


def banner(request):
    return render(request, 'banner.html')