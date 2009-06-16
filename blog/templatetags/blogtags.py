from django import template
from plunatica.blog.models import Blog
from django.http import Http404

register = template.Library()
        
# A blog bar
@register.inclusion_tag('bar.html')
def blogbar( maxNumBlogs ):
    blogs = Blog.objects.all().order_by('-pub_date')[:maxNumBlogs]
    return {'blogs': blogs}
    
# A blog index 
@register.inclusion_tag('index.html')
def blogindex( maxNumBlogs ):
    blogs = Blog.objects.all().order_by('-pub_date')[:maxNumBlogs]
    return {'blogs': blogs}

# A blog entry
@register.inclusion_tag('detail.html')
def blogdetail( slug_name ):
    try:
        if slug_name == None:
            b = Blog.objects.all().order_by('-pub_date')[0]
        else:
            b = Blog.objects.filter(slug=slug_name).order_by('-pub_date')[0]
    except Blog.DoesNotExist:
        raise Http404

    return {'blog': b }
