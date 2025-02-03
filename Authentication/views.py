from django.shortcuts import render
from .sendmessage import generate_otp
# views.py
from django.shortcuts import render, redirect
from .models import CustomUser
from .sms_uitls import send_sms
from .models import CustomUser
from django.contrib import messages

otp_storage = {}  # Kichik loyihalar uchun vaqtinchalik saqlovchi

def send_otp_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = generate_otp()
        otp_storage[phone_number] = otp  # OTPni vaqtinchalik saqlaymiz
        send_sms(phone_number, f"Sizning OTP kodingiz: {otp}")
        messages.success(request, "SMS yuborildi!")
        return redirect('verify_otp')

    return render(request, 'send_otp.html')


def verify_otp_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        entered_otp = request.POST.get('otp')

        # OTPni tekshirish
        if otp_storage.get(phone_number) == entered_otp:
            messages.success(request, "Muvaffaqiyatli login qildingiz!")
            del otp_storage[phone_number]
            return redirect('home')
        else:
            messages.error(request, "Noto'g'ri OTP!")
    
    return render(request, 'verify_otp.html')
