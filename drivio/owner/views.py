from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required


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
            cars=form.save(commit=False)
            cars.user = request.user
            cars.save()
            messages.add_message(request, messages.SUCCESS, 'Car added succesfully')
            return redirect('/main')
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
            instance=form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Product updated successfully')
            return redirect('/main')
        else:
            messages.add_message(request, messages.ERROR,"Please verify the forms")
            return render(request, 'home/addCar.html', {'form':form})
    
    return render(request, 'home/updateCar.html', {'form':CarForm(instance=instance)})


def delete_car(request, car_id):
      instance = Cars.objects.get(id=car_id)
      instance.delete()
      messages.add_message(request, messages.SUCCESS, "Product Deleted successfully")
      return redirect('/addCar')

