from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_app.forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('user_profile', kwargs={'user_id': user.id}))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remember:
                    request.session.set_expiry(604800)  # Неделя (в секундах)
                return redirect('/')
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    if request.method == 'GET':  # Обрабатываем только GET-запросы для выхода пользователя
        # Выполнить выход из системы
        logout(request)
        # Перенаправить пользователя на главную страницу
        return redirect('/')  # Замените 'home' на имя вашего URL-шаблона главной страницы


def my_account(request, user_id):
    # Получите пользователя по его идентификатору
    user = get_object_or_404(User, id=user_id)
    return render(request, 'registration/id.html', {'User': User})


def user_settings(request, user_id):
    # Получите пользователя по его идентификатору
    user = get_object_or_404(User, id=user_id)
    return render(request, 'registration/settings.html', {'User': User})