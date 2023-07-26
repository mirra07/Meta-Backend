from django import forms
from .models import Booking


class BookingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number'}))
    email = forms.CharField(widget=forms.EmailField(attrs={'placeholder': 'Your Email'}))
    num_people = forms.CharField(widget=forms.IntegerField)
    date = forms.DateField(widget=forms.TextInput)
    meal = forms.CharField(widget=forms.ChoiceField, choices=[
        ('Breakfast', 'Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
    ])