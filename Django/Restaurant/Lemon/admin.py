from django.contrib import admin
from .models import Menu, MenuCategory, book_table 


# Register your models here.

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(book_table)