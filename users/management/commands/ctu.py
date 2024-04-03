from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Тестовый пользователь"""
    def handle(self, *args, **options):
        test_user = User.objects.create(
            email='user@test.ru',
            is_active=True,
        )
        test_user.set_password('user')
        test_user.save()
