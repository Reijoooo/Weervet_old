from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

def user_id(request):

    user_id = None
    avatar_url = '/media/avatar/default.jpg'
    if request.user.is_authenticated:
        user_id = request.user.id
        try:
            profile = Profile.objects.get(user=user_id)
            avatar_url = profile.avatar.url if profile.avatar else '/media/avatar/default.jpg'
        except Profile.DoesNotExist:
            profile = None
            avatar_url = '/media/avatar/default.jpg'  # Убедимся, что переменная всегда определена

    return {'user_id': user_id, 'avatar_url': avatar_url}