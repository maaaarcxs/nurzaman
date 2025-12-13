from django.db import models


class User(models.Model):
    USER_STATUS = (
        ("admin", "Админ"),
        ("user", "Пользователь"),
        ("anonymous_user", "Анониммный пользователь")
    )
    status = models.CharField(max_length=20, choices=USER_STATUS, verbose_name="Статус")


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название")
    description = models.CharField(max_length=1200, verbose_name="Описание")
    owner = models.BooleanField(User, default="user")