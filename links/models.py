from django.db import models

# Create your models here.

class Section(models.Model):
    name =  models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Link (models.Model):
    section = models.ForeignKey('Section')
    name = models.CharField(max_length=32)
    url = models.URLField()

    def __unicode__(self):
        return self.name + ":" +self.url
