from unicodedata import name
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .cart import Cart_ses
from apps.products.models import ProductItem


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} cart"

    @receiver(post_save, sender=User)
    def create_user_cart(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(user=instance)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_in_cart')
    amount = models.PositiveIntegerField(default=1, blank=True)
    url = models.IntegerField()
    name = models.CharField(max_length = 100, blank=True)
    image = models.CharField(max_length = 100, blank=True)
    price = models.CharField(max_length = 100, blank=True)
    total_price = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return f"{self.cart.id} = product item"

    
        