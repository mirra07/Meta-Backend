from django.shortcuts import render, redirect
from .models import Dish
from .forms import BookingForm

def home(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, 'home.html', {'about': about_content})

def about(request):
    content={'Us': "At Little Lemon, we bring you an authentic taste of Italy right to your table. Step into our warm and inviting restaurant, where the tantalizing aroma of freshly prepared Italian delicacies will transport you straight to the charming streets of Italy. Our chefs take pride in crafting every dish with the finest and freshest ingredients, ensuring an unforgettable dining experience. From classic pasta dishes to wood-fired pizzas, our menu offers a wide array of mouthwatering options that cater to all tastes. Come and experience the passion, artistry, and flavors that define Italian cooking. We can't wait to welcome you to Little Lemon, where every bite tells a story of Italy.Buon Appetito!"}
    return render(request,'about.html',{'Us':content})

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data and redirect to the confirmation page
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            num_people = form.cleaned_data['num_people']
            date = form.cleaned_data['date']
            meal = form.cleaned_data['meal']

            return render(request, 'confirmation.html', {
                'name': name,
                'phone': phone,
                'email': email,
                'people': num_people,
                'date': date,
                'meal': meal,
            })
    else:
        form = BookingForm()

    return render(request, 'book_table.html', {'form': form})
