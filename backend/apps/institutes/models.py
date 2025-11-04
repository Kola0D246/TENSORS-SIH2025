from django.db import models

class Institute(models.Model):
    name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    official_communication = models.CharField(max_length=255)
    email_domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.department_name} ({self.institute.name})"

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_type = models.CharField(max_length=50, choices=[('major', 'Major'), ('minor', 'Minor'), ('elective', 'Elective')])
    enrolled_students = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    total_theory_hours = models.IntegerField()
    total_practical_hour = models.IntegerField()

    def __str__(self):
        return self.subject_name

class Faculty(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=255)
    primary_subjects = models.ManyToManyField(Subject, related_name='primary_faculties')
    secondary_subjects = models.ManyToManyField(Subject, related_name='secondary_faculties', blank=True)

    def __str__(self):
        return self.faculty_name

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=100, unique=True)
    majors = models.ManyToManyField(Course, related_name='major_students', blank=True)
    minors = models.ManyToManyField(Course, related_name='minor_students', blank=True)
    electives = models.ManyToManyField(Course, related_name='elective_students', blank=True)

    def __str__(self):
        return self.enrollment_no
