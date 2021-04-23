from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register),
    path('lob', views.lob, name='lob'),
    path('', views.home, name='home'),
    path('members', views.members, name='members'),
]