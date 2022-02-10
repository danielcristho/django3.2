from django.contrib import admin
from django.urls import path
from .views import index, tentang

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tentang/', tentang),
    path('index', index),
]
