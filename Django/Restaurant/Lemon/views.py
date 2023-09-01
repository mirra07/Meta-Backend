from django.shortcuts import render
from Lemon.forms import Booking
from .models import Menu
# Create your views here.

def reservation(request):    
    form = Booking()
    if request.method == 'POST':
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        people = form.cleaned_data['people']
        date = form.cleaned_data['date']
        meal = form.cleaned_data['timing']

        return render(request, 'confirmation.html', {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'people': people,
                'date': date,
                'meal': meal,
            })
    context = {"form": form}
    return render(request, "reservation.html", context)

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def menu(request):
    newmenu = Menu.objects.all()
    menu_dict = {'menu': newmenu}
    return render(request, 'menu.html', menu_dict)

