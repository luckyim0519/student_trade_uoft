from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate,login,logout

from .forms import UserCreateForm


@csrf_exempt
def signup(request):
    form_class = UserCreateForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        try:
            signup_form = UserCreateForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                print("user data saved into DB")
            else:
                print("user data not saved into DB")
            return render(request, 'default_page/index.html')

        except:
            signup_form = UserCreateForm()
    else:
        signup_form = UserCreateForm()

    return render(request, 'signup_page/index.html', {'signup_form': signup_form})


