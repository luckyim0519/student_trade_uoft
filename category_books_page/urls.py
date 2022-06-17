from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='bookHome'),
    path('<int:id>/', views.detail, name="detail")
]