from django.db import models
from django.utils import timezone


class BaseMeta(models.Model):
    created_at = models.DateTimeField(default=timezone.datetime.now())  # 現在の時刻を取得することが可能
    updated_at = models.DateTimeField(default=timezone.datetime.now())

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
        ordering = ['startday']
