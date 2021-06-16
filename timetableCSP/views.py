from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')
def teachersList(request):
    return HttpResponse('teachers list')
def subjectsList(request):
    return HttpResponse('subjects list')
def specialitysList(request):
    return HttpResponse('specialities list')
def roomsList(request):
    return HttpResponse('rooms list')


def addTeacher(request):
    return HttpResponse('teacher form')
def addSubject(request):
    return HttpResponse('subject form')
def addSpeciality(request):
    return HttpResponse('speciality form')
def addRoom(request):
    return HttpResponse('room form')


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