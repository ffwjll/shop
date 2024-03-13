from django.db import models
from core.models import User


# User.objects.create_user()
class Product(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')
    desc = models.TextField()
    price = models.FloatField()
    discount = models.IntegerField()
    rating = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Product {self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
