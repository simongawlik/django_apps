from django.conf.urls import patterns, include, url

import blog.views
import personal_website.views


urlpatterns = [
    url(r'^$', personal_website.views.index),
    url(r'^(?P<blog_id>\d+)/$', blog.views.blog),
]
