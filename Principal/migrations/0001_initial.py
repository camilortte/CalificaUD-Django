# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Localidad'
        db.create_table(u'Principal_localidad', (
            ('idLocalidad', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'Principal', ['Localidad'])

        # Adding model 'Facultad'
        db.create_table(u'Principal_facultad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('nombre_decano', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['Facultad'])

        # Adding model 'Carrera'
        db.create_table(u'Principal_carrera', (
            ('codigo', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('coordinador', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('facultad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Facultad'])),
        ))
        db.send_create_signal(u'Principal', ['Carrera'])

        # Adding model 'Docente'
        db.create_table(u'Principal_docente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('informacion', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['Docente'])

        # Adding model 'Horario'
        db.create_table(u'Principal_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lunes', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('martes', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('miercoles', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('jueves', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('viernes', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('sabado', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('domingo', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['Horario'])

        # Adding model 'Materia'
        db.create_table(u'Principal_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero_creditos', self.gf('django.db.models.fields.IntegerField')()),
            ('intensidad_horaria_semanal', self.gf('django.db.models.fields.IntegerField')()),
            ('temario', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('horario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Horario'], null=True, blank=True)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Carrera'])),
        ))
        db.send_create_signal(u'Principal', ['Materia'])

        # Adding M2M table for field profesor on 'Materia'
        m2m_table_name = db.shorten_name(u'Principal_materia_profesor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('materia', models.ForeignKey(orm[u'Principal.materia'], null=False)),
            ('docente', models.ForeignKey(orm[u'Principal.docente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['materia_id', 'docente_id'])


    def backwards(self, orm):
        # Deleting model 'Localidad'
        db.delete_table(u'Principal_localidad')

        # Deleting model 'Facultad'
        db.delete_table(u'Principal_facultad')

        # Deleting model 'Carrera'
        db.delete_table(u'Principal_carrera')

        # Deleting model 'Docente'
        db.delete_table(u'Principal_docente')

        # Deleting model 'Horario'
        db.delete_table(u'Principal_horario')

        # Deleting model 'Materia'
        db.delete_table(u'Principal_materia')

        # Removing M2M table for field profesor on 'Materia'
        db.delete_table(db.shorten_name(u'Principal_materia_profesor'))


    models = {
        u'Principal.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'coordinador': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facultad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Facultad']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'Principal.docente': {
            'Meta': {'object_name': 'Docente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Principal.facultad': {
            'Meta': {'object_name': 'Facultad'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre_decano': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'Principal.horario': {
            'Meta': {'object_name': 'Horario'},
            'domingo': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jueves': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'lunes': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'martes': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'miercoles': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sabado': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'viernes': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'Principal.localidad': {
            'Meta': {'object_name': 'Localidad'},
            'idLocalidad': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Principal.materia': {
            'Meta': {'object_name': 'Materia'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Carrera']"}),
            'horario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Horario']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intensidad_horaria_semanal': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_creditos': ('django.db.models.fields.IntegerField', [], {}),
            'profesor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Principal.Docente']", 'symmetrical': 'False'}),
            'temario': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Principal']