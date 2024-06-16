from django.contrib.auth.models import User
from django.db import models

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    driving_license_front = models.ImageField(upload_to='license_pictures/')
    driving_license_back = models.ImageField(upload_to='license_pictures/')

    def __str__(self):
        return self.user.username
