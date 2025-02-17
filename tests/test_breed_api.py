import pytest
from django.urls import reverse
from rest_framework import status
from dogs_api.models import Breed


@pytest.mark.django_db
class TestBreedAPI:
    """
    Тесты для API пород собак (Breed).
    """

    def test_list_breeds(self, api_client, breed_data):
        """
        Тестирование получения списка пород.
        """
        Breed.objects.create(**breed_data)
        Breed.objects.create(
            name="Bulldog",
            size="Small",
            friendliness=3,
            trainability=2,
            shedding_amount=4,
            exercise_needs=5,
        )

        url = reverse("breed-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_create_breed(self, api_client, breed_data):
        """
        Тестирование создания породы.
        """
        url = reverse("breed-list")
        response = api_client.post(url, breed_data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Breed.objects.count() == 1
        assert Breed.objects.get().name == "Labrador"

    def test_retrieve_breed(self, api_client, breed_data):
        """
        Тестирование получения деталей породы.
        """
        breed = Breed.objects.create(**breed_data)

        url = reverse("breed-detail", kwargs={"pk": breed.id})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Labrador"

    def test_update_breed(self, api_client, breed_data):
        """
        Тестирование обновления породы.
        """
        breed = Breed.objects.create(**breed_data)
        data = {"name": "Golden Retriever", "size": "Large"}
        url = reverse("breed-detail", kwargs={"pk": breed.id})
        response = api_client.put(url, {**breed_data, **data}, format="json")

        assert response.status_code == status.HTTP_200_OK
        breed.refresh_from_db()
        assert breed.name == "Golden Retriever"

    def test_delete_breed(self, api_client, breed_data):
        """
        Тестирование удаления породы.
        """
        breed = Breed.objects.create(**breed_data)

        url = reverse("breed-detail", kwargs={"pk": breed.id})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Breed.objects.count() == 0
