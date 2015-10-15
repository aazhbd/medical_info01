# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q

from patient.models import PatientInformation, AdditionalPatientInformation, Guardian, \
    MedicalHistory, PastMedicalHistory, PresentMedicalHistory, FamilyMedicalHistory, \
    MenstrualHistory, ObstetricHistory, GynaecologicalHistory, ImmunizationHistory, \
    Routinecheckup, LaboratoryTest, UltrasoundScanning, Prescription, PreviousObstetricHistory, \
    PreviousSurgery

class SearchPatientForm(forms.Form):
    q = forms.CharField(label="Search", required=True)

    def results(self):
        """
        Filter the results from PatientInformation
        """
        q = self.cleaned_data['q'].strip()
        patients = PatientInformation.objects.filter(Q(operator__username__contains=q) | \
            Q(patient_id__contains=q) | Q(first_name__contains=q) | Q(last_name__contains=q) | \
            Q(email__contains=q)).distinct()
        return patients

class AddPatientForm(forms.ModelForm):
    """
    Form for add new patient
    """
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    class Meta:
        model = PatientInformation

class PatientInformationForm(forms.ModelForm):
    """
    Form for view or edit patient info
    """
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    class Meta:
        model = PatientInformation
        exclude = ('patient',)

class AdditionalPatientInformationForm(forms.ModelForm):
    """
    Form for view or edit additional patient info
    """
    # def __init__(self, patient=None, *args, **kwargs):
    #     super(AdditionalPatientInformationForm, self).__init__(*args, **kwargs)
    #     if patient:
    #         self.fields['patient'].initial = patient.id
    #         self.fields['patient'].widget.attrs['disabled'] = True

    class Meta:
        model = AdditionalPatientInformation
        exclude = ('patient',)

class GuardianForm(forms.ModelForm):
    """
    Form for view or edit guardian info
    """
    # def __init__(self, patient=None, *args, **kwargs):
    #     super(GuardianForm, self).__init__(*args, **kwargs)
    #     if patient:
    #         self.fields['patient'].initial = patient.id
    #         self.fields['patient'].widget.attrs['disabled'] = True

    class Meta:
        model = Guardian
        exclude = ('patient',)

class MedicalHistoryForm(forms.ModelForm):
    """
    form for MedicalHistory
    """
    class Meta:
        model = MedicalHistory
        exclude = ('patient',)

class PastMedicalHistoryForm(forms.ModelForm):
    """
    form for PastMedicalHistory
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    class Meta:
        model = PastMedicalHistory
        exclude = ('patient',)

class PresentMedicalHistoryForm(forms.ModelForm):
    """
    form for PresentMedicalHistory
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = PresentMedicalHistory
        exclude = ('patient',)

class FamilyMedicalHistoryForm(forms.ModelForm):
    """
    form for FamilyMedicalHistory
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = FamilyMedicalHistory
        exclude = ('patient',)

class MenstrualHistoryForm(forms.ModelForm):
    """
    form for MenstrualHistory
    """
    day_of_visit = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    last_menstrual_periods = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    expected_date_of_delivery = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = MenstrualHistory
        exclude = ('patient',)

class ObstetricHistoryForm(forms.ModelForm):
    """
    form for ObstetricHistory
    """
    class Meta:
        model = ObstetricHistory
        exclude = ('patient',)

class PreviousObstetricHistoryForm(forms.ModelForm):
    """
    form for PreviousObstetricHistory
    """
    dob = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = PreviousObstetricHistory
        exclude = ('patient',)

class GynaecologicalHistoryForm(forms.ModelForm):
    """
    form for GynaecologicalHistory
    """
    date_of_last_pap_smear = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = GynaecologicalHistory
        exclude = ('patient', 'previous_surgery',)

class ImmunizationHistoryForm(forms.ModelForm):
    """
    form for ImmunizationHistory
    """
    tetanus_toxoid1 = forms.DateTimeField(label="First Injection", widget=forms.TextInput(attrs={'class':'datetimepicker'}), required=False)
    tetanus_toxoid2 = forms.DateTimeField(label="Second Injection", widget=forms.TextInput(attrs={'class':'null-date'}), required=False)
    tetanus_toxoid3 = forms.DateTimeField(label="Third Injection", widget=forms.TextInput(attrs={'class':'null-date'}), required=False)

    class Meta:
        model = ImmunizationHistory
        exclude = ('patient',)

    def __init__(self, *args, **kwargs):
        super(ImmunizationHistoryForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            for i in ['tetanus_toxoid2', 'tetanus_toxoid3']:
                if instance.__dict__.get(i):
                    self.fields[i].widget = forms.TextInput(attrs={'class':'datetimepicker'})

class RoutinecheckupForm(forms.ModelForm):
    """
    form for Routinecheckup
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = Routinecheckup
        exclude = ('patient',)

class LaboratoryTestForm(forms.ModelForm):
    """
    form for LaboratoryTest
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = LaboratoryTest
        exclude = ('patient',)

class UltrasoundScanningForm(forms.ModelForm):
    """
    form for UltrasoundScanning
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    temp_img = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = UltrasoundScanning
        exclude = ('patient',)

class PrescriptionForm(forms.ModelForm):
    """
    form for Prescription
    """
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    class Meta:
        model = Prescription
        exclude = ('patient',)

class PreviousSurgeryForm(forms.ModelForm):
    """
    form for PreviousSurgery
    """
    class Meta:
        model = PreviousSurgery
        exclude = ('patient',)
