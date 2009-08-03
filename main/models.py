from django.db import models

from django.utils.safestring import mark_safe
from rstify.utils import rstify

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField()
    description_html = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        
    def save(self, **kwargs):
        self.description_html = mark_safe(rstify(self.description, 1))
        super(Project, self).save(**kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('main.views.project_detail', (), {'project_name': self.slug })

