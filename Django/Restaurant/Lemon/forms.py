from django import forms 
from .models import book_table

class Booking(forms.ModelForm):
    
    class Meta:
        model = book_table
        fields = '__all__' 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    