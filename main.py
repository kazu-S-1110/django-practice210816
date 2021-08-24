import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

from django import setup
from django.utils import timezone
import pytz

setup()

from firstapp.models import Language

# l = Language(
#     fav="python", like="2", startday="1991-01-01"
# )
# l.save()

# 他のDBへの追加方法
# classmethod created_at
# Language.objects.create(
#     fav="JavaScript", like="2", startday="1995-01-01"
# )

# get_or_create(取得or作成)
# obj, created = Language.objects.get_or_create(
#     fav="Node", like="4", startday="2009-01-01"
# )
# print(obj)  # 作られたobjが表示
# print(created)  # booleanで成功したかどうかが表示

# 全てのデータを取得する
# languages = Language.objects.all()
# for language in languages:
#     print(language.id, language.startday, language)
#
# # 特定のデータのみ取得する (以下の結果は全て同じ)
# language = Language.objects.get(id=1)
# print(language)
# languages = Language.objects.get(pk=1)
# print(language)
# language = Language.objects.get(fav="react")
# print(language)
#
# # filterでデータを絞りこんで取得する
# languages = Language.objects.filter(fav="react").all()
# for language in languages:
#     print(language)

# 更新処理
# language = Language.objects.get(id=1)
# print(language)
# language.like = "best"
# language.updated_at = timezone.datetime.now(pytz.timezone("Asia/Tokyo"))
# language.save()


# 複数の更新処理をする場合
# languages = Language.objects.filter(memo__isnull=True).all()
# print(languages)
# 下の処理だと一件毎にsaveをするため効率が悪い
# for language in languages:
#     language.memo = "updated!"
#     language.updated_at = timezone.datetime.now(pytz.timezone("Asia/Tokyo"))
#     language.save()

# まとめてするなら下の方が効率的
# Language.objects.filter(memo__isnull=False).update(
#     memo="update2!",
#     updated_at=timezone.datetime.now(pytz.timezone("Asia/Tokyo"))
# )

# 削除処理
# Language.objects.filter(fav="Node").delete()

# 全件削除
# Language.objects.all().delete()
