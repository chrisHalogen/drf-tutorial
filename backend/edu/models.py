from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.id}" 
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='courses')

    def __str__(self):
        return self.name