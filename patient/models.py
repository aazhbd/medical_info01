# -*- coding: utf-8 -*-
import os, datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings

from irpmemr.models import CommonModel
from irpmemr.const import COOKING_FACILITIES, TOILET_CHOICES, MARITAL_CHOICES, FREQUENCY_CHOICES, LITERATE_CHOICES, LEVEL_CHOICES, EDUCATIONAL_LEVEL_CHOICES, \
    RELATIONSHIP_CHOICES, MENSTRUAL_CYCLE_CHOICES, HAVE_BEEN_PREGNANT_CHOICES, SEX_CHOICES, TYPES_OF_DELIVERY_CHOICES, \
    PROBLEMS_CHOICES, OBSTETRICALOPERATION_CHOICES, METHOD_OF_BIRTH_CONTROL_CHOICES, NORMAL_CHOICES, \
    VACCINATION_CHOICES, VISIT_CHOICES, BLOOD_PRESSURE_CHOICES, URINALYSIS_CHOICES, HEMOGLOBIN_CHOICES, \
    MATERNAL_COMPLICATIONS_CHOICES, PERINATAL_COMPLICATIONS_CHOICES

##############################################Patient Information#####################################################################
class PatientInformation(CommonModel):
    operator = models.ForeignKey(User)
    patient_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()
    telephone_number = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=2, choices=MARITAL_CHOICES)
    email = models.EmailField()

    def __unicode__(self):
        return self.get_fullname()

    def get_fullname(self):
        """
        Return patient full name
        """
        return u"%s %s" % (self.first_name, self.last_name)

    def get_age(self):
        """
        Return calculated age from DOB
        """
        try:
            age = timezone.datetime.now().year - self.date_of_birth.year
            return age
        except:
            return 0

    def get_absolute_url(self):
        return reverse('patient_info', args=[self.id])

class AdditionalPatientInformation(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    cigarettes = models.CharField(max_length=2, choices=FREQUENCY_CHOICES)
    alcohol = models.CharField(max_length=2, choices=FREQUENCY_CHOICES)
    other_harmful_substances = models.CharField(max_length=50)
    toilet_facilities = models.CharField(max_length=20, choices=TOILET_CHOICES)
    cooking_facilities = models.CharField(max_length=20, choices=COOKING_FACILITIES)
    literate = models.CharField(max_length=2, choices=LITERATE_CHOICES)
    psychological_stress = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    educational_level = models.CharField(max_length=2, choices=EDUCATIONAL_LEVEL_CHOICES)
    occupation  = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.patient.get_fullname())

