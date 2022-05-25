from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_views , name="home"),
    path('category_books_page', views.category_books_page_views, name ="category_books_page"),
    path('category_clothings_page', views.category_clothings_page_views, name ="category_clothings_page"),
    path('category_electronics_page', views.category_electronics_page_views, name ="category_electronics_page"),
    path('category_housings_page', views.category_housings_page_views, name ="category_housings_page"),
    path('category_musical_instruments_page', views.category_musical_instruments_page_views, name ="category_musical_instruments_page"),
    path('category_sports_page', views.category_sports_page_views, name ="category_sports_page"),
    path('category_stationaries_page', views.category_stationaries_page_views, name ="category_stationaries_page"),
    path('category_tickets_page', views.category_tickets_page_views, name ="category_tickets_page"),
]