from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import signupModel
from .serializers import signupFormSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

def signup_pageHome(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login_page/index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            user = signupModel.create_user(email=request.POST["email"] , password=request.POST["password"])
            auth.login(request,user)
        return redirect('/login_page/')
    #when it fails to sign in
    return render(request, 'signup_page/index.html')

