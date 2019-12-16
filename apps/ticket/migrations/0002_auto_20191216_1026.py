# Generated by Django 3.0 on 2019-12-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    def forwards_func(apps, schema_editor):
        db_alias = schema_editor.connection.alias

        Status = apps.get_model('ticket', 'Status')
        Status.objects.using(db_alias).bulk_create([
            Status(name='ACCEPTED', id=1),
            Status(name='REJECTE', id=2),
            Status(name='PENDING', id=3),
            Status(name='FAILED', id=4)
        ])

    def reverse_func(apps, schema_editor):
        db_alias = schema_editor.connection.alias

        Status = app.get_model('ticket', 'Status')
        Status.objects.using(db_alias).all().delete()

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
