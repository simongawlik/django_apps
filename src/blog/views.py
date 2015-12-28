from django.shortcuts import render
from models import BlogPost

# Create your views here.
def home(request):
    return render(request, "home.html", {})
    
def blog(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    return render(request, '')