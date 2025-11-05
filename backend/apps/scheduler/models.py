from django.db import models
from apps.institutes.models import Department, Faculty, Subject, Student

class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    period_num = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} P{self.period_num}"

class Infra(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.CharField(max_length=20, choices=[('class', 'Classroom'), ('lab', 'Lab')])
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.room_type.title()} ({self.department})"

class FacultyUnavailability(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.faculty} unavailable at {self.timeslot} ({self.status})"

class Occupancy(models.Model):
    room = models.ForeignKey(Infra, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked'), ('blocked', 'Blocked')])

    class Meta:
        unique_together = ('room', 'timeslot')
