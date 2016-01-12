from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

# class BlogPostQuerySet(models.QuerySet):
#     def published(self):
#         return self.filter(published=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=140, unique=True)
    author = models.CharField(max_length=100, default="Simon")
    tags = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(max_length=15000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField(default=False)
    
#     objects = BlogPostQuerySet.as_manager()
    
    def __unicode__(self):      # Python 3 is __str__
        return self.title
        
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"blog_id": self.id})
            
    # @models.permalink
#     def get_absolute_url(self):
#         return ('blog_post_detail', (), 
#                 {
#                     'slug' :self.slug,
#                 })
# 
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(BlogPost, self).save(*args, **kwargs)