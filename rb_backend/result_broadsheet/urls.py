#Imports
from django.http.response import HttpResponse
from django.urls import path
from . import views


# Urls here
urlpatterns =[
    path('courses/', views.CourseData.as_view(), name='Courses'),
    path('dept/', views.DepartmentData.as_view(), name='Departments'),
    # path('generate-broadsheet/', views.GenerateBroadsheet.as_view()),
    # path('add-result/', views.AddStudentResult.as_view()),
    # path('del-result/<int:pk>', views.AddStudentResult.as_view())
]