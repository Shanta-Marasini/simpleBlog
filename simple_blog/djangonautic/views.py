from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'about.html')        #ignore manin one i.e. templates

def homapage(request):
    return render(request,'homepage.html')