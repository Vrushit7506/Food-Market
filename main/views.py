from django.shortcuts import render
from .models import ChatDB, foodMenu, barMenu

# Create your views here.

def botSends(request):
    ChatDB.objects.create(user = "Vrushit", text = "No Deal! Tonight forecast - 100% chances of fruit juice! No drinks for you!", className = "rejected")
    # ChatDB.objects.create(user = user, text = text, className = className)

def home(request):
    # botSends("Vrushit", "No Deal! Tonight forecast - 100% chances of fruit juice! No drinks for you!", "rejected")
    allChat = ChatDB.objects.all().order_by('chatno')
    allcuisine = foodMenu.objects.all()
    alldrinks = barMenu.objects.all()
    return render(request, 'main/home.html', {'allChat': allChat, 'allcuisine': allcuisine, 'alldrinks':alldrinks})
    
