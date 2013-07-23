# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Criterio'
        db.create_table(u'Principal_criterio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'Principal', ['Criterio'])

        # Adding model 'Comentario'
        db.create_table(u'Principal_comentario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
        ))
        db.send_create_signal(u'Principal', ['Comentario'])

        # Adding M2M table for field docente on 'Comentario'
        m2m_table_name = db.shorten_name(u'Principal_comentario_docente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comentario', models.ForeignKey(orm[u'Principal.comentario'], null=False)),
            ('docente', models.ForeignKey(orm[u'Principal.docente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comentario_id', 'docente_id'])

        # Adding model 'Estudiante'
        db.create_table(u'Principal_estudiante', (
            (u'usuariobase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Principal.UsuarioBase'], unique=True, primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Carrera'])),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Localidad'])),
        ))
        db.send_create_signal(u'Principal', ['Estudiante'])

        # Adding model 'UsuarioBase'
        db.create_table(u'Principal_usuariobase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Principal', ['UsuarioBase'])

        # Adding model 'Calificacion'
        db.create_table(u'Principal_calificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puntaje', self.gf('django.db.models.fields.IntegerField')()),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Principal.Docente'])),
        ))
        db.send_create_signal(u'Principal', ['Calificacion'])

        # Adding M2M table for field criterio on 'Calificacion'
        m2m_table_name = db.shorten_name(u'Principal_calificacion_criterio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('calificacion', models.ForeignKey(orm[u'Principal.calificacion'], null=False)),
            ('criterio', models.ForeignKey(orm[u'Principal.criterio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['calificacion_id', 'criterio_id'])

        # Deleting field 'Horario.Domingo'
        db.delete_column(u'Principal_horario', 'Domingo')

        # Adding field 'Horario.domingo'
        db.add_column(u'Principal_horario', 'domingo',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Criterio'
        db.delete_table(u'Principal_criterio')

        # Deleting model 'Comentario'
        db.delete_table(u'Principal_comentario')

        # Removing M2M table for field docente on 'Comentario'
        db.delete_table(db.shorten_name(u'Principal_comentario_docente'))

        # Deleting model 'Estudiante'
        db.delete_table(u'Principal_estudiante')

        # Deleting model 'UsuarioBase'
        db.delete_table(u'Principal_usuariobase')

        # Deleting model 'Calificacion'
        db.delete_table(u'Principal_calificacion')

        # Removing M2M table for field criterio on 'Calificacion'
        db.delete_table(db.shorten_name(u'Principal_calificacion_criterio'))

        # Adding field 'Horario.Domingo'
        db.add_column(u'Principal_horario', 'Domingo',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Horario.domingo'
        db.delete_column(u'Principal_horario', 'domingo')


    models = {
        u'Principal.calificacion': {
            'Meta': {'object_name': 'Calificacion'},
            'criterio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Principal.Criterio']", 'symmetrical': 'False'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Docente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Principal.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'coordinador': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facultad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Facultad']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'Principal.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'docente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Principal.Docente']", 'symmetrical': 'False'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Principal.criterio': {
            'Meta': {'object_name': 'Criterio'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Principal.docente': {
            'Meta': {'object_name': 'Docente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Principal.estudiante': {
            'Meta': {'object_name': 'Estudiante', '_ormbases': [u'Principal.UsuarioBase']},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Carrera']"}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Principal.Localidad']"}),
            u'usuariobase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['Principal.UsuarioBase']", 'unique': 'True', 'primary_key': 'True'})
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
        },
        u'Principal.usuariobase': {
            'Meta': {'object_name': 'UsuarioBase'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['Principal']