from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Перенаправление на страницу успеха или другую страницу после входа.
            return redirect('success_page_url_name')
        else:
            # Возвращение сообщения об ошибке при неверном входе.
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    # Если метод запроса не POST или аутентификация не удалась, возвращаем страницу входа.
    return render(request, 'login.html')
