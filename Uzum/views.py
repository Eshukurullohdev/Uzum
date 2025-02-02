from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import View

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
def navigation(request):
    return render(request, 'navigation.html')

def banner(request):
    return render(request, 'banner.html')