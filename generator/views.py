from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    try:
        leng = int(request.GET.get('length', 12))
    except ValueError:
        leng = 14

    if leng > 14:
        leng = 14

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    password = ''
    for x in range(int(leng)):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': password})


def about(request):
    return render(request, 'generator/about.html')
