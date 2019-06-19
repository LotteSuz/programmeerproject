from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    lesson_access = models.BooleanField(default=False)
    tryout = models.CharField(max_length=200, null=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
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
    owner = models.CharField(max_length=64)
    items = models.ManyToManyField(Stock, through='CartItem', related_name='itemtype')

class CartItem(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='cart')
    cartowner = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    amount = models.IntegerField(default=1)

class Order(models.Model):
    user = models.CharField(max_length=64)
    product_number = models.IntegerField(null=True, blank=True)
    item = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    amount = models.IntegerField(default=1)

class Participant(models.Model):
    user = models.CharField(max_length=200)
    session = models.ManyToManyField(Event, blank=True, related_name='participant')
