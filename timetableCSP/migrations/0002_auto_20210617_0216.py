# Generated by Django 3.2.4 on 2021-06-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableCSP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject_teacher',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_subjects',
            field=models.ManyToManyField(null=True, to='timetableCSP.Subject'),
        ),
    ]
