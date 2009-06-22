from django import template
from plunatica.links.models import Link
from django.http import Http404

register = template.Library()
        
# A blog bar
@register.inclusion_tag('link.html')
def linklist( section ):
    links = Link.objects.filter(section__exact=section).order_by('name')
    return {'links': links}
