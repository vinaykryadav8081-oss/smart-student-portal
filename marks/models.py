from django.db import models
from students.models import Student
from teachers.models import Teacher


class Marks(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    subject = models.CharField(max_length=100)

    marks = models.IntegerField()
    
def __str__(self):
        return f"{self.student.user.username} - {self.subject}"
   