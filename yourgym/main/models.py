from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.IntegerField()

class Stock(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/', default=None)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    available = models.IntegerField(default=None, blank=True)
    color = models.CharField(max_length=255, blank=True)

class Subscription(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    visual = models.ImageField(upload_to='images/', default=None)
    price_month = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=200)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
