from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('home', views.home, name='home'),
]