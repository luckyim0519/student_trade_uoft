from django.shortcuts import render

# Create your views here.
def home_views(request):
    return render(request, 'category_home_appliances_page/index.html')