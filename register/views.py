from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegisterForm


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect(reverse('homePage')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register/register.html', {'form': form})

class registerForm(TemplateView):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid() == True:
            form.save()
            return redirect(reverse('home'))
        else:
            form = UserRegisterForm()
            return redirect(request, 'register/register.html', {'form': form})