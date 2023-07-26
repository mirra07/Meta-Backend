from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about,name="about"),
    path('menu/', views.menu, name="menu"),
    path('book_table/', views.book_table, name="bookings"),
]
