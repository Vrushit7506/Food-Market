"""Food_Stock_Exchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as mainViews
from registration import views as r


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('registration/', r.registerPage, name="registration"),
    path('register/', include('register.urls')),
    path('home/', include('main.urls')),
    path("home/<int:pk>/", mainViews.chatroom, name="chatroom"),
    path("home/ajax1/<int:pk>/", mainViews.ajax_load_messages, name="chatroom-ajax"),
    path("menu/<str:cuisine>", mainViews.showMenu, name="showMenu"),
    path("barmenu/<str:drinktype>", mainViews.showBarMenu, name="showBarMenu"),
    path("barmenu/ajax/<str:drinktype>", mainViews.showBarMenu_ajax, name="showBarMenu_ajax"),
]
