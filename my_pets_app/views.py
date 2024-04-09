from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PetForm
from .models import Pet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone


def my_pets(request, user_id):
    user = request.user
    pets = Pet.objects.filter(user=user)

    return render(request, 'pets.html', {'user': user, 'pets': pets})


def add_pets(request, user_id):
    default_user_id = request.user.id if request.user.is_authenticated else None
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user_id = request.user.id  # Установка текущего пользователя как владельца питомца

            # Проверяем, был ли передан файл изображения
            if 'avatar' not in request.FILES:
                # Если изображение не передано, устанавливаем стандартное изображение
                pet.avatar = 'avatar/pets/default.jpeg'

            pet.save()
            return redirect('../my_pets', user_id=user_id)  # Перенаправление на страницу со списком питомцев
    else:
        form = PetForm()
    return render(request, 'add_pets.html', {'form': form})


def pet_info(request, user_id, pet_id):
    user = get_object_or_404(User, id=user_id)
    pet = get_object_or_404(Pet, id=pet_id)
    pets = Pet.objects.filter(user_id=user_id)
    return render(request, 'pet_info.html', {'pet': pet, 'user': user})


def pet_edit(request, user_id, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)  # Передаем существующий экземпляр питомца
        if form.is_valid():
            form.save()  # Сохраняем форму
            return redirect('pet_info', user_id=user_id,
                            pet_id=pet_id)  # Перенаправляем на страницу информации о питомце
    else:
        form = PetForm(instance=pet)  # Создаем форму с существующими данными питомца
    return render(request, 'pet_edit.html', {'form': form, 'user_id': user_id, 'pet_id': pet_id})

def pet_delete(request, user_id, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('../../my_pets', user_id=user_id)
    return render(request, 'pet_delete.html', {'pet': pet})