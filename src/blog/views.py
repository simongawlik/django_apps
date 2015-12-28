from django.shortcuts import render
from models import BlogPost

# Create your views here.
def home(request):
    title = "Welcome"
    context = {
        "title": title,
    }
    return render(request, "base.html", context)
    
