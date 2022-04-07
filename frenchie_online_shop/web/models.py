from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    NAME_MAX_LENGTH = 25
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )


class Product(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    image = models.URLField()

    price = models.FloatField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )


class Album(models.Model):
    image = models.URLField()
