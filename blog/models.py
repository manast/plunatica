from django.contrib.syndication.feeds import Feed
from django.db import models

from django.utils.safestring import mark_safe
from restify import *

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    about = models.TextField()
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name + " " + self.surname + ", " + self.email
    
class Tag(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name
        
    @models.permalink
    def get_absolute_url(self):
        return ('main.views.blog_index_by_tag', (), {'tag':self.name} )
# Here we couple the blog app to codetonic. How could we remove this coupling?

class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=64, unique=True)
    content = models.TextField()
    content_html = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey('Author')
    tags = models.ManyToManyField ('Tag')
    published = models.BooleanField (default=False)
    
    def __unicode__(self):
        return self.title
        
    def save(self, **kwargs):
        self.content_html = mark_safe(restify(self.content, 1))
        super(BlogEntry, self).save(**kwargs)
            
    @models.permalink
    def get_absolute_url(self):
        return ('main.views.blog_detail', (), {'blog_slug': self.slug })

class Comment(models.Model):
    author = models.ForeignKey('Author')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

class LatestEntries(Feed):
    title = "Code Tonic"
    link = "/latest/"
    description = "A Fresh Code Tonic."

    def items(self):
        return BlogEntry.objects.order_by('-pub_date')[:5]


