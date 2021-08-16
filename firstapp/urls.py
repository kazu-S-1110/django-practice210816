from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path("hello", views.index, name="index")
]
