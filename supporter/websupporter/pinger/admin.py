from django.contrib import admin
from pinger.models import Host, Runstatus, Bot

admin.site.register(Host)
admin.site.register(Runstatus)
admin.site.register(Bot)
