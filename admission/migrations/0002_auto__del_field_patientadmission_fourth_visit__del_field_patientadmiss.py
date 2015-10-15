# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PatientAdmission.fourth_visit'
        db.delete_column(u'admission_patientadmission', 'fourth_visit')

        # Deleting field 'PatientAdmission.second_visit'
        db.delete_column(u'admission_patientadmission', 'second_visit')

        # Deleting field 'PatientAdmission.other_visit'
        db.delete_column(u'admission_patientadmission', 'other_visit')

        # Deleting field 'PatientAdmission.third_visit'
        db.delete_column(u'admission_patientadmission', 'third_visit')

        # Deleting field 'PatientAdmission.first_visit'
        db.delete_column(u'admission_patientadmission', 'first_visit')

        # Adding field 'PatientAdmission.visit'
        db.add_column(u'admission_patientadmission', 'visit',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PatientAdmission.fourth_visit'
        db.add_column(u'admission_patientadmission', 'fourth_visit',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'PatientAdmission.second_visit'
        db.add_column(u'admission_patientadmission', 'second_visit',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'PatientAdmission.other_visit'
        db.add_column(u'admission_patientadmission', 'other_visit',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'PatientAdmission.third_visit'
        db.add_column(u'admission_patientadmission', 'third_visit',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'PatientAdmission.first_visit'
        db.add_column(u'admission_patientadmission', 'first_visit',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0)),
                      keep_default=False)

        # Deleting field 'PatientAdmission.visit'
        db.delete_column(u'admission_patientadmission', 'visit')


    models = {
        u'admission.patientadmission': {
            'Meta': {'object_name': 'PatientAdmission'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_admission': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_discharge': ('django.db.models.fields.DateTimeField', [], {}),
            'hospital_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.PatientInformation']"}),
            'visit': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
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
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telephone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['admission']