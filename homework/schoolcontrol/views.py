from django.shortcuts import render
from django.views.generic import ListView
from schoolcontrol import models

class StudentsListView(ListView):
    model = models.Student
    context_object_name = 'students'


def teacher_list(request):
    teachers = models.Teacher.objects.all()
    context = {
        "teachers":teachers
    }
    return render(request,'schoolcontrol/teacher_list.html', context)
