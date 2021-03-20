from django.shortcuts import render
from .models import ChatDB

# Create your views here.

def home(request):
    allChat = ChatDB.objects.all().order_by('chatno')
    return render(request, 'main/home.html', {'allChat' : allChat})
