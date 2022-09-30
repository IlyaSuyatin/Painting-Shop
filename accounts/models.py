from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

