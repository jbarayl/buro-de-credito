# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sucursal'
        db.create_table('compras_app_sucursal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('compras_app', ['Sucursal'])

        # Adding model 'Cliente'
        db.create_table('compras_app_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('dir_calle', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dir_no_exterior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dir_no_interior', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dir_colonia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dir_poblacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dir_referencia', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('compras_app', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Sucursal'
        db.delete_table('compras_app_sucursal')

        # Deleting model 'Cliente'
        db.delete_table('compras_app_cliente')


    models = {
        'compras_app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'dir_calle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dir_colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dir_no_exterior': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'dir_no_interior': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'dir_poblacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dir_referencia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'compras_app.sucursal': {
            'Meta': {'object_name': 'Sucursal'},
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['compras_app']