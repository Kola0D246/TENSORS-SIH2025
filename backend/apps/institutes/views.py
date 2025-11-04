from rest_framework import viewsets
from .models import Institute, Department
from .serializers import InstituteSerializer, DepartmentSerializer
from apps.api.permissions import RoleBasedAccessPermission

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [RoleBasedAccessPermission]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [RoleBasedAccessPermission]
