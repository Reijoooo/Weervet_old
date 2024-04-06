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
from users_app.views import signup
# from contact_app.views import contact
# from about_app.views import about
from . import templates
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    # path('', include('weervet.urls')),  # Добавьте маршрут к вашим URL-адресам
    #path('', views.index, name='index'),
    # path('/index.html', RedirectView.as_view(url='/weervet/', permanent=True)),
]
