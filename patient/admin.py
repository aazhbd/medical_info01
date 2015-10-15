# -*- coding: utf-8 -*-

from django.contrib import admin

from patient.models import PatientInformation, AdditionalPatientInformation, Guardian, MedicalHistory, \
    PastMedicalHistory, FamilyMedicalHistory, MenstrualHistory, ObstetricHistory, \
    PreviousObstetricHistory, GynaecologicalHistory, ImmunizationHistory, PreviousSurgery, \
    Routinecheckup, Signanaemia, LaboratoryTest, UltrasoundScanning, Report

admin.site.register(PatientInformation)
admin.site.register(AdditionalPatientInformation)
admin.site.register(Guardian)
admin.site.register(MedicalHistory)
admin.site.register(PastMedicalHistory)
admin.site.register(FamilyMedicalHistory)
admin.site.register(MenstrualHistory)
admin.site.register(ObstetricHistory)
admin.site.register(PreviousObstetricHistory)
admin.site.register(GynaecologicalHistory)
admin.site.register(ImmunizationHistory)
admin.site.register(PreviousSurgery)
admin.site.register(Routinecheckup)
admin.site.register(Signanaemia)
admin.site.register(LaboratoryTest)
admin.site.register(UltrasoundScanning)
admin.site.register(Report)
