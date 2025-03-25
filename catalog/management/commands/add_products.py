from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Класс для добавления тестовых данных в базу данных'

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Мягкие игрушки',
                                                     description='Детские мягкие игрушки из плюша')

        products = [
            {"name": "Мишка", "description": "Плюшевый медведь коричневый", "image": "images/мишка.jpg",
             "category": category, "purchase_price": 860.0},
            {"name": "Зайчик", "description": "Плюшевый зайчик серый", "image": "images/зайчик.jpg",
             "category": category, "purchase_price": 900.0},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Успешное добавление продукта: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Данный продукт уже существует: {product.name}"))