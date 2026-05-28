from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at Chai aur Django Home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You are at Chai aur Django About page.")

def contact(request):
    return HttpResponse("Hello, world. You are at Chai aur Django Contact page.")
