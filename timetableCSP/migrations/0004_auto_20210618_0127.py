# Generated by Django 3.2.4 on 2021-06-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableCSP', '0003_rename_speciality_subjects_speciality_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='speciality_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]