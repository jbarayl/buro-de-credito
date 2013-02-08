# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Compra.estado'
        db.add_column('compras_app_compra', 'estado',
                      self.gf('django.db.models.fields.CharField')(default='P', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Compra.estado'
        db.delete_column('compras_app_compra', 'estado')


    models = {
        'compras_app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'compras_app.compra': {
            'Meta': {'object_name': 'Compra'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Cliente']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '10'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 7, 0, 0)', 'blank': 'True'}),
            'fecha_limite': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 7, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Sucursal']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'tipo_prestamo': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '10'})
        },
        'compras_app.pago': {
            'Compra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Compra']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'Meta': {'object_name': 'Pago'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 7, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Sucursal']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
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