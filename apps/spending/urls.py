from django.urls import path, include
from . import views

urlpatterns = [
    path('open_spend/<int:spending_id>', views.open_spend, name='open_spend'),
    path('registration_spend', views.registration_spend, name='registration_spend'),
]