from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'Blog/home.html')

def about(request):
    return render(request, 'Blog/about.html')
