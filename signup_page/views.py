from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import signupForm
from .serializers import signupFormSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def home_views(request):
    return render(request, 'signup_page/index.html')


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

