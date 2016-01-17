from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.

    
def blog_post_create(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, "blog_form.html", context)

    
def blog_post_detail(request, blog_id):
    instance = get_object_or_404(BlogPost, id=blog_id)
    context = {'instance': instance}
    return render(request, "blog_post.html", context)


def blog_list(request):
    queryset = BlogPost.objects.all()   #.order_by("-created")
    context = {'blogpost_list': queryset}
    return render(request, "blog_overview.html", context)


def blog_post_update(request, blog_id=None):
    instance = get_object_or_404(BlogPost, id=blog_id)
    form = BlogPostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'instance': instance, 
        'form': form,
    }
    
    return render(request, "blog_form.html", context)


def blog_post_delete(request, blog_id=None):
    instance = get_object_or_404(BlogPost, id=blog_id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("blog:list")