# clients/views.py
from django.shortcuts import render
from .models import Client

def home(request):
    return render(request, 'index.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})