from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    """Создание модели Product, которая будет хранить информацию о продуктах"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=CASCADE)
    purchase_price = models.FloatField(default=0.0, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [
            ('Can_unpublish_product', 'Can_unpublish_product'),
            ('Can_delete_product', 'Can_delete_product'),
        ]


class Category(models.Model):
    """Создание модели Category, которая будет хранить информацию о категориях"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
