# -*- coding: utf-8 -*-
import datetime, os

from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponse, Http404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.generic.base import View

from patient.models import PatientInformation
from patient.forms import SearchPatientForm
# from irpmemr.models import Messages, PatientAdmission, BasicPatientInformation, AdditionalPatientInformation, \
#     Guardian, MedicalHistory, PresentMedicalHistory, PastMedicalHistory, FamilyMedicalHistory, MenstrualHistory, \
#     ObstetricHistory, PreviousObstetricHistory, GynaecologicalHistory, ImmunizationHistory, Routinecheckup, \
#     Signanaemia, LaboratoryTest, UltrasoundScanning, Teleconsultation

# import json

def home(request):
    """
    Home page
    """
    if not request.user.is_authenticated():
        return redirect('account_login')

    if request.method == "POST":
        is_search = request.POST.get('q')
        form = SearchPatientForm(request.POST)
        if form.is_valid():
            patients = form.results()
        else:
            patients = PatientInformation.objects.all()
    else:
        form = SearchPatientForm()
        patients = PatientInformation.objects.all()
        is_search = ''
    context = {
        'selected_page': 'home',
        'patients': patients,
        'search_form': form,
        'is_search': is_search,
    }
    return render_to_response('home.html', context, RequestContext(request))

# class UploadImageView(LoginRequiredMixin, CurrentUserIdMixin, View):

#     @method_decorator(csrf_protect)
#     def dispatch(self, *args, **kwargs):
#         return super(UploadImageView, self).dispatch(*args, **kwargs)

# def post(self, request, username):
#     path = 'myproject/media/pictures/guitar.jpg'
#     f = request.FILES['image_file']
#     destination = open(path, 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()

#     return HttpResponse("image uploaded")

# def admission(request):
#     context = RequestContext(request)
#     pa = PatientAdmission.objects.all()
#     context.update({ 'pa' : pa, })

#     return render_to_response("admission.html", context_instance=context)

# def allpatients(request):
#     context = RequestContext(request)
#     bpi = BasicPatientInformation.objects.all()
#     context.update({ 'ph' : bpi, })

#     return render_to_response("allpatients.html", context_instance=context)

# def addiinfo(request, pid):
#     context = RequestContext(request)

#     bpi = BasicPatientInformation.objects.filter(id=pid)
#     api = AdditionalPatientInformation.objects.filter(pid=pid)
#     grd = Guardian.objects.filter(pid=pid)

#     context.update({ 'bpi' : bpi, })
#     context.update({ 'api' : api, })
#     context.update({ 'grd' : grd, })

#     return render_to_response("addiinfo.html", context_instance=context)

# def medhis(request, pid):
#     context = RequestContext(request)

#     bpi = BasicPatientInformation.objects.filter(id=pid)
#     mh = MedicalHistory.objects.filter(pid=pid)
#     premh = PresentMedicalHistory.objects.filter(pid=pid)
#     pmh = PastMedicalHistory.objects.filter(pid=pid)
#     fmh = FamilyMedicalHistory.objects.filter(pid=pid)
#     menh = MenstrualHistory.objects.filter(pid=pid)
#     oh = ObstetricHistory.objects.filter(pid=pid)
#     preoh = PreviousObstetricHistory.objects.filter(pid=pid)
#     gh = GynaecologicalHistory.objects.filter(pid=pid)
#     immun = ImmunizationHistory.objects.filter(pid=pid)

#     context.update({ 'bpi' : bpi, 'premh' : premh, 'pmh' : pmh, 'fmh' : fmh, 'menh' : menh, 'oh' : oh, 'preoh' : preoh })
#     context.update({ 'mh' : mh, 'gh' : gh, 'immun' : immun, })

#     return render_to_response("medhis.html", context_instance=context)

# def routinecheckup(request, pid):
#     context = RequestContext(request)

#     routinechck = Routinecheckup.objects.filter(pid=pid)
#     sgnaemia = Signanaemia.objects.filter(pid=pid)

#     context.update({ 'routinechck' : routinechck,'sgnaemia' : sgnaemia })

#     return render_to_response("routinecheckup.html", context_instance=context)

# def labtest(request, pid):

#     context = RequestContext(request)

#     labtst = LaboratoryTest.objects.filter(pid=pid)

#     context.update({ 'labtst' : labtst,})

#     return render_to_response("labtest.html", context_instance=context)

# def usscanning(request, pid):

#     context = RequestContext(request)

#     usscan = UltrasoundScanning.objects.filter(pid=pid)

#     context.update({ 'usscan' : usscan,})

#     return render_to_response("usscanning.html", context_instance=context)

# def teleconsultation(request):

#     context = RequestContext(request)

#     tele = Teleconsultation.objects.all()

#     context.update({ 'tele' : tele,})

#     return render_to_response("teleconsultation.html", context_instance=context)

# def addmessages(request):
#     c = RequestContext(request)

#     if (request.method == 'POST'):
#         post = request.POST.copy()
#         sender = post.get('sender', '')
#         recver = post.get('receiver', '')
#         submittedat = post.get('submittedat', '')
#         msgbody = post.get('msgbody', '')


#     if recver != '':
#         recv = User.objects.filter(username=recver)
#         for r in recv:
#             newmsg = Messages(sender=request.user, receiver=r, msgbody=msgbody)
#         newmsg.save()

#     return render_to_response('messages.html', context_instance=c)


# def showmessages(request):
#     c = RequestContext(request)

#     messages_q = Messages.objects.filter(receiver=request.user)

#     users = User.objects.all()

#     c.update({'messages': messages_q, 'users': users})

#     msg = []

#     for m in messages_q:
#         msg.append({'sender' : m.sender.username, 'receiver': m.receiver.username, 'body' : m.msgbody })

#     c.update({'messages': messages_q, 'users': users})

#     #print json.dumps(msg)

#     #print "hello" + str(json.dumps(tmp))

#     return HttpResponse(json.dumps(msg), mimetype="application/json")
#     #return render_to_response('messages.html', context_instance=c)

# def messages(request):
#     c = RequestContext(request)

#     messages_q = Messages.objects.filter(receiver=request.user)

#     users = User.objects.all()

#     c.update({'messages': messages_q, 'users': users})

#     return render_to_response('messages.html', context_instance=c)

# def setlogin(request):
#     context = RequestContext(request)

#     usern = request.REQUEST.get('email', False)
#     passd = request.REQUEST.get('pass', False)

#     if usern and passd :
#         login = authenticate(username=usern, password=passd)
#         if login:
#             auth_login(request, login)
#             context.update({
#                 'user_is_loged_in': True
#             })
#         else:
#             context.update({
#                 'user_is_loged_in': False
#             })
#     '''
#     bpi = BasicPatientInformation.objects.all()
#     context.update({ 'ph' : bpi, })
#     '''

#     return render_to_response("home.html", context_instance=context)

# def notification(request):
#     context = RequestContext(request)

#     allps = []
#     allus = []

#     usscan = UltrasoundScanning.objects.all()
#     labtst = LaboratoryTest.objects.all()


#     for u in usscan:
#         print int(u.amount_of_amniotic_fluid)
#         if int(u.amount_of_amniotic_fluid) > 30 :
#             allps.append(u.pid.id)

#     for m in labtst:
#         if int(m.hemoglobin) < 11 :
#             allps.append(m.pid.id)

#     for pid in allps:
#         print pid
#         users = BasicPatientInformation.objects.filter(id=pid)
#         allus.append(users)

#     context.update({ 'allps' : allus, 'allus' : allus})

#     return render_to_response("notification.html", context_instance=context)
