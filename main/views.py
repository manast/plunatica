
from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse, NoReverseMatch

from codetonic.menubar.models import MenuItem
from codetonic.main.models import Project

main_menu = [ MenuItem('Home','/'), 
              MenuItem('Blog','/blog'),
              MenuItem('Projects','/projects'),
              MenuItem('About','/about') ]

def home ( request ):
    menu = ( main_menu, 'Home')
    return render_to_response('codetonic.html', {'maxblogs': '10', 'menu':menu, 'blog_slug':None} )
    
def blog_index ( request ):
    menu = ( main_menu, 'Blog')
    return render_to_response('blog_index.html', {'maxblogs': '10', 'menu':menu, 'tag':None} )

def projects ( request ):
    menu = ( main_menu, 'Projects')
    projects = Project.objects.all()
    return render_to_response('projects.html', {'projects': projects,'menu':menu} )
    
def project_detail ( request, project_slug  ):
    menu = ( main_menu, 'Project')
    
    try:
        project = Project.objects.filter(slug=project_slug)[0]
    except Project.DoesNotExist:
        raise Http404
               
    return render_to_response('project_detail.html', {'project': project,'menu':menu} )
  
def about ( request ):
    menu = ( main_menu, 'About')
    return render_to_response('codetonic.html', {'blog_slug': 'Debut','menu':menu} )
       
def blog_index_by_tag ( request, tag ):
    menu = ( main_menu, 'Blog')
    return render_to_response('blog_index.html', {'maxblogs': '10', 'menu':menu, 'tag':tag} )
    
def blog_detail ( request, blog_slug  ):
    menu = ( main_menu, 'Blog')
    return render_to_response('codetonic.html', {'blog_slug': blog_slug,'menu':menu} )
    