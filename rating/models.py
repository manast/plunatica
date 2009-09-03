#
# Copyright 2008 Darrel Herbst
#
# This file is part of Django-Rabid-Ratings.
#
# Django-Rabid-Ratings is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Django-Rabid-Ratings is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Django-Rabid-Ratings.  If not, see <http://www.gnu.org/licenses/>.
#
# Some modifications by Manuel Astudillo.
#

from django.db import models


class Rating(models.Model):
    ratedObject = models.CharField(verbose_name='Rated Object', max_length=255, unique=True)
    maxRating = models.IntegerField(default=5)
    totalRating = models.FloatField(default=0)
    numVotes = models.IntegerField(default=0)
    averageRating = models.FloatField(default=0)
      
    def __unicode__(self):
        if self.numVotes:
            rate = self.totalRating / self.numVotes;
        else:
            rate = 0
            
        return str(self.ratedObject) + ", rate: " + str(rate)
        
    def add_rating(self, event):
        """
        Adds the given RatingEvent to the key.
        The event will tell you if you need to revise the counter values because 
        the user is updating their vote versus adding a new vote.

        After calling add_rating the caller should save the rating but it is 
        important the caller do the following three steps in a transaction, otherwise
        a race condition could occur:

        1. get the Rating object
        2. rating.add_rating(event)
        3. rating.save()
        """
        
        if event.value <= self.maxRating and event.value >= 0:
            if event.is_changing:
                # the user decided to change their vote, so take away the old value first
                self.totalRating = self.totalRating - event.old_value
                self.numVotes = self.numVotes - 1
        
            self.totalRating = self.totalRating + event.value
            self.numVotes = self.numVotes + 1
            
class RatingEvent(models.Model):
    """
    Each time someone votes, the vote will be recorded by ip address.
    Yes, this is not optimal for proxies, but good enough because if you
    are behind a proxy you should be working, and not rating stuff.
    """
    ratedObject = models.CharField(verbose_name='Rated Object', max_length=255)
    ip = models.IPAddressField()
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        """ A vote is from one ip address - and then it can be changed. """
        super(RatingEvent, self).__init__(*args, **kwargs)

        self.is_changing = False
    
    def __unicode__(self):
        """ Used to identify the object in admin forms. """
        return self.ratedObject + "_" + str(self.ip)
    
    
    


