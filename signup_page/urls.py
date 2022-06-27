from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    #path('', views.signup_pageHome, name='singup_pageHome'),
    path(r'', views.signup, name='signup'),
    path('login_page', views.login_page, name='login_page'),
]