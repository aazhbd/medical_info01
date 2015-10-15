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

from patient.models import PatientInformation, Guardian, MedicalHistory, PastMedicalHistory, PresentMedicalHistory, \
    FamilyMedicalHistory, MenstrualHistory, ObstetricHistory, GynaecologicalHistory, ImmunizationHistory, \
    Routinecheckup, LaboratoryTest, UltrasoundScanning, AdditionalPatientInformation, Prescription, PreviousSurgery

FREQUENCY = ['AL', 'US', 'OF', 'SO', 'SE', 'RA']

def check_additional_patient_information(patient):
    probs = []
    try:
        info = AdditionalPatientInformation.objects.get(patient=patient)
        if info.cigarettes in FREQUENCY:
            probs.append("Cigarettes - %s" % info.get_cigarettes_display())
        if info.alcohol in FREQUENCY:
            probs.append("Alcohol - %s" % info.get_alcohol_display())
        if info.other_harmful_substances in FREQUENCY:
            probs.append("Other harmful subtances - %s" % info.get_other_harmful_substances_display())
    except:
        pass
    return probs

def check_family_medical_history(patient):
    probs = []
    try:
        fmh = FamilyMedicalHistory.objects.get(patient=patient)
        probs_text = []
        if fmh.tuberculosis:
            probs_text.append('tuberculosis')
        if fmh.heart_disease:
            probs_text.append('heart disease')
        if fmh.chronical_renal_disease:
            probs_text.append('chronical renal disease')
        if fmh.epilepsy:
            probs_text.append('epilepsy')
        if fmh.diabetes_melitus:
            probs_text.append('diabetes melitus')
        if fmh.sexually_transmitted_infection:
            probs_text.append('sexually transmitted infection')
        if fmh.hepatitis:
            probs_text.append('hepatitis')
        if fmh.malaria:
            probs_text.append('malaria')
        if fmh.sickle_cell_trait:
            probs_text.append('sickle cell trait')
        if fmh.rhesus_d_antibodies:
            probs_text.append('rhesus d antibodies')
        if fmh.HIV_status_if_known:
            probs_text.append('HIV')
        if fmh.kidney_disease:
            probs_text.append('kidney disease')
        if fmh.liver_problems:
            probs_text.append('liver problems')
        if fmh.hypertension:
            probs_text.append('hypertension')
        if fmh.urinary_tract_surgeries:
            probs_text.append('urinary tract surgeries')
        if fmh.seizures:
            probs_text.append('seizures')
        if fmh.pelvic_backinjuries:
            probs_text.append('pelvic back injuries')
        if fmh.haemorrhage:
            probs_text.append('haemorrhage')
        if fmh.others:
            probs_text.append(fmh.others)
        if probs_text:
            probs.append('Family medical history - ' + ', '.join(probs_text))
    except:
        pass
    return probs

def check_past_medical_history(patient):
    probs = []
    try:
        pmh = PastMedicalHistory.objects.get(patient=patient)
        probs_text = []
        if pmh.tuberculosis:
            probs_text.append('tuberculosis')
        if pmh.heart_disease:
            probs_text.append('heart disease')
        if pmh.chronical_renal_disease:
            probs_text.append('chronical renal disease')
        if pmh.epilepsy:
            probs_text.append('epilepsy')
        if pmh.diabetes_melitus:
            probs_text.append('diabetes melitus')
        if pmh.sexually_transmitted_infection:
            probs_text.append('sexually transmitted infection')
        if pmh.hepatitis:
            probs_text.append('hepatitis')
        if pmh.malaria:
            probs_text.append('malaria')
        if pmh.sickle_cell_trait:
            probs_text.append('sickle cell trait')
        if pmh.rhesus_d_antibodies:
            probs_text.append('rhesus d antibodies')
        if pmh.HIV_status_if_known:
            probs_text.append('HIV')
        if pmh.kidney_disease:
            probs_text.append('kidney disease')
        if pmh.liver_problems:
            probs_text.append('liver problems')
        if pmh.hypertension:
            probs_text.append('hypertension')
        if pmh.urinary_tract_surgeries:
            probs_text.append('urinary tract surgeries')
        if pmh.seizures:
            probs_text.append('seizures')
        if pmh.pelvic_backinjuries:
            probs_text.append('pelvic back injuries')
        if pmh.haemorrhage:
            probs_text.append('haemorrhage')
        if pmh.others:
            probs_text.append(pmh.others)
        if probs_text:
            probs.append('Past medical history - ' + ', '.join(probs_text))
    except:
        pass
    return probs

