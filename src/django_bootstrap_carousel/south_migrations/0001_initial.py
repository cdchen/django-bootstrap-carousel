# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carousel'
        db.create_table(u'django_bootstrap_carousel_carousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, db_index=True)),
            ('interval', self.gf('django.db.models.fields.IntegerField')(default=5000)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_bootstrap_carousel', ['Carousel'])

        # Adding model 'CarouselItem'
        db.create_table(u'django_bootstrap_carousel_carouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carousel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['django_bootstrap_carousel.Carousel'])),
            ('display_title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('display_content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('activated', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
        ))
        db.send_create_signal(u'django_bootstrap_carousel', ['CarouselItem'])


    def backwards(self, orm):
        # Deleting model 'Carousel'
        db.delete_table(u'django_bootstrap_carousel_carousel')

        # Deleting model 'CarouselItem'
        db.delete_table(u'django_bootstrap_carousel_carouselitem')


    models = {
        u'django_bootstrap_carousel.carousel': {
            'Meta': {'object_name': 'Carousel'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '5000'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'})
        },
        u'django_bootstrap_carousel.carouselitem': {
            'Meta': {'ordering': "['carousel', 'weight']", 'object_name': 'CarouselItem'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'carousel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['django_bootstrap_carousel.Carousel']"}),
            'display_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['django_bootstrap_carousel']