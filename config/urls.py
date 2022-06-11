"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from login_page import views
from signup_page import views
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('default_page.urls')),
    path('login_page/', include('login_page.urls')),
    path('signup_page/', views.signup_list),
    path('signup_page/<str:pk>/', views.signup_detail),
    #path('signup_page/', signaction),
    #path('login_page/', loginaction),
    path('main_page/', include('main_page.urls')),
    path('category_tickets_page/', include('category_tickets_page.urls')),
    path('category_stationaries_page/', include('category_stationaries_page.urls')),
    path('category_sports_page/', include('category_sports_page.urls')),
    path('category_musical_instruments_page/', include('category_musical_instruments_page.urls')),
    path('category_housings_page/', include('category_housings_page.urls')),
    path('category_electronics_page/', include('category_housings_page.urls')),
    path('category_clothings_page/', include('category_clothings_page.urls')),
    path('category_books_page/', include('category_books_page.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
