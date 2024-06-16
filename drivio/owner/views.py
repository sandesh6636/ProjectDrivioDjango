from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from driver.models import DriverProfile

# Create your views here.
def index(request):
    return render(request, 'home/main.html')

def show_car(request):
    car = Cars.objects.all()
    context = {
        'car':car
    }
    return render(request, 'home/main.html', context)

def post_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Car added succesfully')
            return redirect('/addCar')
        else:
            messages.add_message(request, messages.ERROR, 'Kindly verify all the filds')
            return render(request, 'home/addCar.html', {'form':form})
        
    context = {
        'form':CarForm
    }

    return render(request, 'home/addCar.html', context)

def update_car(request, car_id):
    instance = Cars.objects.get(id=car_id)
    if request.method =="POST":
        form = CarForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product updated successfully')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,"Please verify the forms")
            return render(request, 'home/addCar.html', {'form':form})
    
    return render(request, 'home/updateCar.html', {'form':CarForm(instance=instance)})


def delete_car(request, car_id):
      instance = Cars.objects.get(id=car_id)
      instance.delete()
      messages.add_message(request, messages.SUCCESS, "Product Deleted successfully")
      return redirect('/')


@login_required
def view_interested_drivers(request, car_id):
    car = Car.objects.get(id=car_id)
    if car.owner != request.user:
        return HttpResponseForbidden()
    interested_drivers = car.interested_drivers.all()
    return render(request, 'owner/interested_drivers.html', {'car': car, 'interested_drivers': interested_drivers})
