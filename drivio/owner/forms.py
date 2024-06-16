from django.forms import ModelForm
from . models import *

class CarForm(ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'