from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django import forms
from .models import Stock


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('description', 'document', )
