from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_views , name="home"),
    path('login_page', views.login_page_views, name='login_page'),
]