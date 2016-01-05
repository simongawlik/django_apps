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

def blog_overview(request):
    blogs = BlogPost.objects.all()
    return render(request, "blog_overview.html", {'blogs': blogs})