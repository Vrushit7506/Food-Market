from django.shortcuts import render
from main.models import barMenu
from django.http.response import JsonResponse
import json
from django.core import serializers

# Create your views here.

def project(request):
    return render(request, "web/index.html")

def stock(request):
    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )

    all_drinks = barMenu.objects.all().order_by('drinktype')

    for i in all_drinks:
        number = int(i.drinktype) - 1
        i.drinktype = all_drinktype[number][1]

    
    return render(request, "web/stock.html", {"all_drinks": all_drinks})


def stock_load_ajax(request):
    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )
    if request.method == 'GET':
        print("------Check----------")
        all_drinks = barMenu.objects.all().order_by('drinktype')

        for i in all_drinks:
            number = int(i.drinktype) - 1
            i.drinktype = all_drinktype[number][1]

        all_drinks = serializers.serialize("json", all_drinks)
        all_drinks = json.loads(all_drinks)
        return JsonResponse(all_drinks, safe=False)