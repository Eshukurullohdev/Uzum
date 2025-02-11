from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_view, name='register'),
    path('send-sms/', views.send_sms, name='send-sms'),
]