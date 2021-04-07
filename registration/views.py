from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def registerPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['password1'] = "foodmarket"
            form.cleaned_data['password2'] = "foodmarket"
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('../home/1/')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/registration.html', {'form':form})

def registerPage1(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['password1'] = "foodmarket"
            form.cleaned_data['password2'] = "foodmarket"
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('../../home/1/')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/registration.html', {'form':form})