from django import forms
from .models import Pet
from django.forms import DateTimeInput


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['avatar', 'name', 'sex', 'species', 'breed', 'age',
                  'owner', 'color', 'country', 'city', 'microchip_number',
                  'date_microchip', 'location_microchip', 'tattoo_number',
                  'date_tattoo', 'special_marks', 'reproduction']

        labels = {'avatar': 'Фотография',
                  'name': 'Имя',
                  'sex': 'Пол',
                  'species': 'Вид',
                  'breed': 'Порода',
                  'age': 'Возраст',
                  'owner': 'Владелец ФИО',
                  'color': 'Цвет',
                  'country': 'Страна',
                  'city': 'Город',
                  'microchip_number': 'Номер микрочипа',
                  'date_microchip': 'Дата введения микрочипа',
                  'location_microchip': 'Расположение микрочипа',
                  'tattoo_number': 'Номер клейма',
                  'date_tattoo': 'Дата клеймения',
                  'special_marks': 'Особые отметины или приметы',
                  'reproduction': 'Сведения о репродукции',
                  }

        widgets = {
            'birth_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_microchip': DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_tatoo': DateTimeInput(attrs={'type': 'datetime-local'}),
        }