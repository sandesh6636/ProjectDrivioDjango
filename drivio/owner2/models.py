from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cars(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=200)
    owner_contact = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    payment_price = models.FloatField()
    description = models.TextField()
    img = models.FileField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return f'{self.user.username} - {self.car_name}'


