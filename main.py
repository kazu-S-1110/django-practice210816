import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

from django import setup

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
obj, created = Language.objects.get_or_create(
    fav="Node", like="4", startday="2009-01-01"
)
print(obj)  # 作られたobjが表示
print(created)  # booleanで成功したかどうかが表示
