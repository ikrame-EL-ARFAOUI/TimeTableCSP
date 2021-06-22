from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib import messages
import subprocess

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *

from django.contrib.auth.decorators import login_required

from timetableCSP.models import TimeTable, Class as CL, Room as R , Subject as Sj, Speciality as Sp, Teacher as T

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'projet.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#algorithme
from  timetableCSP.algorithme.csp_init import *

from  timetableCSP.algorithme.data import *
from  timetableCSP.algorithme.info import init_data,ROOMS,INSTRUCTORS,SUBJECTS,SPECIALITIES
import prettytable
from timetableCSP.algorithme.csp import  *
from timetableCSP.algorithme.degree_heuristic import *
from timetableCSP.algorithme.lcv import *
from timetableCSP.algorithme.mrv import *
from timetableCSP.algorithme.forward_checking import *
from timetableCSP.algorithme.constraint_propagation import *

# Create your views here.

# home
def home(request):
    return render(request, 'home.html')


# lists
def teachersList(request):
    teachers = T.objects.all()
    context = {'teachers': teachers}
    return render(request, 'listTeacher.html', context)


def subjectsList(request):
    subjects = Sj.objects.all()
    context = {'subjects': subjects}
    return render(request, 'listSubject.html', context)


def specialitiesList(request):
    specialities = Sp.objects.all()
    context = {'specialities': specialities}
    return render(request, 'listSpeciality.html', context)


def roomsList(request):
    rooms = R.objects.all()
    context = {'rooms': rooms}
    return render(request, 'listRoom.html', context)


# add
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


# update
def updateSpeciality(request, pk):
    form = Sp.objects.get(speciality_id=pk)
    speciality = SpecialityForm(instance=form)
    context = {'speciality': speciality}
    if request.method == 'POST':
        speciality = SpecialityForm(request.POST, instance=form)
        if speciality.is_valid():
            speciality.save()
            return redirect('list-speciality')
    return render(request, 'AddSpeciality.html', context)


def updateRoom(request, pk):
    form = R.objects.get(room_id=pk)
    room = RoomForm(instance=form)
    context = {'room': room}
    if request.method == 'POST':
        room = RoomForm(request.POST, instance=form)
        if room.is_valid():
            room.save()
            return redirect('list-room')
    return render(request, 'AddRoom.html', context)


def updateTeacher(request, pk):
    form = T.objects.get(teacher_id=pk)
    teacher = TeacherForm(instance=form)
    context = {'teacher': teacher}
    if request.method == 'POST':
        teacher = TeacherForm(request.POST, instance=form)
        if teacher.is_valid():
            teacher.save()
            return redirect('list-teacher')
    return render(request, 'AddTeacher.html', context)


def updateSubject(request, pk):

    form = Sj.objects.get(subject_id=pk)
    subject = SubjectForm(instance=form)
    context = {'subject': subject}
    if request.method == 'POST':
        subject = SubjectForm(request.POST, instance=form)
        if subject.is_valid():
            subject.save()
            return redirect('list-subject')
    return render(request, 'AddSubject.html', context)


def registerPage():
    return None


class Logout:
    pass


def loginPage():
    return None



def deleteSubject(request, pk):
    delete_subject = Sj.objects.get(subject_id=pk)
    context = {'delete_subject': delete_subject}
    if request.method == 'POST':
        delete_subject.delete()
        return redirect('list-subject')

    return render(request, 'deleteSubject.html', context)


def deleteTeacher(request, pk):
    delete_teacher = T.objects.get(teacher_id=pk)
    context = {'delete_teacher': delete_teacher}
    if request.method == 'POST':
        delete_teacher.delete()
        return redirect('list-teacher')

    return render(request, 'deleteTeacher.html', context)


def deleteRoom(request, pk):
    delete_room = R.objects.get(room_id=pk)
    context = {'delete_room': delete_room}
    if request.method == 'POST':
        delete_room.delete()
        return redirect('list-room')

    return render(request, 'deleteRoom.html', context)

def deleteSpeciality(request, pk):
    delete_speciality = Sp.objects.get(speciality_id=pk)
    context = {'delete_speciality': delete_speciality}
    if request.method == 'POST':
        delete_speciality.delete()
        return redirect('list-speciality')

    return render(request, 'deleteSpeciality.html', context)


def TimeTableView(request, pk , teacher_id='', speciality_id = ''):


    teachers = T.objects.all()
    specialities = Sp.objects.all()
    
    MEETING_TIMES = ["08:30 - 09:50",
                     "10:00 - 11:20",
                     "11:40 - 13:00",
                     "13:30 - 14:50",
                     "15:00 - 16:20",
                     "16:30 - 17:50"]
    DAYS = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"]
    classes = []
    timetable = TimeTable.objects.get(timetable_id = pk)
    cls = timetable.class_set.all()
    for cl in cls :
        classes.append(cl)

    if teacher_id != '' :
        classes = []
        tchr = T.objects.get(teacher_id=teacher_id)
        cls = timetable.class_set.all()
        for cl in cls :
            if cl.teacher == tchr :
                classes.append(cl)


    if speciality_id != '' :
        classes = []
        spy = Sp.objects.get(speciality_id=speciality_id)
        cls = timetable.class_set.all()
        for cl in cls :
            if cl.speciality == spy :
                classes.append(cl)

    context={'classes': classes,
             'timetable' : timetable,
             'teachers' : teachers,
             'specialities':specialities,
             'timeSlots' : MEETING_TIMES,
             'DAYS' : DAYS}
    return render(request, 'timetable-view.html',context)

