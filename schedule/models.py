from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class MyEvent(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    # creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False, blank=True, null=True)
    # creator_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False, blank=True, null=True)

    def __str__(self):
        return self.title