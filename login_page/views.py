from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


#django built-in login and logout system
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


def home_views(request):
    return render(request, 'login_page/index.html')


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #if the login is successful, then redirect to the defaul_page
            return redirect('/')
        else:
            return render(request, 'signup_page/login_index.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'signup_page/login_index.html')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('default_page/index.html')