def check_obstetric_history(patient):
    probs = []
    try:
        obh = ObstetricHistory.objects.get(patient=patient)
        if obh.check_if_you_have_been_miscarriages:
            probs.append('miscarriages')
    except:
        pass
    return probs

def check_present_medical_history(patient):
    probs = []
    try:
        pmh = PresentMedicalHistory.objects.get(patient=patient)
        probs_text = []
        if pmh.tuberculosis:
            probs_text.append('tuberculosis')
        if pmh.heart_disease:
            probs_text.append('heart disease')
        if pmh.chronical_renal_disease:
            probs_text.append('chronical renal disease')
        if pmh.epilepsy:
            probs_text.append('epilepsy')
        if pmh.diabetes_melitus:
            probs_text.append('diabetes melitus')
        if pmh.sexually_transmitted_infection:
            probs_text.append('sexually transmitted infection')
        if pmh.hepatitis:
            probs_text.append('hepatitis')
        if pmh.malaria:
            probs_text.append('malaria')
        if pmh.sickle_cell_trait:
            probs_text.append('sickle cell trait')
        if pmh.rhesus_d_antibodies:
            probs_text.append('rhesus d antibodies')
        if pmh.HIV_status_if_known:
            probs_text.append('HIV')
        if pmh.kidney_disease:
            probs_text.append('kidney disease')
        if pmh.liver_problems:
            probs_text.append('liver problems')
        if pmh.hypertension:
            probs_text.append('hypertension')
        if pmh.urinary_tract_surgeries:
            probs_text.append('urinary tract surgeries')
        if pmh.seizures:
            probs_text.append('seizures')
        if pmh.pelvic_backinjuries:
            probs_text.append('pelvic back injuries')
        if pmh.haemorrhage:
            probs_text.append('haemorrhage')
        if pmh.others:
            probs_text.append(pmh.others)
        if probs_text:
            probs.append('Present medical history - ' + ', '.join(probs_text))
    except:
        pass
    return probs

def check_gynaecological_history(patient):
    probs = []
    try:
        gyh = GynaecologicalHistory.objects.get(patient=patient)
        if gyh.result_pap_smear == 'AB':
            probs.append('Gynaecological history - Abnormal')
    except:
        pass
    return probs

def check_previous_surgery(patient):
    probs = []
    try:
        prs = PreviousSurgery.objects.get(patient=patient)
        probs_text = []
        if prs.fibrocystic_breasts:
            probs_text.append('fibrocystic breasts')
        if prs.ovarian_cysts:
            probs_text.append('ovarian cysts')
        if prs.endometriosis:
            probs_text.append('endometriosis')
        if prs.uterine_fibroids:
            probs_text.append('uterine fibroids')
        if prs.others_please_state:
            probs_text.append(prs.others_please_state)
        if probs_text:
            probs.append('Previous surgery - ' + ', '.join(probs_text))
    except:
        pass
    return probs

def check_laboratary_test(patient):
    probs = []
    try:
        labs = LaboratoryTest.objects.filter(patient=patient)
        for lab in labs:
            if lab.urinalysis == 'AB' and not 'Urinalysis > 0.3g/24h' in probs:
                probs.append('Urinalysis > 0.3g/24h')
            if lab.hemoglobin == 'A' and not 'Haemoglobin 9-10' in probs:
                probs.append('Haemoglobin 9-10')
            elif lab.hemoglobin == 'B' and not 'Haemoglobin 7-8 g/dl' in probs:
                probs.append('Haemoglobin 7-8 g/dl')
            elif lab.hemoglobin == 'C' and not 'Haemoglobin <7 g/dl' in probs:
                probs.append('Haemoglobin <7 g/dl')
    except:
        pass
    return probs

@login_required
def notification(request):
    problems = []

    patients = PatientInformation.objects.all()
    for patient in patients:
        probs1 = check_additional_patient_information(patient)
        probs2 = check_family_medical_history(patient)
        probs3 = check_past_medical_history(patient)
        probs4 = check_obstetric_history(patient)
        probs5 = check_present_medical_history(patient)
        probs6 = check_gynaecological_history(patient)
        probs7 = check_previous_surgery(patient)
        probs8 = check_laboratary_test(patient)
        if probs1 or probs2 or probs3 or probs4 or probs5 or probs6 or probs7 or probs8:
            all_probs = probs1 + probs2 + probs3 + probs4 + probs5 + probs6 + probs7 + probs8
            problems.append([patient, all_probs])

    context = {
        'problems': problems,
        'selected_page': 'notification',
    }
    return render_to_response('notification/notification.html', context, RequestContext(request))
