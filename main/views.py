from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .models import User, Message, foodMenu, barMenu
from django.db.models import Q
import json

# Create your views here.


def showMenu(request):
    return render(request, "main/menu.html")

@login_required
def chatroom(request, pk:int):
    allcuisine = foodMenu.objects.order_by().values('cuisine').distinct()
    alldrinks = barMenu.objects.all()
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user) )
    return render(request, "main/home.html", {"other_user": other_user, "messages": messages, 'allcuisine': allcuisine, 'alldrinks':alldrinks})


@login_required
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)
