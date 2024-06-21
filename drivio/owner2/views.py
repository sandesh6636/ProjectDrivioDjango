from django.shortcuts import render
from . models import Cars
from . forms import CarForm , UserRegistraitionForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def main2(request):
    return render(request, 'main2.html')

def car_list(request):
    car=Cars.objects.all()
    return render(request,"all_cars.html" ,{'car':car})
@login_required
def my_car(request):
    car=Cars.objects.all()
    return render(request,"my_cars.html" ,{'car':car})
@login_required
def car_add(request):
    if request.method == "POST":
      form=CarForm(request.POST, request.FILES)
      if form.is_valid():
          car=form.save(commit=False)
          car.user = request.user
          car.save()
          return redirect('car_list')
    else:
        form = CarForm()
    return render(request, "cars_form.html", {'form':form})

@login_required
def car_update(request, car_id):
    car = get_object_or_404(Cars,pk=car_id, user = request.user )
    if request.method== "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('car_list')  
    else:
        form = CarForm(instance=car)
    return render(request,'cars_form.html',{'form':form})

@login_required
def car_delete(request,car_id):
    car = get_object_or_404(Cars,pk = car_id, user = request.user)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars_delete.html',{'car':car})

def register(request):
        if request.method =='POST':
            form =UserRegistraitionForm(request.POST)
            if form.is_valid():
                user =form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request,user)
                return redirect('car_list')
        else:
            form = UserRegistraitionForm()
        return render(request, 'registration/register.html',{'form':form})

    