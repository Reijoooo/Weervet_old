from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def __str__(self):
        return f'Profile for {self.user_id}'