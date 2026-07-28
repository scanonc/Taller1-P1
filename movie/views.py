from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {
        'name': 'Sebastian Cañon'
    })

def about(request):
    return HttpResponse("About")