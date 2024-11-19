from django.db import models
from django.contrib.auth.models import User
from clients.models import ClientType

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone_reserv = models.CharField(max_length=20, blank=True, null=True)
    iin = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    client_type = models.ForeignKey(ClientType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Info"
