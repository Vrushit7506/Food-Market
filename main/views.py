from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import User, Message, foodMenu, barMenu, ordered
from django.http import HttpResponseRedirect
from django.db.models import Q
import json
from decimal import Decimal
from .chatbot import *
from django.core import serializers

# Create your views here.

dname = ""
dqty = ""
dprice = ""
dsavings = ""
other_user = ""
pk1 = 0

def showMenu(request, cuisine):
    global other_user
    all_cuisine = (
        ("1", "Soup"),
        ("2", "Salad"),
        ("3", "Appetizers"),
        ("4", "Italian Mainfare"),
        ("5", "Mexican Mainfare"),
        ("6", "Pastas"),
        ("7", "Pizzas"),
        ("8", "Rice"),
        ("9", "Fondue"),
        ("10", "Desserts"),
    )

    for cuisine1 in all_cuisine:
        if cuisine1[1] == cuisine:
            cuisinename = cuisine
            cuisine = cuisine1[0]
            break
    
    if request.method == "POST":
        dname = request.POST['dname']
        dqty = request.POST['dqty']
        dprice = request.POST['dprice']
        totamt = int(dprice) * int(dqty)
        m = ordered.objects.create(
            user = request.user,
            dish_name=dname, 
            price=totamt, 
            qty=dqty, 
            cooked=False
            )

        msgDish = dname + " is ordered!"
        m1 = Message.objects.create(receiver=request.user, sender=other_user, message=msgDish, className="bot")

    all_dish = foodMenu.objects.all().filter(cuisine__icontains=cuisine)
    return render(request, "main/menu.html", {"all_dish": all_dish, "cuisine":cuisinename})


def showBarMenu(request, drinktype):
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
    for drink in all_drinktype:
        if drink[1] == drinktype:
            drinkname = drinktype
            drinktype = drink[0]
            break
    all_drinks = barMenu.objects.all().filter(drinktype__icontains=drinktype)
    return render(request, "main/barmenu.html", {"all_drinks": all_drinks, "drinktype":drinkname})

def showBarMenu_ajax(request, drinktype):
    if request.method == 'GET':
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
        for drink in all_drinktype:
            if drink[1] == drinktype:
                drinkname = drinktype
                drinktype = drink[0]
                break
            
        all_drinks = barMenu.objects.all().filter(drinktype__icontains=drinktype)

        all_drinks = serializers.serialize("json", all_drinks)

        all_drinks = json.loads(all_drinks)

        return JsonResponse(all_drinks, safe=False)


@login_required
def chatroom(request, pk: int):
    global dname, dqty, dprice, dsavings, other_user, pk1
    
    all_cuisine = (
        ("1", "Soup"),
        ("2", "Salad"),
        ("3", "Appetizers"),
        ("4", "Italian Mainfare"),
        ("5", "Mexican Mainfare"),
        ("6", "Pastas"),
        ("7", "Pizzas"),
        ("8", "Rice"),
        ("9", "Fondue"),
        ("10", "Desserts"),
    )

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

    allcuisine = foodMenu.objects.order_by('cuisine').values('cuisine').distinct()
    for i in allcuisine:
        number = int(i['cuisine']) - 1
        i['cuisine'] = all_cuisine[number][1]

    alldrinks = barMenu.objects.order_by('drinktype').values('drinktype').distinct()
    
    for i in alldrinks:
        number = int(i['drinktype']) - 1
        i['drinktype'] = all_drinktype[number][1]

    all_dishes = foodMenu.objects.values()

    for i in all_dishes:
        number = int(i['cuisine']) - 1
        i['cuisine'] = all_cuisine[number][1]

    all_dishes = json.dumps(list(all_dishes))

    all_ordered = ordered.objects.all()

    newest = foodMenu.objects.all().filter(newest=True)

    for i in newest:
        number = int(i.cuisine) - 1
        i.cuisine = all_cuisine[number][1]


    recommended = foodMenu.objects.all().filter(recommended=True)

    for i in recommended:
        number = int(i.cuisine) - 1
        i.cuisine = all_cuisine[number][1]


    recommended_drink = barMenu.objects.all().filter(recommended_drink = True)

    for i in recommended_drink:
        number = int(i.drinktype) - 1
        i.drinktype = all_drinktype[number][1]

    other_user = get_object_or_404(User, pk=pk)

    pk1 = request.user.pk
    request_user = request.user.username

    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(
        Q(receiver=other_user, sender=request.user))



    if request.method == "POST":

        dname = request.POST['dname']
        dqty = request.POST['dqty']
        dprice = request.POST['dprice']
        dsavings = request.POST['dsavings']
        dtype = request.POST['dtype']

        # print(dname, dqty, dprice, dsavings)
        # print("------------------------")

        msg = ""
        
        if Decimal(dsavings) > 0:
            msg = "Low"
            msg_className = "accepted"
        elif Decimal(dsavings) == 0:
            msg = "Neutral"
            msg_className = "accepted"
        else:
            msg = "High"
            msg_className = "rejected"

        msg1 = str(dtype)

        print(msg1)
        print(msg_className, Decimal(dsavings) > 0)

        msg_price = send_reply_price(msg)
        msg_drink = send_reply_drink(msg1)

        bot_sends_msg = str(msg_price) + " " + str(msg_drink)

        print(str(msg_price) + " " + str(msg_drink))

        m = Message.objects.create(receiver=request.user, sender=other_user, message=bot_sends_msg, className=msg_className)

        # x, y = bargaing(dname, dqty)
        
        
    # x, y = bargaing("White wine", 3)
    # print(x)
    # print(y)
        
    return render(request, "main/home.html", {"other_user": other_user, "request_user": request_user, "messages": messages, 'allcuisine': allcuisine, 'alldrinks': alldrinks, "newest": newest, "recommended": recommended, "recommended_drink": recommended_drink, "all_dishes": all_dishes, "all_ordered": all_ordered})

@login_required
def ajax_load_messages(request, pk):
    global dname, dqty, dprice, dsavings
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "className": message.className,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)    
    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message, className="user_chat")
        message_list.append({
                "sender": request.user.username,
                "message": m.message,
                "sent": True,
                "className": "user_chat",
            })

        if message == "Deal":
            totamt = Decimal(dprice) * int(dqty)
            m = ordered.objects.create(
                user = request.user,
                dish_name=dname, 
                price=Decimal(totamt), 
                qty=int(dqty), 
                cooked=False
                )
            x = bargaing(dname, int(dqty))
            print(x)
        else:
            m = Message.objects.create(receiver=request.user, sender=other_user, message="Order Cancelled", className="bot")
            
    print(message_list)
    return JsonResponse(message_list, safe=False)

@login_required
def ajax_load_messages1(request, pk):
    other_user = get_object_or_404(User, pk=pk)

    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )

    message_list = [{
        "sender": "foodmarket",
        "message": message.message,
        "className": message.className,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)
        bot_message, className = send_reply_drink(message)
        print(className)
        m = Message.objects.create(receiver=request.user, sender=other_user, message=bot_message, className=className)
        message_list.append({
            "sender": "foodmarket",
            "message": bot_message,
            "sent": True,
            "className": "bot",
        })
        print(bot_message)
    return JsonResponse(message_list, safe=False)


def search_view(request):
    if request.method == "POST":
        search_word = request.POST['data']
        print(search_word)
    return render(request, "main/home.html")


def order(request):
    global pk1
    all_ordered = ordered.objects.all().filter(user = pk1)
    return render(request, "main/order.html", {"all_ordered": all_ordered})