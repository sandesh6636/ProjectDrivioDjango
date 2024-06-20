from django.forms import ModelForm
from .models import Cars
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  


class CarForm(ModelForm):
    class Meta:
        model=Cars
        fields = '__all__'

class UserRegistraitionForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')