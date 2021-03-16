from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'homePage'),
    # path('admin/', admin.site.urls),
]
