from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # loginni boshqa nom bilan import qilish
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from decouple import config
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def login(request):
    if request.user.is_authenticated:
        messages.info(request, "siz allaqochon royhatan otgansiz")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user) 
            messages.success(request, "Siz Login Sahifaziga keldingiz!")
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)  # Foydalanuvchini sessiyadan chiqarish
    messages.success(request, "Siz Tizimdan muvaffaqiyatli chiqib ketdingiz!")
    return render(request, 'logout.html')


def register_view(request):
    
    if request.user.is_authenticated:
        messages.info(request, "siz allaqochon royhatan otgansiz")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Parol mosligini tekshirish
        if password != password_confirm:
            messages.error(request, "Parollar mos emas!")
            return redirect('register')

        # Emailning unikal bo'lishini tekshirish
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan!")
            return redirect('register')

        # Foydalanuvchini yaratish
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Foydalanuvchini tizimga kiritish
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz va tizimga kirdingiz!")
            return redirect('home')

        messages.error(request, "Autentifikatsiyada xatolik yuz berdi!")
        return redirect('register')
    return render(request, 'register.html')





# Infobip API konfiguratsiyasi
API_URL = "38kp2v.api.infobip.com"
API_KEY = "dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2"  # Infobip API kalitingizni shu yerga qo'ying

API_KEY = config('dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2', default='dcc7509b1aaaf08bf495f03bd9c8f9f2-449022bd-3b9f-48a1-82d0-0e7d306288e2')
@csrf_exempt
def send_sms(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            phone_number = body.get('phone')
            message = body.get('message')

            if not phone_number or not message:
                return JsonResponse({'error': 'Telefon raqami va xabar kerak'}, status=400)

            # Infobip yoki boshqa SMS xizmat integratsiyasi
            print(f"SMS yuborildi: {phone_number} - {message}")

            return JsonResponse({'message': f"{phone_number} raqamiga SMS yuborildi"})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON formatda noto\'g\'ri ma\'lumot'}, status=400)
        # return JsonResponse({'error': "Faqat POST so'rovlari qabul qilinadi"}, status=405)
    return render(request, 'login-sms.html')

    