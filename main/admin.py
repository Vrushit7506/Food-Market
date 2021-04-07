from django.contrib import admin
from .models import Message
from .models import foodMenu
from .models import barMenu
from .models import ordered

# Register your models here.

admin.site.register(Message)
admin.site.register(foodMenu)
admin.site.register(barMenu)
admin.site.register(ordered)
