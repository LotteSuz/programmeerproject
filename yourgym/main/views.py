from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime, timedelta, date
import time
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from mollie.api.client import Client
import os
from .models import *
from .utils import DocumentForm
import flask
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

api_key = os.environ.get('MOLLIE_API_KEY', 'test_test')
mollie_client = Client()
mollie_client.set_api_key('test_TzprvAWd5Dg8xBGBbJstjJCg8x6mhy')

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
        prodnum = request.POST["productnumber"]
        item = Stock.objects.get(product_number=prodnum)
        curruser = request.user
        usercart = Cart.objects.filter(owner=curruser).first()
        if usercart == None:
            newcart = Cart(owner=curruser)
            newcart.save()
            newcartitem = CartItem(item=item, cartowner=newcart, price=item.price, amount=1)
            newcartitem.save()
        else:
            cartitem = CartItem.objects.filter(cartowner=usercart, item=item).count()
            if cartitem == 0:
                newcartitem = CartItem(item=item, cartowner=usercart, price=item.price, amount=1)
                newcartitem.save()
            else:
                currcartitem = CartItem.objects.filter(cartowner=usercart).get(item=item)
                curramount = currcartitem.amount
                newamount = int(curramount) + 1
                currcartitem.amount = newamount
                currcartitem.save()

        products = CartItem.objects.filter(cartowner=usercart).all()
        total = 0
        qty = 0
        for product in products:
            qty += product.amount
            cost = product.amount * product.price
            total += cost
        context = {
            "products": products,
            "user": curruser,
            "total": total,
            "qty": qty
        }
        return render(request, "main/cart.html", context)
    else:
        curruser = request.user
        usercart = Cart.objects.filter(owner=curruser).first()
        products = CartItem.objects.filter(cartowner=usercart).all()
        total = 0
        qty = 0
        for product in products:
            qty += product.amount
            cost = product.amount * product.price
            total += cost
        context = {
            "products": products,
            "user": curruser,
            "total": total,
            "qty": qty
        }
        return render(request, "main/cart.html", context)

def order(request):
    curruser = request.user
    usercart = Cart.objects.filter(owner=curruser).first()
    orderitems = CartItem.objects.filter(cartowner=usercart).all()
    my_webshop_id = int(time.time())
    payment = mollie_client.payments.create({
       'amount': {
             'currency': 'EUR',
             'value': '10.00'
       },
       'description': 'My first payment',
       'webhookUrl': 'https://webshop.example.org/order/12345/',
       'redirectUrl': request.build_absolute_uri(reverse("index")),
       'metadata': {
             'order_id': '12345'
       }
    })
    for item in orderitems:
        stockitem = Stock.objects.get(cart=item)
        product_number = stockitem.product_number
        itemname = stockitem.description
        price = item.price
        amount = item.amount
        new = Order(user=curruser, product_number=product_number, item=itemname, price=price, amount=amount)
        new.save()
    CartItem.objects.filter(cartowner=usercart).delete()
    return redirect(payment.checkout_url)

def orders(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "main/orders.html", context)

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
        subscription = request.POST["subscription"]
        print(f"subscription1 = {subscription}")

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

        access = Subscription.objects.get(title=subscription).grouplessons
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.lesson_access = access
        user.save()
        return render(request, "main/login.html", {"message":"Registered. You can log in now."})
    else:
        type = request.GET["subtype"]
        context = {
            "subscription_type" : type
        }
        return render(request, "main/register.html", context)

def timetable(request):
    return render(request, "main/timetable.html")

@csrf_exempt
def events(request):
    list = []
    events = Event.objects.all()
    for event in events:
        dict = {"id": event.id, "title": event.title, "start": event.start}
        list.append(dict)

    return JsonResponse(list, safe=False)

@csrf_exempt
def yourevents(request):
    curruser = request.user
    list = []
    events = Event.objects.filter(participant__user=curruser)
    for event in events:
        dict = {"id": event.id, "title": event.title, "start": event.start}
        list.append(dict)

    return JsonResponse(list, safe=False)

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

def ordercomplete(request, user):
    Order.objects.filter(user=user).delete()
    return redirect("orders")

def enroll(request):
    curruser = request.user
    groepsid = request.POST["eventid"]
    eventobj = Event.objects.get(id=groepsid)
    try:
        part = Participant.objects.get(user=curruser)
    except Participant.DoesNotExist:
        participation = Participant(user=curruser)
        participation.save()
        part = Participant.objects.get(user=curruser)
    part.session.add(eventobj)
    part.save()
    return redirect("index")
