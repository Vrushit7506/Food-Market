from django.contrib import admin
from .models import Message
from .models import foodMenu
from .models import barMenu

# Register your models here.

admin.site.register(Message)
admin.site.register(foodMenu)
admin.site.register(barMenu)
