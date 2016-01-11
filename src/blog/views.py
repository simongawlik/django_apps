from django.http import HttpResponse
from django.shortcuts import render
from models import BlogPost

# Create your views here.
# def home(request):
#     title = "Welcome"
#     context = {
#         "title": title,
#     }
#     return render(request, "home.html", context)

    
def blog_post(request, blog_id):
    article = BlogPost.objects.get(pk=blog_id)
    return render(request, "blog_post.html", {'article': article})

def blog_list(request):
    blogs = BlogPost.objects.all()[:4]
    return render(request, "blog_overview.html", {'blogs': blogs})
    
def blog_post_create(request):
    return HttpResponse("<h1>Hello</h1>")
    
def blog_post_update(request):
    return HttpResponse("<h1>Hello</h1>")
    
def blog_post_delete(request):
    return HttpResponse("<h1>Hello</h1>")