# -*- coding: utf-8 -*-

from django import forms

from admission.models import PatientVisit, HospitalAdmission

VISIT_LIST = ['first_visit', 'second_visit', 'third_visit', 'fourth_visit', 'fifth_visit', 'other_visit']

class PatientVisitForm(forms.ModelForm):
    """
    Form for PatientVisit
    """
    first_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    second_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    third_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    fourth_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    fifth_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    other_visit = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'null-date'}), required=False)

    class Meta:
        model = PatientVisit
        exclude = ('patient',)

    def __init__(self, *args, **kwargs):
        super(PatientVisitForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            for i in VISIT_LIST:
                if instance.__dict__.get(i):
                    self.fields[i].widget = forms.TextInput(attrs={'class':'datetimepicker'})


class PatientAdmissionForm(forms.ModelForm):
    """
    Form for HospitalAdmission
    """
    date_of_admission = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'datetimepicker'}))
    date_of_discharge = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'datetimepicker'}))

    class Meta:
        model = HospitalAdmission
        exclude = ('patient',)
