from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

import openpyxl
from .models import Student

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import StudentSerializer

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my API Backend")


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






@api_view()
def query_db_filters(request):
    # all_students = Student.objects.all()

    # all_students = Student.objects.all()

    paginator = PageNumberPagination()
    query_set = Student.objects.all()
    all_students = paginator.paginate_queryset(query_set, request)

    student_data = [{
            'full_name' : f"{student.first_name} {student.last_name}",
            'age' : student.age,
            'gender' : student.gender,
            'gpa' : student.gpa,
            'email' : student.email
        } for student in all_students]
    
    '''
    exact - Exact Match
    iexact - Case insensitive exact match
    contains - Case - sensitive containment test
    icontains - 
    gt, lt, gte, lte
    in
    startswith, endswith
    istartwith, iendswith
    '''
    
    return Response(student_data)

# json response example
@api_view(['GET'])
def json_response_view(request):

    # data = {
    #     'message' : 'hello, this is a JSON Response',
    #     'status' : 'success',
    #     'data' : {
    #         'name' : 'Alex',
    #         'major' : 'Physics',
    #         'age' : 167
    #     }
    # }

    single_student = Student.objects.all().order_by("?").first()
    

    # if single_student:
    #     data['id'] = single_student.id
    #     data['first_name'] = single_student.first_name
    #     data['last_name'] = single_student.last_name
    #     data['age'] = single_student.age
    #     data['major'] = single_student.major

    data = model_to_dict(single_student, 
                         fields=['id', 'first_name','last_name'])

    return Response(data)

class CBV_Example(APIView):
    def get(self, request):
        data = {
            'message' : 'This is a CBV Get response'
        }
        return Response(data)
    
    def post(self, request):
        data = {
            'message' : 'This is a CBV Post response'
        }
        return Response(data)
    
    def put(self, request):
        data = {
            'message' : 'This is a CBV Put response'
        }
        return Response(data)


# Import Data
def import_students_from_excel(request):

    file_path = "/home/halogen/Documents/demo_django/api_env/myProject/static/students_data.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Get the fields of the Student model
    model_fields = [field.name for field in Student._meta.get_fields() if field.name != "id"]

    # Iterate over rows and create Student objects
    for row in sheet.iter_rows(min_row=2, values_only=True):
        student_data = dict(zip(model_fields, row))
        # print(student_data)
        Student.objects.create(**student_data)

    return HttpResponse("Import completed")