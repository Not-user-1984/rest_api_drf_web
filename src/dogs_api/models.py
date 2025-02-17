from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Breed(models.Model):
    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название породы")
    size = models.CharField(
        max_length=10, choices=SIZE_CHOICES, verbose_name="Размер")
    friendliness = models.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_RATING),
            MaxValueValidator(settings.MAX_RATING),
        ],
        verbose_name="Дружелюбие",
    )
    trainability = models.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_RATING),
            MaxValueValidator(settings.MAX_RATING),
        ],
        verbose_name="Дрессируемость",
    )
    shedding_amount = models.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_RATING),
            MaxValueValidator(settings.MAX_RATING),
        ],
        verbose_name="Количество выпадающей шерсти",
    )
    exercise_needs = models.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_RATING),
            MaxValueValidator(settings.MAX_RATING),
        ],
        verbose_name="Потребность в упражнениях",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Имя собаки"
    )
    age = models.PositiveIntegerField(verbose_name="Возраст")
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        verbose_name="Порода")
    gender = models.CharField(max_length=50, verbose_name="Пол")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    favorite_food = models.CharField(
        max_length=100,
        verbose_name="Любимая еда")
    favorite_toy = models.CharField(
        max_length=100,
        verbose_name="Любимая игрушка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
