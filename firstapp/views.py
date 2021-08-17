from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")


def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s page</h1>')


def number_page(request, number, user_name):  # httpResponseに渡すものは複数でも可能
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{number}番の{user_name}のページですよ〜</h1>')


def add_num(request, num1, num2):
    res_add = num1 + num2
    res_product = num1 * num2
    return HttpResponse(f'<h1>result add :{res_add}</h1><br><h2>result product : {res_product}</h2>')


def index(request):
    # indexに変数を渡す方法
    test_text = "yeeeee!"
    return render(request, "index.html",
                  context={"value": "Hello world", "test": test_text})  # デフォルトでtemplates内のファイルを見に行ってくれるらしい
