from django.shortcuts import render,redirect
from .models import BookBoardModel


def index(request):
    all_books = BookBoardModel.objects.all()
    print(all_books)
    for item in all_books:
        print(item.title)
    context = {'all_books': all_books}
    return render(request, 'category_books_page/index.html', context)