from django.conf.urls.defaults import *
from codetonic.blog.models import LatestEntries

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {'latest': LatestEntries}

urlpatterns = patterns('',
    url(r'^admin/blog/blogentry/(?P<object_id>[0-9]+)/preview/$','codetonic.blog.views.preview'),
    (r'^admin/', include(admin.site.urls)),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^', include ('codetonic.main.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    # Static Media
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/manuel/Django-projects/codetonic/media'})
)
