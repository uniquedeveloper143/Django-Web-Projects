from  django.db import models
from .customer import Customer
from .product import Product


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=100, default='', blank=True)


