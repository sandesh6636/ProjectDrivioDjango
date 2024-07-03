from django.db import models
from django.contrib.auth.models import User
from owner2.models import Cars  # Import the Car model from owner2 app

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img =  models.ImageField(default = 'media/default.jpg', upload_to = 'media', null = True, blank = True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    Experinces = models.CharField(max_length=20, null=True)  # Experiences field
    license_photo = models.ImageField(upload_to='licenses/%Y/%m/%d', default='media/default_license.jpg', null=True, blank=True)
    desc = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class InterestedCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    interested_at = models.DateTimeField(auto_now_add=True)