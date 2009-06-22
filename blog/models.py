
from django.db import models

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
# Here we couple the blog app to plunatica. How could we remove this coupling?

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=64)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey('Author')
    tags = models.ManyToManyField ('Tag')
    
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name
                    
class Comment(models.Model):
    author = models.ForeignKey('Author')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    



