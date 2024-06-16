from django import forms
from django.contrib.auth.models import User
from .models import DriverProfile

class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['name', 'age', 'contact', 'location', 'profile_picture', 'driving_license_front', 'driving_license_back']
