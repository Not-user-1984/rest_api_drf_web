import pytest
from rest_framework.test import APIClient
from dogs_api.models import Breed, Dog


@pytest.fixture(autouse=True)
def cleanup_database():
    """
    Фикстура для очистки базы данных перед каждым тестом.
    """
    yield
    Dog.objects.all().delete()
    Breed.objects.all().delete()


@pytest.fixture
def api_client():
    """
    Фикстура для создания APIClient.
    """
    return APIClient()


@pytest.fixture
def breed_data():
    """
    Фикстура для создания тестовой породы.
    """
    return {
        "name": "Labrador",
        "size": "Medium",
        "friendliness": 5,
        "trainability": 4,
        "shedding_amount": 3,
        "exercise_needs": 4,
    }


@pytest.fixture
def breed(breed_data):
    """
    Фикстура для создания тестовой породы.
    """
    return Breed.objects.create(**breed_data)


@pytest.fixture
def dog_data(breed):
    """
    Фикстура для создания тестовой собаки.
    """
    return {
        "name": "Buddy",
        "age": 3,
        "breed": breed.id,
        "gender": "Male",
        "color": "Golden",
        "favorite_food": "Chicken",
        "favorite_toy": "Ball",
    }


@pytest.fixture
def create_breed():
    """
    Фикстура для создания породы в базе данных.
    """

    def _create_breed(**kwargs):
        return Breed.objects.create(**kwargs)

    return _create_breed


@pytest.fixture
def create_dog():
    """
    Фикстура для создания собаки в базе данных.
    """

    def _create_dog(breed, **kwargs):
        return Dog.objects.create(breed=breed, **kwargs)

    return _create_dog


@pytest.fixture
def dog_data_for_manual_creation(breed):
    """
    Фикстура для создания тестовой собаки вручную (без API).
    """
    return {
        "name": "Buddy",
        "age": 3,
        "breed": breed,
        "gender": "Male",
        "color": "Golden",
        "favorite_food": "Chicken",
        "favorite_toy": "Ball",
    }
