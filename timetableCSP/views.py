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
    return render(request,'AddTeacher.html')
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
    return render(request,'AddSpeciality.html')
def addRoom(request):
    return render(request,'AddRoom.html')


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