from django.db import models
from operator_api.models import Operator


class ClientEntity(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Request(models.Model):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (REJECTED, 'Rejected'),
    ]
    client = models.ForeignKey(ClientEntity, on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Pending')
    processed_by = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
