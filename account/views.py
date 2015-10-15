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

from account.forms import AuthenticationForm

def account_login(request):
    """
    User login page
    """
    is_next = request.REQUEST.get('next', '')

    if request.user.is_authenticated():
        if is_next:
            return redirect(is_next)
        else:
            return redirect('home')
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username, password = (
                form.cleaned_data['username'],
                form.cleaned_data['password'],
            )
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, _("You have been signed in."), fail_silently=True)

                try:
                    # set specialist status
                    if request.user.specialist:
                        request.user.specialist.status = "AV"
                        request.user.specialist.save()
                except:
                    pass

                if is_next:
                    return redirect(is_next)
                else:
                    return redirect('home')
    else:
        form = AuthenticationForm(request=request)
    context = {
        'selected_page': 'home',
        'form': form,
    }
    return render_to_response('account/login.html', context, RequestContext(request))

def account_logout(request):
    """
    Logout and redirect to home page.
    """
    try:
        if request.user.specialist:
            request.user.specialist.status = "OF"
            request.user.specialist.save()
    except:
        pass
    logout(request)
    messages.success(request, _('You have been signed out.'), fail_silently=True)
    return redirect('home')
