# Generated by Django 3.2.4 on 2021-06-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetableCSP', '0005_class_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='room',
        ),
        migrations.RemoveField(
            model_name='class',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='class',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
