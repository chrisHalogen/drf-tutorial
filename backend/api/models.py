from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, 
                              choices=[("M", "Male"), ("F","Female")])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    major = models.CharField(max_length=45)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.BooleanField(default=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
