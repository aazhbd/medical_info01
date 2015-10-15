# -*- coding: utf-8 -*-
import os, datetime

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, redirect, HttpResponse, Http404
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

from patient.models import PatientInformation, Guardian, MedicalHistory, PastMedicalHistory, PresentMedicalHistory, \
    FamilyMedicalHistory, MenstrualHistory, ObstetricHistory, GynaecologicalHistory, ImmunizationHistory, \
    Routinecheckup, LaboratoryTest, UltrasoundScanning, AdditionalPatientInformation, Prescription, PreviousObstetricHistory, \
    PreviousSurgery, UltrasoundScanningImage
from patient.forms import AddPatientForm, PatientInformationForm, AdditionalPatientInformationForm, GuardianForm, \
    MedicalHistoryForm, PastMedicalHistoryForm, PresentMedicalHistoryForm, FamilyMedicalHistoryForm, \
    MenstrualHistoryForm, ObstetricHistoryForm, GynaecologicalHistoryForm, ImmunizationHistoryForm, \
    RoutinecheckupForm, LaboratoryTestForm, UltrasoundScanningForm, PrescriptionForm, PreviousObstetricHistoryForm, \
    PreviousSurgeryForm
from admission.models import PatientVisit, HospitalAdmission
from admission.forms import PatientVisitForm, PatientAdmissionForm

def get_patient(patient_id):
    try:
        return PatientInformation.objects.get(id=patient_id)
    except:
        raise Http404

@login_required
def patient_home(request):
    """
    Show patient list. Not used
    """
    context = {
        'selected_page': 'home',
    }
    return render_to_response('patient/patient_home.html', context, RequestContext(request))

@login_required
def patient_visit(request, patient_id):
    """
    Display patient visit info
    """
    patient = get_patient(patient_id)
    try:
        visit = patient.patientvisit
    except:
        visit = None
    admissions = HospitalAdmission.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'visit': visit,
        'admissions': admissions,
    }
    return render_to_response('patient/patient_visit.html', context, RequestContext(request))

@login_required
def patient_visit_add(request, patient_id):
    """
    Add patient visit
    """
    patient = get_patient(patient_id)
    try:
        visit = patient.patientvisit
        form = PatientVisitForm(instance=visit)
    except:
        form = PatientVisitForm()

    if request.method == "POST":
        try:
            visit = patient.patientvisit
            form = PatientVisitForm(request.POST, instance=visit)
        except:
            form = PatientVisitForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('patient_visit', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'selected_tab': 'patient-visit',
        'selected_page': 'patient',
    }
    return render_to_response('patient/patient_visit_add.html', context, RequestContext(request))

@login_required
def patient_admission_add(request, patient_id, admission_id=None):
    """
    Add patient admission
    """
    patient = get_patient(patient_id)
    if admission_id:
        admission = HospitalAdmission.objects.get(id=admission_id)
        form = PatientAdmissionForm(instance=admission)
    else:
        form = PatientAdmissionForm()
    if request.method == "POST":
        if admission_id:
            admission = HospitalAdmission.objects.get(id=admission_id)
            form = PatientAdmissionForm(request.POST, instance=admission)
        else:
            form = PatientAdmissionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('patient_visit', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'selected_tab': 'patient-visit',
        'selected_page': 'patient',
        'admission_id': admission_id,
    }
    return render_to_response('patient/patient_admission_add.html', context, RequestContext(request))

@login_required
def basic_patient_information(request, patient_id):
    """
    Basic Patient Information
    """
    patient = get_patient(patient_id)
    try:
        form = PatientInformationForm(instance=patient)
    except:
        form = PatientInformationForm()

    if request.method == "POST":
        form = PatientInformationForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
    }
    return render_to_response('patient/basic_patient_information.html', context, RequestContext(request))

