from django.contrib import admin
from pinger.models import Host, Runstatus

admin.site.register(Host)
admin.site.register(Runstatus)
