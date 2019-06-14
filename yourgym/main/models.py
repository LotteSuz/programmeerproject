from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    lesson_access = models.BooleanField(default=False)
    tryout = models.CharField(max_length=200, null=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.IntegerField()

class Stock(models.Model):
    product_number = models.IntegerField(null=True, blank=True, unique=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/', default=None)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    available = models.IntegerField(default=None, blank=True)
    color = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description

class Subscription(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    visual = models.ImageField(upload_to='images/', default=None)
    price_month = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    grouplessons = models.BooleanField(default=False)

class Cart(models.Model):
    user = models.CharField(max_length=64)
    item = models.ManyToManyField(Stock, through='CartItems', through_fields=('cart', 'item'))

class CartItems(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
