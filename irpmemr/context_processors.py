# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.conf import settings
from django.utils import timezone

def site(request):
    if request.user.is_authenticated():
        patient_id = request.session.get('patient_id', '')
    else:
        patient_id = None
    return {
        'site': Site.objects.get_current(),
        'JQUERY_VERSION': settings.JQUERY_VERSION,
        'JQUERY_UI_VERSION': settings.JQUERY_UI_VERSION,
        'JQUERY_UI_THEMES': settings.JQUERY_UI_THEMES,
        'CURRENT_YEAR': timezone.now().year,
        'patient_id': patient_id,
    }
