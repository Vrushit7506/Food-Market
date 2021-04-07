from django.shortcuts import render
from main.models import barMenu
from django.http.response import JsonResponse
import json
from django.core import serializers

# Create your views here.

def project(request):
    return render(request, "web/index.html")

def stock(request):
    all_drinks = barMenu.objects.all().order_by('drinktype')
    return render(request, "web/stock.html", {"all_drinks": all_drinks})


def stock_load_ajax(request):
    if request.method == 'GET':
        print("------Check----------")
        all_drinks = serializers.serialize("json", barMenu.objects.all().order_by('drinktype'))
        all_drinks = json.loads(all_drinks)
        return JsonResponse(all_drinks, safe=False)