from django.db import models
from django.contrib.auth.models import User


class VirtualAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    bank_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Account #{self.account_number[:4]}... by {self.user.username}'
