from calendar import HTMLCalendar

from datetime import datetime, timedelta

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Stock, User


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('product_number', 'description', 'document', 'price',
                  'available', 'color')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('lesson_access',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
