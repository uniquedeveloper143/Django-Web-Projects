from django.db import models
from .customer import Customer


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/cart_img/')

