from django.shortcuts import render
from .models import Pet
from django.contrib.auth.models import User


def pet_id(request):
    pet_ids = []  # Создаем пустой список для pet_id
    pets = []  # Создаем пустой список для объектов Pet

    # Получаем id пользователя из запроса
    user_id = request.user.id
    user = request.user
    # Получение всех pet_id для данного пользователя из базы данных
    if user_id is not None:
        # Получаем все записи из таблицы Pet для данного пользователя
        # pets = Pet.objects.filter(user_id=user_id)
        pets = Pet.objects.filter(user=user)
        # Извлекаем pet_id из каждой записи и добавляем в список
        pet_ids = [pet.id for pet in pets]

    # Возвращаем словарь, где ключ - это имя переменной, а значение - значение переменной
    return {'pet_ids': pet_ids, 'pets': pets}