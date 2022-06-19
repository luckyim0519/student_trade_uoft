from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from .models import signupModel
from .serializers import signupFormSerializer

from rest_framework.parsers import JSONParser
import json

def signup_pageHome(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login_page/index.html')

@csrf_exempt
def signupAction(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_check']:
            user = signupModel.create_user(username=request.POST['username'],
                                           email=request.POST['email'],
                                           password=request.POST['password'],
                                           )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup_page/index.html')
    return render(request, 'signup_page/index.html')
