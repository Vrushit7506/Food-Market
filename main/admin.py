from django.contrib import admin
from .models import Message
from .models import foodMenu
from .models import barMenu
from .models import ordered
from import_export.admin import ImportExportModelAdmin
from .resources import barMenuResource

# Register your models here.

class barMenuAdmin(ImportExportModelAdmin):
    resource_class = barMenuResource

admin.site.register(Message)
admin.site.register(foodMenu)
admin.site.register(barMenu)
admin.site.register(ordered)

