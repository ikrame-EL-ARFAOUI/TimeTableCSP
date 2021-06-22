from django.db import models

# Create your models here.

from multiselectfield import MultiSelectField



    
class FreeTime(models.Model):
   
    DOMAINS = (
        ("Monday,08:30 - 09:50","Monday,08:30 - 09:50"),
        ("Monday,10:00 - 11:20","Monday,10:00 - 11:20"),
        ("Monday,11:40 - 13:00","Monday,11:40 - 13:00"),
        ("Monday,13:30 - 14:50","Monday,13:30 - 14:50"),
        ("Monday,15:00 - 16:20","Monday,15:00 - 16:20"),
        ("Monday,16:30 - 17:50","Monday,16:30 - 17:50"),

        ("Tuesday,08:30 - 09:50", "Tuesday,08:30 - 09:50"),
        ("Tuesday,10:00 - 11:20", "Tuesday,10:00 - 11:20"),
        ("Tuesday,11:40 - 13:00", "Tuesday,11:40 - 13:00"),
        ("Tuesday,13:30 - 14:50", "Tuesday,13:30 - 14:50"),
        ("Tuesday,15:00 - 16:20", "Tuesday,15:00 - 16:20"),
        ("Tuesday,16:30 - 17:50", "Tuesday,16:30 - 17:50"),

        ("Wednesday,08:30 - 09:50", "Wednesday,08:30 - 09:50"),
        ("Wednesday,10:00 - 11:20", "Wednesday,10:00 - 11:20"),
        ("Wednesday,11:40 - 13:00", "Wednesday,11:40 - 13:00"),
        ("Wednesday,13:30 - 14:50", "Wednesday,13:30 - 14:50"),
        ("Wednesday,15:00 - 16:20", "Wednesday,15:00 - 16:20"),
        ("Wednesday,16:30 - 17:50", "Wednesday,16:30 - 17:50"),

        ("Thursday,08:30 - 09:50", "Thursday,08:30 - 09:50"),
        ("Thursday,10:00 - 11:20", "Thursday,10:00 - 11:20"),
        ("Thursday,11:40 - 13:00", "Thursday,11:40 - 13:00"),
        ("Thursday,13:30 - 14:50", "Thursday,13:30 - 14:50"),
        ("Thursday,15:00 - 16:20", "Thursday,15:00 - 16:20"),
        ("Thursday,16:30 - 17:50", "Thursday,16:30 - 17:50"),

        ("Friday,08:30 - 09:50", "Friday,08:30 - 09:50"),
        ("Friday,10:00 - 11:20", "Friday,10:00 - 11:20"),
        ("Friday,11:40 - 13:00", "Friday,11:40 - 13:00"),
        ("Friday,13:30 - 14:50", "Friday,13:30 - 14:50"),
        ("Friday,15:00 - 16:20", "Friday,15:00 - 16:20"),
        ("Friday,16:30 - 17:50", "Friday,16:30 - 17:50"),
        
    )
    
    freetime_id = models.AutoField(primary_key=True)
    freetime_key = models.IntegerField(null=True)
    domaine = models.CharField(max_length=2000, null=True, choices=DOMAINS)
    def __str__(self):
        return str(self.freetime_key) + "," + self.domaine
    
    
class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=2000, null=True)
    room_max_students = models.IntegerField(null=True)

    def __str__(self):
        return self.room_name


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=2000, null=True)
    freetimes = models.ManyToManyField(FreeTime, null=True)

    def __str__(self):
        return self.teacher_name


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=1000, null=True)
    subject_number_of_students = models.IntegerField(null=True)
    subject_groups = models.IntegerField(null=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.subject_name


class Speciality(models.Model):
    speciality_id = models.AutoField(primary_key=True)
    speciality_name = models.CharField(max_length=2000, null=True)
    subjects = models.ManyToManyField(Subject, null=True)

    def __str__(self):
        return self.speciality_name


# class TimeSlot(models.Model):
#     timeSlot_id = models.AutoField(primary_key=True)
#     timeSlot_name = models.CharField(max_length=2000, null=True)
#     def __str__(self):
#         return self.timeSlot_name
#
# class Day(models.Model):
#     day_id = models.AutoField(primary_key=True)
#     day_name = models.CharField(max_length=2000, null=True)
#     def __str__(self):
#         return self.day_name

class TimeTable(models.Model):
    timetable_id = models.AutoField(primary_key=True)
    timetable_name = models.CharField(max_length=2000, null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)

    # user = models.ForeignKey(User)

    def __str__(self):
        return self.timetable_id


class Class(models.Model):
    # CLASS_TYPE = (
    #     ('lecture', 'lecture'),
    #     ('practice', 'practice')
    # )

    TimeSlots = (("08:30 - 09:50", "08:30 - 09:50"),
                 ("10:00 - 11:20", "10:00 - 11:20"),
                 ("11:40 - 13:00", "11:40 - 13:00"),
                 ("13:30 - 14:50", "13:30 - 14:50"),
                 ("15:00 - 16:20", "15:00 - 16:20"),
                 ("16:30 - 17:50", "16:30 - 17:50"))

    DAYS = (("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"))

    speciality = models.ForeignKey(Speciality, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    number_of_students = models.IntegerField(null=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    timeSlot = models.CharField(max_length=2000, null=True, choices=TimeSlots)
    day = models.CharField(max_length=2000, null=True, choices=DAYS)
    type_of_class = models.CharField(max_length=2000, null=True)
    timetable = models.ForeignKey(TimeTable, null=True, on_delete=models.SET_NULL)
    map_key =models.IntegerField(null = True)

    def __str__(self):
        return str(self.speciality) + "," + str(self.subject) + "\n" + str(self.teacher) + "," \
               + str(self.type_of_class) + "," + str(self.room) + " \n"
