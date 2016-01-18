from __future__ import unicode_literals

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
    author = models.CharField(max_length=100, default="Simon")
    tags = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True)
    body = models.TextField(max_length=15000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField(default=False)
    
#     objects = BlogPostQuerySet.as_manager()
    
    def __unicode__(self):      # Python 3 is __str__
        return self.title
        
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
           
    class Meta:
        ordering = ["-created", "-updated"] 

# needs to be improved. At this point it appends id in every recursive call.
# should be counting up each time title is reused.
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    queryset = BlogPost.objects.filter(slug=slug).order_by("-id")
    exists = queryset.exists()
    if exists:
        new_slug = "%s-%s" %(slug, queryset.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    

# anytime a blog post is about to be saved this method checks for duplicates
def pre_save_blogpost_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        

pre_save.connect(pre_save_blogpost_receiver, sender=BlogPost)