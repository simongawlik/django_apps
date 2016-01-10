from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "created"]
    list_filter = ["updated", "created"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = BlogPost
    

admin.site.register(BlogPost, BlogPostAdmin)