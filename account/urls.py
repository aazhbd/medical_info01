# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('account.views',
    url(r'^login/$', 'account_login', name="account_login"),
    url(r'^logout/$', 'account_logout', name="account_logout"),
)
