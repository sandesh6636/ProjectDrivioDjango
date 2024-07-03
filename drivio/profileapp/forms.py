from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from django.forms.models import ModelForm
from django import forms

from django.forms.widgets import FileInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
          'license_photo': FileInput(),
         }
        



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
