# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('consultation.views',
    url(r'^specialist/(?P<specialist_id>\w+)/$', 'specialist_view', name="specialist_view"),
    url(r'^telecons/(?P<ps_ky>\w+)/$', 'teleconsultation', name="teleconsultation"),
    url(r'^$', 'specialist', name="specialist"),
)
