from django.db import models
from django.contrib.auth import get_user_model
from business.models import Business, Product



class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    businesses = models.ManyToManyField(Business, related_name='transactions')
    products = models.ManyToManyField(Product, related_name='transactions')
    quantity = models.PositiveIntegerField()
    delivery_address = models.CharField(max_length=255)
    delivery_phone_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)