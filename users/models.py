from django.db import models
from datetime import datetime
from django import forms
from adminbackend.models import Product

# Create your models here.


class Customer(models.Model):
    user_id = models.CharField(max_length=20, default='0102')
    first_name = models.CharField(max_length=200, default='First Name')
    last_name = models.CharField(max_length=200, default='Last Name')
    phone = models.CharField(max_length=200, default='Phone')
    email = models.CharField(max_length=250, default='email')
    password = models.CharField(max_length=200, default='null')
    acc_status = models.CharField(max_length=100, default='Account Status')
    reg_date = models.DateTimeField(default=datetime.now, blank=True)


class Order(models.Model):
    product_title = models.CharField(max_length=500)
    order_id = models.CharField(max_length=15, default='585GH938')
    prod_id = models.CharField(max_length=10, default='58509')
    user_id = models.CharField(max_length=15)
    quantity = models.IntegerField()
    product_price = models.IntegerField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    order_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)

    def get_order_by_customer(customer_id):
        return Order.objects.filter(user_id=customer_id)
