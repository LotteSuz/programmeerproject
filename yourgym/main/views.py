from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import DocumentForm

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def shop(request):
    context = {
        "items": Stock.objects.all(),
    }
    return render(request, "main/shop.html", context)

def cart(request):
    if request.method == "POST":
        product = request.POST["productname"]
        curruser = request.user
        try:
            item = Cart.objects.filter(user=curruser).get(item=product)
            item.amount = int(item.amount) + 1
            item.save()
        except:
            item = Stock.objects.get(name=product)
            amount = 1
            new = Cart(user=curruser, item=item.description, price=item.price, amount=amount)
            new.save()
        total = 0
        qty = 0
        products = Cart.objects.filter(user=curruser)
        for item in products:
            amount += item.amount
            total += item.price
        context = {
            "products": products,
            "user": curruser,
            "total": total,
            "qty": qty
        }
        return render(request, "main/cart.html", context)
    else:
        curruser = request.user
        total = 0
        qty = 0
        products = Cart.objects.filter(user=curruser)
        for item in products:
            qty += 1
            total += item.price
        context = {
            "products": products,
            "user": curruser,
            "total": total,
            "qty": qty
        }
        return render(request, "main/cart.html", context)

def order(request):
    return redirect('index')

def schedule(request):
    context = {
        "pastas": "this is your schedule",
    }
    return render(request, "main/yourschedule.html", context)

def subscriptions(request):
    context = {
        "subscriptions": Subscription.objects.all(),
    }
    return render(request, "main/subscriptions.html", context)

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if not request.POST["first_name"] or not request.POST["last_name"] or not request.POST["username"]:
            return render(request, "register.html", {"message":"You must provide a full name and username."})
        elif not request.POST["email"]:
            return render(request, "register.html", {"message":"You must provide an emailadress."})
        elif not request.POST["password"] or not request.POST["password2"]:
            return render(request, "register.html", {"message":"You must provide a password."})
        elif not password == password2:
            return render(request, "register.html", {"message":"Your password and confirmation should be the same."})

        if User.objects.filter(email=email).exists():
             return render(request, "main/login.html", {"message":"An account with this emailadress already exists, please log in."})

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, "main/login.html", {"message":"Registered. You can log in now."})
    else:
        type = request.GET["subtype"]
        context = {
            "subscription_type" : type
        }
        return render(request, "main/register.html", context)

def timetable(request):
    context = {
        "workouts": Event.objects.all(),
    }
    return render(request, "main/timetable.html", context)

def stock(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, request.POST, request.POST, request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = DocumentForm()
    return render(request, 'main/stock.html', {
        'form': form
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "main/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "main/login.html")


def logout_view(request):
    logout(request)
    return render(request, "main/login.html", {"message": "Logged out."})
