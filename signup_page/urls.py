from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.signupAction, name='signpAction'),
    path('login_page', views.login_page, name='login_page'),
]