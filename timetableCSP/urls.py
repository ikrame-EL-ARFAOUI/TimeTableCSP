

from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home),
    path('teacher/list',views.teachersList),
    path('subject/list', views.subjectsList),
    path('room/list', views.roomsList),
    path('speciality/list', views.specialitysList),

    path('teacher/add', views.addTeacher),
    path('subject/add', views.addSubject),
    path('room/add', views.addRoom),
    path('speciality/add', views.addSpeciality),




]
