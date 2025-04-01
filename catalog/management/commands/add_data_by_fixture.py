from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Класс для добавления тестовых данных в базу данных с помощью фикстуры'

    def handle(self, *args, **options):
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Успешное добавление данных'))