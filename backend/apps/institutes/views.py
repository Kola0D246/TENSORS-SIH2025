from django.shortcuts import render

from rest_framework import viewsets
from .models import Institute, Department
from .serializers import InstituteSerializer, DepartmentSerializer

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
