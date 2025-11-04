from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from apps.api.permissions import RoleBasedAccessPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [RoleBasedAccessPermission]
