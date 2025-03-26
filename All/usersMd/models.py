from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100 , unique=True)
    isManager = models.BooleanField(default=False)
    username = models.CharField(max_length=50 , unique=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'password']

class Companies(models.Model):
    name = models.CharField(max_length=30)


class Work(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='works')
    about = models.CharField(max_length=255)
    work_hour = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.user.id} - {self.company} - {self.date}'
    
