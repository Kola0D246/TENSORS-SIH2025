from rest_framework import serializers
from .models import TimeSlot, Occupancy

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class OccupancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupancy
        fields = '__all__'
