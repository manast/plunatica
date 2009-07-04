
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse, NoReverseMatch

from codetonic.menubar.models import MenuItem

main_menu = [ MenuItem('Home','/'), 
              MenuItem('Blog','/blog'),
              MenuItem('About','/about') ]

def home ( request ):
    menu = ( main_menu, 'Home')
    return render_to_response('codetonic.html', {'maxblogs': '10', 'menu':menu, 'blog_slug':None} )
    
def blog_index ( request ):
    menu = ( main_menu, 'Blog')
    return render_to_response('blog_index.html', {'maxblogs': '10', 'menu':menu, 'tag':None} )
     
def about ( request ):
    menu = ( main_menu, 'About')
    return render_to_response('blog_index.html', {'maxblogs': '10', 'menu':menu, 'tag':None} )

def blog_index_by_tag ( request, tag ):
    menu = ( main_menu, 'Blog')
    return render_to_response('blog_index.html', {'maxblogs': '10', 'menu':menu, 'tag':tag} )
    
def blog_detail ( request, blog_slug  ):
    menu = ( main_menu, 'Blog')
    return render_to_response('codetonic.html', {'blog_slug': blog_slug,'menu':menu} )
    
