from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path("hello", views.index, name="index"),
    path("page/<str:user_name>", views.user_page, name="user_page"),
    path("page_num/<int:number>/<str:user_name>", views.number_page, name="number_page")
]
