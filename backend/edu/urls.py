from django.urls import path
from .views import TeacherDetail, TeacherList, CourseDetail, CourseList, StudentDetail, StudentList

urlpatterns = [
    # Teacher Links
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-list'),

    # Course Links
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-list'),

    # Course Links
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-list'),

]