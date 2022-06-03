from django.shortcuts import render

# Create your views here.
def home_views(request):
    return render(request, 'signup_page/index.html')

def login_page_views(request):
    return render(request, 'login_page/index.html')
