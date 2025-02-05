from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('navigation/', views.navigation, name='navigation'),
    path('banner/', views.banner, name='banner'),
]