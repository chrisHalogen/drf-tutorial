from django.urls import path
from .views import index, import_students_from_excel, json_response_view, CBV_Example, query_db_filters, StudentList, StudentCreate, StudentRetrieve

urlpatterns = [
    path('', index, name="Index"),
    # path('import-data/', import_students_from_excel, name="Import Data"),
    path('return-json-response/', json_response_view, name="Json Response"),
    path('cbv-example/', CBV_Example.as_view(), name="CBV Example"),
    path('query-filters/', query_db_filters, name="query_db_filters"),
    path('student-list/', StudentList.as_view(),name='student-list'),
    path('student-create/', StudentCreate.as_view(),name='student-create'),
    path('student-retrieve/<int:pk>/', StudentRetrieve.as_view(),name='student-retrieve')

]
