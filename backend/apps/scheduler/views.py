from rest_framework import viewsets
from .models import TimeSlot, Occupancy
from .serializers import TimeSlotSerializer, OccupancySerializer

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

class OccupancyViewSet(viewsets.ModelViewSet):
    queryset = Occupancy.objects.all()
    serializer_class = OccupancySerializer

