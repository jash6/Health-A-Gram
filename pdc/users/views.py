from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DetailUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import (DetailView)
from geopy.geocoders import Nominatim
import requests
import json

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    geo_json = requests.get('https://api.ipdata.co?api-key=d452e16e908d2c0e6f9464a6fb5702c168bf59f81971a2e46c2f039d').json()
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    address = str(latitude)+", "+str(longitude)
    geolocator = Nominatim(user_agent="views")
    location = geolocator.reverse(address)
    city = location.raw["address"]["city"]
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile
                                  )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('recommend')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'city': city,
        'address': address,
    }
    return render(request, 'users/profile.html', context)



class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile_view.html'