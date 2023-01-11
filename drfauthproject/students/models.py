from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    stdNum = models.IntegerField("Student Number")
    course = models.CharField("Course", max_length=20)
    img = models.ImageField("Picture", default='A picture of the student')

    def __str__(self):
        return self.first_name
