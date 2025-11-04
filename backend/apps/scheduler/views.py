from rest_framework import viewsets
from .models import TimeSlot, Occupancy
from .serializers import TimeSlotSerializer, OccupancySerializer
from apps.api.permissions import RoleBasedAccessPermission

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [RoleBasedAccessPermission]

class OccupancyViewSet(viewsets.ModelViewSet):
    queryset = Occupancy.objects.all()
    serializer_class = OccupancySerializer
    permission_classes = [RoleBasedAccessPermission]
