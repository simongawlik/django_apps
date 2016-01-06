from django.shortcuts import render

from blog.models import BlogPost

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})
    
def contact(request):
    return render(request, "contact.html", {})
    
    
