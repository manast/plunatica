import os
inport sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'codetonic.settings'

#sys.path.append('/usr/local/codetonic') # uncomment to add this project path
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
