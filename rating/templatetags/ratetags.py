
import math, re

from django.template import Library, Node, TemplateSyntaxError, VariableDoesNotExist, Variable
from django.conf import settings

register = Library()

from rating.models import Rating

STARS = {
	0.0:	("images/star_0.0.png"),
	0.25:	("images/star_0.25.png"),
	0.5:	("images/star_0.5.png"),
	0.75:	("images/star_0.75.png"),
	1.0:	("images/star_1.0.png")
}

class Star(object):
    def __init__(self, pos, img ):
        self.pos = pos
        self.img = img

@register.inclusion_tag('rating.html')
def make_rating( objectKey ):
    rating = Rating.objects.get_or_create( ratedObject=objectKey )[0]
    
    if rating.numVotes > 0:
        avgRating = round((rating.totalRating / rating.numVotes) * 4 ) / 4
    else:
        avgRating = 0
    
    stars = list()

    fraction, integer = math.modf(avgRating)
    for pos in range(0,rating.maxRating):
        if pos < integer:
            stars.append( Star(pos+1, STARS[1.0] ) )
        elif pos == integer:
            stars.append( Star(pos+1, STARS[fraction] ) )
        elif pos > integer:
            stars.append( Star(pos+1, STARS[0.0] ) )
            
    return {'rating': rating, 'imageurl':settings.MEDIA_URL, 'callback':'myCallback', 'stars':stars}
    
@register.inclusion_tag('show_rating.html')
def show_rating( objectKey ):
    return make_rating( objectKey )



