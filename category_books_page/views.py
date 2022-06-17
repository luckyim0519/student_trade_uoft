from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import BookBoardModel

def index(request):
    #-id means the most recent post is posted first
    all_books = BookBoardModel.objects.all().order_by('-id')
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

#user posting into DB
def post(request):
    book = BookBoardModel()
    book.title = request.GET.get('title')
    book.content = request.GET.get('content')
    book.pub_date = timezone.datetime.now()
    book.writer = request.GET.get('writer')
    book.save()
    return redirect('/'+str(book.id))

