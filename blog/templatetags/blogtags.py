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
def blogdetail( blogId ):
    try:
        b = Blog.objects.get(pk=blogId)
        tags = b.tags.filter()
        tag_string = ""
        for t in tags:
            tag_string += str(t) + ", "
        tag_string = tag_string[:-2]
            
    except Blog.DoesNotExist:
        raise Http404
    return {'blog': b, 'tags': tag_string}
