from django.db import models

# Create your models here.

from multiselectfield import MultiSelectField



class Room(models.Model):

    room_id = models.CharField(max_length=2000, primary_key=True)
    room_name = models.CharField(max_length=2000, null=True)
    room_max_students = models.IntegerField(null=True)
    def __str__(self):
        return self.room_id #+ ' - ' + self.room_name


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=2000,primary_key=True)
    teacher_name = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.teacher_name


class Subject(models.Model):
    subject_id = models.CharField(max_length=1000, primary_key=True)
    subject_name = models.CharField(max_length=1000, null=True)
    subject_number_of_students = models.IntegerField(null=True)
    subject_groups = models.IntegerField(null=True)
    subject_teacher = models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject_id + ' - ' + self.subject_name

class Speciality(models.Model):

    speciality_id = models.CharField(max_length=2000, primary_key=True)
    speciality_name = models.CharField(max_length=2000, null=True)
    speciality_subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.speciality_id




