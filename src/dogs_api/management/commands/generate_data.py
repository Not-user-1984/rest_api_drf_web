from django.core.management.base import BaseCommand
from faker import Faker
from dogs_api.models import Breed, Dog
import random


class Command(BaseCommand):
    help = "Генерация фиктивных данных для моделей Breed и Dog"

    def handle(self, *args, **kwargs):
        fake = Faker()

        popular_breeds = [
            "Labrador Retriever",
            "German Shepherd",
            "Golden Retriever",
            "Bulldog",
            "Beagle",
            "Poodle",
            "Rottweiler",
            "Yorkshire Terrier",
            "Boxer",
            "Dachshund",
            "Siberian Husky",
            "Great Dane",
            "Shih Tzu",
            "Chihuahua",
            "Pomeranian",
            "Border Collie",
            "Doberman Pinscher",
            "Australian Shepherd",
            "Cocker Spaniel",
            "Shetland Sheepdog",
            "Bernese Mountain Dog",
            "Basset Hound",
            "Maltese",
            "Weimaraner",
            "Bull Terrier",
            "Saint Bernard",
            "Pug",
            "Boston Terrier",
            "Havanese",
            "Cavalier King Charles Spaniel",
        ]

        self.stdout.write("Создание пород собак...")
        for breed_name in popular_breeds:
            Breed.objects.create(
                name=breed_name,
                size=random.choice(["Tiny", "Small", "Medium", "Large"]),
                friendliness=random.randint(1, 5),
                trainability=random.randint(1, 5),
                shedding_amount=random.randint(1, 5),
                exercise_needs=random.randint(1, 5),
            )
        self.stdout.write(self.style.SUCCESS("Создано 30 пород собак."))

        self.stdout.write("Создание собак...")
        breeds = Breed.objects.all()
        for _ in range(1000):
            Dog.objects.create(
                name=fake.first_name(),
                age=random.randint(1, 15),
                breed=random.choice(breeds),
                gender=random.choice(["Male", "Female"]),
                color=fake.color_name(),
                favorite_food=fake.word(),
                favorite_toy=fake.word(),
            )
        self.stdout.write(self.style.SUCCESS("Создано 1000 собак."))
