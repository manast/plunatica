
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404

from django.core.urlresolvers import reverse, NoReverseMatch

def main ( request ):
    t = loader.get_template('plunatica.html')
    
    blog_id = 1
    c = Context({'blog_id': blog_id})
    return HttpResponse (t.render(c))
       
def blog_detail ( request, blog_slug = None ):
    if blog_slug == None:
        # find latest post
        blog_id = 1
    else:
        blog_id = 1
        # search id correspondig to this slug.
        # blog_id = 

    t = loader.get_template('plunatica.html')
    
    c = Context({'blog_id': blog_id})
    return HttpResponse (t.render(c))
    
 
    

