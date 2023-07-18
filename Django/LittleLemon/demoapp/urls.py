from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    #path('',views.drinks),
    path('drinks/<str:drink_name>', views.drinks),
    path('about/', views.about),
    path('booking/', views.booking),
    path('menu/', views.menu),
]