from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^(?P<blog_id>\d+)/$', 'blog.views.blog'),
]
# urlpatterns = [
#     url(r'^{?P<blog_id>\d+}/$', views.blog_post),
# ]