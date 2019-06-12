from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django import forms
from .models import Stock, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('description', 'document', 'price', 'available', 'color' )

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('lesson_access',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
