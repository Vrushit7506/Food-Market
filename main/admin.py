from django.contrib import admin
from .models import ChatDB
from .models import foodMenu
from .models import barMenu

# Register your models here.

admin.site.register(ChatDB)
admin.site.register(foodMenu)
admin.site.register(barMenu)
