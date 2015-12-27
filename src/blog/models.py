from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, default="Simon")
    #tags        will build this later
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(max_length=15000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField(default=False)
    
    def __unicode__(self):      # Python 3 is __str__
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (), 
                {
                    'slug' :self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)