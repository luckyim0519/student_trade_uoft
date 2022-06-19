from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

from .models import User
from rest_framework.parsers import JSONParser
import json


def signup_pageHome(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        password_check = request.POST.get['password_check']
        res_data = {}

        if not (username and email and password and password_check):
            res_data['error'] = "Enter all the fields"
        if password != password_check:
            res_data['error'] = 'Password is not matching'
        else:
            print(username)
            user = User(username=username, password=make_password(password))
            user.save()
    return render(request, 'signup_page/index.html',res_data)


def login_page(request):
    return render(request, 'login_page/index.html')


