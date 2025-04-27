from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    """Создаем класс ProductForm, который позволяет автоматически создавать форму на основе модели Product"""

    forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар",]

    class Meta:
        """С помощью класса Meta указываем с какой моделью связана форма и определяем поля"""
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']

    def __init__(self, *args, **kwargs):
        """Переопределяем метод __init__ для стилизации полей формы"""
        super().__init__(*args, **kwargs)

        # Добавляем классы CSS к полям формы
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['purchase_price'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите цену продукта'})

    def clean(self):
        """Кастомная валидация для проверки запрещенных слов"""
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in self.forbidden_words:
            if name and word in name.lower():
                self.add_error('name', f"Название продукта не может содержать слово '{word}'.")
            if description and word in description.lower():
                self.add_error('description', f"Описание продукта не может содержать слово '{word}'.")

        return cleaned_data

    def clean_purchase_price(self):
        """Кастомная валидация для поля purchase_price"""
        price = self.cleaned_data.get('purchase_price')

        if price is not None and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной.")

        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            raise ValidationError("Пожалуйста, загрузите изображение.")

        if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
            raise ValidationError("Формат изображения должен быть JPEG или PNG.")

        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return image


class ContactsForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
