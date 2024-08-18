from django.shortcuts import render
from django.views.generic import ListView
from schoolcontrol import models
from django.http import HttpResponse

class StudentsListView(ListView):
    model = models.Student
    context_object_name = 'students'


def teacher_list(request):
    teachers = models.Teacher.objects.all()
    context = {
        "teachers":teachers
    }
    return render(request,'schoolcontrol/teacher_list.html', context)

def student_details(request, pk):
    try:
        student = models.Student.objects.get(id=pk)
        context = {
        "student":student
    }
        return render(request,'schoolcontrol/student_details.html', context)

    except models.Student.DoesNotExist: 
        return HttpResponse('no student', status=404)