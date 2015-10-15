# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

# from patient.views import FileUploadView

urlpatterns = patterns('patient.views',
    url(r'^visit/(?P<patient_id>\w+)/$', 'patient_visit', name="patient_visit"),
    url(r'^visit/add/(?P<patient_id>\w+)/$', 'patient_visit_add', name="patient_visit_add"),

    url(r'^admission/add/(?P<patient_id>\w+)/$', 'patient_admission_add', name="patient_admission_add"),
    url(r'^admission/view/(?P<patient_id>\w+)/(?P<admission_id>\w+)/$', 'patient_admission_add', name="patient_admission_view"),

    url(r'^basic-information/(?P<patient_id>\w+)/$', 'basic_patient_information', name="basic_patient_information"),
    url(r'^additional-details/(?P<patient_id>\w+)/$', 'additional_details', name="additional_details"),

    url(r'^medical-history/(?P<patient_id>\w+)/$', 'medical_history', name="medical_history"),
    url(r'^past-medical-history/(?P<patient_id>\w+)/$', 'past_medical_history', name="past_medical_history"),
    url(r'^menstrual-history/(?P<patient_id>\w+)/$', 'menstrual_history', name="menstrual_history"),
    url(r'^obstetric-history/(?P<patient_id>\w+)/$', 'obstetric_history', name="obstetric_history"),
    url(r'^obstetric-add/(?P<patient_id>\w+)/$', 'obstetric_add', name="obstetric_add"),
    url(r'^present-medical-history/(?P<patient_id>\w+)/$', 'present_medical_history', name="present_medical_history"),
    url(r'^gynaecological-history/(?P<patient_id>\w+)/$', 'gynaecological_history', name="gynaecological_history"),
    url(r'^immunization-history/(?P<patient_id>\w+)/$', 'immunization_history', name="immunization_history"),

    url(r'^routine-checkup/(?P<patient_id>\w+)/$', 'routine_checkup', name="routine_checkup"),
    url(r'^routine-checkup/add/(?P<patient_id>\w+)/$', 'routine_checkup_add', name="routine_checkup_add"),
    url(r'^routine-checkup/view/(?P<patient_id>\w+)/(?P<routine_id>\w+)/$', 'routine_checkup_add', name="routine_checkup_view"),

    url(r'^laboratory-test/(?P<patient_id>\w+)/$', 'laboratory_test', name="laboratory_test"),
    url(r'^laboratory-test/add/(?P<patient_id>\w+)/$', 'laboratory_test_add', name="laboratory_test_add"),
    url(r'^laboratory-test/view/(?P<patient_id>\w+)/(?P<lab_id>\w+)/$', 'laboratory_test_add', name="laboratory_test_view"),

    url(r'^ultrasound-scanning/(?P<patient_id>\w+)/$', 'ultrasound_scanning', name="ultrasound_scanning"),
    url(r'^ultrasound-scanning/add/(?P<patient_id>\w+)/$', 'ultrasound_scanning_add', name="ultrasound_scanning_add"),
    url(r'^ultrasound-scanning/view/(?P<patient_id>\w+)/(?P<us_id>\w+)/$', 'ultrasound_scanning_add', name="ultrasound_scanning_view"),
    url(r'^ultrasound-scanning/img-upload/$', 'upload_image', name="ultrasound_upload_image"),
    url(r'^ultrasound-scanning/img/(?P<img_id>\w+)/$', 'ultrasound_scanning_img', name="ultrasound_scanning_img"),

    url(r'^prescription/(?P<patient_id>\w+)/$', 'prescription', name="prescription"),
    url(r'^prescription/add/(?P<patient_id>\w+)/$', 'prescription_add', name="prescription_add"),
    url(r'^prescription/view/(?P<patient_id>\w+)/(?P<prs_id>\w+)/$', 'prescription_add', name="prescription_view"),

    url(r'^add/$', 'patient_add', name="patient_add"),
    url(r'^(?P<patient_id>\w+)/(?P<current_tab>\w+)/$', 'patient_info', name="patient_info_tab"),
    url(r'^(?P<patient_id>\w+)/$', 'patient_info', name="patient_info"),
    url(r'^$', 'patient_home', name="patient_home"),
)

# urlpatterns += patterns('',
#     (r'^us-upload/$', FileUploadView.as_view()),
# )
