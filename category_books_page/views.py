from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.

def post(request):
    if request.method == 'POST':
        return render(request, 'index.html', {'POST': 'SUCCESS POST'})
    if request.method == 'GET':
        return render(request, 'index.html', {'GET': 'SUCCESS GET'})