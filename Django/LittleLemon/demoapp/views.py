from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def drinks(request, drink_name):
    drink={
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment'
    }
    choice_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_drink)

def menu(request):
    return HttpResponse("Menu for Little Lemon!")

def about(request):
    return HttpResponse("About us")

def booking(request):
    return HttpResponse("Make a booking")
