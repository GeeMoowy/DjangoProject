from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Создаем группы для пользователей приложения"

    def handle(self, *args, **kwargs):
        group_name = 'Модератор продуктов'
        group, created = Group.objects.ger_or_create(name=group_name)
        if created:
            self.stdout.write(self.style.SUCCES(f'Группа "{group_name}" успешно создана.'))
        else:
            self.stdout.write(self.style.WARNING(f'Группа "{group_name}" уже существует.'))