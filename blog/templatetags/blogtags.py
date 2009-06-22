from django import template
from plunatica.blog.models import Blog, Tag
from django.http import Http404

register = template.Library()
        
# A blog bar
@register.inclusion_tag('bar.html')
def blogbar( maxNumBlogs ):
    blogs = Blog.objects.all().order_by('-pub_date')[:maxNumBlogs]
    return {'blogs': blogs}
    
# A blog index 
@register.inclusion_tag('index.html')
def blogindex( maxNumBlogs, tag ):
    if tag == None:
        blogs = Blog.objects.all().order_by('-pub_date')[:maxNumBlogs]
    else:
        blogs = Blog.objects.filter(tags__name__contains=tag).order_by('-pub_date')[:maxNumBlogs]
        
    return {'blogs': blogs}

# A blog entry
@register.inclusion_tag('detail.html')
def blogdetail( slug_name ):
    try:
        if slug_name == None:
            b = Blog.objects.all()
            if len(b) > 0:
                b = b.order_by('-pub_date')[0]
        else:
            blogs = Blog.objects.filter(slug=slug_name)
            if len(blogs) > 0:
                b = blogs.order_by('-pub_date')[0]
            else:
                b = None
           
    except Blog.DoesNotExist:
        raise Http404
        
    return {'blog': b }
    
@register.inclusion_tag('taglist.html')
def taglist( maxNumTags ):
    tags = Tag.objects.all().order_by('name')
    if maxNumTags > 0:
        tags = tags[:maxNumTags]
    return {'tags': tags}
    
# ROT13 email address obfuscator
import re
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


@register.filter()
def obfuscate(email, linktext=None, autoescape=None):
    """
    Given a string representing an email address,
	returns a mailto link with rot13 JavaScript obfuscation.
	
    Accepts an optional argument to use as the link text;
	otherwise uses the email address itself.
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    email = re.sub('@','\\\\100', re.sub('\.', '\\\\056', \
        esc(email))).encode('rot13')

    if linktext:
        linktext = esc(linktext).encode('rot13')
    else:
        linktext = email

    rotten_link = """<script type="text/javascript">document.write \
        ("<n uers=\\\"znvygb:%s\\\">%s<\\057n>".replace(/[a-zA-Z]/g, \
        function(c){return String.fromCharCode((c<="Z"?90:122)>=\
        (c=c.charCodeAt(0)+13)?c:c-26);}));</script>""" % (email, linktext)
    return mark_safe(rotten_link)
obfuscate.needs_autoescape = True


