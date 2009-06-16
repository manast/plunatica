from django.conf.urls.defaults import *
#from views import main

urlpatterns = patterns('main.views', 
                        (r'^$', 'main'),
                        url(r'^(?P<blog_slug>(\w+-?\w)+)/$', 'blog_detail', name='blog-detail')
)

# r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$'
#  (r'^(?P<blog_id>\d+)/$', 'blog_detail'),
#