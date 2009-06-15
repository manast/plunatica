from django.conf.urls.defaults import *
#from views import main

urlpatterns = patterns('main.views', 
                        (r'^$', 'main'),
                        (r'^(?P<blog_id>\d+)/$', 'blog_detail')
)
