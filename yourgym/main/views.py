from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    context = {
        "pastas": "if you see this it works",
    }
    return render(request, "main/index.html", context)
