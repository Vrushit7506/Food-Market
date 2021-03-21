from django.shortcuts import render
from .models import ChatDB, foodMenu, barMenu

# Create your views here.

def home(request):
    allChat = ChatDB.objects.all().order_by('chatno')
    allcuisine = foodMenu.objects.all()
    alldrinks = barMenu.objects.all()
    return render(request, 'main/home.html', {'allChat': allChat, 'allcuisine': allcuisine, 'alldrinks':alldrinks})
    
