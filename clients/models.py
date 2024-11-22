# clients/models.py
from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# Create your models here.