@login_required
def additional_details(request, patient_id):
    """
    Additional patient details
    """
    patient = get_patient(patient_id)
    try:
        add_info = AdditionalPatientInformation.objects.filter(patient=patient).latest('id')
        form = AdditionalPatientInformationForm(prefix='f1', instance=add_info)
    except:
        form = AdditionalPatientInformationForm(prefix='f1')

    try:
        guardian = Guardian.objects.filter(patient=patient).latest('id')
        form2 = GuardianForm(prefix='f2', instance=guardian)
    except:
        form2 = GuardianForm(prefix='f2')

    if request.method == "POST":
        try:
            add_info = AdditionalPatientInformation.objects.filter(patient=patient).latest('id')
            form = AdditionalPatientInformationForm(request.POST, prefix='f1', instance=add_info)
        except:
            form = AdditionalPatientInformationForm(request.POST, prefix='f1')
        try:
            guardian = Guardian.objects.filter(patient=patient).latest('id')
            form2 = GuardianForm(request.POST, prefix='f2', instance=guardian)
        except:
            form2 = GuardianForm(request.POST, prefix='f2')

        save_msg = None
        if form.has_changed():
            if form.is_valid():
                form.save(commit=False)
                form.instance.patient = patient
                form.save()
                save_msg = True
        else:
            try:
                add_info = AdditionalPatientInformation.objects.filter(patient=patient).latest('id')
                form = AdditionalPatientInformationForm(prefix='f1', instance=add_info)
            except:
                form = AdditionalPatientInformationForm(prefix='f1')
        if form2.has_changed():
            if form2.is_valid():
                form2.save(commit=False)
                form2.instance.patient = patient
                form2.save()
                save_msg = True
        else:
            try:
                guardian = Guardian.objects.filter(patient=patient).latest('id')
                form2 = GuardianForm(prefix='f2', instance=guardian)
            except:
                form2 = GuardianForm(prefix='f2')
        if save_msg:
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'form2': form2,
    }
    return render_to_response('patient/additional_details.html', context, RequestContext(request))

@login_required
def medical_history(request, patient_id):
    """
    Family medical history
    """
    patient = get_patient(patient_id)

    try:
        medical3 = FamilyMedicalHistory.objects.filter(patient=patient).latest('id')
        form = FamilyMedicalHistoryForm(instance=medical3)
    except:
        form = FamilyMedicalHistoryForm()

    if request.method == "POST":
        try:
            medical3 = FamilyMedicalHistory.objects.filter(patient=patient).latest('id')
            form = FamilyMedicalHistoryForm(request.POST, instance=medical3)
        except:
            form = FamilyMedicalHistoryForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'fmh',
    }
    return render_to_response('patient/medical_history.html', context, RequestContext(request))

@login_required
def past_medical_history(request, patient_id):
    """
    Past medical history
    """
    patient = get_patient(patient_id)

    try:
        medical1 = PastMedicalHistory.objects.filter(patient=patient).latest('id')
        form = PastMedicalHistoryForm(instance=medical1)
    except:
        form = PastMedicalHistoryForm()

    if request.method == "POST":
        try:
            medical1 = PastMedicalHistory.objects.filter(patient=patient).latest('id')
            form = PastMedicalHistoryForm(request.POST, instance=medical1)
        except:
            form = PastMedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'pah',
    }
    return render_to_response('patient/past_medical_history.html', context, RequestContext(request))

@login_required
def menstrual_history(request, patient_id):
    """
    Menstrual history
    """
    patient = get_patient(patient_id)

    try:
        medical4 = MenstrualHistory.objects.filter(patient=patient).latest('id')
        form = MenstrualHistoryForm(instance=medical4)
    except:
        form = MenstrualHistoryForm()

    if request.method == "POST":
        try:
            medical4 = MenstrualHistory.objects.filter(patient=patient).latest('id')
            form = MenstrualHistoryForm(request.POST, instance=medical4)
        except:
            form = MenstrualHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'meh',
    }
    return render_to_response('patient/menstrual_history.html', context, RequestContext(request))

@login_required
def obstetric_history(request, patient_id):
    """
    Obstetric history
    """
    patient = get_patient(patient_id)

    try:
        medical5 = ObstetricHistory.objects.filter(patient=patient).latest('id')
        form = ObstetricHistoryForm(instance=medical5)
    except:
        form = ObstetricHistoryForm()

    if request.method == "POST":
        try:
            medical5 = ObstetricHistory.objects.filter(patient=patient).latest('id')
            form = ObstetricHistoryForm(request.POST, instance=medical5)
        except:
            form = ObstetricHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)

    prev_obs = PreviousObstetricHistory.objects.filter(patient=patient).order_by('dob')
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'obh',
        'prev_obs': prev_obs,
    }
    return render_to_response('patient/obstetric_history.html', context, RequestContext(request))

@login_required
def obstetric_add(request, patient_id):
    """
    Add obstetric history
    """
    patient = get_patient(patient_id)
    form = PreviousObstetricHistoryForm()
    if request.method == "POST":
        form = PreviousObstetricHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('obstetric_history', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'obh',
    }
    return render_to_response('patient/obstetric_add.html', context, RequestContext(request))

