from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('home', views.home, name='home'),
    path('search_users/', views.search_users, name='search_users'),
]