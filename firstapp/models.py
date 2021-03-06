from django.db import models
from django.utils import timezone
import pytz


class BaseMeta(models.Model):
    created_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone("Asia/Tokyo")))  # 現在の時刻を取得することが可能
    updated_at = models.DateTimeField(default=timezone.datetime.now(pytz.timezone("Asia/Tokyo")))

    class Meta:
        abstract = True  # 抽象クラスにしてこれをインスタンス化できないようにする


class Language(BaseMeta):  # 継承することが可能
    fav = models.CharField(max_length=50)
    like = models.CharField(max_length=40)
    startday = models.DateField(default='2000-01-01')
    email = models.EmailField(db_index=True, blank=True, null=True)
    # インデックスを付与すると検索スピードが上がるが、全てにつけるとデータが重くなってしまうので注意。検索したい項目にだけ付けると良い
    salary = models.FloatField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    web_site = models.URLField(null=True, blank=True)

    class Meta:
        # db_table = 'language'
        index_together = [["fav", "like"]]
        ordering = ['id']  # デフォルトの並び順を指定可能

    def __str__(self):  # objの参照名を定義できる。
        return f'{self.fav}'


class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=30)
    school = models.ForeignKey(
        "Schools", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "students"


class Schools(models.Model):
    name = models.CharField(max_length=20)
    prefecture = models.ForeignKey(
        "Prefectures", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "schools"


class Prefectures(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "prefectures"


# 1対1のテーブルを作ってみる。
class Places(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    class Meta:
        db_table = 'places'


class Restaurants(models.Model):
    place = models.OneToOneField(
        Places,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=40)

    class Meta:
        db_table = "restaurants"