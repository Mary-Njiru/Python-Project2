from django.db import models

class Teacher(models.Model):
    first_name  = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length = 20)
    email = models.EmailField()
    teacher_id = models.PositiveSmallIntegerField()
    nationality= models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    specialization = models.CharField(max_length = 20)
    years_of_experience = models.PositiveSmallIntegerField()



    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.specialization}"