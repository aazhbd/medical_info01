# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prescription'
        db.create_table(u'patient_prescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.PatientInformation'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name_of_prescription', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'patient', ['Prescription'])


        # Changing field 'Routinecheckup.date'
        db.alter_column(u'patient_routinecheckup', 'date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'LaboratoryTest.date'
        db.alter_column(u'patient_laboratorytest', 'date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'UltrasoundScanning.date'
        db.alter_column(u'patient_ultrasoundscanning', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting model 'Prescription'
        db.delete_table(u'patient_prescription')


        # Changing field 'Routinecheckup.date'
        db.alter_column(u'patient_routinecheckup', 'date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'LaboratoryTest.date'
        db.alter_column(u'patient_laboratorytest', 'date', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'UltrasoundScanning.date'
        db.alter_column(u'patient_ultrasoundscanning', 'date', self.gf('django.db.models.fields.DateTimeField')())

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
            'cooking_facilities': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'educational_level': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'literate': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_harmful_substances': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'psychological_stress': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'toilet_facilities': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'date': ('django.db.models.fields.DateField', [], {}),
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
        u'patient.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_of_prescription': ('django.db.models.fields.TextField', [], {}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"})
        },
        u'patient.presentmedicalhistory': {
            'HIV_status_if_known': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'PresentMedicalHistory'},
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'fetal_movement': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_of_examiner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'gestation_age': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name_examiner': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'position_of_the_baby': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'position_of_the_placenta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'saved_ultrasound_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['patient']