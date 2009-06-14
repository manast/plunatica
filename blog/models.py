
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    about = models.TextField()
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name + " " + self.surname + ", " + self.email
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
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

    



