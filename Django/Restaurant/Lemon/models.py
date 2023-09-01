from django.db import models

# Create your models here.
# Menu Category
# Menu

class MenuCategory(models.Model):
    menu_category = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.menu_category

class Menu(models.Model):
    menu_item = models.CharField(max_length = 200)
    price = models.IntegerField(null = False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)
    desc = models.CharField(max_length = 250)
    def __str__(self) -> str:
        return self.menu_item

# class booking(models.Model):

class book_table(models.Model):
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    people = models.IntegerField()
    date = models.DateField()
    meal = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    timing = models.CharField(max_length=10, choices=meal)
    def __str__(self) -> str:
        return self.first_name
