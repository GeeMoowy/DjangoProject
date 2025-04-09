from django.db import models


class Blog(models.Model):
    """Создание модели блога, которая будет хранить информацию о блогах"""

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True)
    sign_of_publication = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title} - {self.created_at}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
