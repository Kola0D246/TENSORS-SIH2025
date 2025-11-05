from rest_framework import viewsets
from .models import Institute, Department, Course, Subject, Faculty, Student
from .serializers import InstituteSerializer, DepartmentSerializer, CourseSerializer, SubjectSerializer, FacultySerializer, StudentSerializer
from apps.api.permissions import RoleBasedAccessPermission

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [RoleBasedAccessPermission]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [RoleBasedAccessPermission]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [RoleBasedAccessPermission]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [RoleBasedAccessPermission]

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [RoleBasedAccessPermission]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [RoleBasedAccessPermission]
