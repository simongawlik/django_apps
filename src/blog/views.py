from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    queryset_list = BlogPost.objects.all()   #.order_by("-created")
    paginator = Paginator(queryset_list, 3) # Show 3 blog entries per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    context = {'blogpost_list': queryset}
    return render(request, "blog_overview.html", context)

"""

from django.shortcuts import render

def listing(request):
    contact_list = Contacts.objects.all()
    

    return render(request, 'list.html', {'contacts': contacts})
"""


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