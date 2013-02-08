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
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('compras_app', ['Cliente'])

        # Adding model 'Compra'
        db.create_table('compras_app_compra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Cliente'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 7, 0, 0), blank=True)),
            ('fecha_limite', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 7, 0, 0), null=True, blank=True)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Sucursal'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('tipo_prestamo', self.gf('django.db.models.fields.CharField')(default='O', max_length=10)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=18, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('compras_app', ['Compra'])

        # Adding model 'Pago'
        db.create_table('compras_app_pago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Compra'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 7, 0, 0), blank=True)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Sucursal'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('compras_app', ['Pago'])


    def backwards(self, orm):
        # Deleting model 'Sucursal'
        db.delete_table('compras_app_sucursal')

        # Deleting model 'Cliente'
        db.delete_table('compras_app_cliente')

        # Deleting model 'Compra'
        db.delete_table('compras_app_compra')

        # Deleting model 'Pago'
        db.delete_table('compras_app_pago')


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