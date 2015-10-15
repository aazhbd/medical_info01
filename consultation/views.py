# -*- coding: utf-8 -*-

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, redirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from consultation.models import Teleconsultation

@login_required
def specialist(request):
    """
    list of specialist
    """
    specialists = User.objects.filter(userprofile__access_type="SP", specialist__isnull=False)

    context = {
        'selected_page': 'consultation',
        'specialists': specialists,
    }
    return render_to_response('consultation/specialist.html', context, RequestContext(request))

@login_required
def specialist_view(request, specialist_id):
    """
    View specialist page before calling
    Here got call button
    """
    try:
        sp = User.objects.get(id=specialist_id, userprofile__access_type="SP", specialist__isnull=False)
        ps_ky = Teleconsultation.objects.generate_unique_key(sp, request.user)
    except:
        raise Http404
    context = {
        'selected_page': 'consultation',
        'specialist': sp,
        'ps_ky': ps_ky,
    }
    return render_to_response('consultation/specialist_view.html', context, RequestContext(request))

@login_required
def teleconsultation(request, ps_ky):
    """
    teleconsultation page
    """
    try:
        tele = Teleconsultation.objects.get(ps_ky=ps_ky)
        if tele.status == "CA":
            tele.status = "SU"
            tele.save()
        else:
            messages.success(request, _('Calling.. Please allow browser to access your camera.'), fail_silently=True)
            tele.status = "CA"
            tele.save()

    except:
        raise Http404
    context = {
        'selected_page': 'consultation',
        'specialist': tele.specialist,
    }
    return render_to_response('consultation/teleconsultation.html', context, RequestContext(request))
