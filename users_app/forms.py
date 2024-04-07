from django import forms
from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUser(AbstractUser):
    # ваша собственная логика модели CustomUser

    class Meta:
        # ваша собственная конфигурация модели
        pass

    # Добавьте related_name для обратной связи с группами
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    # Добавьте related_name для обратной связи с разрешениями пользователей
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    remember = forms.BooleanField(label='Запомнить меня', required=False)
    class Meta:
        model = User
        fields = ('username', 'password')