class Guardian(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    relation = models.CharField(max_length=2, choices=RELATIONSHIP_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    home_address = models.TextField()
    job = models.CharField(max_length=20)
    educational_level = models.CharField(max_length=2, choices=EDUCATIONAL_LEVEL_CHOICES)

    def __unicode__(self):
        return str(self.first_name)

    def get_fullname(self):
        """
        Return guardian full name
        """
        return u"%s %s" % (self.first_name, self.last_name)
######################################################################################################################################
class MedicalHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    past_medical_history = models.ForeignKey('PastMedicalHistory')
    present_medical_history = models.ForeignKey('PresentMedicalHistory')
    family_medical_history = models.ForeignKey('FamilyMedicalHistory')
    menstrual_history = models.ForeignKey('MenstrualHistory')
    obstetric_history = models.ForeignKey('ObstetricHistory')
    gynaecological_history = models.ForeignKey('GynaecologicalHistory')
    immunization_history = models.ForeignKey('ImmunizationHistory')

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Medical History"
        verbose_name_plural = "Medical Histories"

class PastMedicalHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    tuberculosis = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    chronical_renal_disease = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    diabetes_melitus = models.BooleanField(default=False)
    sexually_transmitted_infection = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    malaria = models.BooleanField(default=False)
    sickle_cell_trait = models.BooleanField(default=False)
    rhesus_d_antibodies = models.BooleanField(default=False)
    HIV_status_if_known = models.BooleanField(default=False)
    kidney_disease = models.BooleanField(default=False)
    liver_problems = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    urinary_tract_surgeries = models.BooleanField(default=False)
    seizures = models.BooleanField(default=False)
    pelvic_backinjuries = models.BooleanField(default=False)
    haemorrhage = models.BooleanField(default=False)
    others    = models.TextField(blank=True, default='')

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Medical History"
        verbose_name_plural = "Medical Histories"

class PresentMedicalHistory(CommonModel):

    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    tuberculosis = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    chronical_renal_disease = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    diabetes_melitus = models.BooleanField(default=False)
    sexually_transmitted_infection = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    malaria = models.BooleanField(default=False)
    sickle_cell_trait = models.BooleanField(default=False)
    rhesus_d_antibodies = models.BooleanField(default=False)
    HIV_status_if_known = models.BooleanField(default=False)
    kidney_disease = models.BooleanField(default=False)
    liver_problems = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    urinary_tract_surgeries = models.BooleanField(default=False)
    seizures = models.BooleanField(default=False)
    pelvic_backinjuries = models.BooleanField(default=False)
    haemorrhage = models.BooleanField(default=False)
    others    = models.TextField(blank=True, default='')

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Present Medical History"
        verbose_name_plural = "Present Medical Histories"

class FamilyMedicalHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    tuberculosis = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    chronical_renal_disease = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    diabetes_melitus = models.BooleanField(default=False)
    sexually_transmitted_infection = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    malaria = models.BooleanField(default=False)
    sickle_cell_trait = models.BooleanField(default=False)
    rhesus_d_antibodies = models.BooleanField(default=False)
    HIV_status_if_known = models.BooleanField(default=False)
    kidney_disease = models.BooleanField(default=False)
    liver_problems = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    urinary_tract_surgeries = models.BooleanField(default=False)
    seizures = models.BooleanField(default=False)
    pelvic_backinjuries = models.BooleanField(default=False)
    haemorrhage = models.BooleanField(default=False)
    others    = models.TextField(blank=True, default='')

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Family Medical History"
        verbose_name_plural = "Family Medical Histories"

class MenstrualHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    day_of_visit = models.DateField()
    menstrual_cycle = models.CharField(max_length=2, choices=MENSTRUAL_CYCLE_CHOICES)
    last_menstrual_periods = models.DateField()
    expected_date_of_delivery = models.DateField()
    poa_by_lmp = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Menstrual History"
        verbose_name_plural = "Menstrual Histories"

class ObstetricHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    check_if_you_have_been_miscarriages = models.IntegerField(max_length=2, choices=HAVE_BEEN_PREGNANT_CHOICES, default=0)
    check_if_you_have_been_pregnant = models.IntegerField(max_length=2, choices=HAVE_BEEN_PREGNANT_CHOICES, default=0)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Obstetric History"
        verbose_name_plural = "Obstetric Histories"

class PreviousObstetricHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_weight = models.CharField(max_length=50)
    types_of_delivery = models.CharField(max_length=2, choices=TYPES_OF_DELIVERY_CHOICES)
    length_of_pregnancy = models.CharField(max_length=10)
    name_of_baby = models.CharField(max_length=30)
    age_of_baby = models.CharField(max_length=30)
    periods_of_exclusive_feeding = models.CharField(max_length=30)
    obstetrical_operation = models.CharField(max_length=2, choices = OBSTETRICALOPERATION_CHOICES)
    maternal_complication = models.CharField(max_length=2, choices=MATERNAL_COMPLICATIONS_CHOICES)
    perinatal_complication = models.CharField(max_length=2, choices=PERINATAL_COMPLICATIONS_CHOICES)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Previous Obstetric History"
        verbose_name_plural = "Previous Obstetric Histories"

class GynaecologicalHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    method_of_birth_control = models.CharField(max_length=2, choices=METHOD_OF_BIRTH_CONTROL_CHOICES)
    date_of_last_pap_smear = models.DateField("Date Of Last Pap Smear")
    result_pap_smear =    models.CharField(max_length=2, choices=NORMAL_CHOICES)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Gynaecological History"
        verbose_name_plural = "Gynaecological Histories"

class ImmunizationHistory(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    vaccination = models.CharField(max_length=2, choices=VACCINATION_CHOICES)
    tetanus_toxoid1 = models.DateTimeField("First Injection", null=True)
    tetanus_toxoid2 = models.DateTimeField("Second Injection", null=True)
    tetanus_toxoid3 = models.DateTimeField("Third Injection", null=True)
    others_injection    = models.TextField(blank=True, default='')

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Immunization History"
        verbose_name_plural = "Immunization Histories"

class PreviousSurgery(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    fibrocystic_breasts = models.BooleanField(default=False)
    ovarian_cysts = models.BooleanField(default=False)
    endometriosis = models.BooleanField(default=False)
    uterine_fibroids = models.BooleanField(default=False)
    others_please_state = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    class Meta:
        verbose_name = "Previous Surgery"
        verbose_name_plural = "Previous Surgeries"

class Routinecheckup(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    visit = models.CharField(max_length=2, choices=VISIT_CHOICES)
    date = models.DateField()
    name_of_examiner = models.CharField(max_length=50)
    symptom_events = models.CharField(max_length=300)
    # sign_of_severe_anaemia = models.ForeignKey('Signanaemia')
    weight = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    blood_pressure = models.CharField(max_length=2, choices=BLOOD_PRESSURE_CHOICES)
    chest_and_heart_auscultation = models.CharField(max_length=2, choices=NORMAL_CHOICES)
    abdominal_changes = models.CharField(max_length=2, choices=NORMAL_CHOICES)
    fetal_movement = models.CharField(max_length=300)
    uterine_height = models.CharField(max_length=200)
    vaginal_examination = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    def get_absolute_url(self):
        return reverse('routine_checkup_view', args=[self.patient.id, self.id])

class Signanaemia(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    pale_complexion = models.CharField(max_length=200)
    fingernails = models.CharField(max_length=200)
    conjunctiva = models.CharField(max_length=200)
    oral_mucosa = models.CharField(max_length=200)
    tip_of_tongue = models.CharField(max_length=200)
    shortness_of_breath = models.CharField(max_length=200)
    others_please_state = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.patient.get_fullname())

class LaboratoryTest(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    urinalysis = models.CharField(max_length=2, choices=URINALYSIS_CHOICES)
    serological_test_for_syphilis = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=200)
    hemoglobin = models.CharField(max_length=1, choices=HEMOGLOBIN_CHOICES)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    def get_absolute_url(self):
        return reverse('laboratory_test_view', args=[self.patient.id, self.id])

class UltrasoundScanning(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    gestation_age = models.CharField(max_length=40)
    name_examiner = models.CharField(max_length=40)
    # saved_ultrasound_image = models.FileField(upload_to="images/", null=True, blank=True)
    CRL =  models.CharField(max_length=10)
    BPD =  models.CharField(max_length=10)
    FL =  models.CharField(max_length=10)
    HC =  models.CharField(max_length=10)
    AC =  models.CharField(max_length=10)
    amount_of_amniotic_fluid =  models.IntegerField(max_length=10)
    position_of_the_placenta =  models.CharField(max_length=10)
    position_of_the_baby = models.CharField(max_length=10)

    def __unicode__(self):
        return str(self.patient.get_fullname())

    def get_absolute_url(self):
        return reverse('ultrasound_scanning_view', args=[self.patient.id, self.id])

    def get_image_url(self):
        try:
            img = self.ultrasoundscanningimage_set.latest('id')
            return "%s" % img.image.url
        except:
            return None

def _generate_img_filename(instance, old_filename):
    """
    Use to generate image filename.
    """
    ext = os.path.splitext(old_filename)[1].lower()
    filename = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    return 'ultrasound/%s%s' % (filename, ext,)

class UltrasoundScanningImage(CommonModel):
    us = models.ForeignKey('UltrasoundScanning', null=True, blank=True)
    image = models.ImageField(upload_to=_generate_img_filename, null=True, blank=True)

    def get_image_url(self):
        try:
            return "%s" % self.image.url
        except:
            return None

class Prescription(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    date = models.DateField()
    name_of_prescription = models.TextField()

    def __unicode__(self):
        return str(self.patient.get_fullname())

    def get_absolute_url(self):
        return reverse('prescription_view', args=[self.patient.id, self.id])

class Report(CommonModel):
    patient = models.ForeignKey('PatientInformation')
    pregnancy = models.BooleanField(default=False)
    diabetis = models.BooleanField(default=False)
    hiv = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.patient.get_fullname())

