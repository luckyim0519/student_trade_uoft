from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home_views(request):
    return render(request, 'login_page/index.html')
#put csrf_exempt to ensure that when you make a request via a form you
#want the form being submitted to your view to originate from your website and not come from
#other domain
@csrf_exempt
def login(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request))
        email = request.POST.get('user-email','')
        pwd = request.POST.get('user-pwd','')
        print("id =" + email + "pw = " + pwd)
    return render(request, 'login_page/index.html')