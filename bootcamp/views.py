from django.shortcuts import render
from django.http import HttpResponse
from .models import Relationsips

def home(request):
    return render(request, 'main.html')

def details(request):
    return render(request, 'program-details.html')

def reviews(request):
    context = {
        'posts': Relationsips.objects.all()
    }
    return render(request, 'program-reviews.html', context)

def certificate(request):
    return render(request, 'program-certificate.html')

def signin(request):
    return render(request, 'sign-in.html')

def signup(request):
    return render(request, 'sign-up.html')