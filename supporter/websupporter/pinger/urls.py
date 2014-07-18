from django.conf.urls import patterns, include, url
from pinger.views import pinger_main_page, run_pinger, stop_pinger, update_table

urlpatterns = patterns('',
    url(r'^$', pinger_main_page),
    url(r'^run/$', run_pinger),
    url(r'^stop/$', stop_pinger),
    url(r'^update_table/$', update_table),
)