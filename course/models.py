from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    trainer_name = models.CharField(max_length=20)
    description = models.TextField()
    level = models.CharField(max_length=20)
    duration = models.PositiveBigIntegerField()
    objective = models.TextField()
    module = models.PositiveSmallIntegerField()
    learning_materials = models.TextField()
    class_hours = models.DurationField()
    attendance_per_week = models.PositiveSmallIntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course_name} {self.duration}"