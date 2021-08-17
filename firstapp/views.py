from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s page</h1>')


def number_page(request, number, user_name):  # httpResponseに渡すものは複数でも可能
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{number}番の{user_name}のページですよ〜</h1>')
