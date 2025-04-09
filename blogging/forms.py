from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """Создаем класс BlogForm, который позволяет автоматически создавать форму на основе модели Blog"""
    class Meta:
        """С помощью класса Meta указываем с какой моделью связана форма и определяем поля"""
        model = Blog
        fields = ['title', 'content', 'preview', 'sign_of_publication']
