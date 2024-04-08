from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PetForm
from .models import Pet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

def my_pets(request, user_id):
    user = get_object_or_404(User, id=user_id)
    pets = Pet.objects.filter(user_id=user_id)  # Фильтрация животных по владельцу (пользователю)

    return render(request, 'pets.html', {'user': user, 'pets': pets})


def add_pets(request, user_id):
    default_user_id = request.user.id if request.user.is_authenticated else None
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user_id = request.user.id  # Установка текущего пользователя как владельца питомца
            pet.save()
            return redirect('../my_pets', user_id=user_id)  # Перенаправление на страницу со списком питомцев
    else:
        form = PetForm()
    return render(request, 'add_pets.html', {'form': form})