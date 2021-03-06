"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)


urlpatterns = [
    #urls to apps
    path('', include('default_page.urls')),
    path('login_page/', include('login_page.urls')),
    path('signup_page/', include('signup_page.urls')),
    path('main_page/', include('main_page.urls')),
    path('category_tickets_page/', include('category_tickets_page.urls')),
    path('category_stationaries_page/', include('category_stationaries_page.urls')),
    path('category_sports_page/', include('category_sports_page.urls')),
    path('category_musical_instruments_page/', include('category_musical_instruments_page.urls')),
    path('category_home_appliances_page/', include('category_home_appliances_page.urls')),
    path('category_electronics_page/', include('category_electronics_page.urls')),
    path('category_clothings_page/', include('category_clothings_page.urls')),
    path('category_books_page/', include('category_books_page.urls')),
    path('category_furniture_page/', include('category_furniture_page.urls')),

    #admin page
    path('admin/', admin.site.urls),
    #restful api page
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
