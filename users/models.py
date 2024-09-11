from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

payment_choices = (
    ("Cash", "Наличные"),
    ("Transfer on account", "Перевод на счет"),
)


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Your email address"
    )

    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Phone",
        help_text="Your phone number",
    )
    city = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="City", help_text="Your city"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Avatar",
        help_text="Your photo",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Пользователь", help_text="Введите ФИО", blank=True, null=True)
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Оплаченный курс"
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name="Урок",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Оплаченный урок"
    )
    amount_of_payment = models.PositiveIntegerField(verbose_name="Стоимость курса/урока", help_text="Укажите сумму оплаты")
    payment_type = models.CharField(max_length=25, choices=payment_choices, verbose_name='Тип оплаты', help_text="Выберите способ оплаты")

    def __str__(self):
        return f"{self.amount_of_payment} руб."

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
