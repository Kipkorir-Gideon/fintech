from django.db import models
from django.contrib.auth.models import User



class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'currency')
        
    def __str__(self):
        return f'{self.currency} Wallet for {self.user.username}'
