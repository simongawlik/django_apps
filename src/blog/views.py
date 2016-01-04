from django.shortcuts import render
from models import BlogPost

# Create your views here.
def home(request):
    title = "Welcome"
    context = {
        "title": title,
    }
    return render(request, "home.html", context)
    
def blog(request):
    title = "Welcome"
    context = {
        "title": title,
    }
    return render(request, "blog.html", context)