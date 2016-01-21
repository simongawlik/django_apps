from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.

    
def blog_post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, "blog_form.html", context)
    # return render(request, "blog/blog_form.html", context)

    
def blog_post_detail(request, slug):
    instance = get_object_or_404(BlogPost, slug=slug)
    if instance.draft or instance.published > timezone.now():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {'instance': instance}
    return render(request, "blog_post.html", context)


def blog_list(request):
    queryset_list = BlogPost.objects.active()   #.order_by("-created")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = BlogPost.objects.all()
    paginator = Paginator(queryset_list, 3) # Show 3 blog entries per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    context = {
        'blogpost_list': queryset,
        'page_request_var': page_request_var
    }
        
    return render(request, "blog_overview.html", context)


def blog_post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(BlogPost, slug=slug)
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


def blog_post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(BlogPost, id=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("blog:list")