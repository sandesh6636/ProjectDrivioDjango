from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import DriverRegistrationForm, DriverProfileForm
from .models import DriverProfile
from owner.models import Cars # Assuming the Car model is in the 'owner' app

def register_driver(request):
    if request.method == 'POST':
        user_form = DriverRegistrationForm(request.POST)
        profile_form = DriverProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('driver_profile')
    else:
        user_form = DriverRegistrationForm()
        profile_form = DriverProfileForm()
    return render(request, 'driver/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def driver_profile(request):
    profile = DriverProfile.objects.get(user=request.user)
    return render(request, 'driver/profile.html', {'profile': profile})

@login_required
def express_interest(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.interested_drivers.add(request.user.driverprofile)
        return redirect('car_list')
    return render(request, 'driver/express_interest.html', {'car': car})
