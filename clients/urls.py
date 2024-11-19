# clients/urls.py
from django.urls import path
from .views import client_list

urlpatterns = [
    path('', client_list, name='client_list'),
]
