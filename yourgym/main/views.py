from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def shop(request):
    context = {
        "pastas": "this is the shop",
    }
    return render(request, "main/shop.html", context)

def cart(request):
    context = {
        "pastas": "this is the shoppingcart",
    }
    return render(request, "main/cart.html", context)

def timetable(request):
    context = {
        "pastas": "this is the timetable",
    }
    return render(request, "main/timetable.html", context)

def schedule(request):
    context = {
        "pastas": "this is your schedule",
    }
    return render(request, "main/yourschedule.html", context)

def subscriptions(request):
    context = {
        "pastas": "these are the subscriptions",
    }
    return render(request, "main/subscriptions.html", context)

def register(request):
    context = {
        "pastas": "this is the register page",
    }
    return render(request, "main/register.html", context)
