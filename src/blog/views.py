from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import BlogPost

# Create your views here.
# def home(request):
#     title = "Welcome"
#     context = {
#         "title": title,
#     }
#     return render(request, "home.html", context)

    

    
def blog_post_create(request):
    return HttpResponse("<h1>Create</h1>")
    
def blog_post_detail(request, blog_id):
    instance = get_object_or_404(BlogPost, id=blog_id)
    article = BlogPost.objects.get(pk=blog_id)
    context = {'instance': instance}
    return render(request, "blog_post.html", context)

def blog_list(request):
    queryset = BlogPost.objects.all()[:4]
    context = {'blogpost_list': queryset}
    return render(request, "blog_overview.html", context)

def blog_post_update(request):
    return HttpResponse("<h1>Update</h1>")

def blog_post_delete(request):
    return HttpResponse("<h1>Delete</h1>")