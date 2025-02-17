from rest_framework import serializers
from dogs_api.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Breed.

    Атрибуты:
        dogs_count (IntegerField): Поле для количества собак данной породы.
    """

    dogs_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "dogs_count",
        ]


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Dog.

    Атрибуты:
        same_breed_count (IntegerField): Поле для количества собак той же породы.
        breed_avg_age (FloatField): Поле для среднего возраста собак данной породы.
    """

    same_breed_count = serializers.IntegerField(read_only=True)
    breed_avg_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "same_breed_count",
            "breed_avg_age",
        ]


class DogListSerializer(DogSerializer):
    """
    Сериализатор для списка собак с вложенной информацией о породе.

    Атрибуты:
        breed (BreedSerializer): Вложенный сериализатор для породы.
    """

    breed = BreedSerializer(read_only=True)
