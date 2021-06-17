

from django.urls import path,include
from . import views

urlpatterns = [

    path('teacher/list',views.teachersList, name='list-teacher'),
    path('subject/list', views.subjectsList, name='list-subject'),
    path('room/list', views.roomsList, name='list-room'),
    path('speciality/list', views.specialitiesList, name='list-speciality'),


    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('subject/add', views.addSubject, name='add-subject'),
    path('teacher/add', views.addTeacher, name='add-teacher'),
    path('room/add', views.addRoom, name='add-room'),
    path('speciality/add', views.addSpeciality, name='add-speciality'),

    path('subject/update/<str:pk>/', views.updateSubject, name='update-subject'),
    path('teacher/update/<str:pk>/', views.updateTeacher, name='update-teacher'),
    path('room/update/<str:pk>/', views.updateRoom, name='update-room'),
    path('speciality/update/<str:pk>/', views.updateSpeciality, name='update-speciality'),

    path('subject/delete/<str:pk>/', views.deleteSubject, name='delete-subject'),
    path('teacher/delete/<str:pk>/', views.deleteTeacher, name='delete-teacher'),
    path('room/delete/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('speciality/delete/<str:pk>/', views.deleteSpeciality, name='delete-speciality'),

    #path('timetable/', views.TimeTable, name='timetable'),
    path('generate-timetable/<str:id>/', views.GenerateTimeTable, name='generate-timetable'),
    #path('addweek-info/', views.WeekDayFormView, name='weekday-info'),
    path('timetable/<str:id>/', views.TimeTableView, name='timetable')




]
