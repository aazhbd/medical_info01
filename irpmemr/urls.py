from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # # url(r'^irpmemr/', include('irpmemr.foo.urls')),
    # url(r'^admission/', 'irpmemr.views.admission', name='admission'),

    # url(r'^allpatients/', 'irpmemr.views.allpatients', name='allpatients'),

    # url(r'^addiinfo/(?P<pid>\w+)$', 'irpmemr.views.addiinfo', name='addiinfo'),

    # url(r'^medhis/(?P<pid>\w+)$', 'irpmemr.views.medhis', name='medhis'),

    # url(r'^routinecheckup/(?P<pid>\w+)$', 'irpmemr.views.routinecheckup', name='routinecheckup'),

    # url(r'^labtest/(?P<pid>\w+)$', 'irpmemr.views.labtest', name='labtest'),

    # url(r'^usscanning/(?P<pid>\w+)$', 'irpmemr.views.usscanning', name='usscanning'),

    # url(r'^notification$', 'irpmemr.views.notification', name='notification'),

    # url(r'^teleconsultation$', 'irpmemr.views.teleconsultation', name='teleconsultation'),

    # url(r'^setlogin$', 'irpmemr.views.setlogin', name='setlogin'),

    # url(r'^msg/add/$', 'irpmemr.views.addmessages', name='addmessages'),
    # url(r'^msg/show/$', 'irpmemr.views.showmessages', name='showmessages'),
    # url(r'^msg$', 'irpmemr.views.messages', name='messages'),

    url(r'^account/', include('account.urls')),
    url(r'^patient/', include('patient.urls')),
    url(r'^teleconsultation/', include('consultation.urls')),
    url(r'^notification/', include('notification.urls')),
    url(r'^$', 'irpmemr.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True,}),
)

urlpatterns += staticfiles_urlpatterns()
