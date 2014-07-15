from django.conf.urls import patterns, include, url
#from websupporter.views import login, logout, main, start, ajax_query, ajax_mac, ajax_cable, ajax_ip, ajax_portstatus, \
#ajax_port, ajax_info, ajax_log, ajax_multicast, ajax_tools
from websupporter.views import login, logout, main, ajax_tools, start
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', start),
    url(r'^logout$', logout),
    url(r'^login/$', login),
    url(r'^main$', main),
    url(r'^supporter/', include('supporter.urls')),
    url(r'^pinger/', include('pinger.urls')),
    #url(r'^ajaxexample_json/$', ajax_query),
    #url(r'^ajaxexample_mac/$', ajax_mac),
    #url(r'^ajaxexample_cable/$', ajax_cable),
    #url(r'^ajaxexample_ip/$', ajax_ip),
    #url(r'^ajaxexample_portstatus/$', ajax_portstatus),
    #url(r'^ajaxexample_port/$', ajax_port),
    #url(r'^ajaxexample_info/$', ajax_info),
    #url(r'^ajaxexample_log/$', ajax_log),
    #url(r'^ajaxexample_multicast/$', ajax_multicast),
    url(r'^ajax_tools/$', ajax_tools),
    # url(r'^websupporter/', include('websupporter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url('^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/hate2pay/supporter/websupporter/supporter/media'})
)
