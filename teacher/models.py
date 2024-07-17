from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    teacher_id = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    specialization = models.CharField(max_length=20)
    years_of_experience = models.PositiveSmallIntegerField()
    classes_per_week = models.PositiveSmallIntegerField()
    teacher_bio = models.TextField()
    phone_number = models.PositiveIntegerField()
    bank_account_number = models.TextField()
    profile = models.ImageField()



    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.specialization}"
    
    