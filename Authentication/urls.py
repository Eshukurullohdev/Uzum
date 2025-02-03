from django.urls import path
from . import views


urlpatterns = [
    path('sent_otp/', views.send_otp_view, name='index'),
    path('verify_otp/', views.verify_otp_view, name='verify_otp'),
]