from .models import barMenu
from .models import foodMenu
from import_export import resources

class barMenuResource(resources.ModelResource):
    class Meta:
        model = barMenu

class foodMenuResource(resources.ModelResource):
    class Meta:
        model = foodMenu