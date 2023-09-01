from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about, name="about"),
    path('reservation/',views.reservation, name="reservation"),
    path('menu/', views.menu, name="menu"),
]
