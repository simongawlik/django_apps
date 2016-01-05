from django.conf.urls import patterns, include, url

import blog.views


urlpatterns = [
    url(r'^$', blog.views.blog_overview, name='blog'),
    url(r'^(?P<blog_id>\d+)/$', blog.views.blog_post),
]
