# -*- coding: utf-8 -*-

from django.contrib import admin

from account.models import UserProfile, Specialist

admin.site.register(UserProfile)
admin.site.register(Specialist)
