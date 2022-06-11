from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import signupForm
from .serializers import signupFormSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json


def login_page_views(request):
    return render(request, 'login_page/index.html')

@csrf_exempt
def signup_list(request):

    if request.method == 'GET':
        print("GET 사인업")
        query_set = signupForm.objects.all()
        serializer = signupFormSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print("사인업 성공!")
        data = JSONParser().parse(request)
        serializer = signupFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def signup_detail(request, pk):

    obj = signupForm.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = signupFormSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = signupFormSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def login(request):
    if request.method =="POST":
        print("request log: "+ str(request.body))
        id = request.POST.get('userid', '')
        pwd = request.POST.get('userpwd', '')
        print("id = "+ id + "pwd =" + pwd)

        result = authenticate(username=id, password=pwd)

        if result:
            print("login successful!")
            return HttpResponse(status=200)
        else:
            print("login failed")
            return HttpResponse(status=401)

    return render(request, 'signup_page/index.html')

