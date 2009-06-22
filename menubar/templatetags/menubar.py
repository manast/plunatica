from django import template
from django.http import Http404

register = template.Library()
        
@register.inclusion_tag('menubar.html')
def show_menubarOld( selected ):
    try:
        options = MenuOption.objects.all()
    except Blog.DoesNotExist:
        raise Http404

    return {'options': options, 'selected': selected}


@register.inclusion_tag('menubar.html')
def show_menubar( menu ):
    return {'menu': menu[0], 'selected': menu[1]}

