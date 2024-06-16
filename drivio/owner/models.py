

# Create your models here.
from django.db import models
from driver.models import DriverProfile 
# Create your models here.
class Cars(models.Model):
    owner_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    payment_price = models.FloatField()
    description = models.TextField()
    img = models.FileField(upload_to='static/uploads')
    interested_drivers = models.ManyToManyField(DriverProfile, related_name='interested_cars', blank=True)

    def __str__(self):
        return str(self.owner_name)
