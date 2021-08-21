from django.db import models
from django.utils import timezone


class Language(models.Model):
    fav = models.CharField(max_length=50)
    like = models.CharField(max_length=40)
    startday = models.DateField(default='2000-01-01')
    email = models.EmailField(db_index=True, blank=True, null=True)
    # インデックスを付与すると検索スピードが上がるが、全てにつけるとデータが重くなってしまうので注意。検索したい項目にだけ付けると良い
    salary = models.FloatField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    web_site = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.datetime.now())
    # 現在の時刻を取得することが可能


class Framework(models.Model):
    like1 = models.CharField(max_length=40)
    like2 = models.CharField(max_length=40)

