
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404

from django.core.urlresolvers import reverse, NoReverseMatch

def main ( request ):
    t = loader.get_template('plunatica.html')
    
    c = Context({})
    return HttpResponse (t.render(c))
    
 
    

