from django.db import models

from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.user.username.capitalize()} added {self.product.title} -> {self.quantity}"
    
    @property
    def sub_total(self):
        return self.product.price * self.quantity
