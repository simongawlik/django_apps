from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title', 
            'body',
            'draft',
            'published',
        ]
        exclude = ['author', 'slug']