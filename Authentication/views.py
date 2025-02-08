from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # loginni boshqa nom bilan import qilish
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user) 
            print('ohshadi')# to'g'ri login chaqiruv
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
            return redirect('login')

    return render(request, 'login.html')
