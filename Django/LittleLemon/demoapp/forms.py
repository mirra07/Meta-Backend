from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email', max_length=100)
    people = forms.IntegerField(label='Number of People')
    date = forms.DateField(label='Date of Reseravation') 
    meal = forms.ChoiceField(label='Meal', choices=[
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ])
