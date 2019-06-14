from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, Stock, Subscription, Cart, User, CartItems
from .utils import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = UserAdmin.fieldsets + (
                                    ('Access to group lessons', {'fields': ('lesson_access',)}),
    )

class CartItemsInLine(admin.TabularInline):
    model = CartItems
    extra = 1

class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemsInLine,)

# Register your models here.
admin.site.register(Event)
admin.site.register(Stock)
admin.site.register(Subscription)
admin.site.register(Cart, CartAdmin)
admin.site.register(User, CustomUserAdmin)
