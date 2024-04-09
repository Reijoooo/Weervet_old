from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings


class Pet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    SEX_CHOICES = [
        ('М', 'Мальчик'),
        ('Д', 'Девочка'),
    ]

    REPRODUCTION_CHOICES = [
        ('К', 'Кастрирован'),
        ('С', 'Стерилизована'),
        ('Н', 'Ничего')
    ]

    # avatar = models.ImageField(upload_to='avatar/pets', null=True, blank=True)
    #
    # name = models.CharField(max_length=100)
    # sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    # species = models.CharField(max_length=50, null=True, blank=True)
    # breed = models.CharField(max_length=100, null=True, blank=True)
    #
    # age = models.IntegerField((), null=True, blank=True)
    #
    # owner = models.CharField(max_length=100, null=True, blank=True)
    # color = models.CharField(max_length=100)
    #
    # country = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    #
    # microchip_number = models.CharField(max_length=50, null=True, blank=True)
    # date_microchip = models.DateField((), null=True, blank=True)
    # location_microchip = models.CharField(max_length=50, null=True, blank=True)
    #
    # tattoo_number = models.CharField(max_length=50, null=True, blank=True)
    #
    # date_tattoo = models.DateField((), null=True, blank=True)
    #
    # special_marks = models.CharField(max_length=150, null=True, blank=True)
    #
    # reproduction = models.CharField(max_length=1, choices=REPRODUCTION_CHOICES, null=True, blank=True)

    avatar = models.ImageField(upload_to='avatar/pets', null=True, blank=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    species = models.CharField(max_length=50, null=True, blank=True)
    breed = models.CharField(max_length=100, null=True, blank=True)

    age = models.IntegerField((), null=True, blank=True)

    owner = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    microchip_number = models.CharField(max_length=50, null=True, blank=True)
    date_microchip = models.DateField((), null=True, blank=True)
    location_microchip = models.CharField(max_length=50, null=True, blank=True)

    tattoo_number = models.CharField(max_length=50, null=True, blank=True)

    date_tattoo = models.DateField((), null=True, blank=True)

    special_marks = models.CharField(max_length=150, null=True, blank=True)

    reproduction = models.CharField(max_length=1, choices=REPRODUCTION_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name