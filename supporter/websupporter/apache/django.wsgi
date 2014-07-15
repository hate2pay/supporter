import os
import sys

sys.path.append('/home/hate2pay/supporter/websupporter/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'websupporter.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
