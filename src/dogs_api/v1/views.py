from rest_framework import viewsets
from dogs_api.v1.serializers import (
    BreedSerializer,
    DogSerializer,
    DogListSerializer,
)
from .services import BreedService, DogService

# perform_create, perform_update,
# и perform_destroy являются методами,
# которые можно переопределить в классах ViewSet
# для выполнения пользовательской логики при создании,
# обновлении и удалении объектов.

# Преимущества
# Разделение логики: Эти методы позволяют разделить бизнес-логику от логики представления,
#  что делает код более чистым и поддерживаемым.

# Повторное использование: Логика, реализованная в этих методах,
# может быть повторно использована в других частях приложения.

# Гибкость: Они предоставляют гибкость для выполнения дополнительных действий,
# таких как ведение журнала, отправка уведомлений или выполнение сложных проверок.

class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с породами собак.

    Атрибуты:
        serializer_class (Serializer): Класс сериализатора для породы.

    Методы:
        get_queryset: Возвращает набор данных для пород.
        perform_create: Создает новую породу.
        perform_update: Обновляет существующую породу.
        perform_destroy: Удаляет породу.
    """

    serializer_class = BreedSerializer

    def get_queryset(self):
        """
        Возвращает набор данных для пород.

        Returns:
            QuerySet: Набор данных для пород.
        """
        return BreedService.get_queryset()

    def perform_create(self, serializer):
        """
        Создает новую породу.

        Args:
            serializer (Serializer): Сериализатор с валидированными данными.

        Returns:
            None
        """
        instance = BreedService.create_breed(serializer.validated_data)
        serializer.instance = instance

    def perform_update(self, serializer):
        """
        Обновляет существующую породу.

        Args:
            serializer (Serializer): Сериализатор с валидированными данными.

        Returns:
            None
        """
        instance = BreedService.update_breed(
            serializer.instance, serializer.validated_data)
        serializer.instance = instance

    def perform_destroy(self, instance):
        """
        Удаляет породу.

        Args:
            instance (Model): Экземпляр модели породы.

        Returns:
            None
        """
        BreedService.delete_breed(instance)


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с собаками.

    Методы:
        get_serializer_class: Возвращает класс сериализатора в зависимости от действия.
        get_queryset: Возвращает набор данных для собак.
        perform_create: Создает новую собаку.
        perform_update: Обновляет существующую собаку.
        perform_destroy: Удаляет собаку.
    """

    def get_serializer_class(self):
        """
        Возвращает класс сериализатора в зависимости от действия.

        Returns:
            Serializer: Класс сериализатора.
        """
        if self.action in ["list", "retrieve"]:
            return DogListSerializer
        return DogSerializer

    def get_queryset(self):
        """
        Возвращает набор данных для собак.

        Returns:
            QuerySet: Набор данных для собак.
        """
        return DogService.get_queryset()

    def perform_create(self, serializer):
        """
        Создает новую собаку.

        Args:
            serializer (Serializer): Сериализатор с валидированными данными.

        Returns:
            None
        """
        instance = DogService.create_dog(serializer.validated_data)
        serializer.instance = instance

    def perform_update(self, serializer):
        """
        Обновляет существующую собаку.

        Args:
            serializer (Serializer): Сериализатор с валидированными данными.

        Returns:
            None
        """
        DogService.update_dog(serializer.instance, serializer.validated_data)

    def perform_destroy(self, instance):
        """
        Удаляет собаку.

        Args:
            instance (Model): Экземпляр модели собаки.

        Returns:
            None
        """
        DogService.delete_dog(instance)
