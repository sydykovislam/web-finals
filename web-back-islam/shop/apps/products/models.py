from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='product name')
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    name = models.CharField(max_length = 255, db_index=True, verbose_name='product item name')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_img', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name