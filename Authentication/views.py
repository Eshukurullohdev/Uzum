from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # loginni boshqa nom bilan import qilish
from django.contrib.auth import logout as auth_logout

from django.contrib import messages

def login(request):
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