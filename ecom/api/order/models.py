from django.db import models
from api.user.models import CustomUser
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    products = models.CharField(max_length=50)
    total_prodcuts = models.CharField(max_length=50, default=0)

    total_amount = models.CharField(max_length=50, default=0)
    transaction_id = models.CharField(max_length=50, default=0)

    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)