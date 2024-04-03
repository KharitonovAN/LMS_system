from django.core.management.base import BaseCommand
from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Тестовые данные для Payment"""
    test_payment_1 = Payment.objects.create(
        user_id=1,
        pay_date='2024-03-31',
        paid_course_id=1,
        payment_amount=100,
        payment_method=Payment.PaymentMethod.CASH
    )

    test_payment_2 = Payment.objects.create(
        user_id=1,
        pay_date='2024-04-01',
        paid_lesson_id=2,
        payment_amount=300,
        payment_method=Payment.PaymentMethod.TRANSFER
    )