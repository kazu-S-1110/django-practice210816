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


def home(request):
    my_name = "hoge sage"
    books = ["excel", "word", "python"]
    pc = {
        "apple": "mac",
        "widnows": "surface",
        "lenovo": "ideapad"
    }
    return render(request, "home.html", context={
        "my_name": my_name,
        "books": books,
        "pc": pc
    })


def sample1(request):
    return render(request, "sample1.html")


def sample2(request):
    return render(request, "sample2.html")


def sample(request):
    name = "React"
    birth = 2013
    age = 2021
    page_url = "https://ja.reactjs.org"
    favo = [
        "js", "jsx", "ts", "tsx"
    ]
    msg = """hello, react
    I like nextjs,
    and redux,
    """
    return render(request, "sample.html", context={
        "name": name,
        "birth": birth,
        "age": age,
        "page_url": page_url,
        "favo": favo,
        "msg": msg
    })


class Country:

    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


def sample3(request):
    country = Country("Japan", 10000000, "Tokyo")
    return render(request, "sample3.html", context={
        "country": country
    })
