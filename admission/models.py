# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from irpmemr.models import CommonModel

class PatientVisit(CommonModel):
    patient = models.OneToOneField('patient.PatientInformation')
    first_visit = models.DateTimeField(null=True, blank=True)
    second_visit = models.DateTimeField(null=True, blank=True)
    third_visit = models.DateTimeField(null=True, blank=True)
    fourth_visit = models.DateTimeField(null=True, blank=True)
    fifth_visit = models.DateTimeField(null=True, blank=True)
    other_visit = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.patient.get_fullname())

class HospitalAdmission(CommonModel):
    patient = models.ForeignKey('patient.PatientInformation')
    hospital_name = models.CharField(max_length=50)
    date_of_admission = models.DateTimeField("Date of admission")
    date_of_discharge = models.DateTimeField("Date of discharge")

    def __unicode__(self):
        return str(self.patient.get_fullname())

    def get_absolute_url(self):
        return reverse('patient_admission_view', args=[self.patient.id, self.id])


