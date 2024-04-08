from django.contrib.auth.models import User
import os
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def __str__(self):
        return f'Profile for {self.user_id}'

    def delete_avatar(self):
        # Удаляем файл аватара, если он существует

        if self.avatar:
            # Удаляем путь к файлу из базы данных и сам файл из хранилища
            self.avatar.delete(save=False)