@login_required
def present_medical_history(request, patient_id):
    """
    Present medical history
    """
    patient = get_patient(patient_id)

    try:
        medical2 = PresentMedicalHistory.objects.filter(patient=patient).latest('id')
        form = PresentMedicalHistoryForm(instance=medical2)
    except:
        form = PresentMedicalHistoryForm()

    if request.method == "POST":
        try:
            medical2 = PresentMedicalHistory.objects.filter(patient=patient).latest('id')
            form = PresentMedicalHistoryForm(request.POST, instance=medical2)
        except:
            form = PresentMedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'prh',
    }
    return render_to_response('patient/present_medical_history.html', context, RequestContext(request))

@login_required
def gynaecological_history(request, patient_id):
    """
    Gynaecological history
    """
    patient = get_patient(patient_id)

    try:
        medical6 = GynaecologicalHistory.objects.filter(patient=patient).latest('id')
        form = GynaecologicalHistoryForm(prefix='f1', instance=medical6)
    except:
        form = GynaecologicalHistoryForm(prefix='f1')
    try:
        medical7 = PreviousSurgery.objects.filter(patient=patient).latest('id')
        form2 = PreviousSurgeryForm(prefix='f2', instance=medical7)
    except:
        form2 = PreviousSurgeryForm(prefix='f2')

    if request.method == "POST":
        try:
            medical6 = GynaecologicalHistory.objects.filter(patient=patient).latest('id')
            form = GynaecologicalHistoryForm(request.POST, prefix='f1', instance=medical6)
        except:
            form = GynaecologicalHistoryForm(request.POST, prefix='f1')
        try:
            medical7 = PreviousSurgery.objects.filter(patient=patient).latest('id')
            form2 = PreviousSurgeryForm(request.POST, prefix='f2', instance=medical7)
        except:
            form2 = PreviousSurgeryForm(request.POST, prefix='f2')
        if form.is_valid() and form2.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            form2.save(commit=False)
            form2.instance.patient = patient
            form2.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'form2': form2,
        'medical_tab': 'gyh',
    }
    return render_to_response('patient/gynaecological_history.html', context, RequestContext(request))

@login_required
def immunization_history(request, patient_id):
    """
    Immunization history
    """
    patient = get_patient(patient_id)

    try:
        medical7 = ImmunizationHistory.objects.filter(patient=patient).latest('id')
        form = ImmunizationHistoryForm(instance=medical7)
    except:
        form = ImmunizationHistoryForm()

    if request.method == "POST":
        try:
            medical7 = ImmunizationHistory.objects.filter(patient=patient).latest('id')
            form = ImmunizationHistoryForm(request.POST, instance=medical7)
        except:
            form = ImmunizationHistoryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
    context = {
        'patient': patient,
        'form': form,
        'medical_tab': 'imh',
    }
    return render_to_response('patient/immunization_history.html', context, RequestContext(request))

@login_required
def routine_checkup(request, patient_id):
    """
    routine checkup
    """
    patient = get_patient(patient_id)
    routines = Routinecheckup.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'routines': routines,
    }
    return render_to_response('patient/routine_checkup.html', context, RequestContext(request))

@login_required
def routine_checkup_add(request, patient_id, routine_id=None):
    """
    routine checkup add
    """
    patient = get_patient(patient_id)

    if routine_id:
        routine = Routinecheckup.objects.get(id=routine_id)
        form = RoutinecheckupForm(instance=routine)
    else:
        form = RoutinecheckupForm()
    if request.method == "POST":
        if routine_id:
            routine = Routinecheckup.objects.get(id=routine_id)
            form = RoutinecheckupForm(request.POST, instance=routine)
        else:
            form = RoutinecheckupForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('routine_checkup', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'routine_id': routine_id,
    }
    return render_to_response('patient/routine_checkup_add.html', context, RequestContext(request))

@login_required
def laboratory_test(request, patient_id):
    """
    laboratory test
    """
    patient = get_patient(patient_id)
    labs = LaboratoryTest.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'labs': labs,
    }
    return render_to_response('patient/laboratory_test.html', context, RequestContext(request))

