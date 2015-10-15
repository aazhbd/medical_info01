# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PatientInformation'
        db.create_table(u'patient_patientinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('operator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('telephone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'patient', ['PatientInformation'])

        # Adding model 'AdditionalPatientInformation'
        db.create_table(u'patient_additionalpatientinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('cigarettes', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('alcohol', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('literate', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('educational_level', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'patient', ['AdditionalPatientInformation'])

        # Adding model 'Guardian'
        db.create_table(u'patient_guardian', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('relation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('home_address', self.gf('django.db.models.fields.TextField')()),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('educational_level', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'patient', ['Guardian'])

        # Adding model 'MedicalHistory'
        db.create_table(u'patient_medicalhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('past_medical_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PastMedicalHistory'])),
            ('present_medical_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PresentMedicalHistory'])),
            ('family_medical_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.FamilyMedicalHistory'])),
            ('menstrual_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.MenstrualHistory'])),
            ('obstetric_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.ObstetricHistory'])),
            ('gynaecological_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.GynaecologicalHistory'])),
            ('immunization_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.ImmunizationHistory'])),
        ))
        db.send_create_signal(u'patient', ['MedicalHistory'])

        # Adding model 'PastMedicalHistory'
        db.create_table(u'patient_pastmedicalhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('tuberculosis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('heart_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('chronical_renal_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('epilepsy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diabetes_melitus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sexually_transmitted_infection', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hepatitis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('malaria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sickle_cell_trait', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rhesus_d_antibodies', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('HIV_status_if_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('kidney_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('liver_problems', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hypertension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('urinary_tract_surgeries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('seizures', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pelvic_backinjuries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haemorrhage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('others', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'patient', ['PastMedicalHistory'])

        # Adding model 'PresentMedicalHistory'
        db.create_table(u'patient_presentmedicalhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('tuberculosis', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('heart_disease', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('chronical_renal_disease', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('epilepsy', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('diabetes_melitus', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sexually_transmitted_infection', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('hepatitis', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('malaria', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sickle_cell_trait', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rhesus_d_antibodies', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('HIV_status_if_known', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('kidney_disease', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('liver_problems', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('hypertension', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('urinary_tract_surgeries', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('seizures', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pelvic_backinjuries', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('haemorrhage', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('others', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'patient', ['PresentMedicalHistory'])

        # Adding model 'FamilyMedicalHistory'
        db.create_table(u'patient_familymedicalhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('tuberculosis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('heart_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('chronical_renal_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('epilepsy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diabetes_melitus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sexually_transmitted_infection', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hepatitis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('malaria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sickle_cell_trait', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rhesus_d_antibodies', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('HIV_status_if_known', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('kidney_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('liver_problems', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hypertension', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('urinary_tract_surgeries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('seizures', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pelvic_backinjuries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('haemorrhage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('others', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'patient', ['FamilyMedicalHistory'])

        # Adding model 'MenstrualHistory'
        db.create_table(u'patient_menstrualhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('day_of_visit', self.gf('django.db.models.fields.DateField')()),
            ('menstrual_cycle', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('last_menstrual_periods', self.gf('django.db.models.fields.DateField')()),
            ('expected_date_of_delivery', self.gf('django.db.models.fields.DateField')()),
            ('poa_by_lmp', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patient', ['MenstrualHistory'])

        # Adding model 'ObstetricHistory'
        db.create_table(u'patient_obstetrichistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('check_if_you_have_been_miscarriages', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('check_if_you_have_been_pregnant', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('list_previous_obstetric_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PreviousObstetricHistory'])),
        ))
        db.send_create_signal(u'patient', ['ObstetricHistory'])

        # Adding model 'PreviousObstetricHistory'
        db.create_table(u'patient_previousobstetrichistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('year', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birth_weight', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('types_of_delivery', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('length_of_pregnancy', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('problems', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name_of_baby', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('age_of_baby', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('periods_of_exclusive_feeding', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('obstetrical_operation', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'patient', ['PreviousObstetricHistory'])

        # Adding model 'GynaecologicalHistory'
        db.create_table(u'patient_gynaecologicalhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('method_of_birth_control', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('previous_surgery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PreviousSurgery'])),
            ('date_of_last_pap_smear', self.gf('django.db.models.fields.DateField')()),
            ('result_pap_smear', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'patient', ['GynaecologicalHistory'])

        # Adding model 'ImmunizationHistory'
        db.create_table(u'patient_immunizationhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('vaccination', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('tetanus_toxoid1', self.gf('django.db.models.fields.DateTimeField')()),
            ('tetanus_toxoid2', self.gf('django.db.models.fields.DateTimeField')()),
            ('tetanus_toxoid3', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'patient', ['ImmunizationHistory'])

        # Adding model 'PreviousSurgery'
        db.create_table(u'patient_previoussurgery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('fibrocystic_breasts', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('ovarian_cysts', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('endometriosis', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('uterine_fibroids', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('others_please_state', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'patient', ['PreviousSurgery'])

        # Adding model 'Routinecheckup'
        db.create_table(u'patient_routinecheckup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('visit', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name_of_examiner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('symptom_events', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('sign_of_severe_anaemia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Signanaemia'])),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('blood_pressure', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('chest_and_heart_auscultation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('abdominal_changes', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fetal_movement', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('uterine_height', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('vaginal_examination', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'patient', ['Routinecheckup'])

        # Adding model 'Signanaemia'
        db.create_table(u'patient_signanaemia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('pale_complexion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fingernails', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('conjunctiva', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('oral_mucosa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tip_of_tongue', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shortness_of_breath', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('others_please_state', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'patient', ['Signanaemia'])

        # Adding model 'LaboratoryTest'
        db.create_table(u'patient_laboratorytest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('urinalysis', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('serological_test_for_syphilis', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hemoglobin', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'patient', ['LaboratoryTest'])

        # Adding model 'UltrasoundScanning'
        db.create_table(u'patient_ultrasoundscanning', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('gestation_age', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name_examiner', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('saved_ultrasound_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('CRL', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('BPD', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('FL', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('HC', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('AC', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount_of_amniotic_fluid', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('position_of_the_placenta', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('position_of_the_baby', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'patient', ['UltrasoundScanning'])

        # Adding model 'Report'
        db.create_table(u'patient_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('pregnancy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diabetis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hiv', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'patient', ['Report'])


    def backwards(self, orm):
        # Deleting model 'PatientInformation'
        db.delete_table(u'patient_patientinformation')

        # Deleting model 'AdditionalPatientInformation'
        db.delete_table(u'patient_additionalpatientinformation')

        # Deleting model 'Guardian'
        db.delete_table(u'patient_guardian')

        # Deleting model 'MedicalHistory'
        db.delete_table(u'patient_medicalhistory')

        # Deleting model 'PastMedicalHistory'
        db.delete_table(u'patient_pastmedicalhistory')

        # Deleting model 'PresentMedicalHistory'
        db.delete_table(u'patient_presentmedicalhistory')

        # Deleting model 'FamilyMedicalHistory'
        db.delete_table(u'patient_familymedicalhistory')

        # Deleting model 'MenstrualHistory'
        db.delete_table(u'patient_menstrualhistory')

        # Deleting model 'ObstetricHistory'
        db.delete_table(u'patient_obstetrichistory')

        # Deleting model 'PreviousObstetricHistory'
        db.delete_table(u'patient_previousobstetrichistory')

        # Deleting model 'GynaecologicalHistory'
        db.delete_table(u'patient_gynaecologicalhistory')

        # Deleting model 'ImmunizationHistory'
        db.delete_table(u'patient_immunizationhistory')

        # Deleting model 'PreviousSurgery'
        db.delete_table(u'patient_previoussurgery')

        # Deleting model 'Routinecheckup'
        db.delete_table(u'patient_routinecheckup')

        # Deleting model 'Signanaemia'
        db.delete_table(u'patient_signanaemia')

        # Deleting model 'LaboratoryTest'
        db.delete_table(u'patient_laboratorytest')

        # Deleting model 'UltrasoundScanning'
        db.delete_table(u'patient_ultrasoundscanning')

        # Deleting model 'Report'
        db.delete_table(u'patient_report')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patient.additionalpatientinformation': {
            'Meta': {'object_name': 'AdditionalPatientInformation'},
            'alcohol': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cigarettes': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'educational_level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literate': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"})
        },
        u'patient.familymedicalhistory': {
            'HIV_status_if_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'FamilyMedicalHistory'},
            'chronical_renal_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diabetes_melitus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'epilepsy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haemorrhage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'heart_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hepatitis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hypertension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kidney_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver_problems': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'malaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'pelvic_backinjuries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rhesus_d_antibodies': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seizures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexually_transmitted_infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sickle_cell_trait': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuberculosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urinary_tract_surgeries': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'patient.guardian': {
            'Meta': {'object_name': 'Guardian'},
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'educational_level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'home_address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'relation': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'patient.gynaecologicalhistory': {
            'Meta': {'object_name': 'GynaecologicalHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_last_pap_smear': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method_of_birth_control': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'previous_surgery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PreviousSurgery']"}),
            'result_pap_smear': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'patient.immunizationhistory': {
            'Meta': {'object_name': 'ImmunizationHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'tetanus_toxoid1': ('django.db.models.fields.DateTimeField', [], {}),
            'tetanus_toxoid2': ('django.db.models.fields.DateTimeField', [], {}),
            'tetanus_toxoid3': ('django.db.models.fields.DateTimeField', [], {}),
            'vaccination': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'patient.laboratorytest': {
            'Meta': {'object_name': 'LaboratoryTest'},
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'hemoglobin': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'serological_test_for_syphilis': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'urinalysis': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'patient.medicalhistory': {
            'Meta': {'object_name': 'MedicalHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'family_medical_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.FamilyMedicalHistory']"}),
            'gynaecological_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.GynaecologicalHistory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immunization_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.ImmunizationHistory']"}),
            'menstrual_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.MenstrualHistory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obstetric_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.ObstetricHistory']"}),
            'past_medical_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PastMedicalHistory']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'present_medical_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PresentMedicalHistory']"})
        },
        u'patient.menstrualhistory': {
            'Meta': {'object_name': 'MenstrualHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'day_of_visit': ('django.db.models.fields.DateField', [], {}),
            'expected_date_of_delivery': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_menstrual_periods': ('django.db.models.fields.DateField', [], {}),
            'menstrual_cycle': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'poa_by_lmp': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patient.obstetrichistory': {
            'Meta': {'object_name': 'ObstetricHistory'},
            'check_if_you_have_been_miscarriages': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'check_if_you_have_been_pregnant': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_previous_obstetric_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PreviousObstetricHistory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"})
        },
        u'patient.pastmedicalhistory': {
            'HIV_status_if_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'PastMedicalHistory'},
            'chronical_renal_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diabetes_melitus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'epilepsy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'haemorrhage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'heart_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hepatitis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hypertension': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kidney_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver_problems': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'malaria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'pelvic_backinjuries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rhesus_d_antibodies': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seizures': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexually_transmitted_infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sickle_cell_trait': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuberculosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urinary_tract_surgeries': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'patient.patientinformation': {
            'Meta': {'object_name': 'PatientInformation'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'telephone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'patient.presentmedicalhistory': {
            'HIV_status_if_known': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'Meta': {'object_name': 'PresentMedicalHistory'},
            'chronical_renal_disease': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diabetes_melitus': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'epilepsy': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'haemorrhage': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'heart_disease': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hepatitis': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hypertension': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kidney_disease': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'liver_problems': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'malaria': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'others': ('django.db.models.fields.TextField', [], {}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'pelvic_backinjuries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rhesus_d_antibodies': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'seizures': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sexually_transmitted_infection': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sickle_cell_trait': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tuberculosis': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'urinary_tract_surgeries': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'patient.previousobstetrichistory': {
            'Meta': {'object_name': 'PreviousObstetricHistory'},
            'age_of_baby': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'birth_weight': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_pregnancy': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_of_baby': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'obstetrical_operation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'periods_of_exclusive_feeding': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'problems': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'types_of_delivery': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.DateField', [], {})
        },
        u'patient.previoussurgery': {
            'Meta': {'object_name': 'PreviousSurgery'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'endometriosis': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fibrocystic_breasts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'others_please_state': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ovarian_cysts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'uterine_fibroids': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'patient.report': {
            'Meta': {'object_name': 'Report'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'diabetis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hiv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'pregnancy': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'patient.routinecheckup': {
            'Meta': {'object_name': 'Routinecheckup'},
            'abdominal_changes': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'blood_pressure': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'chest_and_heart_auscultation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'fetal_movement': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_of_examiner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'sign_of_severe_anaemia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Signanaemia']"}),
            'symptom_events': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uterine_height': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vaginal_examination': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'visit': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'patient.signanaemia': {
            'Meta': {'object_name': 'Signanaemia'},
            'conjunctiva': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fingernails': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'oral_mucosa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'others_please_state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pale_complexion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'shortness_of_breath': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tip_of_tongue': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'patient.ultrasoundscanning': {
            'AC': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'BPD': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'CRL': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'FL': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'HC': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'object_name': 'UltrasoundScanning'},
            'amount_of_amniotic_fluid': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'gestation_age': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_examiner': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'position_of_the_baby': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'position_of_the_placenta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'saved_ultrasound_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['patient']