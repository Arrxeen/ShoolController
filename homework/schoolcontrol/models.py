from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    subject = models.ForeignKey('Subject',on_delete=models.DO_NOTHING)


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