from django.db import models
from accounts.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username