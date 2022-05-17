from django.shortcuts import render
from django.http import HttpResponse


def home_views(request):
    return render(request, 'default_page_template/index.html')
