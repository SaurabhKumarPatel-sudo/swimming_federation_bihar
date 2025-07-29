from django.shortcuts import render, redirect
from .models import Event, Record, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserForm, ProfileForm, CoachProfileForm
from .models import Profile

def main_page(request):
    """Main page view that renders all content in base.html"""
    events = Event.objects.all()
    records = Record.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Message sent successfully!')
            return redirect('main_page')
    
    return render(request, 'sfb/base.html', {
        'events': events,
        'records': records
    })

def home(request):
    return redirect('main_page')

def events(request):
    return redirect('main_page')

def registration_choice(request):
    """Page to choose between Athlete and Coach registration."""
    return render(request, 'sfb/registration_choice.html')

from django.db import transaction

@transaction.atomic
def athlete_registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # Do not set password; admin will set and share credentials
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.user_type = 'athlete'
            profile.save()
            
            messages.success(request, 'Athlete registration successful! Login credentials will be shared by admin.')
            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        
    return render(request, 'sfb/athlete_registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@transaction.atomic
def coach_registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = CoachProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # Do not set password; admin will set and share credentials
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.user_type = 'coach'
            profile.save()
            
            messages.success(request, 'Coach registration successful! Login credentials will be shared by admin.')
            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = CoachProfileForm()
        
    return render(request, 'sfb/coach_registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('profile')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "sfb/login.html", {"login_form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('main_page')

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # This case should ideally not happen with the current registration flow
        profile = None
    return render(request, 'sfb/profile.html', {'profile': profile})

def records(request):
    return redirect('main_page')

def rules(request):
    return redirect('main_page')

def about(request):
    return redirect('main_page')

def contact(request):
    return redirect('main_page')

def gallery(request):
    return redirect('main_page')

def discipline_swimming(request):
    return render(request, 'sfb/discipline_swimming.html')

def discipline_masters_swimming(request):
    return render(request, 'sfb/discipline_masters_swimming.html')

def discipline_synchronized_swimming(request):
    return render(request, 'sfb/discipline_synchronized_swimming.html')

def discipline_diving(request):
    return render(request, 'sfb/discipline_diving.html')

def discipline_high_diving(request):
    return render(request, 'sfb/discipline_high_diving.html')

def discipline_water_polo(request):
    return render(request, 'sfb/discipline_water_polo.html')
