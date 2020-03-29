from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"users/home.html",{"title":"Home Page"})

def about(request):
    return render(request,"users/about.html",{"title":"About Page"})