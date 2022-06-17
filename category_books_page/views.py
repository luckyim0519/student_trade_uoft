from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404
from .models import BookBoardModel

def index(request):
    all_books = BookBoardModel.objects.all()
    context = {'all_books': all_books}
    return render(request, 'category_books_page/index.html', context)


#path converter
def detail(request, id):
    try:
        book_detail = BookBoardModel.objects.get(pk=id)
    except BookBoardModel.DoesNotExist:
        raise Http404("Book does not exist")

    context = {'book_detail': book_detail}
    return render(request, 'category_books_page/detail.html', context)