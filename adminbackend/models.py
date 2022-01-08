from django.db import models
from datetime import datetime

# Create your models here.


class Feature(models.Model):
    name = models.CharField(max_length=100, default='very fast')
    details = models.CharField(max_length=500, default='something cool')


class Product(models.Model):
    prod_id = models.CharField(max_length=20, default='0102')
    product_title = models.CharField(max_length=200, default='Post title')
    product_price = models.CharField(max_length=200, default='Product Price')
    product_picture = models.ImageField(upload_to='products/', null=True)
    product_category = models.CharField(max_length=100, default='category')
    product_description = models.TextField(default='Post Body')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.product_title

    def get_products_by_id(cart_product_id):
        return Product.objects.filter(prod_id__in=cart_product_id)


class ProductImage(models.Model):
    prod_id = models.CharField(max_length=20, default='0102')
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title
