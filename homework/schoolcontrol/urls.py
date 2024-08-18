from django.urls import path
from schoolcontrol import views

urlpatterns = [
    path('students/', views.StudentsListView.as_view(), name='student-list'),
    path('teachers/', views.teacher_list, name='teacher-list')
]
