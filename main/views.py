from django.shortcuts import render
from .models import ChatDB
from .chatbot import *

# Create your views here.

def botSends(request):
    ChatDB.objects.create(user = "Vrushit", text = "No Deal! Tonight forecast - 100% chances of fruit juice! No drinks for you!", className = "rejected")
    # ChatDB.objects.create(user = user, text = text, className = className)

def home(request):
    # botSends("Vrushit", "No Deal! Tonight forecast - 100% chances of fruit juice! No drinks for you!", "rejected")
    allChat = ChatDB.objects.all().order_by('chatno')
    return render(request, 'main/home.html', {'allChat' : allChat})
