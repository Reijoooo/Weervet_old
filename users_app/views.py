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
    # Получите пользователя по его идентификатору
    user = get_object_or_404(User, id=user_id)
    return render(request, 'registration/id.html', {'User': User})


def user_settings(request, user_id):
    # Получите пользователя по его идентификатору
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Пытаемся получить профиль пользователя
                profile = Profile.objects.get(user=request.user)
                # Если профиль найден, обновляем его данные
                previous_avatar_path = profile.avatar.path
                os.remove(previous_avatar_path)
                profile.avatar = form.cleaned_data['avatar']
                profile.save()
            except Profile.DoesNotExist:
                # Если профиль не найден, создаем новый профиль
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
    else:
        form = ProfileForm()

    return render(request, 'registration/settings.html', {'user_id': user_id, 'form': form})


# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Сохраняем данные профиля
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             # return redirect('profile_updated')  # Редирект на страницу с подтверждением обновления профиля
#     else:
#         form = ProfileForm()
#     return render(request, 'registration/settings.html', {'form': form})


# def upload_avatar(request):
#     if request.method == 'POST':
#         avatar = request.FILES['avatar']
#         # Проверяем, что загруженный файл является изображением
#         if avatar.content_type.startswith('image'):
#             # Путь для сохранения аватара
#             avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
#             # avatar_path = os.path.join(settings.MEDIA_ROOT, 'avatars', avatar.name)
#             # Открываем файл на запись в бинарном режиме и записываем данные
#             with open(avatar_path, 'wb') as f:
#                 for chunk in avatar.chunks():
#                     f.write(chunk)
#             # Далее можно выполнить дополнительные действия с сохраненным файлом,
#             # например, обновить профиль пользователя с ссылкой на аватар
#             # Например:
#             # request.user.profile.avatar = 'avatars/' + avatar.name
#             request.user.profile.save()
#             return render(request, 'registration/id.html', {'avatar_url': '/media/avatars/' + avatar.name})
#         else:
#             # Если файл не является изображением, выводим сообщение об ошибке
#             return render(request, 'registration/settings.html')
#     return render(request, 'registration/settings.html')