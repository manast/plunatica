from django.conf.urls.defaults import *
#from views import main

urlpatterns = patterns('main.views', 
                        (r'^$', 'main'),
                        (r'^(?P<blog_id>\d+)/$', 'blog_detail'),
                        (r'^(?P<blog_slug>\w+-?\w)+/$', 'blog_detail')
)

# r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$'
#
#