import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

from django import setup

setup()

from firstapp.models import Places, Restaurants

places = [
    ("motomachi", "yokohama"), ("tsukiji", "tokyo")
]

restaurants = ["restaurant A", "restaurant B"]

for place_name, place_address in places:
    p = Places(name=place_name, address=place_address)
    p.save()
    for restaurant_name in restaurants:
# 下二行の方法だと作られるレコードはどちらも同じ名前になる
        r = Restaurants(place=p, name=restaurant_name)
        r.save()
        # Restaurants.objects.create(
        #     place=p,
        #     name=restaurant_name
        # )
