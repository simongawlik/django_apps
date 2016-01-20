from django.conf.urls import patterns, include, url

from blog import views


urlpatterns = [
    url(r'^$', views.blog_list, name='list'),
    url(r'^create/$', views.blog_post_create),
    url(r'^(?P<slug>[\w-]+)/$', views.blog_post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.blog_post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.blog_post_delete),
    
]
