from django.shortcuts import render,redirect, get_object_or_404
from .models import BookBoardModel

def index(request):
    all_books = BookBoardModel.objects.all()

    context = {'all_books': all_books}
    return render(request, 'category_books_page/index.html', context)

def detail(request, id):
    book_detail = get_object_or_404(BookBoardModel, pk=id)
    context = {'book_detail': book_detail}
    return render(request, 'category_books_page/detail.html', context)