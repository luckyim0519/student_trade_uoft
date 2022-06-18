from django.contrib.auth import authenticate
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

