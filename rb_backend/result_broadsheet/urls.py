#Imports
from django.http.response import HttpResponse
from django.urls import path
from . import views 


# Urls here
urlpatterns =[
    path('d/', views.CourseList.as_view(), name='List'),
    path('', views.index, name='Index'),   
    path('generate-broadsheet/', views.GenerateBroadsheet.as_view()),
    path('add-result/', views.AddStudentResult.as_view()),
    path('del-result/<int:pk>', views.AddStudentResult.as_view())
]