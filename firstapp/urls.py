from django.urls import path
from . import views

app_name = "firstapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("sam", views.sample, name="sample"),
    path("sam1", views.sample1, name="sample1"),
    path("sam2", views.sample2, name="sample2"),
    path("sam3", views.sample3, name="sample3"),
    path("page/<str:user_name>", views.user_page, name="user_page"),
    path("page_num/<int:number>/<str:user_name>", views.number_page, name="number_page"),
    path("page/<int:num1>/<int:num2>", views.add_num, name="add")
]
