from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.TextField()

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    num_people = models.PositiveIntegerField()
    meal = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    timing = models.CharField(max_length=10, choices=meal)
    date = models.DateField()

    def __str__(self):
        return self.name
