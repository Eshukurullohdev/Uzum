from django.shortcuts import render
from .models import Uzum
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decouple import config

@login_required(login_url='login')
def home(request):
    uzum = Uzum.objects.all()
    return render(request, 'home.html' , {'uzums': uzum})

def navigation(request):
    return render(request, 'navigation.html')

def banner(request):
    return render(request, 'banner.html')


API_URL = "38kp2v.api.infobip.com"
API_KEY = "dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2"  # Infobip API kalitingizni shu yerga qo'ying

API_KEY = config('dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2', default='dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2')