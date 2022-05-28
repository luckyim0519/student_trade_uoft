from django.shortcuts import render
from django.http import HttpResponse

def home_views(request):
    return render(request, 'index.html')

def category_books_page_views(request):
    return render(request, 'category_books_page/index.html')

def category_clothings_page_views(request):
    return render(request, 'category_clothings_page/index.html')

def category_electronics_page_views(request):
    return render(request, 'category_electronics_page/index.html')

def category_housings_page_views(request):
    return render(request, 'category_housings_page/index.html')

def category_musical_instruments_page_views(request):
    return render(request, 'category_musical_instruments_page/index.html')

def category_sports_page_views(request):
    return render(request, 'category_sports_page/index.html')

def category_stationaries_page_views(request):
    return render(request, 'category_stationaries_page/index.html')

def category_tickets_page_views(request):
    return render(request, 'category_tickets_page/index.html')

def login_page_views(request):
    return render(request, 'login_page/index.html')

def signup_views(request):
    return render(request, 'signup_page/index.html')