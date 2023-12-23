from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer
from rest_framework import status
from django.forms.models import model_to_dict

# Create your views here.
# Teachers
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Course
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request):

        t = Teacher.objects.get(pk=request.data['teacher'])

        new_course = Course.objects.create(
            name=request.data['name'],
            teacher=t
        )

        data = model_to_dict(new_course)
        data['teacher'] = model_to_dict(t)

        return Response(data, status=status.HTTP_201_CREATED)
        

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Student
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer