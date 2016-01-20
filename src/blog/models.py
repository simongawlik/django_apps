from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

# class BlogPostQuerySet(models.QuerySet):
#     def published(self):
#         return self.filter(published=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    #author = models.CharField(max_length=100, default="Simon")
    tags = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True)
    body = models.TextField(max_length=15000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    draft = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=False, auto_now=False)
    
    
    def __unicode__(self):      # Python 3 is __str__
        return self.title
        
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
           
    class Meta:
        ordering = ["-created", "-updated"] 


# if the title of the post occurs in multiple rows of the DB, the first 
# occurrence will just have the title slugified. The second occurrence will 
# have "-1" attached, etc. The counter is used to keep track and is 
# initialized with 1 in pre_save_blogpost_receiver.
def create_slug(instance, counter, new_slug=None):
    existing_slug = slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    queryset = BlogPost.objects.filter(slug=slug).order_by("-id")
    exists = queryset.exists()
    if exists:
        new_slug = "%s-%s" %(existing_slug, counter)
        return create_slug(instance, counter + 1, new_slug=new_slug)
    return slug

# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     queryset = BlogPost.objects.filter(slug=slug).order_by("-id")
#     exists = queryset.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, queryset.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
    

# anytime a blog post is about to be saved this method checks for duplicates
def pre_save_blogpost_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, 1)
        

pre_save.connect(pre_save_blogpost_receiver, sender=BlogPost)
