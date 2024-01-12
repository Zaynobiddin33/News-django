from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def allnews(request):
    context = {}
    return render(request, 'front/allnews.html', context)

def category(request):
    context = {}
    return render(request, 'front/category.html', context)

def contact(request):
    
    context = {}
    return render(request, 'front/contact.html', context)

def details(request):
    context = {}
    return render(request, 'front/details.html', context)