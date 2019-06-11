from django.contrib import admin
from .models import Event, Stock, Subscription, Profile

# Register your models here.
admin.site.register(Event)
admin.site.register(Stock)
admin.site.register(Subscription)
admin.site.register(Profile)
