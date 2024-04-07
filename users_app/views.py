from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_app.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(request, '/id/<int:user_id>/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def set_session_expiry(request):
    if request.POST.get('remember_me'):
        # Устанавливаем срок действия куки на неделю (7 дней)
        request.session.set_expiry(604800)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id # Сохраняем ID пользователя в сессии
                user_id = request.auth_user.id if request.user.is_authenticated else None
                render(request, '../context_processors.py', {'user_id': user_id})
                if remember:
                    request.session.set_expiry(set_session_expiry)  # Неделя (в секундах)
                # Redirect to a success page.
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('')


def my_account(request, user_id):
    # Получите пользователя по его идентификатору
    user = get_object_or_404(User, id=user_id)
    return render(request, 'registration/id.html', {'user': user})


# @login_required
# def my_account(request):
#     return render(request, 'registration/id.html')
