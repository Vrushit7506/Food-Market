from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # path('', views.home, name = 'homePage'),
    # path('admin/', admin.site.urls),
    path("<int:pk>/", views.chatroom, name="chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),
]
