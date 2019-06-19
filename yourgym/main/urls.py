from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop", views.shop, name="shop"),
    path("cart", views.cart, name="cart"),
    path("timetable", views.timetable, name="timetable"),
    path("schedule", views.schedule, name="schedule"),
    path("subscriptions", views.subscriptions, name="subscriptions"),
    path("register", views.register, name="register"),
    path("stock", views.stock, name="stock"),
    path("order", views.order, name="order"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("orders", views.orders, name="orders"),
    path("ordercomplete/<str:user>", views.ordercomplete, name="ordercomplete"),
    path("events", views.events, name="events"),
    path("enroll", views.enroll, name="enroll"),
    path("yourevents", views.yourevents, name="yourevents")
]
