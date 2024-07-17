from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    student_bio = models.TextField()
    student_profile = models.ImageField()
    number_of_courses = models.PositiveSmallIntegerField()
    student_class = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=50)
    place_of_residence = models.CharField(max_length=100)
    national_id = models.PositiveSmallIntegerField()
    phone_number = models.PositiveIntegerField()
    kcse_grade = models.CharField(max_length=10)
    medical_condition = models.TextField()
    room_number = models.PositiveSmallIntegerField()

