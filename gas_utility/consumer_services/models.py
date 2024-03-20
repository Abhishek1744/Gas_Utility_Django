from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_type} - {self.user.username if self.user else 'Anonymous'}"
# class ServiceRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     request_type = models.CharField(max_length=100)
#     description = models.TextField()
#     status = models.CharField(max_length=50, default='Pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.request_type} - {self.user.username}"

class AccountInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    consumption_history = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Account Information"