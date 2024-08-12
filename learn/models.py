from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER =((1,'ADMIN'),(2,'TEACHER'),(3,'STUDENT'))
    user_type=models.IntegerField(choices=USER,default=3)

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    teacher=models.ForeignKey(CustomUser,limit_choices_to={"user_type":2}, on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, limit_choices_to={'user_type': 3}, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')
        