from django.contrib import admin
from schoolcontrol.models import Teacher, Student, Class, Subject, Schedule, Grade

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Grade)