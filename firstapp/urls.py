from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("page/<str:user_name>", views.user_page, name="user_page"),
    path("page_num/<int:number>/<str:user_name>", views.number_page, name="number_page"),
    path("page/<int:num1>/<int:num2>", views.add_num, name="add")
]
