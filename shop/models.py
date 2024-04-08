from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone


UserModel = get_user_model()


# class Item(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE, default=timezone.now)
#     name = models.CharField(max_length=50, default="")
#     description = models.TextField(default="")
#     price = models.FloatField(null=True, blank=True)
#     category = models.TextField(default="")
#     image = models.ImageField(upload_to="item_images/")
#
#     class Meta:
#         unique_together = ('user', 'name')
#
#     def __str__(self):
#         return self.name

class Item(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    price = models.FloatField(null=True, blank=True)
    category = models.TextField(default="")
    image = models.ImageField(upload_to="item_images/")

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, default=timezone.now)
    total = models.FloatField()
    quantity = models.IntegerField()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="item_images/")
    price = models.FloatField()
    user = models.ForeignKey(UserModel, default=1, null=True, on_delete=models.SET_NULL)
