from django.contrib import admin
from .models import Message
from .models import foodMenu
from .models import barMenu
from .models import ordered
from import_export.admin import ImportExportModelAdmin
from .resources import barMenuResource, foodMenuResource

# Register your models here.

class barMenuAdmin(ImportExportModelAdmin):
    resource_class = barMenuResource

class foodMenuAdmin(ImportExportModelAdmin):
    resource_class = foodMenuResource

admin.site.register(Message)
admin.site.register(foodMenu, ImportExportModelAdmin)
admin.site.register(barMenu, ImportExportModelAdmin)
admin.site.register(ordered)

