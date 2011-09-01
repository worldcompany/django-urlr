# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        if not db.dry_run:
            # Find all dupes, with possible false positives, since we're only aggregating on object_id
            links = orm.LinkShortenedItem.objects.values('content_type', 'object_id').annotate(id_count=models.Count('object_id')).filter(id_count__gt=1)
            for link in links:
                dupes = LinkShortenedItem.objects.filter(content_type=link['content_type'], object_id=link['object_id'])
                for dupe in dupes[1:]:
                    dupe.delete()

        # Adding unique constraint on 'LinkShortenedItem', fields ['content_type', 'object_id']
        db.create_unique('urlr_linkshorteneditem', ['content_type_id', 'object_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'LinkShortenedItem', fields ['content_type', 'object_id']
        db.delete_unique('urlr_linkshorteneditem', ['content_type_id', 'object_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'urlr.linkshorteneditem': {
            'Meta': {'unique_together': "(('object_id', 'content_type'),)", 'object_name': 'LinkShortenedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'shortened_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['urlr']
