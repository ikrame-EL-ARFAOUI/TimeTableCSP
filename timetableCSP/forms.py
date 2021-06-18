from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import *
from django import forms


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_number_of_students', 'subject_groups', 'teacher']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'room_max_students']


class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['speciality_name', 'subjects']





