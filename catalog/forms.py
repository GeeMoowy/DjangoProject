from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Создаем класс ProductForm, который позволяет автоматически создавать форму на основе модели Product"""
    class Meta:
        """С помощью класса Meta указываем с какой моделью связана форма и определяем поля"""
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']


class ContactsForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
