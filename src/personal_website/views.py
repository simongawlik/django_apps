from django.shortcuts import render

from blog.models import BlogPost

def about(request):
    return render(request, "about.html", {})
    

def contact(request):
    return render(request, "contact.html", {})
    

def home(request):
    return render(request, "home.html", {})