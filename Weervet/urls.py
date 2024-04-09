"""
URL configuration for Weervet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import home_page_app
from home_page_app.views import index
from users_app.views import register, user_logout, user_login, my_account, user_settings
from about_app.views import about
from contact_app.views import contact
from my_pets_app.views import my_pets, add_pets, pet_info, pet_edit, pet_delete
from schedule.views import event_list, event_detail, create_event, edit_event, delete_event, ajax_event_list
from . import templates
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Основное
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    # Регистрация/авторизация
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Аккаунт и настройка
    path('id/<int:user_id>/', my_account, name='user_profile'),
    path('id/<int:user_id>/settings/', user_settings, name='user_settings'),

    # Информационные ссылки
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # Мои животные
    path('id/<int:user_id>/my_pets/', my_pets, name='pets'),
    path('id/<int:user_id>/my_pets/add_pets', add_pets, name='add_pets'),
    path('id/<int:user_id>/pet/id/<int:pet_id>', pet_info, name='pet_info'),
    path('id/<int:user_id>/pet_edit/id/<int:pet_id>', pet_edit, name='pet_edit'),
    path('id/<int:user_id>/pet_delete/id/<int:pet_id>', pet_delete, name='pet_delete'),

    # Календарь
    # path('id/<int:user_id>/my_calendar/', my_calendar, name='my_calendar'),

    path('id/<int:user_id>/event/', event_list, name='event_list'),  # Главная страница с календарем
    path('id/<int:user_id>/event/<int:event_id>/', event_detail, name='event_detail'),  # Страница деталей события
    path('id/<int:user_id>/event/add/', create_event, name='create_event'),  # Страница добавления события
    path('id/<int:user_id>/event/<int:event_id>/edit/', edit_event, name='edit_event'),  # Страница редактирования события
    path('id/<int:user_id>/event/<int:event_id>/delete/', delete_event, name='delete_event'),  # Удаление события
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)