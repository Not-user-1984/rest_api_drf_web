from dogs_api.models import Breed, Dog
from django.db.models import Count, Avg, OuterRef, Subquery


class BreedService:
    @staticmethod
    def get_queryset():
        """
        Возвращает набор данных для пород с аннотацией количества собак.

        Returns:
            QuerySet: Набор данных для пород с количеством собак.
        """
        return Breed.objects.annotate(dogs_count=Count("dog"))

    @staticmethod
    def create_breed(validated_data):
        """
        Создает новую породу.

        Args:
            validated_data (dict): Валидированные данные для создания породы.

        Returns:
            Breed: Созданная порода.
        """
        breed = Breed.objects.create(**validated_data)
        return breed

    @staticmethod
    def update_breed(breed, validated_data):
        """
        Обновляет существующую породу.

        Args:
            breed (Breed): Экземпляр породы для обновления.
            validated_data (dict): Валидированные данные для обновления породы.

        Returns:
            Breed: Обновленная порода.
        """
        for attr, value in validated_data.items():
            setattr(breed, attr, value)
        breed.save()
        return breed

    @staticmethod
    def delete_breed(breed):
        """
        Удаляет породу.

        Args:
            breed (Breed): Экземпляр породы для удаления.

        Returns:
            None
        """
        breed.delete()


class DogService:
    @staticmethod
    def get_queryset():
        """
        Возвращает набор данных для собак с аннотацией количества собак той же породы и среднего возраста породы.

        Returns:
            QuerySet: Набор данных для собак с дополнительной информацией.
        """
        return Dog.objects.annotate(
            same_breed_count=Count("breed__dog"),
            breed_avg_age=Subquery(
                Dog.objects.filter(breed=OuterRef("breed"))
                .values("breed")
                .annotate(avg_age=Avg("age"))
                .values("avg_age")
            ),
        )

    @staticmethod
    def create_dog(validated_data):
        """
        Создает новую собаку.

        Args:
            validated_data (dict): Валидированные данные для создания собаки.

        Returns:
            Dog: Созданная собака.
        """
        return Dog.objects.create(**validated_data)

    @staticmethod
    def update_dog(dog, validated_data):
        """
        Обновляет существующую собаку.

        Args:
            dog (Dog): Экземпляр собаки для обновления.
            validated_data (dict): Валидированные данные для обновления собаки.

        Returns:
            Dog: Обновленная собака.
        """
        for attr, value in validated_data.items():
            setattr(dog, attr, value)
        dog.save()
        return dog

    @staticmethod
    def delete_dog(dog):
        """
        Удаляет собаку.

        Args:
            dog (Dog): Экземпляр собаки для удаления.

        Returns:
            None
        """
        dog.delete()
