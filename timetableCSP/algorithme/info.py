#import export as export
#export DJANGO_SETTINGS_MODULE=projet.settings

# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'projet.settings'
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'projet.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from timetableCSP.models import Teacher,Subject,Speciality,Room

# ROOMS = [["101",20],
# 		 ["105",35],
# 		 ["121",30],
# 		 ["124",60],
# 		 ["202",55],
# 		 ["210",15],
# 		 ["303",60],
# 		 ["308",70],
# 		 ["317",35],
# 		 ["340",60],
# 		 ["402",60],
# 		 ["134",10],
# 		 ["125",10],
# 		 ["128",10],
# 		 ["130",10]]
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
ROOMS =[]
INSTRUCTORS = []
SUBJECTS = []
SPECIALITIES = []
def init_data():
	print("hi")
	rooms = Room.objects.all()
	for room in rooms:
		l = [room.room_name,room.room_max_students]
		ROOMS.append(l)
	
	# INSTRUCTORS = [	{"name":"James Web", "subject": "Algorithms"},
	# 				{"name":"Mike Brown", "subject": "Algebra"},
	# 				{"name":"Steve Day", "subject": "AI"},
	# 				{"name":"Jane Doe", "subject": "NIT"},
	# 				{"name":"Lily Johns", "subject": "C++"},
	# 				{"name":"George Miller", "subject": "Mopi"},
	# 				{"name":"Andrew Lively", "subject": "Mmoz"},
	# 				{"name":"Jannifer Dickens", "subject": "Android"},
	# 				{"name":"Hatim Guermah", "subject": "java"},
	# 				{"name": "bouchra asri", "subject": "oracle"},
	# 				{"name":"Mounia Abik", "subject": "IOS"}]
	
	
	teachers = Teacher.objects.all()
	for teacher in teachers:
		
		ftimes = teacher.freetimes.all()	
		timesList =[]
		for t in ftimes:
			timesList.append(t.freetime_key)
	
		for subject in teacher.subject_set.all():
			dict = {"name": teacher.teacher_name, "subject": subject.subject_name,"freeTime" : timesList }
			print(dict)
			INSTRUCTORS.append(dict)
		
		
		# SUBJECTS = [ {"name":"Algorithms", "number_of_students": 60, "groups": 3, "teacher":"James Web"},
		# 			 {"name":"Algebra", "number_of_students": 50,"groups": 2,"teacher":"Mike Brown"},
		# 			 {"name":"AI", "number_of_students": 40, "groups": 4,"teacher":"Steve Day"},
		# 			 {"name":"NIT", "number_of_students": 60, "groups": 3,"teacher":"Jane Doe"},
		# 			 {"name":"C++", "number_of_students": 40, "groups": 4,"teacher":"Lily Johns"},
		# 			 {"name":"Mopi", "number_of_students": 50, "groups": 5,"teacher":"George Miller"},
		# 			 {"name":"Mmoz", "number_of_students": 45, "groups": 3,"teacher":"Andrew Lively"},
		# 			 {"name":"Android", "number_of_students": 60, "groups": 3,"teacher":"Jannifer Dickens"},
		# 			 {"name":"java", "number_of_students": 60, "groups": 3,"teacher":"Hatim Guermah"},
		# 			 {"name":"oracle", "number_of_students": 60, "groups": 3,"teacher":"bouchra asri"},
		# 			 {"name":"IOS", "number_of_students": 30, "groups": 3,"teacher":"Mounia Abik"}
		# 			 ]
	
	
	
	subjects = Subject.objects.all()
	for subject in subjects:
		dict = {"name":subject.subject_name, "number_of_students": subject.subject_number_of_students, "groups": subject.subject_groups,"teacher":subject.teacher.teacher_name}
		SUBJECTS.append(dict)
	
	
	
	# SPECIALITIES = [{"name":"KN", "subjects": ["Algorithms", "Algebra", "Mmoz", "Mopi", "Android"]},
	# 				{"name":"IPZ", "subjects":["Algorithms", "AI", "NIT", "IOS", "C++","java"]},
	# 				{"name":"PRYMAT", "subjects":["Algebra", "NIT", "C++", "IOS", "oracle"]}]
	
	
	
	specialities = Speciality.objects.all()
	for speciality in specialities:
		subj = speciality.subjects.all()
		subjList = []
		for sub in subj :
			subjList.append(sub.subject_name)
	
		dict = {"name":speciality.speciality_name, "subjects": subjList}
		SPECIALITIES.append(dict)
	
	return True
