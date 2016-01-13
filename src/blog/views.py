from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.

    
def blog_post_create(request):
    form = BlogPostForm()
    if request.method == "POST":
        print request.POST
    context = {'form': form}
    return render(request, "blog_form.html", context)

    
def blog_post_detail(request, blog_id):
    instance = get_object_or_404(BlogPost, id=blog_id)
    context = {'instance': instance}
    return render(request, "blog_post.html", context)


def blog_list(request):
    queryset = BlogPost.objects.all()
    context = {'blogpost_list': queryset}
    return render(request, "blog_overview.html", context)


def blog_post_update(request):
    return HttpResponse("<h1>Update</h1>")


def blog_post_delete(request):
    return HttpResponse("<h1>Delete</h1>")