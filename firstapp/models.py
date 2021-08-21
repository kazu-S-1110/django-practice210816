from django.db import models


class Language(models.Model):
    fav = models.CharField(max_length=50)
    like = models.CharField(max_length=40)


class Framework(models.Model):
    like1 = models.CharField(max_length=40)
    like2 = models.CharField(max_length=40)
