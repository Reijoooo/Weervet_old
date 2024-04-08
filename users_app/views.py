from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_app.forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.db import models
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
from django.views.generic.detail import DetailView
from django.db import IntegrityError
from django.shortcuts import redirect
from .models import Profile

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
    user = get_object_or_404(User, id=user_id)
    try:
        profile = Profile.objects.get(user=user)
        avatar_url = profile.avatar.url if profile.avatar else '/media/avatar/default.jpg'
    except Profile.DoesNotExist:
        profile = None
        avatar_url = '/media/avatar/default.jpg'  # Убедимся, что переменная всегда определена

    return render(request, 'registration/id.html', {'user': user, 'avatar_url': avatar_url})


def user_settings(request, user_id):
    user = get_object_or_404(User, id=user_id)

    try:
        profile = Profile.objects.get(user=user)
        previous_avatar_path = profile.avatar.path if profile.avatar else None
    except Profile.DoesNotExist:
        profile = None
        previous_avatar_path = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_avatar_path = profile.avatar.path if profile.avatar else None
            if 'delete_avatar' in request.POST:
                # Если пользователь выбрал удалить аватар, удаляем его
                profile.delete_avatar()

            else:
                # Если пользователь загрузил новый аватар, сохраняем его
                form.save()

            # Проверяем, был ли загружен новый аватар, и удалён ли предыдущий
                if new_avatar_path and previous_avatar_path and new_avatar_path != previous_avatar_path:
                    # Проверяем, существует ли файл по указанному пути
                    if os.path.exists(previous_avatar_path):
                        # Удаляем предыдущий аватар из файловой системы
                        os.remove(previous_avatar_path)
        return redirect('user_settings', user_id=user_id)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'registration/settings.html', {'user_id': user_id, 'form': form})

