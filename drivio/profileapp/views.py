from django.shortcuts import render, redirect
from django.http import HttpResponse
from owner2.models import Cars

from .forms import CreateUserForm, ProfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@login_required(login_url='loginD')
def index(request):
    car=Cars.objects.all()
    return render(request,'profileapp/homeP.html' ,{'car':car})
    # return render(request, 'profileapp/homeP.html')

@login_required(login_url='loginD')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profileapp/profile.html', context)

@login_required(login_url='loginD')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('homeP')  # Redirect to the same page after updating the profile
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form, 'user': request.user}  # Pass the user object to the template
    return render(request, 'profileapp/editprofile.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect('homeP')  # Redirect to the 'home' URL pattern name
        else:
            messages.info(request, 'Wrong password or username')
            return redirect('loginD')
    return render(request, 'profileapp/login_page.html')

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('loginD')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'profileapp/register_page.html', context)

    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)

@login_required(login_url='loginD')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('loginD')