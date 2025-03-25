from django.db import models
from django.db.models import CASCADE


class Product(models.Model):
    """Создание модели Product, которая будет хранить информацию о продуктах"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=255, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=CASCADE)
    purchase_price = models.FloatField(default=0.0, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


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
