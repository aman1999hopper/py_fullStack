from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'products/home.html')

def members(request):
    return HttpResponse("Hello world!")