@login_required
def laboratory_test_add(request, patient_id, lab_id=None):
    """
    laboratory test add
    """
    patient = get_patient(patient_id)
    if lab_id:
        lab = LaboratoryTest.objects.get(id=lab_id)
        form = LaboratoryTestForm(instance=lab)
    else:
        form = LaboratoryTestForm()
    if request.method == "POST":
        if lab_id:
            lab = LaboratoryTest.objects.get(id=lab_id)
            form = LaboratoryTestForm(request.POST, instance=lab)
        else:
            form = LaboratoryTestForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('laboratory_test', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'lab_id': lab_id,
    }
    return render_to_response('patient/laboratory_test_add.html', context, RequestContext(request))

@login_required
def ultrasound_scanning(request, patient_id):
    """
    ultrasound scanning
    """
    patient = get_patient(patient_id)
    scans = UltrasoundScanning.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'scans': scans,
    }
    return render_to_response('patient/ultrasound_scanning.html', context, RequestContext(request))

@login_required
def ultrasound_scanning_add(request, patient_id, us_id=None):
    """
    ultrasound scanning add
    """
    patient = get_patient(patient_id)
    if us_id:
        scan = UltrasoundScanning.objects.get(id=us_id)
        form = UltrasoundScanningForm(instance=scan)
    else:
        scan = None
        form = UltrasoundScanningForm()
    if request.method == "POST":
        if us_id:
            scan = UltrasoundScanning.objects.get(id=us_id)
            form = UltrasoundScanningForm(request.POST, instance=scan)
        else:
            scan = None
            form = UltrasoundScanningForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            scan = form.save()
            img_id = request.POST.get('temp_img', None)
            if img_id:
                img = UltrasoundScanningImage.objects.get(id=img_id)
                img.us = scan
                img.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('ultrasound_scanning', args=[patient.id]))

    if scan:
        image = scan.get_image_url()
    else:
        image = ''
    context = {
        'patient': patient,
        'form': form,
        'us_id': us_id,
        'image': image,
        'scan': scan,
    }
    return render_to_response('patient/ultrasound_scanning_add.html', context, RequestContext(request))

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        img = UltrasoundScanningImage(image=request.FILES.get('file_upload'))
        scan_id = int(request.POST.get('scan', None))
        if scan_id:
            scan = UltrasoundScanning.objects.get(id=scan_id)
            img.us = scan
        img.save()
        return HttpResponse(img.id)
    return HttpResponse('')

@login_required
def ultrasound_scanning_img(request, img_id):
    image = ''
    try:
        img = UltrasoundScanningImage.objects.get(id=img_id)
        image = '<img src="%s" alt="Ultrasound Scan Image" class="ultrasound-img" />' % img.image.url
    except:
        pass
    return HttpResponse(image)

@login_required
def prescription(request, patient_id):
    """
    prescription
    """
    patient = get_patient(patient_id)
    prescriptions = Prescription.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'prescriptions': prescriptions,
    }
    return render_to_response('patient/prescription.html', context, RequestContext(request))

@login_required
def prescription_add(request, patient_id, prs_id=None):
    """
    prescription add
    """
    patient = get_patient(patient_id)
    if prs_id:
        prs = Prescription.objects.get(id=prs_id)
        form = PrescriptionForm(instance=prs)
    else:
        form = PrescriptionForm()
    if request.method == "POST":
        if prs_id:
            prs = Prescription.objects.get(id=prs_id)
            form = PrescriptionForm(request.POST, instance=prs)
        else:
            form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.patient = patient
            form.save()
            messages.success(request, _("Successfully save."), fail_silently=True)
            return redirect(reverse('prescription', args=[patient.id]))
    context = {
        'patient': patient,
        'form': form,
        'prs_id': prs_id,
    }
    return render_to_response('patient/prescription_add.html', context, RequestContext(request))

@login_required
def patient_info(request, patient_id, current_tab=1):
    """
    Display patient info
    """
    try:
        patient = PatientInformation.objects.get(id=patient_id)
        request.session['patient_id'] = patient.id
    except:
        raise Http404
    context = {
        'selected_page': 'patient',
        'patient': patient,
        'current_tab': current_tab,
    }
    return render_to_response('patient/patient_info.html', context, RequestContext(request))

@login_required
def patient_add(request):
    """
    Add new patient
    """
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            request.session['patient_id'] = patient.id
            # return redirect('patient_info', patient_id=patient.id)
            return redirect(reverse('patient_info', args=[patient.id]))
    else:
        form = AddPatientForm()
    context = {
        'selected_page': 'patient',
        'form': form,
    }
    return render_to_response('patient/patient_add.html', context, RequestContext(request))
