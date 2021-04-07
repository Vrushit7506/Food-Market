from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
  path("", views.project, name="project"),
  path("stock/", views.stock, name="stock"),
  path("stock/ajax", views.stock_load_ajax, name="stock_load_ajax"),
]
