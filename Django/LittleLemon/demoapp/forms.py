from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'num_people', 'timing', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
