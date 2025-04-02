from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Создаем класс ProductForm, который позволяет автоматически создавать форму на основе модели Product"""
    class Meta:
        """С помощью класса Meta указываем с какой моделью связана форма и определяем поля"""
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']
