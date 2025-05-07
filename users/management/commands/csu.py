from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(username='admin', email='admin@example.com')
        user.set_password('123qwe')
        user.is_activ = True
        user.is_stuff = True
        user.is_superuser = True
        user.save()