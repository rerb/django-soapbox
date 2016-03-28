# -*- coding: utf-8 -*-
from django.db import models


try:
    from django.db import migrations

    class Migration(migrations.Migration):

        dependencies = [
        ]

        operations = [
            migrations.CreateModel(
                name='Message',
                fields=[
                    ('id',
                     models.AutoField(verbose_name='ID',
                                      serialize=False,
                                      auto_created=True,
                                      primary_key=True)),
                    ('message',
                     models.TextField()),
                    ('is_global',
                     models.BooleanField(
                         default=False,
                         help_text=(b'If checked, this message will '
                                    b'display on all pages.'))),
                    ('is_active',
                     models.BooleanField(
                         default=True,
                         help_text=b'Only active messages will be displayed.')),
                    ('url',
                     models.CharField(
                         help_text=(b'Message will be displayed on any URL '
                                    b'which matches this.'),
                         max_length=255,
                         null=True,
                         verbose_name=b'URL',
                         blank=True)),
                ],
                options={
                    'ordering': ['-id'],
                },
            ),
        ]

except ImportError:

    from south.db import db
    from south.v2 import SchemaMigration

    class Migration(SchemaMigration):

        def forwards(self, orm):
            # Adding model 'Message'
            db.create_table('soapbox_message', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('message', self.gf('django.db.models.fields.TextField')()),
                ('is_global', self.gf('django.db.models.fields.BooleanField')(default=False)),
                ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
                ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ))
            db.send_create_signal('soapbox', ['Message'])


        def backwards(self, orm):
            # Deleting model 'Message'
            db.delete_table('soapbox_message')


        models = {
            'soapbox.message': {
                'Meta': {'ordering': "['-id']", 'object_name': 'Message'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
                'is_global': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
                'message': ('django.db.models.fields.TextField', [], {}),
                'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
            }
        }

        complete_apps = ['soapbox']
