from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher,Subject,Speciality,Room
from .forms import *
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

#home
def home(request):
    return render(request,'home.html')

#lists
def teachersList(request):
    teachers = Teacher.objects.all()
    context={'teachers': teachers}
    return render(request,'listTeacher.html',context)
def subjectsList(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'listSubject.html', context)
def specialitiesList(request):
    specialities = Speciality.objects.all()
    context = {'specialities': specialities}
    return render(request, 'listSpeciality.html', context)
def roomsList(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'listRoom.html', context)

#add
def addTeacher(request):
    teacher = TeacherForm()
    context = {'teacher': teacher}

    if request.method == 'POST':
        teacher = TeacherForm(request.POST)
        if teacher.is_valid():
            messages.success(request, 'Teacher has been added successfully.')
            teacher.save()
        else:
            messages.success(request, 'Teacher already exists or you have added wrong attributes.')

    return render(request, 'AddTeacher.html', context)


def addSubject(request):
    subject = SubjectForm()
    context = {'subject': subject}

    if request.method == 'POST':
        subject = SubjectForm(request.POST)
        if subject.is_valid():
            messages.success(request, 'Subject has been added successfully.')
            subject.save()
        else:
            messages.success(request, 'Subject already exists or you have added wrong attributes.')

    return render(request, 'AddSubject.html', context)



def addSpeciality(request):

    speciality = SpecialityForm()
    context = {'speciality': speciality}

    if request.method == 'POST':
        speciality = SpecialityForm(request.POST)
        if speciality.is_valid():
            messages.success(request, 'Speciality has been added successfully.')
            speciality.save()
        else:
            messages.success(request, 'Speciality already exists or you have added wrong attributes.')

    return render(request, 'AddSpeciality.html', context)


def addRoom(request):
    room = RoomForm()
    context = {'room': room}

    if request.method == 'POST':
        room = RoomForm(request.POST)
        if room.is_valid():
            messages.success(request, 'Room has been added successfully.')
            room.save()
        else:
            messages.success(request, 'Room already exists or you have added wrong attributes.')

    return render(request, 'AddRoom.html', context)

def updateSpeciality():
    return None


def updateRoom():
    return None


def updateTeacher():
    return None


def updateSubject():
    return None


def registerPage():
    return None


class Logout:
    pass


def loginPage():
    return None


class GenerateTimeTable:
    pass


class TimeTableView:
    pass


def deleteSubject():
    return None


def deleteTeacher():
    return None


def deleteRoom():
    return None


def deleteSpeciality():
    return None