# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('tasks_category')

        # Adding field 'Type.name'
        db.add_column('tasks_type', 'name', self.gf('django.db.models.fields.CharField')(default=2, max_length=100), keep_default=False)

        # Deleting field 'Task.assigned_to'
        db.delete_column('tasks_task', 'assigned_to_id')

        # Deleting field 'Task.submitter'
        db.delete_column('tasks_task', 'submitter_id')

        # Adding field 'Priority.name'
        db.add_column('tasks_priority', 'name', self.gf('django.db.models.fields.CharField')(default=2, max_length=100), keep_default=False)

        # Adding field 'Status.name'
        db.add_column('tasks_status', 'name', self.gf('django.db.models.fields.CharField')(default=2, max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('tasks_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('tasks', ['Category'])

        # Deleting field 'Type.name'
        db.delete_column('tasks_type', 'name')

        # Adding field 'Task.assigned_to'
        db.add_column('tasks_task', 'assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']), keep_default=False)

        # Adding field 'Task.submitter'
        db.add_column('tasks_task', 'submitter', self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='submitter', to=orm['auth.User']), keep_default=False)

        # Deleting field 'Priority.name'
        db.delete_column('tasks_priority', 'name')

        # Deleting field 'Status.name'
        db.delete_column('tasks_status', 'name')


    models = {
        'tasks.priority': {
            'Meta': {'object_name': 'Priority'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tasks.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tasks.task': {
            'Meta': {'ordering': "('submitted_date',)", 'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Priority']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Status']"}),
            'submitted_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Type']"})
        },
        'tasks.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tasks']
