from django.shortcuts import render

from blog.models import BlogPost

def about(request):
    return render(request, "about.html", {})
    

def contact(request):
    return render(request, "contact.html", {})
    

def index(request):
    blogs = BlogPost.objects.all()
    return render(request, "index.html", {'blogs': blogs})