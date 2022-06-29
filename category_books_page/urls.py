from django.urls import path
from django.contrib import admin
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='bookHome'),
    path('detail/<int:id>', views.detail, name="detail"),
    path('post/', views.post, name="post"),
]

# Access image path
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