def GenerateTimeTable(request):
    
    
    print(SPECIALITIES)
    print(INSTRUCTORS)

    result_default = backtracking(init_assignment_default(my_csp), my_csp, default_heuristic)
    # print("Counter for default backtracking: " + str(get_counter_default()))

    result_lcv = backtracking_lcv(init_assignment_lcv(my_csp), my_csp, lcv_heuristic)
    print("Counter for backtracking with LCV: " + str(get_counter_lcv()))

    result_mrv = mrv_backtracking(init_assignment_mrv(my_csp), my_csp)
    print("Counter for backtracking with MRV: " + str(get_counter_mrv()))

    result_degree = degree_backtracking(init_assignment_degree(my_csp), my_csp)
    print("Counter for backtracking with Degree Heuristic: " + str(get_counter_degree()))

    result_forward_check = forward_checking(init_assignment_forw(my_csp), my_csp)
    print("Counter for backtracking with Forward Checking: " + str(get_counter_forw()))

    result_constraint_propagation = constraint_propagation(init_assignment_con(my_csp), my_csp)
    print("Counter for backtracking with Constraint Propagation: " + str(get_counter_con()))

    result = result_constraint_propagation

    # ========saving timetable and classes =========================

    TimeSlots = ["08:30 - 09:50",
                 "10:00 - 11:20",
                 "11:40 - 13:00",
                 "13:30 - 14:50",
                 "15:00 - 16:20",
                 "16:30 - 17:50"]

    timetable = TimeTable.objects.create()
    # self._speciality = speciality
    #         self._subject = subject
    #         self._teacher = self._subject._teacher
    #         self._number_of_students = self._subject._number_of_students
    #         self._room = room
    #         self._time = time
    #         self._day = day
    #         self._type_of_class = type_of_class

    for seance in result.keys():

        cl = CL()
        cl.room = R.objects.get(room_name=seance._room[0])
        cl.speciality = Sp.objects.get(speciality_name=seance._speciality._name)
        cl.subject = Sj.objects.get(subject_name=seance._subject._name)

        cl.teacher = T.objects.get(teacher_name=seance._teacher["name"])
        cl.number_of_students = seance._number_of_students
        cl.type_of_class = seance._type_of_class
        cl.map_key = result[seance]

        cl.timeSlot = TimeSlots[result[seance] % 6]
        cl.timetable = timetable
        if result[seance] < 6:
            cl.day = "Monday"
        elif result[seance] < 12 and result[seance] >= 6:
            cl.day = "Tuesday"
        elif result[seance] < 18 and result[seance] >= 12:
            cl.day = "Wednesday"
        elif result[seance] < 24 and result[seance] >= 18:
            cl.day = "Thursday"
        elif result[seance] >= 24:
            cl.day = "Friday"
        cl.save()

    # ==============================================================

    monday, tuesday, wednesday, thursday, friday = [], [], [], [], []
    days = [monday, tuesday, wednesday, thursday, friday]
    for i in result.keys():
        if result[i] < 6:
            monday.append((i, result[i]))
        elif result[i] < 12 and result[i] >= 6:
            tuesday.append((i, result[i] - 6))
        elif result[i] < 18 and result[i] >= 12:
            wednesday.append((i, result[i] - 12))
        elif result[i] < 24 and result[i] >= 18:
            thursday.append((i, result[i] - 18))
        elif result[i] >= 24:
            friday.append((i, result[i] - 24))

    def print_day(day, l):
        r = ""
        for d, n in day:
            if (l == n):
                r += str(d) + "\n"
        return r

    table = prettytable.PrettyTable(['Lesson Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    k = 0
    for i in range(len(MEETING_TIMES)):
        table.add_row([MEETING_TIMES[i], print_day(monday, k), print_day(tuesday, k), print_day(wednesday, k),
                       print_day(thursday, k), print_day(friday, k)])
        k += 1
    print(table)

    return redirect('timetable', pk=timetable.timetable_id)


def timetablesList(request):
    timetables = TimeTable.objects.all().order_by('-date_creation')
    context = {'timetables': timetables}
    return render(request, 'listTimetables.html', context)


def updateTimetable(request,pk):

    form = TimeTable.objects.get(timetable_id=pk)
    timetable = TimeTableForm(instance=form)
    context = {'timetable': timetable}
    if request.method == 'POST':
        timetable = TimeTableForm(request.POST, instance=form)
        if timetable.is_valid():
            timetable.save()
            return redirect('list-timetable')
    return render(request, 'UpdateTimetable.html', context)


def deleteTimetable(request,pk):
    delete_timetable = TimeTable.objects.get(timetable_id=pk)
    context = {'delete_timetable': delete_timetable}
    if request.method == 'POST':
        delete_timetable.delete()
        return redirect('list-timetable')

    return render(request, 'deleteTimetable.html', context)