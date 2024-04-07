from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_app.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/id/<int:user_id>/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base.html', {'user': user})
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
