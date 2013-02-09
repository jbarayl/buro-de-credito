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
            ('dir_ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_light.City'], null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('dir_calle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dir_no_exterior', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('dir_no_interior', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('dir_colonia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dir_poblacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dir_referencia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institucion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('compras_app', ['Cliente'])

        # Adding model 'Compra'
        db.create_table('compras_app_compra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Cliente'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 9, 0, 0), blank=True)),
            ('fecha_limite', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 9, 0, 0), null=True, blank=True)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Sucursal'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('tipo_prestamo', self.gf('django.db.models.fields.CharField')(default='O', max_length=10)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('adeudo', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=18, decimal_places=2, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='P', max_length=10)),
        ))
        db.send_create_signal('compras_app', ['Compra'])

        # Adding model 'Pago'
        db.create_table('compras_app_pago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compras_app.Compra'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 9, 0, 0), blank=True)),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=18, decimal_places=2)),
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
        'cities_light.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Region']", 'null': 'True', 'blank': 'True'}),
            'search_names': ('cities_light.models.ToSearchTextField', [], {'default': "''", 'max_length': '4000', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'cities_light.country': {
            'Meta': {'object_name': 'Country'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        },
        'cities_light.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'alternate_names': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"})
        },
        'compras_app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'dir_calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dir_ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cities_light.City']", 'null': 'True', 'blank': 'True'}),
            'dir_colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dir_no_exterior': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dir_no_interior': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dir_poblacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dir_referencia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'compras_app.compra': {
            'Meta': {'object_name': 'Compra'},
            'adeudo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '18', 'decimal_places': '2', 'blank': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Cliente']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '10'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 9, 0, 0)', 'blank': 'True'}),
            'fecha_limite': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 9, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Sucursal']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'tipo_prestamo': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '10'})
        },
        'compras_app.pago': {
            'Compra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compras_app.Compra']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'Meta': {'object_name': 'Pago'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '2'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 9, 0, 0)', 'blank': 'True'}),
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