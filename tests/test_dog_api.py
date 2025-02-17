import pytest
from django.urls import reverse
from rest_framework import status
from dogs_api.models import Dog


@pytest.mark.django_db
class TestDogAPI:
    """
    Тесты для API собак (Dog).
    """

    def test_create_dog(self, api_client, dog_data):
        """
        Тестирование создания собаки.
        """
        url = reverse("dog-list")
        response = api_client.post(url, dog_data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Dog.objects.count() == 1
        assert Dog.objects.get().name == "Buddy"

    def test_retrieve_dog(self, api_client, dog_data_for_manual_creation):
        """
        Тестирование получения деталей собаки.
        """
        dog = Dog.objects.create(**dog_data_for_manual_creation)

        url = reverse("dog-detail", kwargs={"pk": dog.id})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Buddy"

    def test_update_dog(
            self, api_client,
            dog_data,
            dog_data_for_manual_creation
            ):
        """
        Тестирование обновления собаки.
        """
        dog = Dog.objects.create(**dog_data_for_manual_creation)

        data = {"name": "Max", "age": 5}

        url = reverse("dog-detail", kwargs={"pk": dog.id})
        response = api_client.put(url, {**dog_data, **data}, format="json")

        assert response.status_code == status.HTTP_200_OK
        dog.refresh_from_db()
        assert dog.name == "Max"

    def test_delete_dog(self, api_client, dog_data_for_manual_creation):
        """
        Тестирование удаления собаки.
        """
        dog = Dog.objects.create(**dog_data_for_manual_creation)
        print(dog)

        url = reverse("dog-detail", kwargs={"pk": dog.id})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Dog.objects.count() == 0
