from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home_views),
    path('login_page', views.login_page_views, name='login_page'),
]