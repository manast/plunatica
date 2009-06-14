from django.conf.urls.defaults import *
from views import index, detail

urlpatterns = patterns('blog.views',
    (r'^$', index),
    (r'^(?P<blog_id>\d+)/$', detail),
)
