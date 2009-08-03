from django.conf.urls.defaults import *
#from views import main

urlpatterns = patterns('main.views', 
                        (r'^$', 'home'),
                        (r'^comments/', include('django.contrib.comments.urls')),
                        url(r'^blog/$', 'blog_index', name='blog-index'),
                        url(r'^blog/tags/(?P<tag>(\w+-?\w)+)/$', 'blog_index_by_tag', name='blog-index-tag'),
                        url(r'^about/$', 'about', name='about'),
                        url(r'^blog/(?P<blog_slug>(\w+-?\w)+)/$', 'blog_detail', name='blog-detail'),
                        url(r'^projects/$', 'projects', name='projects'),
                        url(r'^project/(?P<project_slug>(\w+-?\w)+)/$', 'project_detail', name='project-detail'),
)

# r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$'
#  (r'^(?P<blog_id>\d+)/$', 'blog_detail'),
#