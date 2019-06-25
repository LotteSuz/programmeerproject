from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("subscriptions", views.subscriptions, name="subscriptions"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("stock", views.stock, name="stock"),
    path("shop", views.shop, name="shop"),
    path("cart", views.cart, name="cart"),
    path("order", views.order, name="order"),
    path("payment/<int:userid>", views.payment, name="payment"),
    path("orders", views.orders, name="orders"),
    path("ordercomplete/<str:user>", views.ordercomplete,
         name="ordercomplete"),
    path("timetable", views.timetable, name="timetable"),
    path("events", views.events, name="events"),
    path("enroll", views.enroll, name="enroll"),
    path("schedule", views.schedule, name="schedule"),
    path("yourevents", views.yourevents, name="yourevents"),
    path("members", views.members, name="members"),
]
