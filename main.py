import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

from django import setup

setup()

from firstapp.models import Language

l = Language(
    fav="python", like="2", startday="1991-01-01"
)
l.save()