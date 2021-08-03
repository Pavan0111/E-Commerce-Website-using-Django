from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render (request,'shop/index.html')

def about (request):
    return HttpResponse("we are at about")

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def productView (request):
    return HttpResponse("we are at productView")

def checkout (request):
    return HttpResponse("we are at checkout")




