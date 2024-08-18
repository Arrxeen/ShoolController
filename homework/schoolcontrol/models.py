from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    subject = models.ForeignKey('Subject',on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Class(models.Model):
    number = models.CharField(max_length=100)
    letter = models.CharField(max_length=100)

    def __str__(self):
        a = self.number +'-'+ self.letter
        return a

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    id_class = models.ForeignKey('Class',on_delete=models.DO_NOTHING)
    

class Schedule(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey('Class', on_delete=models.DO_NOTHING)
    date_time = models.DateTimeField()


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)