from django.shortcuts import render
from .models import Uzum
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    uzum = Uzum.objects.all()
    messages.success(request, 'Siz Tizimga muvaffaqiyatli kirdingiz!')
    return render(request, 'home.html' , {'uzums': uzum})


def navigation(request):
    return render(request, 'navigation.html')


def banner(request):
    return render(request, 'banner.html')