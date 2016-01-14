from django.conf.urls import patterns, include, url

from . import views


urlpatterns = [
    url(r'^$', views.blog_list, name='list'),
    url(r'^create/$', views.blog_post_create),
    url(r'^(?P<blog_id>\d+)/$', views.blog_post_detail, name='detail'),
    url(r'^(?P<blog_id>\d+)/edit/$', views.blog_post_update, name='update'),
    url(r'^(?P<blog_id>\d+)/delete/$', views.blog_post_delete),
    
]
