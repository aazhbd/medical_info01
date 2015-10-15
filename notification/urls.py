# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('notification.views',
    url(r'^$', 'notification', name="notifications"),
)
