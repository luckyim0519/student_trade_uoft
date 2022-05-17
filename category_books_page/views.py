from django.shortcuts import render

# Create your views here.
def home_views(request):
    return render(request, 'category_books_page/index.html')