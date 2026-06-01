from django.db import models
from accounts.models import CustomUser

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username