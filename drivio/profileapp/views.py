from django.shortcuts import render, redirect
from django.http import HttpResponse
from owner2.models import Cars

from .forms import CreateUserForm, ProfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.core.mail import send_mail, BadHeaderError


from .forms import ContactForm 

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
            return redirect('editprofile')
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



 # Make sure you have this form in your forms.py

# views.py
from django.core.mail import EmailMessage


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                email_message = EmailMessage(
                    subject=f'Contact Form Submission from {name}',
                    body=message,
                    from_email='2dolist99@gmail.com',  # Your authenticated email
                    to=['2dolist99@gmail.com'],  # Your email
                    reply_to=[email]  # The user's email
                )
                email_message.send(fail_silently=False)
                messages.success(request, 'Your message has been sent successfully.')
                return redirect('success')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'profileapp/contact.html', {'form': form})


from owner2.models import Cars  # Import the Car model from owner2 app
from .models import InterestedCar
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def mark_interested(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    InterestedCar.objects.get_or_create(user=request.user, car=car)
    messages.success(request, f"You have marked {car.car_name} as interested.")
    return redirect('homeP')

@login_required
def interested_cars(request):
    interested_cars = InterestedCar.objects.filter(user=request.user)
    return render(request, 'profileapp/interested_cars.html', {'interested_cars': interested_cars})


from django.views.generic import ListView, DetailView
class CarSearchView(ListView):
    model = Cars
    template_name = 'all_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Cars.objects.filter(car_name__icontains=query).order_by('-created_at')