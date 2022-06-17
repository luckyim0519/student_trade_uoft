from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import BookBoardModel
from .forms import BookBoardForm

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


@csrf_exempt
def post(request):
    if request.method == 'POST':
        postform = BookBoardForm(request.POST)
        if postform.is_valid():
            postform.save()
        return redirect('/category_books_page/')
    else:
        postform = BookBoardForm()

    return render(request, 'category_books_page/post.html', {'postform': postform})