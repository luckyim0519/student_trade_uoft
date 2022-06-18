from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.signup, name='singup_pageHome'),
    path('login_page', views.login_page, name='login_page'),
]