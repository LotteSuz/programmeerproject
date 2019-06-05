from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/shop", views.shop, name="shop"),
    path("/cart", views.cart, name="cart"),
    path("/timetable", views.timetable, name="timetable"),
    path("/schedule", views.schedule, name="schedule"),
    path("/subscriptions", views.subscriptions, name="subscriptions"),
    path("/register", views.register, name="register")
]
