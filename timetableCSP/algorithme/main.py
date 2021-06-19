from csp_init import *
import prettytable
from csp import *
from degree_heuristic import *
from lcv import *
from mrv import *
from forward_checking import *
from constraint_propagation import *

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'projet.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from timetableCSP.models import TimeTable,Class as CL,Room, Subject,Speciality,Teacher







result_default = backtracking(init_assignment_default(my_csp), my_csp, default_heuristic)
#print("Counter for default backtracking: " + str(get_counter_default()))

result_lcv = backtracking_lcv(init_assignment_lcv(my_csp), my_csp, lcv_heuristic)
print("Counter for backtracking with LCV: " + str(get_counter_lcv()))


result_mrv = mrv_backtracking(init_assignment_mrv(my_csp),my_csp)
print("Counter for backtracking with MRV: " + str(get_counter_mrv()))



result_degree = degree_backtracking(init_assignment_degree(my_csp), my_csp)
print("Counter for backtracking with Degree Heuristic: " + str(get_counter_degree()))


result_forward_check = forward_checking(init_assignment_forw(my_csp), my_csp)
print("Counter for backtracking with Forward Checking: " + str(get_counter_forw()))


result_constraint_propagation = constraint_propagation(init_assignment_con(my_csp), my_csp)
print("Counter for backtracking with Constraint Propagation: " + str(get_counter_con()))


result = result_constraint_propagation

#========saving timetable and classes =========================

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
    cl.room = Room.objects.get(room_name = seance._room[0])
    cl.speciality = Speciality.objects.get(speciality_name = seance._speciality._name)
    cl.subject = Subject.objects.get(subject_name = seance._subject._name)
    cl.teacher = Teacher.objects.get(teacher_name= seance._teacher )
    cl.number_of_students = seance._number_of_students
    cl.type_of_class = seance._type_of_class
    cl.map_key = result[seance]


    cl.timeSlot = TimeSlots[result[seance] % 6]
    cl.timetable = timetable
    if result[seance] < 6:
        cl.day = "Monday"
    elif result[seance] < 12 and result[seance]>=6:
        cl.day = "Tuesday"
    elif result[seance] < 18 and result[seance]>=12:
        cl.day = "Wednesday"
    elif result[seance] < 24 and result[seance]>=18:
        cl.day = "Thursday"
    elif result[seance] >= 24:
        cl.day = "Friday"
    cl.save()



#==============================================================

monday, tuesday, wednesday, thursday, friday = [], [], [], [], []
days = [monday, tuesday, wednesday, thursday, friday]
for i in result.keys():
    if result[i] < 6:
        monday.append((i,result[i]))
    elif result[i] < 12 and result[i]>=6:
        tuesday.append((i,result[i]-6))
    elif result[i] < 18 and result[i]>=12:
        wednesday.append((i,result[i] - 12))
    elif result[i] < 24 and result[i]>=18:
        thursday.append((i, result[i] - 18))
    elif result[i] >= 24:
        friday.append((i, result[i] - 24))


def print_day(day,l):
	r = ""
	for d,n in day:
		if (l == n):
			r += str(d) + "\n" 
	return r


table = prettytable.PrettyTable(['Lesson Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
k = 0
for i in range(len(MEETING_TIMES)):
    table.add_row([MEETING_TIMES[i], print_day(monday,k), print_day(tuesday,k), print_day(wednesday,k), print_day(thursday,k), print_day(friday,k)])
    k+=1
print(table)
	



