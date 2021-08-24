import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

from django import setup

setup()

from firstapp.models import Students, Schools, Prefectures

prefectures = ["Tokyo", "Osaka", "Kyoto"]
schools = ["east high school", "west high school", "central high school"]
students = ["Taro", "Shinji", "Asuka", "Rei"]


def insert_records():
    for prefecture_name in prefectures:
        prefecture = Prefectures(
            name=prefecture_name
        )
        prefecture.save()
        for school_name in schools:
            school = Schools(
                name=school_name,
                prefecture=prefecture
            )
            school.save()
            for student_name in students:
                student = Students(
                    name=student_name,
                    age=14,
                    major="eva",
                    school=school
                )
                student.save()


insert_records()
