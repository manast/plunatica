from django import template
from blog.models import BlogEntry, Tag
from django.http import Http404

register = template.Library()
        
# A blog bar
@register.inclusion_tag('bar.html')
def blogbar( maxNumBlogs ):
    blogs = BlogEntry.objects.filter(published=True).order_by('-pub_date')[:maxNumBlogs]
    return {'blogs': blogs}
    
# A blog index 
@register.inclusion_tag('index.html')
def blogindex( maxNumBlogs, tag ):
    if tag == None:
        blogs = BlogEntry.objects.filter(published=True).order_by('-pub_date')[:maxNumBlogs]
    else:
        blogs = BlogEntry.objects.filter(published=True, tags__name__contains=tag).order_by('-pub_date')[:maxNumBlogs]
        
    return {'blogs': blogs}

# A blog entry
@register.inclusion_tag('detail.html')
def blogdetail( slug_name ):
    try:
        if slug_name == None:
            b = BlogEntry.objects.filter(published=True)
            if len(b) > 0:
                b = b.order_by('-pub_date')[0]
        else:
            blogs = BlogEntry.objects.filter(slug=slug_name, published=True)
            if len(blogs) > 0:
                b = blogs.order_by('-pub_date')[0]
            else:
                b = None
           
    except BlogEntry.DoesNotExist:
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


# Install a code-block directive to be used for ReST

"""
    The Pygments reStructuredText directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Docutils_ 0.4 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``code-block`` directive that you can use instead of
    normal code blocks like this::

        .. code-block:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. code-block:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: 2007 by Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

# Options
# ~~~~~~~

# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = False

from pygments.formatters import HtmlFormatter

# The default formatter
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES)

# Add name -> formatter pairs for every variant you want to use
VARIANTS = {
    'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}


from docutils import nodes
from docutils.parsers.rst import directives

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        # no lexer found - use the text one instead of an exception
        lexer = TextLexer()
    # take an arbitrary option if more than one is given
    formatter = options and VARIANTS[options.keys()[0]] or DEFAULT
    parsed = highlight(u'\n'.join(content), lexer, formatter)
    parsed = '<div class="codeblock">%s</div>' % parsed
    
    return [nodes.raw('', parsed, format='html')]

pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
pygments_directive.options = dict([(key, directives.flag) for key in VARIANTS])

directives.register_directive('code-block', pygments_directive)




