from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dogs_api.v1.views import BreedViewSet, DogViewSet

router = DefaultRouter()

router.register(r"breeds", BreedViewSet, basename="breed")
router.register(r"dogs", DogViewSet, basename="dog")

urlpatterns = [
    path("", include(router.urls)),
]
