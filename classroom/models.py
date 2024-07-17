from django.db import models


class ClassRoom(models.Model):
    class_name = models.CharField(max_length=20)
    courses = models.TextField()
    class_representative = models.TextField(default = 'Default class mission')
    class_size = models.TextField()
    class_capacity = models.TextField(default = 100)
    room_number = models.CharField(max_length=20)
    class_vision = models.TextField()
    class_mission = models.TextField(default = 'Default class mission')
    class_enrollment = models.PositiveIntegerField(default = 200)
    number_of_tables = models.PositiveIntegerField()
    number_of_laptops = models.PositiveIntegerField()
    number_of_windows = models.PositiveSmallIntegerField()
    number_of_television = models.PositiveSmallIntegerField()





    def __str__(self):
        return f"{self.name} {self.capacity}"